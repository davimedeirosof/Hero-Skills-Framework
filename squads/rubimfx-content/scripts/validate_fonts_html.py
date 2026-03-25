#!/usr/bin/env python3
"""
Validador de tamanhos de fonte para slides HTML de carrossel Instagram.
Detecta font-size abaixo do minimo permitido (22px por padrao).

Elementos decorativos com excecao (permitidos abaixo do minimo):
  - profile-name, profile-handle, profile-info
  - meta-time, meta-views, tweet-meta
  - slide-counter
  - breaking-badge, breaking-dot
  - stat-label (em stats-bar sobre fotos)
  - card-row-label (no comparativo antes/depois)
  - card-label-top (label sobre big number)
  - card-header (badge ANTES/AGORA)
  - browser-url, browser-dot
  - article-source, article-category, article-tag-text
  - image-caption, embed-caption
  - byline-name, byline-date, byline-avatar
  - translation-label
  - photo-label
  - share-btn
  - topic-badge
  - footer-text
  - diff-label, diff-desc
  - header-section, news-section-tag
  - vs-badge
  - corner-deco

Uso:
  python validate_fonts_html.py <pasta-html>
  python validate_fonts_html.py <pasta-html> --min 22
  python validate_fonts_html.py ../output/posts/2026-03-17-tema/html/

Retorna exit code 1 se encontrar fontes proibidas (bloqueia pipeline).
"""

import os
import sys
import re
import glob
import argparse

# Classes/seletores decorativos que TEM permissao de usar fontes menores
DECORATIVE_SELECTORS = {
    "profile-name", "profile-handle", "profile-info", "profile-pic",
    "meta-time", "meta-views", "tweet-meta",
    "slide-counter",
    "breaking-badge", "breaking-dot",
    "stat-label",
    "card-row-label",
    "card-label-top",
    "card-header",
    "browser-url", "browser-dot", "browser-dots", "browser-bar",
    "article-source", "article-category", "article-tag-text", "article-tag-dot",
    "image-caption", "embed-caption",
    "byline-name", "byline-date", "byline-avatar", "byline-info",
    "translation-label",
    "photo-label",
    "share-btn",
    "topic-badge",
    "footer-text",
    "diff-label", "diff-desc",
    "header-section", "news-section-tag",
    "vs-badge",
    "corner-deco", "corner-tl", "corner-br",
    "bretas-caption-name", "bretas-caption-detail",
    "dino-embed-caption",
    "metropoles-logo",
    "news-logo",
    "warning-desc",
}


def parse_css_blocks(css_text):
    """
    Extrai blocos CSS como (seletor, propriedades_texto).
    Retorna lista de (selector_string, properties_string, line_offset).
    """
    blocks = []
    # Encontrar blocos { ... }
    depth = 0
    selector_start = 0
    block_start = None

    for i, ch in enumerate(css_text):
        if ch == '{':
            if depth == 0:
                selector = css_text[selector_start:i].strip()
                block_start = i + 1
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0 and block_start is not None:
                properties = css_text[block_start:i]
                # Contar linhas ate o seletor para offset
                line_offset = css_text[:selector_start].count('\n')
                blocks.append((selector, properties, line_offset))
                selector_start = i + 1
                block_start = None

    return blocks


def selector_is_decorative(selector):
    """Verifica se o seletor corresponde a um elemento decorativo (excecao)."""
    selector_lower = selector.lower().strip()
    for deco in DECORATIVE_SELECTORS:
        if f".{deco}" in selector_lower:
            return True
    return False


def find_small_fonts_in_css(css_text, min_size, style_line_start):
    """
    Analisa blocos CSS e retorna lista de violacoes.
    Cada violacao: (seletor, tamanho_encontrado, linha_aproximada)
    """
    violations = []
    blocks = parse_css_blocks(css_text)

    for selector, properties, line_offset in blocks:
        if selector_is_decorative(selector):
            continue

        # Buscar font-size em px
        for match in re.finditer(r'font-size:\s*(\d+(?:\.\d+)?)px', properties):
            size = float(match.group(1))
            if size < min_size:
                # Calcular linha aproximada
                prop_before = properties[:match.start()]
                line_in_block = prop_before.count('\n')
                approx_line = style_line_start + line_offset + line_in_block + 1
                violations.append({
                    'selector': selector,
                    'size': size,
                    'line': approx_line,
                })

    return violations


def find_inline_small_fonts(html_text, min_size, lines):
    """
    Analisa estilos inline (style="...font-size:Xpx...") fora do bloco <style>.
    """
    violations = []
    in_style = False

    for line_num, line in enumerate(lines, 1):
        if '<style' in line.lower():
            in_style = True
        if '</style' in line.lower():
            in_style = False
            continue
        if in_style:
            continue

        # Buscar style="..." inline
        for style_match in re.finditer(r'style="([^"]*)"', line):
            style_content = style_match.group(1)
            for font_match in re.finditer(r'font-size:\s*(\d+(?:\.\d+)?)px', style_content):
                size = float(font_match.group(1))
                if size < min_size:
                    # Verificar se o elemento tem classe decorativa
                    tag_start = line[:style_match.start()]
                    is_deco = False
                    class_match = re.search(r'class="([^"]*)"', line)
                    if class_match:
                        classes = class_match.group(1).split()
                        for cls in classes:
                            if cls in DECORATIVE_SELECTORS:
                                is_deco = True
                                break
                    if not is_deco:
                        violations.append({
                            'selector': f'inline style',
                            'size': size,
                            'line': line_num,
                        })

    return violations


def validate_file(filepath, min_size):
    """Valida um arquivo HTML. Retorna lista de violacoes."""
    filename = os.path.basename(filepath)
    violations = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    # Extrair bloco <style>
    style_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
    if style_match:
        css_text = style_match.group(1)
        # Calcular linha de inicio do bloco style
        style_line_start = content[:style_match.start(1)].count('\n') + 1
        css_violations = find_small_fonts_in_css(css_text, min_size, style_line_start)
        for v in css_violations:
            v['file'] = filename
        violations.extend(css_violations)

    # Verificar estilos inline
    inline_violations = find_inline_small_fonts(content, min_size, lines)
    for v in inline_violations:
        v['file'] = filename
    violations.extend(inline_violations)

    return violations


def main():
    parser = argparse.ArgumentParser(
        description="Valida tamanhos de fonte em slides HTML de carrossel."
    )
    parser.add_argument('html_dir', help="Pasta contendo os arquivos slide-*.html")
    parser.add_argument('--min', type=int, default=22,
                        help="Tamanho minimo permitido em px (default: 22)")
    parser.add_argument('--strict', action='store_true',
                        help="Modo estrito: nao permite excecoes decorativas")

    args = parser.parse_args()
    html_dir = os.path.abspath(args.html_dir)
    min_size = args.min

    html_files = sorted(glob.glob(os.path.join(html_dir, "slide-*.html")))

    if not html_files:
        print(f"Nenhum slide-*.html encontrado em {html_dir}")
        sys.exit(1)

    print(f"Validando fontes em {len(html_files)} arquivos (minimo: {min_size}px)...\n")

    total_violations = []
    for filepath in html_files:
        violations = validate_file(filepath, min_size)
        total_violations.extend(violations)

    if total_violations:
        print(f"{len(total_violations)} FONTES ABAIXO DE {min_size}px ENCONTRADAS:\n")
        for v in total_violations:
            print(f"  {v['file']}:{v['line']} -- {v['selector']} -> {v['size']}px (minimo: {min_size}px)")
        print()
        print(f"{'=' * 50}")
        print(f"BLOQUEADO: Corrija {len(total_violations)} fontes antes de renderizar.")
        print(f"\nDica: Substitua valores abaixo de {min_size}px por {min_size}px ou mais.")
        print(f"Elementos decorativos (profile-name, meta-time, slide-counter, etc.) sao permitidos.")
        sys.exit(1)
    else:
        print(f"Todos os {len(html_files)} arquivos passaram na validacao de fontes!")
        sys.exit(0)


if __name__ == "__main__":
    main()
