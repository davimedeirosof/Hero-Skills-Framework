# Opensquad — Skills Globais

Skills instaladas em `skills/` no repositório `opensquad-content-os`. Cada skill tem um `SKILL.md` com frontmatter YAML + instruções Markdown.

---

## Estrutura de diretórios

```
skills/
├── apify/                  SKILL.md
├── blotato/                SKILL.md
├── canva/                  SKILL.md
├── image-creator/          SKILL.md
├── image-fetcher/          SKILL.md
├── instagram-publisher/    SKILL.md + scripts/
├── opensquad-agent-creator/ SKILL.md
└── opensquad-skill-creator/ SKILL.md + agents/ + assets/ + eval-viewer/ + references/ + scripts/
```

---

## apify

**Tipo:** `mcp`
**Versão:** 1.0.0
**Env:** `APIFY_TOKEN`
**Cmd:** `npx -y @apify/actors-mcp-server@latest`
**Categorias:** scraping, data, automation

### Quando usar
Extrair dados de websites, scrape de perfis em redes sociais, queries de busca, automação de coleta de dados. Apify oferece milhares de scrapers prontos (Actors).

### Atores populares
`web-scraper`, `instagram-scraper`, `google-search-scraper`, `youtube-scraper`, `twitter-scraper`, `tiktok-scraper`

### Operações disponíveis
- **Run Actor** — executa qualquer Apify Actor com parâmetros customizados
- **Web Scraping** — extrai dados estruturados de qualquer website
- **Social Media Scraping** — scrape de perfis, posts e dados de engajamento (IG, YouTube, Twitter/X, TikTok)
- **Search Scraping** — queries de busca (Google, Bing) e coleta de resultados
- **Data Export** — recupera datasets em JSON

### Best practices
- Começar com o Actor mais simples que atenda a necessidade
- Usar `maxItems` para limitar resultados e evitar custos excessivos
- Verificar preço do Actor antes de executar (alguns têm custo por resultado)
- Parsear resultados e extrair apenas os campos necessários

---

## blotato

**Tipo:** `mcp` (HTTP)
**Versão:** 1.0.0
**URL:** `https://mcp.blotato.com/mcp`
**Env:** `BLOTATO_API_KEY`
**Categorias:** social-media, automation, publishing, scheduling

### Quando usar
Publicar e agendar posts em múltiplas plataformas (Instagram, LinkedIn, Twitter/X, TikTok, YouTube) a partir de uma interface única.

### Workflow chave
1. `blotato_list_accounts` — obter IDs de conta e plataformas
2. `blotato_upload_media` — fazer upload de imagens/vídeos antes de criar post
3. `blotato_create_post` — publicar ou agendar
4. `blotato_get_post_status` — confirmar sucesso

### Operações disponíveis
- **List Accounts** — contas conectadas e seus tipos de plataforma
- **Upload Media** — upload de imagens e vídeos
- **Create Post** — publicação imediata ou agendada
- **Get Post Status** — monitorar status ("published", "scheduled", "failed")

### Requisitos
- Conta Blotato (blotato.com)
- Conta Business (não Personal/Creator no Instagram)
- Para posts agendados: formato ISO 8601 para datetime

---

## canva

**Tipo:** `mcp` (HTTP)
**Versão:** 1.0.0
**URL:** `https://mcp.canva.com/mcp`
**Auth:** OAuth
**Categorias:** design, ui, assets, automation

### Quando usar
Criar, buscar ou exportar designs visuais. Suporta apresentações, posts de redes sociais, logos e outros visuais via templates da conta do usuário.

### Operações disponíveis
- **Create Design** — gerar novos designs do zero ou a partir de templates
- **Search Designs** — buscar designs existentes na conta Canva do usuário
- **Autofill Template** — preencher placeholders de template com texto, imagens e brand elements
- **Export Design** — exportar como PDF, PNG, JPG ou outros formatos
- **Browse Templates** — buscar na biblioteca de templates do Canva

### Best practices
- Usar templates quando possível (mais rápido e on-brand)
- Ao preencher templates, combinar conteúdo com nomes dos placeholders
- Exportar no formato mais útil para o pipeline (PNG para social, PDF para documentos)

### Requisitos
- Conta Canva (free ou paga)
- Autorização OAuth necessária no primeiro uso
- Autofill de templates requer plano pago do Canva

---

## image-creator

**Tipo:** `mcp` (Playwright)
**Versão:** 1.0.0
**Categorias:** design, automation, images

### Quando usar
Gerar imagens prontas para produção a partir de HTML/CSS. Motor principal para criar carrosséis Instagram, slides, infográficos e qualquer conteúdo visual definido por templates HTML.

### Workflow principal
1. **Gerar HTML** — arquivo completo self-contained com CSS inline
2. **Salvar HTML** — em `output/slides/slide-01.html`
3. **Iniciar servidor HTTP** — `python -m http.server 8765 --directory "OUTPUT_DIR" &`
4. **Renderizar** — Playwright: `browser_navigate` → `browser_resize` → `browser_take_screenshot`
5. **Verificar** — ler screenshot para confirmar qualidade
6. **Parar servidor** — `pkill -f "http.server 8765" 2>/dev/null || true`

### Viewport presets (width x height)
| Formato | Dimensões |
|---------|-----------|
| Instagram Feed (square) | 1080x1080 |
| Instagram Feed (portrait) | 1080x1350 |
| Instagram Carousel | 1080x1440 |
| Instagram Story/Reel | 1080x1920 |
| LinkedIn | 1200x627 |
| YouTube Thumbnail | 1280x720 |

### Regras de HTML
- 100% self-contained: CSS inline, sem CDN, sem JS, sem fontes externas (exceto Google Fonts @import)
- Fontes mínimas: 20px (ideal 22px+)
- Sem URLs externas no HTML
- Grid/Flexbox para layout

---

## image-fetcher

**Tipo:** `hybrid` (Playwright + web_search)
**Versão:** 1.0.0
**Categorias:** assets, scraping, automation, images

### Quando usar
Obter assets visuais de múltiplas fontes para uso em conteúdo. Três modos de aquisição.

### Modos
1. **Web Image Search** — usa `web_search` para encontrar imagens por keyword
2. **Live Screenshot** — Playwright navega a URL e captura screenshot
3. **Asset Organization** — salva assets com nomes descritivos em `reference/` ou `output/`

### Modos de screenshot
- `viewport` — apenas a área visível (padrão)
- `full_page` — página inteira scrollável
- `selector` — elemento CSS específico

### Dimensões padrão
- IG post: 1080x1080 | IG carousel: 1080x1440 | Story/Reel: 1080x1920 | Genérico: 1280x720

### Limites
- Timeout: 30s por screenshot
- Máx: 1920x1920px
- Bloqueia: `file://` e IPs privados

---

## instagram-publisher

**Tipo:** `script` (Node.js)
**Versão:** 1.0.0
**Script:** `scripts/publish.js`
**Env:** `INSTAGRAM_ACCESS_TOKEN`, `INSTAGRAM_USER_ID`, `IMGBB_API_KEY`
**Categorias:** social-media, publishing, instagram

### Quando usar
Publicar carrosséis Instagram a partir de imagens locais. Fluxo completo: JPEG → imgbb → Graph API → publicação.

### Workflow
1. Listar JPEGs em `squads/{squad}/output/images/` ordenados por nome
2. Apresentar lista ao usuário para confirmar ordem
3. Extrair caption do rascunho de conteúdo (hook + CTA, máx 2200 chars)
4. Executar script de publicação (adicionar `--dry-run` para testar sem publicar)
5. Em sucesso: salvar URL e post ID no arquivo de output do step
6. Em falha: exibir erro e perguntar ao usuário como proceder

### Constraints
- Imagens: JPEG only, 2-10 por carousel
- Caption: máx 2200 caracteres
- Rate limit: 25 posts/24h via API
- Requer conta Business (não Personal/Creator)

---

## opensquad-agent-creator

**Tipo:** `prompt`
**Versão:** 2.0.0
**Categorias:** opensquad, workflow

### Quando usar
Criar e manter arquivos de best-practice na biblioteca `_opensquad/core/best-practices/`. Valida formato, referências cruzadas, versionamento e consistência do catálogo.

### Mínimos obrigatórios por arquivo
| Seção | Mínimo |
|-------|--------|
| Total de linhas | 200+ |
| Core Principles | 6+ regras numeradas |
| Técnicas & Frameworks | 3+ técnicas concretas |
| Vocabulário Always Use | 5+ termos |
| Vocabulário Never Use | 3+ termos |
| Output Examples | 2 completos, 15+ linhas cada |
| Anti-Patterns (Never Do) | 4+ |
| Anti-Patterns (Always Do) | 3+ |
| Quality Criteria | 4+ itens verificáveis |

### Frontmatter YAML obrigatório
- `id`: lowercase kebab-case
- `name`: nome de exibição
- `whenToUse`: escopo positivo E negativo ("NOT for: ...")
- `version`: "1.0.0" para novos

### Semver
- `patch` = typos/clarificações
- `minor` = novo conteúdo dentro do escopo
- `major` = reestruturação de seções

---

## opensquad-skill-creator

**Tipo:** `prompt`
**Versão:** variável
**Categorias:** opensquad, workflow

### Quando usar
Criar novas skills para o sistema Opensquad. Guia pelo ciclo completo de desenvolvimento.

### Ciclo de desenvolvimento
```
draft → test → evaluate → improve → repeat
```

### Estrutura do SKILL.md
- YAML frontmatter obrigatório + instruções Markdown
- Máximo 500 linhas

### Evals
- 2-3 prompts realistas em `evals/evals.json`
- Execução paralela: with-skill vs baseline simultaneamente
- Viewer via `generate_review.py` antes de auto-avaliar

### Pasta adicional
- `agents/` — agentes auxiliares para o skill creator
- `assets/` — assets de referência
- `eval-viewer/` — interface para visualizar resultados de evals
- `references/` — documentação de referência
- `scripts/` — scripts auxiliares
