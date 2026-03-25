---
id: create-instagram-feed
name: Create Instagram Carousel
agent: iago-instagram
trigger: manual
inputs:
  - selected_angle: object (the chosen angle from generate-angles output)
  - news_story: string (original news headline + summary)
  - pillar: enum (macro, ict-education, trade-analysis, summit-prop, orderflow-mindset)
  - trade_reference: string (optional — specific chart or setup details from Gabriel)
outputs:
  - carousel: list of 8-10 slide objects
  - caption: string (Instagram caption with hashtags)
---

# Create Instagram Carousel

Produces a complete Instagram carousel (8-10 slides) following the selected angle. Each slide is a self-contained visual unit with controlled word density, designed for the @economesteter editorial style.

## Process

### Step 1 — Define the Narrative Arc
Map the 8-10 slides into a structure:
- **Slide 1 (Cover)**: Magazine-cover style. Bold headline, zero body text. Must stop the scroll.
- **Slides 2-3 (Hook + Context)**: Set the stage. Present the fact/news/problem. Create tension.
- **Slides 4-6 (Development)**: Build the argument. Each slide adds one layer. Progressive disclosure.
- **Slides 7-8 (Bridge + Synthesis)**: Connect macro to trading (if applicable). Deliver the key takeaway.
- **Slide 9 (Takeaway)**: One clear, memorable conclusion the reader walks away with.
- **Slide 10 (CTA)**: Call-to-action relevant to the content. Vary between salvar, seguir, comentar, compartilhar, link na bio.

### Step 2 — Write Each Slide
For each slide, produce:
- **Headline**: Bold, 3-8 words, functions as the visual anchor of the slide
- **Supporting Text**: 40-80 words (hard limit for content slides 2-9). Zero text for cover and minimal for CTA.
- **Accent Keywords**: 2-4 words per slide to be highlighted visually (bold, color, underline — designer decides)
- **Background Note**: Suggest light/dark alternation or color tone for visual rhythm

### Step 3 — Write the Caption
Write the Instagram caption (max 300 words) including:
- Opening hook (first 2 lines visible before "more")
- Brief summary that complements (not repeats) the carousel
- 3-5 relevant hashtags
- CTA that matches slide 10

### Step 4 — Self-Check
Verify every slide against constraints before outputting:
- Word count within 40-80 for content slides
- One idea per slide
- Accent keywords marked
- Bridge slide exists (for macro pillar)

## Output Format

```
CAROUSEL: [Titulo do Carousel]
ANGULO: [Nome do angulo selecionado]
PILAR: [Pilar de conteudo]
TOTAL SLIDES: [8-10]

---

SLIDE 1 — COVER
Headline: [titulo bold — max 8 palavras]
Supporting Text: —
Accent Keywords: [palavras para destaque visual]
Background: [sugestao de cor/tom]

SLIDE 2
Headline: [3-8 palavras]
Supporting Text: [40-80 palavras]
Accent Keywords: [2-4 palavras]
Background: [sugestao]

SLIDE 3
Headline: [3-8 palavras]
Supporting Text: [40-80 palavras]
Accent Keywords: [2-4 palavras]
Background: [sugestao]

[... slides 4-9 seguem o mesmo formato ...]

SLIDE 10 — CTA
Headline: [chamada para acao — max 6 palavras]
Supporting Text: [15-30 palavras com instrucao clara]
Accent Keywords: [2-3 palavras]
Background: [sugestao]

---

CAPTION:
[Texto da legenda — max 300 palavras]

HASHTAGS: #tag1 #tag2 #tag3 #tag4 #tag5
```

## Output Example

```
CAROUSEL: NFP fraco → Dolar caiu → Meu trade no EUR/USD
ANGULO: Ponte Macro→Trading
PILAR: Macro/Economy
TOTAL SLIDES: 10

---

SLIDE 1 — COVER
Headline: NFP FRACO. DOLAR CAIU. EU ENTREI.
Supporting Text: —
Accent Keywords: NFP, DOLAR, ENTREI
Background: Escuro (preto/cinza grafite) com texto branco bold

SLIDE 2
Headline: O que aconteceu na sexta
Supporting Text: Non-Farm Payrolls veio em 120 mil vagas. O mercado esperava 180 mil. Uma diferenca de 60 mil empregos a menos. Parece so um numero. Mas para quem opera forex, esse desvio e combustivel puro para volatilidade no dolar.
Accent Keywords: 120 mil, 180 mil, desvio, volatilidade
Background: Claro (branco/cinza claro)

SLIDE 3
Headline: A reacao imediata no DXY
Supporting Text: O indice dolar (DXY) caiu 0.6% em 45 minutos. Perdeu o suporte de 103.80 e foi buscar liquidez abaixo de 103.50. Quando o NFP decepciona assim, o mercado precifica corte de juros mais cedo. Dolar fraco. Moedas contra o dolar, fortes.
Accent Keywords: DXY, liquidez, corte de juros, dolar fraco
Background: Escuro

SLIDE 4
Headline: O que o smart money fez
Supporting Text: Antes do NFP, o EUR/USD caiu ate 1.0830. Parecia fraqueza. Mas era inducement. O mercado varreu a liquidez dos comprados que tinham stop abaixo de 1.0835. Classico liquidity sweep antes de expansao. Se voce conhece ICT, reconheceu o padrao.
Accent Keywords: inducement, liquidity sweep, ICT, 1.0830
Background: Claro

SLIDE 5
Headline: O displacement confirmou
Supporting Text: Apos o sweep, veio um candle de alta forte no M15 — displacement bullish. Fechou acima da estrutura anterior. Isso e change of character. A direcao mudou. E deixou um FVG claro entre 1.0845 e 1.0855. Ali era a zona de entrada.
Accent Keywords: displacement, change of character, FVG, entrada
Background: Escuro

SLIDE 6
Headline: Minha entrada — sem misterio
Supporting Text: Compra no reteste do FVG em 1.0850. Stop abaixo do sweep em 1.0825. Alvo 1: 1.0900 (estrutura anterior). Alvo 2: 1.0935 (premium zone). Risco-retorno de 1:3. Nao foi intuicao. Foi leitura de estrutura apos catalisador macro.
Accent Keywords: FVG, 1.0850, risco-retorno 1:3, estrutura
Background: Claro

SLIDE 7
Headline: O resultado do trade
Supporting Text: EUR/USD atingiu 1.0920 na sessao de Londres seguinte. Alvo 1 batido. Parcial realizada. O restante com stop no breakeven buscando 1.0935. Macro deu a direcao. Tecnico deu o timing. Essa e a combinacao que transforma noticia em lucro.
Accent Keywords: 1.0920, parcial, macro, tecnico
Background: Escuro

SLIDE 8
Headline: A licao que poucos entendem
Supporting Text: A maioria dos traders le o NFP e nao sabe o que fazer. Alguns operam no impulso. Poucos esperam o sweep, o displacement e o FVG. A ponte entre macro e tecnico e o que separa quem reage de quem executa. Essa ponte e o meu metodo.
Accent Keywords: ponte, macro, tecnico, metodo
Background: Claro

SLIDE 9
Headline: Macro sem tecnico e opiniao. Tecnico sem macro e cego.
Supporting Text: Voce nao precisa escolher entre analise fundamentalista e tecnica. Precisa conectar as duas. Todo grande movimento comeca com um catalisador macro. Todo trade lucrativo termina com um setup tecnico. Aprenda a construir essa ponte.
Accent Keywords: conectar, catalisador, setup, ponte
Background: Escuro

SLIDE 10 — CTA
Headline: Salva. Pratica. Evolui.
Supporting Text: Salva esse carrossel pra revisar antes do proximo NFP. Segue @rubimfx pra mais pontes macro→trading toda semana.
Accent Keywords: Salva, @rubimfx, macro→trading
Background: Escuro com destaque na cor de acento

---

CAPTION:
NFP veio em 120k. Esperavam 180k.
O dolar caiu. E eu ja estava posicionado.

Nesse carrossel eu mostro o raciocinio COMPLETO:
- O dado macro
- A reacao no DXY
- O liquidity sweep no EUR/USD
- O FVG que gerou minha entrada
- O resultado do trade

Isso e o que eu chamo de Ponte Macro→Trading.
Nao e so ler noticia. E transformar informacao em operacao.

Salva pra revisar antes do proximo Payroll.

HASHTAGS: #forex #trading #nfp #ict #smartmoney
```

## Quality Criteria

- [ ] Carousel has exactly 8-10 slides
- [ ] Slide 1 is a cover with bold headline only (no supporting text)
- [ ] Every content slide (2-9) has 40-80 words of supporting text
- [ ] Each slide has exactly one core idea
- [ ] Accent keywords are marked (2-4 per slide)
- [ ] Background alternation is suggested for visual rhythm
- [ ] Bridge slide exists connecting macro to trading setup (mandatory for macro pillar)
- [ ] CTA on final slide is specific and relevant to the content
- [ ] Caption complements the carousel without repeating slide content verbatim

## Veto Conditions

- **VETO if** any content slide exceeds 80 words or falls below 40 words
- **VETO if** the carousel has fewer than 8 or more than 10 slides
- **VETO if** the carousel is in the macro pillar and no slide explicitly bridges to a trading setup
- **VETO if** slide 1 contains body text (cover must be headline-only)
