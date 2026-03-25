# Guia de Consistência — Content OS @rubimfx

## 1. FLUXO DE PRODUÇÃO (passo a passo)

1. Pesquisar notícias virais (WebSearch + research-analyst agent)
2. Gabriel escolhe tema + estilo
3. Gerar fotos temáticas novas (SEMPRE para capa + slides-chave)
4. Pode reusar fotos do book nos slides secundários
5. Baixar fotos editoriais reais (og:image dos artigos via Firecrawl)
6. Criar 10 slides HTML usando templates Kaique Epic
7. Renderizar via Playwright (http server + screenshot 1080x1350)
8. Verificar visualmente ANTES de mostrar ao Gabriel
9. Publicar via Playwright (Chrome fechado → Instagram → Criar → Upload → 4:5 → Avançar → Caption → Compartilhar)

## 2. ESTILOS DE CARROSSEL (6 testados)

| Estilo | Quando usar |
|---|---|
| **Kaique Epic** ⭐ FAVORITO | Capas épicas com fotos dramáticas + tweet cards brancos. Usar para qualquer tema viral, notícias impactantes, mindset. O padrão principal. |
| **Twitter Dark** | 7 tipos de card diferentes, ideal para conteúdo educativo, dados, threads explicativas. Fundo escuro, tipografia forte. |
| **Esteter Style** | Tweet thread + screenshots reais de reportagens. Bom para compilar múltiplas fontes sobre um tema. 5 tipos de slide (cover, tweet, screenshot, data, CTA). |
| **Hollyfield News** | Foto hero gigante + header laranja. Para notícias de grande impacto visual, breaking news, eventos marcantes. |
| **BrunoGPT Neon** | Neon vibrante, estética tech/IA. Usar para temas de tecnologia, inteligência artificial, inovação, teasers InvisIA. |
| **Minimal Clean** | Minimalista, foco em listas e dados. Bom para conteúdo mais leve, listas, rankings, comparações simples. |

## 3. REGRAS VISUAIS OBRIGATÓRIAS

- **Dimensão:** 1080x1350px (4:5 Instagram)
- **Fonte mínima:** 22px (NADA abaixo de 20px)
- **Headlines:** 64-80px+ (Anton para Epic, Inter 900 para Tweet)
- **Body:** 28-34px
- **Português com acentos SEMPRE** (á, é, í, ó, ú, ã, õ, ç)
- **@rubimfx visível em TODOS os slides**
- **Mínimo 3 layouts diferentes** no carrossel
- **CTA último slide SEMPRE** com "Segue @rubimfx"
- **Fotos temáticas NOVAS** para capa e slides-chave de cada post
- Pode reusar book (minimalista/impactante) nos slides secundários

## 4. FOTOS — REGRAS

- **Fotos editoriais reais:** baixar og:image dos artigos (Firecrawl scrape)
- **Fotos clone Gabriel:** usar `clone_image.py` com 3 referências (IMG_8579, IMG_1092, DSC04575)
- **Fotos temáticas:** gerar via Gemini API (gemini-2.5-flash-image)
- **NUNCA** usar stock/Unsplash genérico
- Gabriel prefere estilo **DRAMÁTICO** e **MINIMALISTA**
- Books disponíveis: `book-minimalista/` e `book-impactante/`

## 5. LEGENDA — TOM DO GABRIEL

- Informal, direto, sem formalidade
- Letras minúsculas (exceto ênfases em CAPS)
- Sem emojis em excesso (máximo 2-3 por post)
- Frases curtas. Parágrafos de 1-2 linhas.
- Tom: como se estivesse falando com um amigo no WhatsApp
- Viés conservador de direita (política)
- Fé cristã presente naturalmente (não forçado)
- Sempre terminar com CTA: "salva", "manda pra alguém", "comenta"

## 6. TEMAS QUE FUNCIONAM

- Notícias virais (política, economia, geopolítica)
- Mindset/disciplina (trading + vida)
- Fé e espiritualidade (Deus, processo, preparo)
- Família e valores (Thays, filhos, legado)
- Trading/mercado (SMC, prop firm, protocolo)
- Teaser InvisIA (quando autorizado)

## 7. PALETA DE CORES

**Kaique Epic:**
- Amarelo destaque: `#FFD600`
- Vermelho alerta: `#FF3B30` / `#F4212E`
- Azul info: `#1D9BF0`
- Card branco: `#FFFFFF`
- Texto preto: `#0F1419`
- Body gray: `#292F33`

**InvisIA Teaser:**
- Preto puro: `#000000`
- Branco gelo: `#F5F5F5`
- Roxo acento: `#7C3AED`

## 8. FONTES PREFERIDAS DE NOTÍCIAS

- Gazeta do Povo
- Revista Oeste
- Jovem Pan
- O Antagonista
- CNN Brasil
- Poder360
- InfoMoney
- Bloomberg Línea

## 9. TEMPLATES DISPONÍVEIS

| Template | Arquivo |
|---|---|
| Dark Tweet | `template-01-dark-tweet.html` |
| News Magazine | `template-02-news-magazine.html` |
| Neon Data | `template-03-neon-data.html` |
| Minimal Clean | `template-04-minimal-clean.html` |
| Breaking News | `template-05-breaking-news.html` |
| Personal Brand | `template-06-personal-brand.html` |
| Infographic | `template-07-infographic.html` |
| Meme Editorial | `template-08-meme-editorial.html` |
| Kaique Epic Cover | `template-09-kaique-epic.html` |
| Kaique Tweet Card | `template-10-kaique-tweet.html` |
| Hollyfield News | `template-11-hollyfield-news.html` |
| BrunoGPT Cover | `template-12-brunogpt-cover.html` |
| BrunoGPT Content | `template-13-brunogpt-content.html` |
| Esteter Cover | `template-14-esteter-cover.html` |
| Esteter Tweet | `template-15-esteter-tweet.html` |
| Esteter Screenshot | `template-16-esteter-screenshot.html` |
| Esteter Data | `template-17-esteter-data.html` |
| Esteter CTA | `template-18-esteter-cta.html` |
| CTA Fixed | `slide-10-cta-fixed.html` |

## 10. SCRIPTS DISPONÍVEIS

| Script | Função |
|---|---|
| `clone_image.py` | Clone PRO com Identity Header, 12 cenários, camera/color presets |
| `render_slides.py` | Renderizar slides para PNG via Playwright |
| `generate_image.py` | Gerar imagens via API |
| `generate_biblical.py` | Gerar imagens bíblicas via Gemini API |
| `publish_carousel.py` | Publicar carrossel no Instagram via Playwright |
| `validate_accents.py` | Validar acentos corretos em português |
| `validate_fonts_html.py` | Validar tamanhos de fonte nos HTMLs |
| `preflight_check.py` | Checagem pré-publicação automatizada |
| `find-photos.js` | Buscar fotos nos books disponíveis |
| `pipeline.py` | Pipeline completo de produção |

## 11. BOOKS DE FOTOS

- **book-minimalista/** — 5 fotos (headshot, branding, turtleneck, rembrandt, casual)
- **book-impactante/** — 6 fotos (close dramático, silhueta, olhar lateral, braços cruzados P&B, low key noir, sorriso dramático)
- **book-profissional/** — Fotos profissionais adicionais

## 12. CHECKLIST PRÉ-PUBLICAÇÃO

- [ ] Todos os slides têm @rubimfx visível
- [ ] Capa tem foto temática NOVA (não reusada)
- [ ] Fontes acima de 20px em todos os slides
- [ ] Acentos corretos em português
- [ ] Mínimo 3 layouts diferentes
- [ ] CTA no último slide
- [ ] Legenda no tom informal do Gabriel
- [ ] Hashtags relevantes (sem exagero)
- [ ] Crop 4:5 selecionado antes de avançar
