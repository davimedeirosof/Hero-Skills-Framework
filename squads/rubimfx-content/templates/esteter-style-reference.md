# Esteter Style Reference — Sistema Visual para @rubimfx

> Baseado na análise do @economesteter. Referência obrigatória para sub-agentes ao criar carrosséis no estilo Esteter.

---

## PALETA DE CORES

```
Background:     #0A0A0A  (near-black, NÃO preto puro)
Card:           #16181C
Border:         #2F3336
Text primary:   #E7E9EA
Text muted:     #71767B
Accent blue:    #1D9BF0
Alert red:      #F4212E
Green:          #00BA7C
```

---

## FONTES

- **Font family:** `-apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif`
- Headlines (capa): **40-48px**, weight **900**
- Tweet body: **28-32px**, weight **500**
- Termos-chave dentro do body: mesmo tamanho, weight **800**, opcionalmente cor `#1D9BF0`
- Labels/meta: **22-24px** mínimo
- **NADA abaixo de 20px em texto de conteúdo**

---

## 5 TIPOS DE SLIDE

### Type A — CAPA (Slide 1, sempre)

Template: `template-14-esteter-cover.html`

- Background: `#0A0A0A`
- **Profile row** (topo): foto circular 48px + "Gabriel Rubim ✓" + @rubimfx + ícone brand top-right
- **Badge**: emoji 🚨 (notícia/escândalo) ou 📊 (dados/mercado)
- **Headline**: 40-48px, branco, bold 900, 2-3 linhas máx. Palavras-chave em **BOLD**
- **Body text**: 24-28px, regular 500, 1-2 linhas
- **CTA**: "Entenda [frame]! 👇" em 24px
- **Bottom 45%**: 2 fotos REAIS lado a lado (personagens da história)
- Indicador de dots (slide position)

### Type B — TWEET THREAD CARD (Slides internos)

Template: `template-15-esteter-tweet.html`

- Simula um post real do X/Twitter
- **Header**: "← Post" esquerda, "X.com" direita
- **Profile**: foto circular + "Gabriel Rubim ✓" + @rubimfx
- **"Show translation"** link (decorativo)
- **Ponto numerado**: 1️⃣ "Título da seção" em bold ~32px
- **Body text**: ~28-32px, regular, 3-5 linhas máx. Frases-chave em **BOLD**
- **Timestamp**: "20:08 · 17/03/26"
- **Engagement bar**: reply, retweet, heart, bookmark icons
- **Abaixo do tweet**: screenshot real da matéria original (Metrópoles, Bloomberg, etc.)

### Type C — FULL SCREENSHOT (1-2 por carrossel)

Template: `template-16-esteter-screenshot.html`

- Print completo de matéria real (Metrópoles, Folha, Bloomberg, etc.)
- Chrome do browser simulado no topo (opcional)
- Sem overlay — print puro como prova de credibilidade
- Placeholder: `{{SCREENSHOT_IMG}}`

### Type D — DATA/STATS CARD

Template: `template-17-esteter-data.html`

- Background escuro com métrica grande centralizada
- **Número**: 56-72px, cor de destaque (vermelho ou azul)
- **Contexto abaixo**: 28-32px
- **Fonte/citação** no rodapé
- **Stats bar** com 2-3 valores

### Type E — CTA FINAL (Último slide)

Template: `template-18-esteter-cta.html`

- Gradiente escuro azul/roxo
- "Segue @rubimfx" proeminente
- Brand footer com logo/avatar

---

## ESTRUTURA PADRÃO — 10 SLIDES

```
Slide 01 → Type A — Capa (sempre)
Slide 02 → Type B — Tweet thread #1 (contexto/o que aconteceu)
Slide 03 → Type B — Tweet thread #2 (detalhes/números)
Slide 04 → Type C — Screenshot da matéria (prova/fonte)
Slide 05 → Type B — Tweet thread #3 (quem está envolvido)
Slide 06 → Type B — Tweet thread #4 (implicações)
Slide 07 → Type D — Data/Stats (números impactantes)
Slide 08 → Type C — Screenshot de segunda fonte
Slide 09 → Type B — Tweet thread #5 (conclusão/próximos passos)
Slide 10 → Type E — CTA final
```

---

## REGRAS DE FOTOS

- **SEMPRE** fotos reais editoriais (screenshots de sites de notícias, fotos de pessoas públicas)
- **NUNCA** fotos de IA ou stock genérico (Unsplash, Pexels)
- `profile-photo.jpeg` apenas para o avatar circular (48-52px)
- Fotos temáticas para áreas de conteúdo
- Screenshots de reportagens reais como prova de credibilidade
- Buscar via DuckDuckGo Images ou capturar via Firecrawl

---

## FÓRMULA DE HEADLINE

```
🚨 [REVELAÇÃO/FATO com nome + valor R$/% específico]
```

Exemplos:
- 🚨 JUIZ AFASTADO GANHAVA R$39 MIL/MÊS SEM TRABALHAR
- 📊 DÓLAR SOBE 12% EM 2026: O QUE ESTÁ POR TRÁS

Regras:
- SEMPRE inclua número específico (R$, %, quantidade)
- SEMPRE inclua nome de pessoa/instituição quando possível
- Palavras-chave em **BOLD** (JUIZ, R$39 MIL, DÓLAR)
- 2-3 linhas máximo
- Tom: revelação, escândalo, urgência

---

## FÓRMULA DE CAPTION

```
Bloco 1 (Hook): 🚨 [Headline espelhada] (1 frase, 15-25 palavras)

Bloco 2 (Contexto): [O que aconteceu] + [detalhe específico "bizarro"] + [fonte citada] (2-4 frases)

Bloco 3 (CTA): "Entenda [frame]! 👇" ou "Salva e manda pra quem precisa ver! 📊"

Bloco 4: Hashtags (5-7, #tema #nomes #instituições)
```

Exemplo:
```
🚨 Juiz afastado por corrupção continuava recebendo R$39 mil por mês do seu bolso

O CNJ descobriu que 126 magistrados punidos mantinham salários integrais. O custo? R$41 milhões por ano. Fonte: Agência Brasil.

Entenda o esquema! 👇

#justiça #judiciário #corrupção #cnj #stf #rubimfx #trading
```

---

## PLACEHOLDERS DOS TEMPLATES

### template-14 (Cover)
`{{BADGE_EMOJI}}` `{{HEADLINE}}` `{{BODY}}` `{{CTA}}` `{{PHOTO_1}}` `{{PHOTO_2}}`

### template-15 (Tweet)
`{{SLIDE_NUM}}` `{{SECTION_TITLE}}` `{{BODY}}` `{{SCREENSHOT_IMG}}`

### template-16 (Screenshot)
`{{SCREENSHOT_IMG}}`

### template-17 (Data)
`{{METRIC}}` `{{METRIC_LABEL}}` `{{CONTEXT}}` `{{STAT_1}}` `{{STAT_2}}` `{{STAT_3}}`

### template-18 (CTA)
Sem placeholders variáveis (branding fixo @rubimfx)

---

## QUANDO USAR ESTILO ESTETER

- ✅ Notícias de escândalo/corrupção/política
- ✅ Revelações com dados específicos
- ✅ Matérias com fontes jornalísticas citáveis
- ✅ Temas que geram indignação/engajamento
- ✅ Conteúdo com screenshots reais de reportagens
- ❌ Conteúdo educacional puro (preferir Minimal Clean)
- ❌ Mindset/motivação (preferir Personal Brand)
- ❌ Análise técnica de trading (preferir Neon Data)

---

## CHECKLIST DE VALIDAÇÃO

- [ ] Fonte mínima 20px em todo conteúdo
- [ ] Fotos reais (nunca IA/stock)
- [ ] profile-photo.jpeg sem ../
- [ ] Acentuação completa (á, é, í, ó, ú, ã, õ, ç)
- [ ] @rubimfx visível em todos os slides
- [ ] 1080x1350px
- [ ] HTML standalone (zero dependências externas)
- [ ] Headline com número/valor específico
- [ ] Alternância correta de tipos (A→B→B→C→B→B→D→C→B→E)
