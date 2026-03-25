# Twitter Dark (Modelo Dino) -- Referencia Compacta para Sub-Agentes

**LEIA ESTE DOCUMENTO INTEIRO ANTES DE CRIAR QUALQUER SLIDE.**
**NAO pule nenhuma secao. Cada slide tem um design UNICO.**

---

## REGRA #1: CADA SLIDE TEM UM LAYOUT COMPLETAMENTE DIFERENTE

Os 10 slides usam 7 tipos distintos de card. Se voce criar 2 slides parecidos, o carrossel sera REJEITADO.

---

## DIMENSOES E BASE CSS (obrigatorio em TODOS os slides)

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1080px;
  height: 1350px;
  background: #000000;
  font-family: -apple-system, "Segoe UI", Arial, sans-serif;
  color: #E7E9EA;
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
}
```

Meta tag obrigatoria: `<meta name="viewport" content="width=1080">`

---

## PALETA DE CORES

| Uso | Cor | Hex |
|-----|-----|-----|
| Fundo principal | Preto | `#000000` ou `#0D0000` |
| Cards/containers | Dark gray | `#16181C` ou `#1a1a2a` |
| Bordas | Gray | `#2F3336` ou `rgba(255,255,255,0.1)` |
| Destaque vermelho | Red | `#F4212E` ou `#FF3333` |
| Destaque azul | Blue | `#1D9BF0` |
| Destaque verde | Green | `#00BA7C` |
| Texto principal | Light | `#E7E9EA` |
| Texto muted | Gray | `#71767B` |
| Destaque laranja | Orange | `#FFA500` |
| Destaque roxo | Purple | `#7856FF` |

---

## REGRAS DE FONTES -- MINIMOS ABSOLUTOS

| Elemento | Tamanho | Weight |
|----------|---------|--------|
| Headlines (titulos principais) | 38-56px | 800-900 |
| Sub-headlines | 26-48px | 600-800 |
| Body text | 22-36px | 500 |
| Bullets/items | 21-32px | 500-600 |
| Labels/meta/captions | 22px MINIMO | 600-700 |
| Stat values | 26-54px | 900 |
| Big numbers (hero) | 96-180px | 900 |

**PROIBIDO: Qualquer font-size abaixo de 20px.**

Excecoes UNICAS permitidas abaixo de 20px (SOMENTE estes elementos decorativos):
- `.profile-name` (17px) -- nome do perfil no profile row
- `.profile-handle` (15px) -- @handle no profile row
- `.meta-time`, `.meta-views` (14px) -- metadata de tweet
- `.slide-counter` (13-14px) -- contador de slide
- `.breaking-badge` (13px) -- badge de urgencia
- `.stat-label` em stats bar sobre fotos (13px)
- `.card-row-label` no comparativo (11px)
- `.browser-url` (13px) -- URL na barra de browser
- `.article-source`, `.article-category` (12px) -- fonte do artigo
- `.image-caption` (12-13px) -- legenda de foto em artigos
- `.byline-name`, `.byline-date` (13-14px) -- autor em artigos
- `.translation-label` (12px) -- label "Traducao"
- `.card-label-top` (13px) -- label sobre big number

**Regra: Se o texto e LIDO pelo usuario como conteudo, deve ter NO MINIMO 20px. Os itens acima sao decorativos/contextuais.**

---

## REGRAS DE FOTOS

1. **NUNCA usar URLs do Unsplash, Pexels, ou qualquer CDN externo**
2. **Todas as imagens devem ser arquivos locais** na pasta `html/` (ex: `src="photo-dino.jpg"`)
3. **Fotos REAIS**: screenshots de reportagens, fotos de politicos/CEOs, fotos de locais reais
4. **Buscar via DuckDuckGo Images** ou capturar screenshots via Firecrawl
5. **Fallback**: se nao encontrar foto adequada, use gradiente ou cor solida + icone SVG inline
6. Fotos com `object-fit: cover; object-position: center top;`
7. Fotos em cards: `border-radius: 18px`
8. Gradient overlay em fotos de fundo: `linear-gradient(180deg, rgba(0,0,0,0.25) 0%, rgba(0,0,0,0.6) 100%)`

### Quando usar profile-photo.jpeg
- **SIM**: No profile-row (avatar 52px, circulo com borda azul) -- slides 1-10
- **SIM**: No CTA final (slide 10, avatar 44px)
- **NAO**: Como foto de fundo ou foto principal em NENHUM slide

### Profile Row (reutilizar em quase todos os slides dark)

```css
.profile-row {
  display: flex;
  align-items: center;
  gap: 14px;
}
.profile-pic {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #1D9BF0;
  flex-shrink: 0;
}
.profile-name {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 17px;
  font-weight: 700;
  color: #E7E9EA;
}
.profile-handle { font-size: 15px; color: #71767B; }
```

HTML (copiar e colar -- inclui verified badge SVG):
```html
<div class="profile-row">
  <img class="profile-pic" src="profile-photo.jpeg" alt="rubimfx">
  <div>
    <div class="profile-name">
      rubimfx
      <svg class="verified" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M20.396 11c-.018-.646-.215-1.275-.57-1.816-.354-.54-.852-.972-1.438-1.246.223-.607.27-1.264.14-1.897-.131-.634-.437-1.218-.882-1.687-.47-.445-1.053-.75-1.687-.882-.633-.13-1.29-.083-1.897.14-.273-.587-.704-1.086-1.245-1.44S11.647 1.62 11 1.604c-.646.017-1.273.213-1.813.568s-.969.854-1.24 1.44c-.608-.223-1.267-.272-1.902-.14-.635.13-1.22.436-1.69.882-.445.47-.749 1.055-.878 1.688-.13.633-.08 1.29.144 1.896-.587.274-1.087.705-1.443 1.245-.356.54-.555 1.17-.574 1.817.02.647.218 1.276.574 1.817.356.54.856.972 1.443 1.245-.224.606-.274 1.263-.144 1.896.13.634.433 1.218.877 1.688.47.443 1.054.747 1.687.878.633.132 1.29.084 1.897-.136.274.586.705 1.084 1.246 1.439.54.354 1.17.551 1.816.569.647-.016 1.276-.213 1.817-.567s.972-.854 1.245-1.44c.604.239 1.266.296 1.903.164.636-.132 1.22-.438 1.69-.882.445-.47.749-1.055.878-1.687.13-.633.08-1.29-.144-1.896.587-.274 1.087-.705 1.443-1.246.354-.54.553-1.17.57-1.817zm-6.081.414L9.24 16.8a.75.75 0 01-1.06 0l-2.52-2.52a.75.75 0 111.06-1.06l1.99 1.99 4.544-4.992a.75.75 0 011.103 1.014l-.002.002z" fill="#1D9BF0"/>
      </svg>
    </div>
    <div class="profile-handle">@rubimfx</div>
  </div>
</div>
```

CSS para verified:
```css
.verified { width: 20px; height: 20px; flex-shrink: 0; }
```

---

## OS 10 SLIDES -- ESTRUTURA E CSS DE CADA UM

---

### SLIDE 1: CAPA BREAKING NEWS
**Tipo:** Tweet card escuro no topo + collage de 2 fotos na parte inferior + stats bar

**Layout:**
- Top half: profile-row + breaking-badge + tweet-card (headline 38px w900 + body 23px)
- Bottom half: 2 fotos lado a lado (60% / 40%) com divider de 3px
- Stats bar overlay no fundo das fotos (3 valores coloridos)

**Background:** `#000` com radial-gradient azul sutil

**Elementos-chave CSS:**
```css
.breaking-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(244,33,46,0.15);
  border: 1.5px solid rgba(244,33,46,0.5);
  border-radius: 100px;
  padding: 6px 20px;
  font-size: 13px;
  font-weight: 700;
  color: #F4212E;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}

.tweet-card {
  background: #16181C;
  border: 1px solid #2F3336;
  border-radius: 20px;
  padding: 32px 40px 28px;
}

.tweet-headline {
  font-size: 38px;
  font-weight: 900;
  line-height: 1.15;
  letter-spacing: -0.8px;
}

.stats-bar {
  position: absolute;
  bottom: 0;
  left: 0; right: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.85) 40%, rgba(0,0,0,0.97) 100%);
  padding: 48px 56px 40px;
  display: flex;
}

.stat-value { font-size: 30px; font-weight: 900; }
```

**Fotos:** 2 fotos reais (pessoa principal + local/contexto). Gradient overlay em ambas.
**Conteudo:** Badge urgencia + headline impactante + 3 stats numeros.

---

### SLIDE 2: TWEET CARD + ARTIGO BRANCO
**Tipo:** Tweet dark no topo + card branco simulando artigo de jornal na parte inferior

**Layout:**
- Top: profile-row + tweet-card dark (numero + texto 27px)
- Bottom: card branco com foto lateral (340px) + headline + subtitulo + fonte

**Background:** `#000`

**Elementos-chave CSS:**
```css
.tweet-text {
  font-size: 27px;
  font-weight: 500;
  line-height: 1.5;
}

.article-card {
  background: #FFFFFF;
  border-radius: 20px;
  overflow: hidden;
  flex: 1;
}

/* Barra colorida no topo do card branco */
.article-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 5px;
  background: linear-gradient(90deg, #1D9BF0, #7856FF);
}

.article-headline {
  font-size: 22px;
  font-weight: 800;
  color: #0F1419;
}
```

**Fotos:** Foto real no card branco (foto da pessoa do tema).
**Conteudo:** Contexto do que aconteceu + simulacao de artigo jornalistico.

---

### SLIDE 3: SCREENSHOT DE REPORTAGEM (Fonte 1)
**Tipo:** Simulacao de print de tela de site de noticias (fundo branco)

**Layout:**
- Browser bar no topo (dots vermelho/amarelo/verde + URL fake)
- Header do jornal (logo + secao)
- Foto grande do tema
- Titulo do artigo 36px w900
- Subtitulo com borda-left vermelha
- Byline (autor + data)

**Background:** `#F5F5F5` (fundo claro -- este slide NAO e dark!)

**Elementos-chave CSS:**
```css
.browser-bar {
  background: #FFFFFF;
  height: 44px;
  display: flex;
  align-items: center;
  padding: 0 20px;
  gap: 10px;
  border-bottom: 1px solid #E0E0E0;
}

.browser-dot { width: 13px; height: 13px; border-radius: 50%; }
.dot-red { background: #FF5F57; }
.dot-yellow { background: #FFBD2E; }
.dot-green { background: #28C840; }

.browser-url {
  flex: 1;
  background: #F0F0F0;
  border-radius: 8px;
  height: 28px;
  font-size: 13px;
  color: #666;
}

.article-title {
  font-size: 36px;
  font-weight: 900;
  color: #0F1419;
  line-height: 1.2;
}

.article-subtitle {
  font-size: 19px;
  color: #444;
  border-left: 3px solid #E8001D;
  padding-left: 16px;
}
```

**Fotos:** Foto real do local/contexto no corpo do artigo.
**Conteudo:** Manchete completa + subtitulo detalhado + fonte jornalistica.
**Jornais sugeridos:** Metropoles, Gazeta do Povo, Folha, Estadao, Agencia Brasil.

---

### SLIDE 4: LISTA DE BULLETS DARK
**Tipo:** Bullet points em cards escuros com borda colorida lateral + foto embaixo

**Layout:**
- Profile-row + slide-counter
- Tweet-header card (#16181C) com titulo da secao
- 5 bullet-items em cards escuros com borda-left colorida
- Foto real embaixo (220px height, border-radius 18px)

**Background:** `#000` com radial-gradients sutis

**Elementos-chave CSS:**
```css
.bullet-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 18px 22px;
  background: #16181C;
  border-radius: 14px;
  border-left: 3px solid transparent;
}
/* Alternar cores das bordas: */
.bullet-item:nth-child(1) { border-left-color: #F4212E; }
.bullet-item:nth-child(2) { border-left-color: #F4212E; }
.bullet-item:nth-child(3) { border-left-color: #FFA500; }
.bullet-item:nth-child(4) { border-left-color: #FFA500; }
.bullet-item:nth-child(5) { border-left-color: #71767B; }

.bullet-text {
  font-size: 23px;
  font-weight: 500;
  line-height: 1.4;
}

.pill {
  display: inline-block;
  background: rgba(244,33,46,0.12);
  border-radius: 6px;
  padding: 2px 8px;
  font-weight: 800;
  font-size: 22px;
  color: #F4212E;
}
```

**Fotos:** Foto real tematica embaixo dos bullets.
**Conteudo:** 5 bullet points com dados-chave, palavras em destaque colorido.

---

### SLIDE 5: NUMERO GIGANTE
**Tipo:** Data card central com numero hero gigante + 3 stat cards embaixo

**Layout:**
- Profile-row + slide-counter
- Tweet-top card (titulo da secao)
- Big data card central (borda vermelha, numero gigante)
- Money strip (foto com overlay + texto sobre)
- 3 stat-cards lado a lado

**Background:** `#000` com radial-gradient vermelho sutil

**Elementos-chave CSS:**
```css
.big-data-card {
  background: linear-gradient(160deg, #1A0000 0%, #0D0000 100%);
  border: 2px solid rgba(244,33,46,0.4);
  border-radius: 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 48px;
}

/* Barra vermelha no topo */
.big-data-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, #F4212E, #FF6B6B, #F4212E);
}

.big-number {
  font-size: 128px;
  font-weight: 900;
  color: #F4212E;
  line-height: 0.9;
  letter-spacing: -4px;
}

.stat-card {
  flex: 1;
  background: #16181C;
  border: 1px solid #2F3336;
  border-radius: 16px;
  padding: 20px 22px;
}

.stat-card-value { font-size: 26px; font-weight: 900; }
```

**Fotos:** Foto tematica no money-strip (150px height com overlay escuro).
**Conteudo:** Numero impactante central + 3 stats contextuais.

---

### SLIDE 6: CITACAO/QUOTES + FOTO
**Tipo:** Blocos de citacao com aspas + traducao/explicacao + foto embedded

**Layout:**
- Profile-row + slide-counter
- Tweet-number (titulo)
- 3 quote-blocks (background #16181C, borda-left azul)
- Translation-box (explicacao simplificada)
- Foto embedded (260px, border-radius 18px) com caption overlay

**Background:** `#000` com radial-gradients sutis

**Elementos-chave CSS:**
```css
.quote-block {
  background: #16181C;
  border-left: 4px solid #1D9BF0;
  border-radius: 0 14px 14px 0;
  padding: 18px 24px;
}

.quote-text {
  font-size: 22px;
  font-weight: 500;
  font-style: italic;
  line-height: 1.5;
}

.translation-box {
  background: rgba(29,155,240,0.08);
  border: 1px solid rgba(29,155,240,0.2);
  border-radius: 16px;
  padding: 20px 24px;
}

.translation-text {
  font-size: 22px;
  font-weight: 600;
}
```

**Fotos:** Foto real da pessoa citada/exemplo.
**Conteudo:** 2-3 citacoes diretas + traducao em linguagem simples.

---

### SLIDE 7: COMPARATIVO ANTES vs DEPOIS
**Tipo:** 2 cards lado a lado (vermelho vs verde) com banner de foto no topo

**Layout:**
- Profile-row + slide-counter
- Tweet-top card (titulo)
- Banner de foto (200px, border-radius 18px) com texto overlay
- 2 compare-cards lado a lado (ANTES vermelho / AGORA verde)
- VS badge centralizado entre os cards
- Difference callout bar no fundo

**Background:** `#000` com radial-gradients vermelho e verde

**Elementos-chave CSS:**
```css
.compare-card.before-card {
  background: linear-gradient(160deg, #1A0000 0%, #100000 100%);
  border: 2px solid rgba(244,33,46,0.4);
}

.compare-card.after-card {
  background: linear-gradient(160deg, #001A0D 0%, #001008 100%);
  border: 2px solid rgba(0,186,124,0.4);
}

/* Barra colorida no topo de cada card */
.compare-card.before-card::before { background: linear-gradient(90deg, #F4212E, #FF6B6B); }
.compare-card.after-card::before { background: linear-gradient(90deg, #00BA7C, #00D68F); }

.card-header.red {
  background: rgba(244,33,46,0.15);
  color: #F4212E;
}
.card-header.green {
  background: rgba(0,186,124,0.15);
  color: #00BA7C;
}

.card-row-value { font-size: 19px; font-weight: 700; }

.vs-badge {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 46px; height: 46px;
  background: #000;
  border: 2px solid #2F3336;
  border-radius: 50%;
  font-size: 13px;
  font-weight: 900;
  color: #71767B;
}

.diff-value { font-size: 32px; font-weight: 900; color: #00BA7C; }
```

**Fotos:** Foto tematica no banner (martelo da justica, graficos, etc).
**Conteudo:** 4 comparacoes (label + valor) em cada card + valor de diferenca.

---

### SLIDE 8: SCREENSHOT DE REPORTAGEM (Fonte 2)
**Tipo:** Igual ao Slide 3 mas com OUTRO jornal e conteudo diferente

**Layout:** Mesmo formato de screenshot:
- Browser bar + header do jornal + foto + titulo + lista de pontos

**Background:** `#FFFFFF` (fundo claro!)

**IMPORTANTE:** Use uma fonte jornalistica DIFERENTE do Slide 3.
- Slide 3 usa Metropoles/Gazeta? Slide 8 usa Agencia Brasil/Revista Oeste/Jovem Pan
- O conteudo deve ser um contraponto, ressalva, ou aprofundamento

**Variacao adicional:** Este slide pode ter uma lista de warnings com icones:
```css
.warning-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 18px 22px;
  border-radius: 14px;
  border: 1.5px solid #E7E9EA;
  background: #FAFAFA;
}
.warning-item::before {
  content: '';
  position: absolute;
  top: 0; left: 0; bottom: 0;
  width: 4px;
  background: #FFA500;
}
.warning-title { font-size: 18px; font-weight: 700; color: #0F1419; }
.warning-desc { font-size: 15px; color: #536471; }
```

---

### SLIDE 9: CONCLUSAO + CTA
**Tipo:** Bullet points conclusivos com setas verdes + foto + CTA bar

**Layout:**
- Profile-row + slide-counter
- Tweet-number (titulo)
- Conditional card (frase condicional)
- 4 consequence-items (cards dark com seta verde e borda right verde)
- Foto embedded (200px) com caption
- CTA bar (gradient azul/roxo sutil)

**Background:** `#000` com radial-gradients verde e azul

**Elementos-chave CSS:**
```css
.consequence-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 18px 22px;
  background: #16181C;
  border-radius: 16px;
  border: 1px solid #2F3336;
}
/* Barra verde lateral */
.consequence-item::after {
  content: '';
  position: absolute;
  top: 0; right: 0; bottom: 0;
  width: 3px;
  background: linear-gradient(180deg, #00BA7C, transparent);
}

.consequence-text { font-size: 21px; font-weight: 500; line-height: 1.45; }

.cta-bar {
  background: linear-gradient(135deg, rgba(29,155,240,0.12), rgba(120,86,255,0.12));
  border: 1px solid rgba(29,155,240,0.2);
  border-radius: 18px;
  padding: 24px 28px;
  text-align: center;
}

.cta-question { font-size: 25px; font-weight: 800; }
.cta-action { font-size: 18px; color: #1D9BF0; font-weight: 600; }
```

**Fotos:** Foto real da pessoa principal ou cena do tema.
**Conteudo:** 4 consequencias/conclusoes + pergunta de engajamento.

---

### SLIDE 10: CTA FINAL GRADIENTE
**Tipo:** Fundo gradiente dark blue/purple + @rubimfx gigante + botao CTA

**Layout:**
- Background: gradient escuro com orbs decorativos + grid sutil
- Top area: profile-row pequeno + slide counter
- Centro: topic-badge + headline 44px + subheadline 22px
- @rubimfx em 96px com gradient text (branco -> azul -> roxo)
- Botao "Segue @rubimfx" azul
- Footer: "Escola Trader Financiado + ETF + SMC20k"
- Corner decorations (linhas nos cantos)

**Background:** `linear-gradient(160deg, #050A1A 0%, #0A0520 35%, #0D0826 60%, #020210 100%)`

**Elementos-chave CSS:**
```css
/* Orbs decorativos */
.orb-1 {
  width: 700px; height: 700px;
  background: radial-gradient(circle, rgba(29,155,240,0.14) 0%, transparent 70%);
  top: -200px; left: -200px;
}
.orb-2 {
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(120,86,255,0.17) 0%, transparent 70%);
  bottom: -150px; right: -150px;
}

/* Grid sutil */
.grid-overlay {
  background-image:
    linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
  background-size: 80px 80px;
}

.big-handle {
  font-size: 96px;
  font-weight: 900;
  letter-spacing: -3px;
  background: linear-gradient(135deg, #E7E9EA 0%, #1D9BF0 50%, #7856FF 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.cta-button {
  background: #1D9BF0;
  color: #FFFFFF;
  font-size: 24px;
  font-weight: 800;
  padding: 18px 52px;
  border-radius: 100px;
}
```

**Fotos:** NENHUMA foto tematica. Apenas profile-photo no avatar pequeno do topo.
**Conteudo FIXO:**
- Tags: "POLITICA + ECONOMIA + MERCADO"
- Headline: "Politica + economia + seu dinheiro."
- Sub: "Conteudo que importa, sem enrolacao."
- Handle: "@rubimfx"
- Botao: "Segue @rubimfx"
- Footer: "Escola Trader Financiado + ETF + SMC20k"

---

## SLIDE COUNTER

Presente em todos os slides exceto slide 1 (opcional) e slide 10 (obrigatorio).
```css
.slide-counter {
  position: absolute;
  top: 46px;
  right: 56px;
  font-size: 14px;
  font-weight: 600;
  color: #71767B;
  z-index: 3;
}
```
Formato: `2 / 10`, `3 / 10`, etc.

---

## BACKGROUND TEXTURES (decorativas, usar em slides dark)

```css
/* Tipo 1: Glow azul no topo */
.bg-glow {
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 700px 400px at 50% 25%, rgba(29,155,240,0.14) 0%, transparent 65%), #000;
  pointer-events: none;
}

/* Tipo 2: Dois focos sutis */
.bg-texture {
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 600px 400px at 90% 10%, rgba(29,155,240,0.06) 0%, transparent 60%),
    radial-gradient(ellipse 500px 500px at 10% 90%, rgba(120,86,255,0.06) 0%, transparent 60%);
  pointer-events: none;
}

/* Tipo 3: Glow vermelho central */
.bg-glow-red {
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 800px 600px at 50% 55%, rgba(244,33,46,0.07) 0%, transparent 70%);
  pointer-events: none;
}
```

---

## DESTAQUES DE TEXTO (usar inline com spans)

```html
<span class="red">texto vermelho</span>     <!-- #F4212E, weight 800 -->
<span class="blue">texto azul</span>        <!-- #1D9BF0, weight 700 -->
<span class="green">texto verde</span>      <!-- #00BA7C, weight 800 -->
<span class="orange">texto laranja</span>   <!-- #FFA500, weight 800 -->
<span class="em">texto enfatizado</span>    <!-- weight 800 -->
```

CSS:
```css
.red { color: #F4212E; font-weight: 800; }
.blue { color: #1D9BF0; font-weight: 700; }
.green { color: #00BA7C; font-weight: 800; }
.orange { color: #FFA500; font-weight: 800; }
.em { font-weight: 800; }
```

---

## CHECKLIST ANTES DE ENTREGAR CADA SLIDE

- [ ] Dimensoes: body { width: 1080px; height: 1350px; overflow: hidden; }
- [ ] Nenhum font-size abaixo de 20px (exceto itens decorativos listados acima)
- [ ] Nenhuma URL externa (sem https://unsplash.com, sem https://images.pexels.com)
- [ ] Todas as imagens sao arquivos locais: src="photo-nome.jpg"
- [ ] profile-photo.jpeg usado APENAS no profile-row (avatar pequeno)
- [ ] Portugues com acentuacao COMPLETA (nao, voce, ja, e -> nao, voce, ja, e com acentos)
- [ ] Design e DIFERENTE dos outros slides (nao repetir layout)
- [ ] Texto legivel (nao muito pequeno, nao muito apertado)
- [ ] @rubimfx visivel em algum lugar do slide
- [ ] Slide 10 sempre e o CTA gradiente (conteudo fixo)

---

## RESUMO RAPIDO DOS 10 SLIDES

| # | Tipo | Fundo | Foto | Elemento principal |
|---|------|-------|------|--------------------|
| 1 | Capa Breaking | Dark | 2 fotos collage | Tweet + stats bar |
| 2 | Tweet + Artigo | Dark | 1 foto no card branco | Card branco de jornal |
| 3 | Screenshot Jornal 1 | Claro | 1 foto no artigo | Simulacao de site |
| 4 | Bullets Dark | Dark | 1 foto embaixo | 5 bullet-items coloridos |
| 5 | Numero Gigante | Dark | 1 foto strip | Numero 128px vermelho |
| 6 | Citacao/Quotes | Dark | 1 foto embedded | Quote blocks + traducao |
| 7 | Comparativo | Dark | 1 foto banner | Cards ANTES vs AGORA |
| 8 | Screenshot Jornal 2 | Claro | 1 foto no artigo | Outro site de noticias |
| 9 | Conclusao + CTA | Dark | 1 foto embedded | Consequence items + CTA |
| 10 | CTA Gradiente | Gradient | Nenhuma (so avatar) | @rubimfx gigante + botao |
