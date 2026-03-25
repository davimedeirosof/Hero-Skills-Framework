#!/usr/bin/env node
/**
 * find-photos.js
 * Automatically searches for and downloads the best photo for each carousel
 * slide that needs a background or embedded image.
 *
 * Search engines tried in order (first success wins):
 *   1. DuckDuckGo Images  — no API key, no CAPTCHA in headless
 *   2. Bing Images        — no API key required for basic results
 *   3. Unsplash source    — deterministic, no API key (source.unsplash.com)
 *
 * Usage:
 *   node find-photos.js                   # download all missing photos
 *   node find-photos.js --force            # re-download even if file exists
 *   node find-photos.js --slide cover      # only the cover photo
 *   node find-photos.js --slide food       # only the food photo
 *
 * Dependencies: playwright (already in package.json)
 * First time:   npx playwright install chromium
 */

'use strict';

const { chromium } = require('playwright');
const fs   = require('fs');
const path = require('path');
const https = require('https');
const http  = require('http');

// ---------------------------------------------------------------------------
// Paths
// ---------------------------------------------------------------------------

const ROOT_DIR   = path.resolve(__dirname, '..');
const SLIDES_DIR = path.join(ROOT_DIR, 'output', 'slides');
const PHOTOS_DIR = path.join(SLIDES_DIR, 'photos');

// ---------------------------------------------------------------------------
// Photo targets
// ---------------------------------------------------------------------------

/**
 * key        - identifier used with --slide flag
 * slide      - slide number (for logging)
 * filename   - saved inside photos/
 * queries    - search terms tried in sequence across all engines
 * fallbackUrl- remote URL kept in HTML via onerror when local file absent
 */
const PHOTO_TARGETS = [
  {
    key: 'cover',
    slide: 1,
    filename: 'cover.jpg',
    queries: [
      'supermercado Brasil inflação preços',
      'Brazilian supermarket grocery prices',
      'supermarket grocery store prices inflation',
    ],
    fallbackUrl:
      'https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=1080&h=700&fit=crop&q=85',
  },
  {
    key: 'food',
    slide: 7,
    filename: 'food.jpg',
    queries: [
      'feira mercado alimentos Brasil carne arroz',
      'grocery food market brazil vegetables',
      'supermarket food aisle fresh produce',
    ],
    fallbackUrl:
      'https://images.unsplash.com/photo-1542838132-92c53300491e?w=1016&h=380&fit=crop&q=85',
  },
];

// ---------------------------------------------------------------------------
// CLI
// ---------------------------------------------------------------------------

const args      = process.argv.slice(2);
const FORCE     = args.includes('--force');
const slideFlag = (() => {
  const i = args.indexOf('--slide');
  return i !== -1 ? args[i + 1] : null;
})();

const targets = slideFlag
  ? PHOTO_TARGETS.filter(t => t.key === slideFlag)
  : PHOTO_TARGETS;

// ---------------------------------------------------------------------------
// Download helper
// ---------------------------------------------------------------------------

function downloadImage(url, filepath) {
  return new Promise((resolve, reject) => {
    const proto = url.startsWith('https') ? https : http;
    const req = proto.get(
      url,
      {
        headers: {
          'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' +
            '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
          'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        },
      },
      (res) => {
        if (res.statusCode === 301 || res.statusCode === 302) {
          const loc = res.headers.location;
          if (!loc) return reject(new Error('Redirect with no Location'));
          return downloadImage(loc, filepath).then(resolve).catch(reject);
        }
        if (res.statusCode !== 200) {
          return reject(new Error(`HTTP ${res.statusCode}`));
        }
        const ct = res.headers['content-type'] || '';
        if (!ct.startsWith('image/')) {
          return reject(new Error(`Not an image: ${ct}`));
        }
        const file = fs.createWriteStream(filepath);
        res.pipe(file);
        file.on('finish', () => file.close(() => resolve(filepath)));
        file.on('error', (e) => { fs.unlink(filepath, () => {}); reject(e); });
      }
    );
    req.on('error', (e) => { fs.unlink(filepath, () => {}); reject(e); });
    req.setTimeout(15000, () => { req.destroy(); reject(new Error('Timeout')); });
  });
}

// ---------------------------------------------------------------------------
// URL validation
// ---------------------------------------------------------------------------

function isValidSrc(src) {
  if (!src || !src.startsWith('http')) return false;
  const blocked = ['google.com', 'gstatic.com', 'googleapis.com', 'bing.com/th?', 'duckduckgo.com/t/'];
  if (blocked.some(b => src.includes(b))) return false;
  return src.length > 40;
}

// ---------------------------------------------------------------------------
// Search engine adapters
// ---------------------------------------------------------------------------

/**
 * DuckDuckGo Images – no login, no CAPTCHA issues with Playwright.
 * Returns list of candidate image URLs.
 */
async function searchDuckDuckGo(page, query) {
  const url = `https://duckduckgo.com/?q=${encodeURIComponent(query)}&iax=images&ia=images`;
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
  await page.waitForTimeout(2500);

  // DDG lazy-loads images via data-src on <img> inside anchor tiles
  const candidates = await page.evaluate(() => {
    const urls = [];
    // Thumbnails store the actual image URL in data-src or in the surrounding <a> href
    document.querySelectorAll('img[data-src]').forEach(img => {
      const s = img.getAttribute('data-src');
      if (s && s.startsWith('http')) urls.push(s);
    });
    // Also scan anchor tiles whose href is the image URL
    document.querySelectorAll('a[href]').forEach(a => {
      const h = a.href;
      if (h && /\.(jpg|jpeg|png|webp)/i.test(h) && h.startsWith('http')) urls.push(h);
    });
    return urls;
  });

  return candidates.filter(isValidSrc);
}

/**
 * Bing Images – collects murl (media URL) values embedded in the page JSON.
 * These are direct links to source images, not Bing thumbnails.
 */
async function searchBing(page, query) {
  const url = `https://www.bing.com/images/search?q=${encodeURIComponent(query)}&qft=+filterui:imagesize-large&FORM=IRFLTR`;
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
  await page.waitForTimeout(2000);

  // Bing embeds image metadata in m={...} attributes on anchor elements
  const candidates = await page.evaluate(() => {
    const urls = [];
    document.querySelectorAll('a[m]').forEach(a => {
      try {
        const meta = JSON.parse(a.getAttribute('m'));
        if (meta && meta.murl) urls.push(meta.murl);
      } catch (_) {}
    });
    // Fallback: data-src on img
    document.querySelectorAll('img[data-src]').forEach(img => {
      const s = img.getAttribute('data-src');
      if (s && s.startsWith('http')) urls.push(s);
    });
    return urls;
  });

  return candidates.filter(isValidSrc);
}

/**
 * Unsplash Source – deterministic URLs, always returns a valid image.
 * No API key needed. Used as last-resort engine.
 *
 * Returns a single URL list so it fits the same interface as the other engines.
 */
function buildUnsplashSourceUrl(query) {
  // source.unsplash.com/1080x1080?{keyword} always returns a random matching photo
  const keyword = encodeURIComponent(query.split(' ').slice(0, 3).join(','));
  return [`https://source.unsplash.com/1080x1080?${keyword}`];
}

// ---------------------------------------------------------------------------
// Find a single image URL across all engines
// ---------------------------------------------------------------------------

/**
 * Tries DuckDuckGo → Bing → Unsplash Source for each query.
 * Returns the first valid URL found.
 */
async function findImageUrl(browser, query) {
  const page = await browser.newPage();
  // Block heavy assets to speed things up
  await page.route('**/*.{woff,woff2,ttf,css,mp4,webm,svg}', r => r.abort());

  try {
    // --- Engine 1: DuckDuckGo ---
    console.log(`      [ddg] "${query}"`);
    try {
      const ddgResults = await searchDuckDuckGo(page, query);
      if (ddgResults.length > 0) {
        console.log(`      [ddg] found ${ddgResults.length} candidates`);
        return ddgResults[0];
      }
      console.log(`      [ddg] no results`);
    } catch (e) {
      console.log(`      [ddg] error: ${e.message}`);
    }

    // --- Engine 2: Bing ---
    console.log(`      [bing] "${query}"`);
    try {
      const bingResults = await searchBing(page, query);
      if (bingResults.length > 0) {
        console.log(`      [bing] found ${bingResults.length} candidates`);
        return bingResults[0];
      }
      console.log(`      [bing] no results`);
    } catch (e) {
      console.log(`      [bing] error: ${e.message}`);
    }

    return null;
  } finally {
    await page.close();
  }
}

// ---------------------------------------------------------------------------
// Per-photo orchestration
// ---------------------------------------------------------------------------

async function findAndDownloadPhoto(browser, target) {
  const filepath = path.join(PHOTOS_DIR, target.filename);

  if (!FORCE && fs.existsSync(filepath)) {
    const sizeKB = Math.round(fs.statSync(filepath).size / 1024);
    console.log(`  [skip] ${target.filename} already exists (${sizeKB} KB)`);
    return filepath;
  }

  console.log(`\n  Searching for slide-${String(target.slide).padStart(2, '0')} (${target.key})...`);

  // Try each query across search engines
  for (const query of target.queries) {
    console.log(`    query: "${query}"`);

    const imageUrl = await findImageUrl(browser, query);

    if (imageUrl) {
      console.log(`    downloading: ${imageUrl.substring(0, 90)}...`);
      try {
        await downloadImage(imageUrl, filepath);
        const sizeKB = Math.round(fs.statSync(filepath).size / 1024);
        if (sizeKB < 5) {
          fs.unlinkSync(filepath);
          console.log(`    too small (${sizeKB} KB), trying next query`);
          continue;
        }
        console.log(`  [ok] ${target.filename} saved (${sizeKB} KB)`);
        return filepath;
      } catch (e) {
        console.log(`    download failed: ${e.message}`);
      }
    }

    await new Promise(r => setTimeout(r, 1000));
  }

  // Last resort: Unsplash Source (always works, deterministic)
  console.log(`    [unsplash-source] using deterministic fallback...`);
  const usUrl = buildUnsplashSourceUrl(target.queries[0])[0];
  try {
    await downloadImage(usUrl, filepath);
    const sizeKB = Math.round(fs.statSync(filepath).size / 1024);
    if (sizeKB >= 5) {
      console.log(`  [ok] ${target.filename} saved via Unsplash Source (${sizeKB} KB)`);
      return filepath;
    }
    fs.unlinkSync(filepath);
  } catch (e) {
    console.log(`    Unsplash Source failed: ${e.message}`);
  }

  console.log(`  [fail] could not download photo for slide ${target.slide}`);
  return null;
}

// ---------------------------------------------------------------------------
// HTML patching
// ---------------------------------------------------------------------------

/**
 * Rewrites an img src in an HTML file to use a local path,
 * with an onerror fallback to the original remote URL.
 */
function patchHtmlPhotoSrc(htmlFile, localSrc, remoteSrc) {
  if (!fs.existsSync(htmlFile)) {
    console.log(`  [html] not found: ${path.basename(htmlFile)}`);
    return;
  }

  let html = fs.readFileSync(htmlFile, 'utf8');

  if (html.includes(`src="${localSrc}"`)) {
    console.log(`  [html] already patched: ${path.basename(htmlFile)}`);
    return;
  }

  const escapedRemote = remoteSrc.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const pattern = new RegExp(
    `(<img\\b[^>]*?)\\ssrc="${escapedRemote}"([^>]*?)(/?>)`,
    'g'
  );
  const onerror = `onerror="this.onerror=null;this.src='${remoteSrc}'"`;

  const updated = html.replace(pattern, (_, before, after, close) => {
    const hasOnerror = before.includes('onerror') || after.includes('onerror');
    return `${before} src="${localSrc}"${hasOnerror ? '' : ' ' + onerror}${after}${close}`;
  });

  if (updated === html) {
    console.log(`  [html] img src not found in ${path.basename(htmlFile)}`);
    return;
  }

  fs.writeFileSync(htmlFile, updated, 'utf8');
  console.log(`  [html] patched: ${path.basename(htmlFile)}`);
}

function patchAllHtmlFiles() {
  console.log('\nPatching HTML files...');

  const patches = [
    {
      key: 'cover',
      htmlFile: path.join(SLIDES_DIR, 'slide-01-cover.html'),
      localSrc: 'photos/cover.jpg',
      remoteSrc:
        'https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=1080&h=700&fit=crop&q=85',
    },
    {
      key: 'food',
      htmlFile: path.join(SLIDES_DIR, 'slide-07-food.html'),
      localSrc: 'photos/food.jpg',
      remoteSrc:
        'https://images.unsplash.com/photo-1542838132-92c53300491e?w=1016&h=380&fit=crop&q=85',
    },
  ];

  for (const patch of patches) {
    const inScope = targets.some(t => t.key === patch.key);
    if (!inScope) continue;

    const localAbsolute = path.join(SLIDES_DIR, patch.localSrc);
    if (!fs.existsSync(localAbsolute)) {
      console.log(`  [html] skipping ${path.basename(patch.htmlFile)} — photo not downloaded`);
      continue;
    }

    patchHtmlPhotoSrc(patch.htmlFile, patch.localSrc, patch.remoteSrc);
  }
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  fs.mkdirSync(PHOTOS_DIR, { recursive: true });

  if (targets.length === 0) {
    const valid = PHOTO_TARGETS.map(t => t.key).join(', ');
    console.error(`Unknown slide key: "${slideFlag}". Valid: ${valid}`);
    process.exit(1);
  }

  console.log('find-photos.js');
  console.log(`  photos dir : ${PHOTOS_DIR}`);
  console.log(`  targets    : ${targets.map(t => t.key).join(', ')}`);
  console.log(`  force      : ${FORCE}`);
  console.log('');

  const browser = await chromium.launch({
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-blink-features=AutomationControlled',
    ],
  });

  const results = [];

  for (let i = 0; i < targets.length; i++) {
    const target = targets[i];
    const filepath = await findAndDownloadPhoto(browser, target);
    results.push({ target, filepath, success: filepath !== null });
    if (i < targets.length - 1) {
      await new Promise(r => setTimeout(r, 2000));
    }
  }

  await browser.close();

  patchAllHtmlFiles();

  console.log('\n--- Summary ---');
  for (const { target, filepath, success } of results) {
    const status = success ? 'ok  ' : 'fail';
    const detail = success
      ? path.relative(SLIDES_DIR, filepath)
      : `remote fallback: ${target.fallbackUrl.substring(0, 55)}...`;
    console.log(`  [${status}] slide-${String(target.slide).padStart(2, '0')} ${target.filename}: ${detail}`);
  }

  const failed = results.filter(r => !r.success).length;
  if (failed > 0) {
    console.log(`\n${failed} photo(s) unavailable — slides use remote fallback URLs.`);
  } else {
    console.log('\nAll photos ready.');
  }
}

main().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});
