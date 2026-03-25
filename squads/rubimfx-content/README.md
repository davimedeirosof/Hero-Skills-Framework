# Squad @rubimfx — Sistema de Produção de Conteúdo Instagram

> **Squad automatizada de IA que pesquisa notícias de mercado em tempo real, gera carrosséis educativos e publica direto no Instagram da @rubimfx**

---

## Visão Geral

O **Squad @rubimfx — Content OS** é um sistema multi-agente orquestrado que automatiza o ciclo completo de produção de conteúdo Instagram para a conta @rubimfx.

**O que faz:**
- Pesquisa notícias de mercado em tempo real (macro, economia, geopolítica)
- Gera 5 ângulos editoriais diferentes para cada notícia
- Cria carrosséis de 8-10 slides em HTML/CSS
- Renderiza slides como imagens PNG de alta qualidade
- Valida português com acentos completos
- Publica automaticamente no Instagram

**Para quem:**
- Traders e investidores brasileiros (público @rubimfx)
- Público de macro/economia/trading/forex
- Investidores interessados em mesa proprietária

**O que produz:**
- Carrosséis de 8-10 slides no feed Instagram
- 1 publicação a cada 24-48h
- 40% Macro/Notícias | 25% ICT/Educação | 15% Trade Analysis | 10% Summit Prop | 10% Mindset

---

## Equipe de Agentes (6 Agentes)

| # | Agente | Icon | Tipo | Função |
|---|--------|------|------|---------|
| 1 | **Nara Notícia** | 🔍 | Subagent | Pesquisa notícias de mercado em tempo real (Reuters, Bloomberg, Investing.com) |
| 2 | **Vitor Visual** | 🎨 | Subagent | Encontra imagens IA para carrosséis (CAT-1 a CAT-8) |
| 3 | **Iago Instagram** | 💡 | Inline | Gera 5 ângulos editoriais e estrutura de slides |
| 4 | **Léo Legenda** | ✍️ | Inline | Escreve captions com CTA para publicação |
| 5 | **Diana Design** | 🖼️ | Inline | Escolhe templates visuais (8 estilos distintos) |
| 6 | **Renata Revisão** | ✅ | Inline | Valida português, acentos, tipografia e qualidade |

---

## Fluxo Completo de Produção (12 Passos)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   PIPELINE DE CONTEÚDO @RUBIMFX                        │
└─────────────────────────────────────────────────────────────────────────┘

STEP 01: Pesquisa Focus (Checkpoint)
         └─→ Usuário define: tema (FOMC, dólar, ouro, etc) + período

STEP 02: Pesquisa de Notícias (Nara Notícia — Subagent)
         └─→ Busca Top 5 stories com fonte, dados, ativos impactados

STEP 02b: Visual Trends (Vitor Visual — Subagent)
         └─→ Identifica tendências de imagem para o tema

STEP 03: Seleção da Notícia (Checkpoint)
         └─→ Usuário escolhe qual das 5 notícias usar

STEP 04: Geração de Ângulos (Iago Instagram — Inline)
         └─→ Cria 5 ângulos editoriais distintos (Bridge, Educacional,
             Contrarian, Timeline, Prático)

STEP 05: Seleção do Ângulo (Checkpoint)
         └─→ Usuário escolhe qual dos 5 ângulos usar

STEP 06: Criação do Carrossel (Iago Instagram — Inline)
         └─→ Gera estrutura de slides (8-10) com placeholders

STEP 07: Escrita da Caption (Léo Legenda — Inline)
         └─→ Redige caption com hook, CTA, hashtags

STEP 08: Aprovação de Conteúdo (Checkpoint)
         └─→ Usuário aprova texto dos slides e caption

STEP 09: Criação de Visuais (Diana Design + Vitor Visual)
         └─→ Escolhe templates (8 tipos), categorias de imagem,
             processa fotos IA

STEP 10: Revisão (Renata Revisão — Inline)
         └─→ Valida português, acentos, fonts, dimensões 1080×1350

STEP 11: Pre-Flight Check (Checkpoint)
         └─→ Verifica: profile-photo.jpeg ✓, acentos ✓, fonts ✓,
             renderização ✓

STEP 12: Publicação e Música (Instagram + Celular)
         └─→ Publica carrossel, adiciona música pelo celular
```

### Passo 1: Pesquisa Focus (Checkpoint)
**Agente:** Nenhum
**Input:** Usuário define foco de pesquisa
**Output:** `research-focus.md`

Usuário escolhe:
- **Tema:** FOMC | Dados Econômicos | Commodities | Geopolítica | Forex | Mesa Prop | Evergreen
- **Período:** Últimas 24h | 7 dias | 1 mês | Evergreen

Exemplo:
```
Foco: FOMC — Decisão de juros do Federal Reserve
Horizonte: Últimas 24h
Palavras-chave: FOMC, Federal Reserve, taxa juros, DXY, ouro
```

### Passo 2: Pesquisa de Notícias
**Agente:** Nara Notícia (Subagent — powerful)
**Input:** `research-focus.md`
**Output:** `news-research.md`

Nara busca em:
- Reuters, Bloomberg, Financial Times (macro global)
- Investing.com, ForexFactory (dados econômicos)
- InfoMoney, Valor Econômico (perspectiva BR)
- Twitter/X analistas, relatórios de bancos centrais

Retorna **Top 5 Stories** com:
- Título e fonte
- Resumo (2-3 frases)
- Dados-chave (números concretos)
- Ativos impactados
- Bridge macro→trading (conexão com operação)
- Score (0-10)

Critério de score:
- Relevância para trading (3x)
- Potencial de engajamento (2x)
- Bridge macro→trading (2x)
- Frescor da notícia (1x)
- Originalidade (1x)

### Passo 3: Seleção da Notícia
**Tipo:** Checkpoint
**Input:** `news-research.md` (Top 5)
**Output:** Usuário marca "Selected Story"

Usuário escolhe qual das 5 notícias usar para o carrossel.

### Passo 4: Geração de Ângulos
**Agente:** Iago Instagram (Inline)
**Input:** Selected Story, company.md, style-guide
**Output:** `angles.md`

Iago cria **5 ângulos editoriais distintos** para a mesma notícia:

1. **Ângulo A: Bridge Macro→Trading**
   - Conecta evento macro com operação prática
   - Ex: "NFP fraco → dólar caiu → EUR/USD setup ativado"
   - Público: traders operacionais

2. **Ângulo B: Educacional**
   - Explica conceito no estilo @economesteter
   - Ex: "O que é FOMC e por que move o mercado?"
   - Público: iniciantes, alto save

3. **Ângulo C: Contrarian**
   - Questiona consenso, apresenta riscos
   - Ex: "Todo mundo bullish em ouro. Cuidado."
   - Público: analistas, debate

4. **Ângulo D: Timeline/Sequência**
   - Conta história cronologicamente
   - Ex: "Os 5 eventos que levaram ouro ao ATH"
   - Público: geral, narrativa forte

5. **Ângulo E: Prático/Impacto**
   - Impacto direto na vida do trader
   - Ex: "Selic subiu — o que muda no seu bolso?"
   - Público: @rubimfx específico, ação

Cada ângulo inclui:
- Hook (frase de impacto, máx 15 palavras)
- Estrutura de slides (6-10 slides)
- Tom predominante
- Justificativa ("por que funciona")

### Passo 5: Seleção do Ângulo
**Tipo:** Checkpoint
**Input:** `angles.md` (5 ângulos)
**Output:** Usuário marca "Selected Angle"

Usuário escolhe qual dos 5 ângulos usar.

### Passo 6: Geração dos Slides (HTML)
**Agente:** Iago Instagram (Inline)
**Input:** Selected Angle, templates catalog
**Output:** `carousel-draft.md` com HTML dos slides

Iago gera HTML puro (sem dependências externas) com:
- 8-10 slides
- Templates alternados (nunca 2 iguais consecutivos)
- Placeholders para: `{{PROFILE_PHOTO}}`, `{{USERNAME}}`, `{{DATE}}`, `{{HEADLINE}}`, `{{BIG_NUMBER}}`, `{{PHOTO_1}}`, `{{STAT_1}}`, etc
- Dimensões exatas: 1080×1350px (4:5)
- Fonts em português completo

Exemplo de slide HTML:
```html
<div class="slide" style="width: 1080px; height: 1350px; background: #000;">
  <div class="headline" style="font-size: 72px; color: #fff;">{{HEADLINE}}</div>
  <img src="{{PHOTO_1}}" alt="news" />
  <div class="stat" style="font-size: 48px; color: #1D9BF0;">{{BIG_NUMBER}}</div>
</div>
```

### Passo 7: Validação de Acentos
**Agente:** Renata Revisão (Inline)
**Input:** `carousel-draft.md`
**Output:** `carousel-validated.md`

Renata verifica:
- Português correto: é, á, ã, õ, ç (NUNCA omitir)
- Sem erros de digitação
- Sem jargão em inglês desnecessário
- Tone of voice consistente com @economesteter

**Regra de Ouro:** Português é tão importante quanto a renderização. Um acento faltando é problema.

### Passo 8: Renderização (PNG)
**Script:** `render_slides.py`
**Input:** HTML dos slides + imagens IA + profile-photo.jpeg
**Output:** 8-10 arquivos PNG (1080×1350 cada)

```bash
python scripts/render_slides.py \
  --carousel carousel-validated.md \
  --output output/posts/YYYY-MM-DD-slug/pngs \
  --headless false
```

Requisitos:
- `headless: false` obrigatório (permite ver a renderização)
- Server rodando na pasta `html/`
- Chrome **fechado** antes de começar Playwright
- `profile-photo.jpeg` na pasta root (sem `../`)

### Passo 9: Escrita da Caption
**Agente:** Léo Legenda (Inline)
**Input:** Selected Angle, dados da notícia
**Output:** Caption completa para Instagram

Caption inclui:
- Hook (frase de impacto)
- 2-3 pontos-chave
- Contextualização
- CTA claro ("Salve", "Compartilhe", "Comente sua opinião")
- Hashtags relevantes (máx 30)
- Menções (se pertinente)

Exemplo:
```
🔍 O Fed decidiu. O ouro ouviu.

O Federal Reserve manteve juros em 5.25%,
mas o dot plot revisou para baixo — maioria
prevê corte em junho.

Resultado? XAU/USD em ATH: $2.385 🎯

E o mercado já está precificando isso...

👇 O que você acha? Ouro vai voltar a
$2.200 ou segue em novo ciclo?

Comenta aí 👇

#Forex #Trading #Macro #Ouro #FOMC
#Economia #Mercado #Daytrader #Investimento
```

### Passo 10: Pre-Flight Check
**Script:** `preflight_check.py`
**Input:** Pasta `/output/posts/YYYY-MM-DD-slug/`
**Output:** Checklist de validação

Verifica:
- ✅ PNGs existem (8-10 arquivos)
- ✅ Dimensões: 1080×1350px exatas
- ✅ `profile-photo.jpeg` acessível
- ✅ Acentos presentes (é, á, ã, õ, ç)
- ✅ Fonts legíveis (mínimo 20px, headlines 64-80px)
- ✅ Contraste OK (WCAG AA)
- ✅ Caption formatada
- ✅ Hashtags em ordem

```bash
python scripts/preflight_check.py \
  --post-folder output/posts/2026-03-16-dino-juizes
```

Se passar: `✅ PRÉ-VÔO AUTORIZADO`

Se falhar: lista exata do que corrigir.

### Passo 11: Publicação no Instagram
**Script:** `publish_carousel.py`
**Input:** Folder com PNGs validados + caption
**Output:** Post publicado em @rubimfx

```bash
python scripts/publish_carousel.py \
  --post-folder output/posts/2026-03-16-dino-juizes \
  --caption "caption-aqui.txt" \
  --publish true
```

Método: Playwright MCP (headless: false)
- Loga na conta @rubimfx (sessão persistente)
- Faz upload de cada PNG
- Configura caption e hashtags
- Publica carrossel

**Importante:** Antes de publicar, selecionar **proporção 4:5** no crop do Instagram (não automático).

### Passo 12: Pós-Publicação (Música)
**Manual pelo celular**

Após publicar:
1. Abrir o post no Instagram pelo celular
2. Clicar em "Editar"
3. Selecionar música (sugestões: de acordo com tema)
4. Salvar

Spotify playlists recomendadas:
- Tema Macro/Economia: "Business & Ambition"
- Tema Trading: "Focused Energy"
- Tema Análise: "Deep Focus"
- Tema Urgência: "High Intensity"

---

## Templates Visuais (8 Estilos)

Cada slide pode usar um dos 8 templates. Nunca 2 templates iguais consecutivos.

| # | Nome | Descrição | Quando Usar | Paleta |
|---|------|-----------|------------|--------|
| **01** | Dark Tweet | Estética X/Twitter. Fundo preto, card de tweet, badge alerta, foto collage, barra stats. Ambient glow azul. | Slide cover (impacto máximo), notícias virais | `#000` bg, `#16181C` card, `#1D9BF0` azul |
| **02** | News Magazine | Editorial premium de revista. Foto hero, barra fonte vermelha, manchete serifa, stats. Fundo branco. | Slides 2-3 (artigos reais, manchetes), contexto jornalístico | `#F4F4F4` bg, `#CC0000` vermelho |
| **03** | Neon Data | Tech/futurista. Deep navy, grid de linhas, glow cyan/verde, número gigante neon, 4 data cards, dashboard. | Slides com números, análise dados, estatísticas macro | `#060611` bg, `#00FFE0` cyan, `#FF3B3B` vermelho |
| **04** | Minimal Clean | Minimalista puro. Fundo branco, headline 64px massiva, subhead, callout box azul, espaço branco. | Slides 4-5 ou 8 (contexto, explicação, narrativa), pós-impacto | `#FFFFFF` bg, `#0A0A0A` título, `#1A56DB` accent |
| **05** | Breaking News | CNN/GloboNews ao vivo. Dark preto-vermelho, glow vermelho, foto 30% opacidade, breaking bar vermelha, headline 68px, stats translúcidos. | Notícias urgentes, decisões históricas, eventos impactantes | `#0D0000` bg, `#E00000` vermelho, `#FFD700` dourado |
| **06** | Personal Brand | Foto full-bleed, gradiente escuro, texto sobreposto branco, aspas douradas, badge translúcido, CTA pílula. | Último slide (CTA/engajamento), opinião pessoal, call-to-action | `#000` bg, `#FFFFFF` texto, `#F5C842` dourado |
| **07** | Infographic | @visualcapitalist. Cinza claro, header escuro, seção título branca, 4 stats coloridos, tabela comparação, gráfico barras. | Comparações, rankings, timelines, antes/depois, análise macro | `#F0F2F5` bg, `#FFFFFF` cards, `#059669` verde |
| **08** | Meme Editorial | Browser/app móvel simulado. Chrome bar, status bar, URL bar, screenshot de artigo como BG, banner amarelo irônico sobreposto, reações emoji, atribuição. | Reação irônica a notícia absurda, humor inteligente nicho, alto viral | `#1C1C1E` chrome, `#FFD60A` amarelo, `#FF453A` vermelho |

### Sequência Padrão (10 Slides)

```
Slide 01 → Template 01 (Dark Tweet)      — Cover de impacto máximo
Slide 02 → Template 02 (News Magazine)   — Fonte/artigo que embasou
Slide 03 → Template 08 (Meme Editorial)  — Screenshot irônico / contexto
Slide 04 → Template 03 (Neon Data)       — Os números / dados
Slide 05 → Template 04 (Minimal Clean)   — Explicação / por que importa
Slide 06 → Template 03 (Neon Data)       — Mais dados / segundo ângulo
Slide 07 → Template 05 (Breaking News)   — O impacto / urgência
Slide 08 → Template 04 (Minimal Clean)   — Análise / consequências
Slide 09 → Template 07 (Infographic)     — Comparativo / conclusão visual
Slide 10 → Template 06 (Personal Brand)  — CTA / engajamento pessoal
```

Regra: Nunca 2 templates iguais consecutivos.

---

## Categorias de Imagem IA (8 Categorias)

Quando precisa de imagem, pedir especificando a categoria:

| Sigla | Nome | Descrição | Exemplos | Estilo |
|-------|------|-----------|----------|--------|
| **CAT-1** | 📸 Foto Realista | Cenário realista, contexto | Wall Street, Banco Central, STF, sala trading | Fotojornalismo editorial, Canon EOS R5 |
| **CAT-2** | 🤖 Ilustração Conceitual | IA, tecnologia, conceitos abstratos | Robôs mercado, cérebro digital, rede neural | Digital art, neon azul/cyan, futurista |
| **CAT-3** | 📰 Composição Editorial | Pessoa + dados + contexto jornalístico | Empresário com gráficos, juiz tribunal | Bloomberg/Reuters, luz dramática |
| **CAT-4** | 🔥 Thumbnail Impactante | Maximum impact para cover | Close-up dramático, objeto simbólico | Alto contraste, fundo escuro, close-up |
| **CAT-5** | 📊 Dados Visuais | Gráficos, comparativos, dashboards | Gráfico 3D, dashboard holográfico, moedas | 3D render, fundo escuro, elementos brilhantes |
| **CAT-6** | 🌍 Geopolítica/Macro | Guerra, petróleo, moedas, comércio global | Globo com rotas, barris petróleo, bandeiras | Cinematográfico, tensão, tons escuros |
| **CAT-7** | 🧠 Mindset/Motivacional | Psicologia trader, disciplina, jornada | Meditação, xadrez, montanha, espelho | Tons dourados + sombras frias, emocional |
| **CAT-8** | 🇧🇷 Brasil/Política | Política brasileira, economia nacional | Congresso, Real, Planalto, supermercado | Documental jornalístico, luz natural |

Exemplo de request:
```
"Gera uma imagem CAT-4 mostrando close-up de moedas/dólar em queda livre"
"Preciso de uma CAT-5 mostrando gráfico 3D da Selic 2025 vs 2026"
"Faz uma CAT-8 do Congresso Nacional pra cover sobre reforma tributária"
```

---

## Scripts de Automação

Todos os scripts estão em `/squads/rubimfx-content/scripts/`

| Script | O que faz | Como usar |
|--------|-----------|-----------|
| **generate_slide.py** | Gera HTML de um slide com placeholders | `python scripts/generate_slide.py --template 01 --output output.html` |
| **find-photos.js** | Busca imagens IA para o tema do carrossel | `node scripts/find-photos.js --theme FOMC --category CAT-1` |
| **fetch_images.py** | Baixa/processa imagens IA (Nano Banana 2) | `python scripts/fetch_images.py --carousel carousel.md` |
| **render_slides.py** | Renderiza HTML → PNG (Playwright) | `python scripts/render_slides.py --carousel carousel.md --output /posts/pngs` |
| **validate_accents.py** | Valida português, acentos, tipografia | `python scripts/validate_accents.py --html carousel.html` |
| **preflight_check.py** | Checa antes de publicar (PNGs, acentos, fonts) | `python scripts/preflight_check.py --post-folder output/posts/2026-03-16-slug` |
| **publish_carousel.py** | Publica carrossel no Instagram | `python scripts/publish_carousel.py --post-folder output/posts/2026-03-16-slug --publish true` |

---

## Estrutura de Pastas

```
squads/rubimfx-content/
├── README.md                          ← Você está aqui
├── squad.yaml                         ← Config principal da squad
│
├── agents/                            ← Definições de agentes
│   ├── nara-noticia/
│   │   ├── agent.md
│   │   └── tasks/
│   ├── vitor-visual/
│   │   ├── agent.md
│   │   └── tasks/
│   ├── iago-instagram/
│   │   ├── agent.md
│   │   └── tasks/
│   ├── leo-legenda/
│   │   ├── agent.md
│   │   └── tasks/
│   ├── diana-design/
│   │   ├── agent.md
│   │   └── tasks/
│   └── renata-revisao/
│       ├── agent.md
│       └── tasks/
│
├── templates/                         ← Templates HTML dos slides
│   ├── catalog.md                     ← Referência dos 8 templates
│   ├── image-categories.md            ← Referência das 8 categorias de imagem
│   ├── template-01-dark-tweet.html
│   ├── template-02-news-magazine.html
│   ├── template-03-neon-data.html
│   ├── template-04-minimal-clean.html
│   ├── template-05-breaking-news.html
│   ├── template-06-personal-brand.html
│   ├── template-07-infographic.html
│   └── template-08-meme-editorial.html
│
├── scripts/                           ← Scripts de automação
│   ├── generate_slide.py              ← Gera HTML de slides
│   ├── find-photos.js                 ← Busca imagens IA
│   ├── fetch_images.py                ← Baixa imagens
│   ├── render_slides.py               ← HTML → PNG
│   ├── validate_accents.py            ← Valida português
│   ├── preflight_check.py             ← Pre-flight check
│   └── publish_carousel.py            ← Publica Instagram
│
├── html/                              ← Servidor HTTP para renderização
│   ├── index.html
│   ├── css/
│   └── js/
│
├── pipeline/                          ← Definições do pipeline
│   ├── steps/
│   │   ├── step-01-research-focus.md
│   │   ├── step-02-news-research.md
│   │   ├── step-02b-visual-trends.md
│   │   ├── step-03-news-selection.md
│   │   ├── step-04-generate-angles.md
│   │   ├── step-05-angle-selection.md
│   │   ├── step-06-create-carousel.md
│   │   ├── step-07-write-caption.md
│   │   ├── step-08-content-approval.md
│   │   ├── step-09-create-visuals.md
│   │   ├── step-10-review.md
│   │   └── step-11-final-approval.md
│   └── data/
│       ├── research-focus.md          ← Foco de pesquisa do usuário
│       ├── domain-framework.md        ← Framework de domínio
│       ├── quality-criteria.md        ← Critérios de qualidade
│       ├── output-examples.md         ← Exemplos de output
│       ├── anti-patterns.md           ← O que NUNCA fazer
│       ├── tone-of-voice.md           ← Tom de voz @rubimfx
│       └── style-guide-economesteter.md ← Style guide
│
└── output/                            ← Conteúdo produzido
    ├── news-research.md               ← Top 5 notícias
    ├── angles.md                      ← 5 ângulos editoriais
    ├── carousel-draft.md              ← HTML dos slides
    ├── carousel-validated.md          ← HTML validado
    ├── caption.txt                    ← Caption para Instagram
    │
    ├── templates/
    │   └── slide-variations-catalog.md ← Catálogo de variações
    │
    └── posts/                         ← Posts já publicados
        ├── 2026-03-16-dino-juizes/
        │   ├── carousel.html
        │   ├── carousel.md
        │   ├── caption.txt
        │   ├── pngs/
        │   │   ├── 01.png
        │   │   ├── 02.png
        │   │   ├── ...
        │   │   └── 10.png
        │   ├── images/
        │   │   ├── photo-1.jpg
        │   │   ├── photo-2.jpg
        │   │   └── ...
        │   └── metadata.json
        │
        ├── 2026-03-16-economia-bolso/
        ├── 2026-03-16-ia-agentica/
        ├── 2026-03-16-mercado-brutal/
        ├── 2026-03-16-operando-ou-apostando/
        └── 2026-03-16-ouro-5000/
```

---

## Regras de Ouro (NUNCA quebrar)

1. **Dimensões exatas:** 1080×1350px (proporção 4:5 do Instagram feed)
   - Não aceitar 1080×1080 (quadrado)
   - Não aceitar 1080×2000 (stories)

2. **Fontes mínimas de leitura:**
   - Headlines: 64-80px (bold)
   - Body text: 28-34px
   - Labels/stats: 22px+
   - Nada, absolutamente nada, abaixo de 20px

3. **Português correto com acentuação completa:**
   - é, á, ã, õ, ç obrigatórios
   - Não aceitar "ECONOMIA" em vez de "ECONÔMIA"
   - Não aceitar "SEO" em vez de "SÉO"
   - Validar com `validate_accents.py` SEMPRE

4. **Profile photo sem `../`:**
   - Usar: `src="profile-photo.jpeg"`
   - NUNCA: `src="../profile-photo.jpeg"`
   - Arquivo deve estar na raiz: `/squads/rubimfx-content/profile-photo.jpeg`

5. **Servidor HTTP obrigatório:**
   - Rodar servidor em `/squads/rubimfx-content/html/`
   - Playwright precisa acessar via `http://localhost:8000/slide-01.html`
   - Não funciona com file:/// local

6. **Proporção de crop no Instagram:**
   - Antes de avançar após publicação, selecionar **4:5** no crop
   - Não usar "automático"
   - Certificar que imagem preenche tela verticalmente

7. **Chrome fechado antes de renderizar:**
   - Playwright não consegue abrir janela se Chrome já está rodando
   - Fechar completamente (não apenas minimizar)
   - Se erro "Chrome is already running", matar processo: `pkill -f Chrome`

8. **Headless obrigatoriamente FALSE:**
   - Usar: `--headless false`
   - Permite ver a renderização em tempo real
   - Mais lento mas essencial para debug

9. **Música adicionada manualmente pelo celular:**
   - Script publica carrossel
   - No celular, abrir post > Editar > Selecionar música
   - Não tenta adicionar via script (ainda não suportado)

10. **Alternância de templates obrigatória:**
    - Nunca 2 slides com mesmo template consecutivos
    - Validar com `validate_accents.py --check-templates`

11. **Imagens IA com categoria obrigatória:**
    - Sempre especificar CAT-1 a CAT-8
    - Nunca pedir imagem genérica
    - Descrever contexto visual específico

12. **Validação de qualidade pré-publicação:**
    - Rodar `preflight_check.py` SEMPRE
    - Não publicar com erros reportados pelo script
    - Checklist visual: acentos, tamanho fonte, contraste

---

## Estratégia de Conteúdo

A estratégia @rubimfx é **Macro-First**: atrai público amplo com economia/notícias e depois direciona para trading especializado.

### Mix de Conteúdo

```
40% Macro/Economia/Notícias
   → Notícias em tempo real
   → Análise de decisões econômicas
   → Impacto em ativos
   → Alto engajamento (topo de funil)

25% ICT/Educação (Smart Money Concepts)
   → Conceitos de Order Flow
   → Estruturas de mercado (FVG, breakers)
   → Análise técnica avançada
   → Retenção de público interessado em trading

15% Trade Analysis
   → Análise de trades feitos
   → Prova social
   → Resultados operacionais
   → Conversão para Summit Prop

10% Summit Prop
   → Chamadas para mesa proprietária
   → Histórias de aprovação
   → Desafios de prop trading
   → Conversão

10% Mindset + Order Flow
   → Psicologia do trader
   → Disciplina, gestão emocional
   → Jornada de aprendizado
   → Diferenciação
```

### Bridge Macro→Trading (DIFERENCIAL ÚNICO)

A conexão que diferencia @rubimfx:
```
Evento Macro (FOMC)
   ↓
Qual ativo move? (DXY, XAU/USD)
   ↓
Qual é a estrutura técnica? (FVG, order block)
   ↓
Qual é o setup operável? (Entrada, SL, TP)
   ↓
Como eu operei isso? (Resultado real)
```

Exemplo prático:
```
"NFP fraco (110K vs 180K esperado)
 → Dólar caiu (DXY abaixo 104)
 → EUR/USD rompeu 1.0900 (liquidity sweep)
 → Eu estava comprado em EUR/USD desde 1.0850
 → Peguei até 1.0940 (90 pips)
 → Sai antes do close (Fed fala em 2h)
```

---

## Comandos Rápidos

### Rodar a squad completa
```bash
/opensquad run rubimfx-content
```

### Criar novo carrossel (passo a passo)
```bash
# Step 01: Define o foco
/opensquad run rubimfx-content --start-at step-01

# Após escolher o foco, aguarda Step 02 (Nara pesquisa)

# Step 03: Escolhe notícia dentre Top 5
# Step 04: Gera 5 ângulos (Iago)
# Step 05: Escolhe 1 ângulo
# Step 06: Gera carrossel HTML (Iago)
# Step 07: Escreve caption (Léo)
# Step 08: Aprova conteúdo
# Step 09: Gera visuais (Diana + Vitor)
# Step 10: Revisa (Renata)
# Step 11: Pre-flight check
# Step 12: Publica (Playwright)
```

### Renderizar slides manualmente
```bash
cd /squads/rubimfx-content

# 1. Rodar servidor HTTP
python -m http.server 8000 --directory html &

# 2. Renderizar
python scripts/render_slides.py \
  --carousel output/carousel-validated.md \
  --output output/posts/$(date +%Y-%m-%d-novo-post)/pngs

# 3. Validar
python scripts/validate_accents.py \
  --html output/carousel-validated.md

# 4. Pre-flight check
python scripts/preflight_check.py \
  --post-folder output/posts/$(date +%Y-%m-%d-novo-post)
```

### Publicar carrossel
```bash
python scripts/publish_carousel.py \
  --post-folder output/posts/2026-03-16-seu-tema \
  --caption "seu-caption.txt" \
  --publish true
```

### Editar squad
```bash
/opensquad edit rubimfx-content
```

### Ver histórico de posts
```bash
ls -la output/posts/
```

---

## Configuração Inicial (Do Zero)

### 1. Instalar dependências

```bash
cd /squads/rubimfx-content

# Python venv
python -m venv venv
source venv/bin/activate

# Dependências Python
pip install -r requirements.txt
# Esperado: playwright, pillow, requests, instagrapi

# Playwright browsers
playwright install chromium
```

### 2. Configurar variáveis de ambiente

Criar `.env`:
```
INSTAGRAM_USERNAME=rubimfx
INSTAGRAM_PASSWORD=sua-senha-aqui
INSTAGRAM_2FA_CODE=não-necessário-se-usar-sessão-persistente

AI_MODEL=claude-3-5-sonnet
AI_API_KEY=sua-chave-anthropic

NANO_BANANA_API=sua-chave-nano-banana
UNSPLASH_API=sua-chave-unsplash

# Playwright config
HEADLESS=false
BROWSER=chromium
```

### 3. Configurar Playwright

No arquivo `/squads/rubimfx-content/scripts/render_slides.py`:
```python
browser = await p.chromium.launch(
    headless=False,  # OBRIGATÓRIO
    args=['--start-maximized']
)
```

### 4. Copiar profile-photo.jpeg

```bash
cp /seu-arquivo/profile-photo.jpeg \
   /squads/rubimfx-content/profile-photo.jpeg
```

Deve ser quadrada (1:1), mínimo 200×200px, idealmente 500×500px.

### 5. Testar renderização básica

```bash
# Rodar servidor
python -m http.server 8000 --directory html &

# Testar renderização de 1 slide
python scripts/render_slides.py \
  --template template-01 \
  --output test-output.png

# Deve gerar: test-output.png (1080×1350)
```

Se passar em tudo: Sistema pronto! 🚀

---

## Troubleshooting

### ❌ "Chrome is already running"
**Causa:** Outra instância de Chrome/Chromium está aberta
**Solução:**
```bash
pkill -f Chrome
pkill -f Chromium
# Aguardar 3s
python scripts/render_slides.py ...
```

### ❌ "Profile photo 404 / File not found"
**Causa:** `profile-photo.jpeg` não está na raiz ou path incorreto
**Solução:**
```bash
# Verificar localização
ls -la /squads/rubimfx-content/profile-photo.jpeg

# No HTML, usar SEMPRE: src="profile-photo.jpeg"
# NUNCA: src="../profile-photo.jpeg" ou src="/profile-photo.jpeg"
```

### ❌ "Imagem cortada no Instagram"
**Causa:** Usuário não selecionou 4:5 no crop
**Solução:**
1. Abrir post
2. Editar
3. Selecionar "Proporção: 4:5"
4. NÃO usar "automático"
5. Salvar

### ❌ "Acentos faltando (é virou e)"
**Causa:** Encoding UTF-8 não configurado corretamente
**Solução:**
```python
# No início de todo script:
import sys
sys.stdout.reconfigure(encoding='utf-8')

# No HTML:
<meta charset="UTF-8">

# Validar com:
python scripts/validate_accents.py --carousel carousel.html
```

### ❌ "Fonte muito pequena (pixel peeping)"
**Causa:** Headlines < 64px ou body < 28px
**Solução:** Aumentar:
```html
<!-- Errado (20px) -->
<h1 style="font-size: 20px;">Título</h1>

<!-- Certo (72px) -->
<h1 style="font-size: 72px; font-weight: bold;">Título</h1>
```

Validar com: `python scripts/validate_accents.py --check-fonts`

### ❌ "Instagrapi 2FA bloqueado"
**Causa:** Instagram detectou login suspeito
**Solução:**
```bash
# Usar sessão persistente (salva cookies)
# Primeira vez: fazer login manualmente
python scripts/publish_carousel.py --first-login true

# Próximas vezes: reutiliza sessão (sem 2FA)
python scripts/publish_carousel.py --post-folder ... --publish true
```

### ❌ "Servidor HTTP não inicia"
**Causa:** Porta 8000 já em uso
**Solução:**
```bash
# Matar processo anterior
lsof -i :8000 | grep LISTEN | awk '{print $2}' | xargs kill -9

# Usar porta diferente
python -m http.server 9000 --directory html &
# E ajustar no script: http://localhost:9000/slide-01.html
```

### ❌ "Carrossel não publica (erro Instagrapi)"
**Causa:** Credenciais incorretas ou conta bloqueada
**Solução:**
```bash
# Testar credenciais
python -c "
from instagrapi import Client
cl = Client()
cl.login('seu-user', 'sua-senha')
print('Login OK')
"

# Se falhar: resetar senha no Instagram e tentar novamente
```

### ❌ "HTML não renderiza (imagem branca)"
**Causa:** Servidor não rodando ou CSS quebrado
**Solução:**
```bash
# Verificar servidor está up
curl http://localhost:8000/slide-01.html

# Se erro 404: arquivo não existe
# Se erro 500: CSS quebrado

# Ver logs do Playwright:
python scripts/render_slides.py --verbose
```

---

## Posts Produzidos

Histórico de carrosséis publicados em @rubimfx:

| Data | Tema | Ângulo | Slides | Status | Link |
|------|------|--------|--------|--------|------|
| 2026-03-16 | Dino pune juízes | Impacto econômico | 10 | ✅ Publicado | [@rubimfx/1234...](https://instagram.com/rubimfx) |
| 2026-03-16 | Economia vs Bolso | Prático/Impacto | 8 | ✅ Publicado | [@rubimfx/1235...](https://instagram.com/rubimfx) |
| 2026-03-16 | IA Agentica | Bridge Macro→Trading | 9 | ✅ Publicado | [@rubimfx/1236...](https://instagram.com/rubimfx) |
| 2026-03-16 | Mercado Brutal | Timeline | 10 | ✅ Publicado | [@rubimfx/1237...](https://instagram.com/rubimfx) |
| 2026-03-16 | Operando ou Apostando | Educacional | 8 | ✅ Publicado | [@rubimfx/1238...](https://instagram.com/rubimfx) |
| 2026-03-16 | Ouro $5000 | Contrarian | 9 | ✅ Publicado | [@rubimfx/1239...](https://instagram.com/rubimfx) |

---

## Referências de Qualidade

### Perguntas de Auto-Check Antes de Publicar

- [ ] Dimensões exatas 1080×1350?
- [ ] Todos os acentos presentes (é, á, ã, õ, ç)?
- [ ] Headlines legíveis (64-80px)?
- [ ] Body text legível (28-34px)?
- [ ] Templates alternados (nunca 2 iguais)?
- [ ] Profile photo acessível?
- [ ] Fonte jornalística citada?
- [ ] Ângulo diferenciado (não cópia)?
- [ ] Bridge macro→trading claro (se aplicável)?
- [ ] Caption com CTA?
- [ ] Preflight check passou?

### Exemplos de Ângulos Fracos (Evitar)

```
❌ "Entenda o que aconteceu ontem no mercado"
   (Genérico demais)

❌ "3 coisas que você precisa saber"
   (Clickbait vago)

❌ "O Fed subiu juros"
   (Sem bridge, sem impacto)
```

### Exemplos de Ângulos Fortes (Inspiração)

```
✅ "NFP fraco → dólar caiu → EUR/USD liquidity sweep → meu setup"
   (Específico, ponte clara)

✅ "O Fed sinaliza corte em junho. O ouro já precificou. Você ainda não?"
   (Provocação, dados, urgência)

✅ "5 eventos em cadeia que você não viu levaram ouro a $2.385"
   (Narrativa, educacional, profundo)
```

---

## Glossário de Termos

| Termo | Significado |
|-------|------------|
| **Carrossel** | Post Instagram com 2-10 imagens que usuário desliza |
| **Hook** | Frase de impacto no slide 1 que prende atenção (máx 15 palavras) |
| **Bridge Macro→Trading** | Conexão entre evento econômico e operação prática |
| **FVG** | Fair Value Gap (estrutura de mercado ICT) |
| **Order Block** | Zona de demanda/oferta onde instituições operaram |
| **Liquidity Sweep** | Acionamento de stops antes de reversão |
| **ATH** | All Time High (máxima histórica) |
| **Prop Trading** | Mesa proprietária (Summit Prop) |
| **SMC/ICT** | Smart Money Concepts / Inner Circle Trader (método) |
| **Dot Plot** | Projeção de juros futuros do Federal Reserve |
| **DXY** | Dollar Index (índice do dólar americano) |
| **XAU/USD** | Par forex: Ouro vs Dólar |
| **Slider** | Uma imagem individual do carrossel |
| **Preflight** | Checklist antes de publicação |
| **Headless** | Modo browser sem interface visual |

---

## Suporte e Próximas Etapas

### Próximas Features
- [ ] Agendamento automático de publicações
- [ ] Auto-resposta de comentários com IA
- [ ] Análise de performance (likes, saves, comments) por tipo de conteúdo
- [ ] Integração com TradingView (charts em tempo real)
- [ ] Publicação em Stories + Reels + Feed (em vez de só feed)
- [ ] Adição de música automática via API Spotify

### Como Reportar Problemas
1. Descrever o erro exato (print screen se possível)
2. Indicar qual script falhou
3. Anexar log completo (se houver)
4. Tentar reproduzir de novo para confirmar

### Contato
- **Responsável Squad:** Gabriel Rubim (@rubimfx)
- **Agentes IA:** Nara, Vitor, Iago, Léo, Diana, Renata

---

**Última atualização:** 16 de março de 2026
**Versão:** 1.0
**Status:** Ativo em produção

