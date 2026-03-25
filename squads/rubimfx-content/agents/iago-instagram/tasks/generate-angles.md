---
id: generate-angles
name: Generate Content Angles
agent: iago-instagram
trigger: manual
inputs:
  - news_story: string (the selected news headline + summary)
  - pillar: enum (macro, ict-education, trade-analysis, summit-prop, orderflow-mindset)
  - context: string (optional — any extra context from Gabriel)
outputs:
  - angles: list of 5 angle objects
---

# Generate Content Angles

Generates 5 distinct editorial angles from ONE selected news story or topic. Each angle reframes the same information through a different emotional and strategic lens, giving Gabriel maximum creative optionality before committing to a carousel.

## Process

### Step 1 — Deconstruct the News
Read the input news story and extract:
- The core fact (what happened)
- The market implication (what it means for forex/gold/indices)
- The audience relevance (why a funded trader or aspiring trader should care)
- The ICT/SMC connection (which concepts does this activate — liquidity sweep, displacement, BoS, etc.)

### Step 2 — Generate 5 Angles
Produce exactly 5 angles, one for each lens:

1. **Medo/Urgencia** — Frame the news as a threat or warning. What could go wrong if the trader ignores this? What risk is now on the table?
2. **Oportunidade** — Frame the news as a window opening. What setup does this create? What can the attentive trader capture?
3. **Educacional** — Use the news as a vehicle to teach an ICT/SMC concept. The news is the hook; the lesson is the payload.
4. **Contrario** — Take the opposite stance of consensus. If everyone is bullish, argue the bearish case (or vice versa). Must be intellectually honest, not contrarian for shock value.
5. **Ponte Macro→Trading** — THE signature angle. Start with the macro headline, walk through the chain of causation, and land on a specific trading setup. This is the @rubimfx differentiator.

### Step 3 — Score and Rank
For each angle, assign:
- **Hook Strength** (1-5): How likely is this to stop a scroll?
- **Swipe Potential** (1-5): How much curiosity does this create for 8-10 slides?
- **Bridge Clarity** (1-5): How clearly does this connect to actionable trading?
- **Recommended**: Mark the top 1-2 angles as recommended.

## Output Format

```
NOTICIA BASE:
"[headline da noticia]"

---

ANGULO 1 — MEDO/URGENCIA
Titulo: [headline do carousel — max 12 palavras]
Gancho: [frase de abertura — o que prende no slide 1]
Arco: [resumo do arco narrativo em 2 frases]
Bridge: [como conecta ao trading — 1 frase]
Hook Strength: X/5 | Swipe Potential: X/5 | Bridge Clarity: X/5

ANGULO 2 — OPORTUNIDADE
Titulo: [headline do carousel — max 12 palavras]
Gancho: [frase de abertura]
Arco: [resumo do arco narrativo em 2 frases]
Bridge: [como conecta ao trading — 1 frase]
Hook Strength: X/5 | Swipe Potential: X/5 | Bridge Clarity: X/5

ANGULO 3 — EDUCACIONAL
Titulo: [headline do carousel — max 12 palavras]
Gancho: [frase de abertura]
Arco: [resumo do arco narrativo em 2 frases]
Bridge: [como conecta ao trading — 1 frase]
Hook Strength: X/5 | Swipe Potential: X/5 | Bridge Clarity: X/5

ANGULO 4 — CONTRARIO
Titulo: [headline do carousel — max 12 palavras]
Gancho: [frase de abertura]
Arco: [resumo do arco narrativo em 2 frases]
Bridge: [como conecta ao trading — 1 frase]
Hook Strength: X/5 | Swipe Potential: X/5 | Bridge Clarity: X/5

ANGULO 5 — PONTE MACRO→TRADING [RECOMENDADO]
Titulo: [headline do carousel — max 12 palavras]
Gancho: [frase de abertura]
Arco: [resumo do arco narrativo em 2 frases]
Bridge: [como conecta ao trading — 1 frase]
Hook Strength: X/5 | Swipe Potential: X/5 | Bridge Clarity: X/5

---
RECOMENDACAO: Angulo X e Angulo Y — [justificativa em 1 frase]
```

## Output Example

```
NOTICIA BASE:
"NFP dos EUA veio em 120k vs expectativa de 180k — pior resultado em 6 meses"

---

ANGULO 1 — MEDO/URGENCIA
Titulo: O mercado de trabalho dos EUA esta quebrando. E agora?
Gancho: 120 mil vagas. Esperavam 180 mil. A diferenca nao e um numero — e um sinal.
Arco: Mostrar como a desaceleracao do emprego antecipa cortes de juros e volatilidade no dolar. Cada slide revela um indicador que confirma a fraqueza.
Bridge: Setup de venda no DXY com liquidity sweep acima de 104.200.
Hook Strength: 4/5 | Swipe Potential: 4/5 | Bridge Clarity: 3/5

ANGULO 2 — OPORTUNIDADE
Titulo: NFP fraco abriu a porta. Voce vai entrar?
Gancho: Quando o Payroll decepciona, o dolar sangra. E quem esta preparado, lucra.
Arco: Explicar o fluxo NFP fraco → expectativa de corte → dolar cai → EUR/USD sobe. Mostrar a janela de oportunidade nos proximos 5 dias uteis.
Bridge: Compra em EUR/USD no FVG de H4 em 1.0850 com alvo em 1.0920.
Hook Strength: 4/5 | Swipe Potential: 5/5 | Bridge Clarity: 5/5

ANGULO 3 — EDUCACIONAL
Titulo: O que e o NFP e por que ele move o dolar assim?
Gancho: Todo primeiro sexta do mes, um numero muda tudo. Voce sabe ler ele?
Arco: Ensinar o que e Non-Farm Payrolls, como o mercado precifica expectativa vs realidade, e por que o desvio importa mais que o numero absoluto. Usar o dado de hoje como exemplo vivo.
Bridge: Mostrar como o desvio de -60k criou displacement no EUR/USD M15.
Hook Strength: 3/5 | Swipe Potential: 4/5 | Bridge Clarity: 4/5

ANGULO 4 — CONTRARIO
Titulo: NFP fraco? Calma. O dolar pode surpreender voce.
Gancho: Todo mundo vendeu dolar. Eu nao. E tenho 3 razoes.
Arco: Argumentar que um NFP fraco isolado nao reverte a tendencia do DXY se o Fed mantiver discurso hawkish. Mostrar dados de sessoes anteriores pos-NFP fraco onde o dolar se recuperou.
Bridge: Possivel inducement na venda do dolar — smart money pode estar acumulando.
Hook Strength: 5/5 | Swipe Potential: 4/5 | Bridge Clarity: 3/5

ANGULO 5 — PONTE MACRO→TRADING [RECOMENDADO]
Titulo: De NFP fraco a trade no EUR/USD — meu raciocinio completo
Gancho: NFP veio 120k. O dolar caiu. A liquidez foi varrida. E EU ENTREI.
Arco: Cadeia completa: dado macro → reacao do dolar → estrutura tecnica no EUR/USD H1 → liquidity sweep abaixo de 1.0830 → displacement bullish → entrada no FVG. Cada slide e um elo da cadeia.
Bridge: Trade real com entrada, stop e alvo — o macro virou operacao.
Hook Strength: 5/5 | Swipe Potential: 5/5 | Bridge Clarity: 5/5

---
RECOMENDACAO: Angulo 5 e Angulo 2 — Angulo 5 e a assinatura do @rubimfx (ponte completa), e Angulo 2 capitaliza urgencia com setup claro.
```

## Quality Criteria

- [ ] Exactly 5 angles produced, one per lens (Medo, Oportunidade, Educacional, Contrario, Ponte)
- [ ] Each title has max 12 words and functions as a standalone carousel cover headline
- [ ] Each angle has a distinct emotional and strategic framing — no two angles feel like the same idea rephrased
- [ ] Scores are honest and differentiated (not all 5/5)
- [ ] At least one angle is marked as recommended with justification

## Veto Conditions

- **VETO if** fewer than 5 angles are produced or any lens is skipped
- **VETO if** the Ponte Macro→Trading angle does not include a specific pair/instrument and setup type (e.g., "compra EUR/USD no FVG de H4")
- **VETO if** any angle title exceeds 12 words
