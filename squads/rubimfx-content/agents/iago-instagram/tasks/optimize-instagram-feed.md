---
id: optimize-instagram-feed
name: Optimize Instagram Carousel
agent: iago-instagram
trigger: manual
inputs:
  - carousel_draft: object (full carousel output from create-instagram-feed)
  - optimization_focus: enum (hook, flow, density, all) (default: all)
outputs:
  - optimized_carousel: object (revised carousel with changes annotated)
  - cover_ab_variant: object (alternative cover slide for A/B testing)
  - optimization_report: object (summary of changes and scores)
---

# Optimize Instagram Carousel

Reviews and optimizes a carousel draft across four dimensions: hook strength, swipe-through flow, accent keyword highlights, and information density. Produces an optimized version plus an A/B variant of the cover slide.

## Process

### Step 1 — Audit the Draft
Run a structured audit on the carousel draft checking:

**Hook Audit (Slide 1)**:
- Does the headline create curiosity, urgency, or both?
- Would this stop a scroll in a feed full of memes and reels?
- Is it under 8 words and visually impactful?
- Score: 1-10

**Swipe-Through Audit (Slides 2-9)**:
- Does each slide end with an implicit "and then what?" that motivates the next swipe?
- Are there any dead zones where the reader might drop off?
- Is the information arc progressive (not front-loaded or repetitive)?
- Score per transition: 1-10

**Density Audit (Slides 2-9)**:
- Count exact words per slide. Flag any slide outside the 40-80 range.
- Identify slides that feel too sparse (information gap) or too packed (visual overload).

**Accent Keyword Audit**:
- Are 2-4 keywords marked per slide?
- Are the keywords the right ones — terms that carry visual weight and conceptual importance?
- Are any critical terms missed (especially ICT/SMC terms and key numbers)?

### Step 2 — Optimize
Apply fixes for every issue found in the audit:
- Rewrite weak headlines
- Add swipe-bridges (cliffhanger phrases at end of slides that pull to next)
- Trim or expand slides outside word-count range
- Adjust accent keywords for visual impact
- Suggest background color adjustments if rhythm is broken

Mark every change with `[CHANGED]` tag so Gabriel can see what was modified.

### Step 3 — Generate Cover A/B Variant
Create an alternative cover slide (Slide 1) using a different headline strategy:
- If original is a statement, variant is a question (or vice versa)
- If original uses numbers, variant uses emotion (or vice versa)
- Both must be equally strong but appeal to different scroll-stopping triggers

### Step 4 — Produce Optimization Report
Summarize all changes, before/after scores, and the A/B variant rationale.

## Output Format

```
OPTIMIZATION REPORT
==================

AUDIT SCORES (BEFORE):
- Hook Strength: X/10
- Avg Swipe-Through: X/10
- Density Compliance: X/8 slides within range
- Accent Keyword Quality: X/10

CHANGES MADE:
1. [Slide X] [Tipo de mudanca] — [descricao curta]
2. [Slide X] [Tipo de mudanca] — [descricao curta]
...

AUDIT SCORES (AFTER):
- Hook Strength: X/10
- Avg Swipe-Through: X/10
- Density Compliance: X/8 slides within range
- Accent Keyword Quality: X/10

---

OPTIMIZED CAROUSEL:
[Carousel completo no mesmo formato do create-instagram-feed, com mudancas marcadas [CHANGED]]

---

COVER A/B VARIANT:

VARIANTE A (Original):
Headline: [headline original]
Estrategia: [tipo de hook usado]

VARIANTE B (Alternativa):
Headline: [headline alternativo]
Estrategia: [tipo de hook usado]
Supporting Text: —
Accent Keywords: [palavras para destaque]
Background: [sugestao]

RECOMENDACAO DE TESTE: [qual testar primeiro e por que — 1 frase]
```

## Output Example

```
OPTIMIZATION REPORT
==================

AUDIT SCORES (BEFORE):
- Hook Strength: 7/10
- Avg Swipe-Through: 6/10
- Density Compliance: 6/8 slides within range
- Accent Keyword Quality: 5/10

CHANGES MADE:
1. [Slide 1] Headline reescrito — original generico, novo com numero + urgencia
2. [Slide 3] Texto expandido de 35 para 52 palavras — estava abaixo do minimo
3. [Slide 5] Swipe-bridge adicionado — frase final "E foi ai que tudo mudou." para puxar pro slide 6
4. [Slide 6] Accent keywords ajustados — adicionado "FVG" e "1:3" que estavam sem destaque
5. [Slide 7] Texto cortado de 88 para 75 palavras — dividida uma frase composta
6. [Slide 8] Headline reescrito — original descritivo, novo com contraste emocional
7. [Slide 4] Background corrigido — dois slides claros seguidos, alternado para escuro
8. [Caption] Hook da legenda reescrito — primeira linha mais direta

AUDIT SCORES (AFTER):
- Hook Strength: 9/10
- Avg Swipe-Through: 8/10
- Density Compliance: 8/8 slides within range
- Accent Keyword Quality: 8/10

---

OPTIMIZED CAROUSEL:
[... carousel completo com [CHANGED] nos slides modificados ...]

SLIDE 1 — COVER [CHANGED]
Headline: 120K VAGAS. -60K DO ESPERADO. EU JA TINHA O TRADE.
Supporting Text: —
Accent Keywords: 120K, -60K, TRADE
Background: Escuro (preto com tipografia branca bold)

[... demais slides ...]

---

COVER A/B VARIANT:

VARIANTE A (Original):
Headline: 120K VAGAS. -60K DO ESPERADO. EU JA TINHA O TRADE.
Estrategia: Numeros concretos + afirmacao de autoridade

VARIANTE B (Alternativa):
Headline: VOCE LEU O NFP. EU OPEREI ELE. QUAL DEU MAIS LUCRO?
Estrategia: Pergunta provocativa + contraste direto com a audiencia
Supporting Text: —
Accent Keywords: NFP, OPEREI, LUCRO
Background: Escuro com acento em amarelo/dourado

RECOMENDACAO DE TESTE: Publicar Variante A primeiro (numeros concretos performam melhor no nicho finance); usar Variante B como repost/stories caso A nao atinja 3% de save rate.
```

## Quality Criteria

- [ ] Every slide in the optimized version has 40-80 words (content slides)
- [ ] All changes are tagged with `[CHANGED]` for easy review
- [ ] Before and after audit scores are provided with honest differentiation
- [ ] Cover A/B variants use genuinely different hook strategies (not minor word swaps)
- [ ] Swipe-through flow has no dead zones (every transition score >= 6/10)
- [ ] Accent keywords include all ICT/SMC terms and key numbers present in the text

## Veto Conditions

- **VETO if** the optimization report is missing before/after scores
- **VETO if** the A/B cover variant uses the same headline strategy as the original (must be structurally different)
- **VETO if** any content slide in the optimized version falls outside the 40-80 word range
