---
type: checkpoint
---

# Step 08 — Content Approval (Checkpoint)

## Context Loading

- `squads/rubimfx-content/output/carousel-draft.md` — carrossel completo slide por slide
- `squads/rubimfx-content/output/caption.md` — legenda + hashtags
- `squads/rubimfx-content/output/angles.md` — ângulo selecionado (para referência)
- `squads/rubimfx-content/output/news-research.md` — notícia base (para verificação factual)

## Instructions

Este checkpoint apresenta TODO o conteúdo textual produzido para aprovação do usuário antes de seguir para design visual.

### Processo

1. **Apresentar overview** — Resumo executivo do que foi produzido:
   > **Carrossel pronto para revisão**
   > Tema: [título da notícia]
   > Ângulo: [nome do ângulo]
   > Slides: [número]
   > Tom: [tom predominante]

2. **Apresentar carrossel slide por slide** — Mostrar cada slide com:
   - Número e tipo (capa, contexto, dados, bridge, CTA)
   - Texto completo do slide
   - Nota de destaque se houver dado numérico importante

   Formato compacto para fácil leitura:
   > **Slide 1 (Capa):** "O Fed falou. O ouro ouviu."
   > **Slide 2 (Contexto):** "Juros mantidos. Mas o recado mudou." — Fed em 5.25-5.50%, dot plot sinaliza corte em junho.
   > [...]

3. **Apresentar legenda** — Mostrar a legenda completa, pronta para copiar.

4. **Apresentar hashtags** — Listar as hashtags selecionadas com contagem total.

5. **Solicitar decisão** — Perguntar:
   > "O conteúdo está aprovado para seguir para design?"

   Opções claras:
   - **"Aprovado"** — segue para Step 09 (design visual)
   - **"Ajustar [slide X]"** — indica qual slide precisa de mudança e o que mudar
   - **"Ajustar legenda"** — indica o que mudar na legenda
   - **"Refazer"** — volta ao Step 06 para reescrever o carrossel (mantendo o ângulo)
   - **"Trocar ângulo"** — volta ao Step 05 para escolher outro ângulo
   - **"Trocar notícia"** — volta ao Step 03 para escolher outra notícia

6. **Processar ajustes** — Se o usuário pedir ajustes pontuais:
   - Aplicar a mudança solicitada
   - Reapresentar apenas o slide/legenda alterado
   - Pedir nova confirmação
   - Repetir até aprovação completa

7. **Registrar aprovação** — Quando aprovado, marcar no carousel-draft.md e caption.md como `## Status: APPROVED` com timestamp.

## Output Format

```
## Carrossel para Revisão

**Tema:** [título]
**Ângulo:** [nome] ([tipo])
**Slides:** [número] | **Tom:** [tom]

---

### Slides

**1 (Capa):** "[texto do hook]"

**2 (Contexto):** "[título]" — [resumo do corpo]

**3 (Dados):** [dado principal em destaque] — [contexto]

[...]

**[N] (CTA):** "[texto do CTA]"

---

### Legenda
[legenda completa]

### Hashtags ([contagem])
[hashtags]

---

O conteúdo está aprovado para seguir para design?
- "Aprovado" → segue para design visual
- "Ajustar slide [X]" → indica a mudança
- "Ajustar legenda" → indica a mudança
- "Refazer" → reescreve o carrossel
- "Trocar ângulo" → volta à seleção de ângulo
- "Trocar notícia" → volta à seleção de notícia
```

## Output Example

```
## Carrossel para Revisão

**Tema:** Fed mantém juros mas sinaliza corte em junho
**Ângulo:** A — "O Fed falou. O ouro ouviu." (Bridge Macro→Trading)
**Slides:** 8 | **Tom:** Informativo + provocação

---

### Slides

**1 (Capa):** "O Fed falou. O ouro ouviu."

**2 (Contexto):** "Juros mantidos. Mas o recado mudou." — Fed em 5.25-5.50%, dot plot sinaliza corte em junho

**3 (Dados/Educacional):** "Dot Plot: o mapa dos juros" — Maioria projeta corte, mediana 4.75% ao fim de 2026

**4 (Dados):** "+2.3%" — Ouro em $2.385/oz, nova máxima histórica. ETFs: $1.2bi de fluxo em 24h

**5 (Educacional/Bridge):** "Juros caem → Dólar enfraquece → Ouro sobe" — Relação inversa juros x ouro explicada

**6 (Dados):** "DXY perdeu 104.00" — Primeira vez em 2 meses abaixo desse nível

**7 (Bridge/Prático):** "E na prática?" — Ouro: suporte $2.350, alvo $2.450. EUR/USD: acima de 1.0900. Atenção: NFP pode mudar tudo

**8 (CTA):** "E você?" — Ouro ou dólar? Comenta e salva para consultar antes do NFP

---

### Legenda
O Fed manteve os juros. Nenhuma surpresa.

Mas o dot plot contou uma história diferente: a maioria dos membros já projeta corte em junho.

O ouro não esperou confirmação. Subiu 2.3% e renovou máxima histórica em $2.385.

O dólar perdeu o suporte de 104 que segurava há 2 meses.

Resumo rápido: o macro está falando. Quem opera precisa ouvir.

Passa os slides para entender o que mudou, por que o ouro reagiu assim e como isso pode impactar suas operações.

.
.
.

Comenta aqui: você está mais de olho no ouro ou no dólar essa semana?

Se esse conteúdo te ajudou a entender o cenário, salva e manda pra aquele amigo que opera sem olhar pro macro.

### Hashtags (14)
#forex #trading #mercadofinanceiro #investimentos #forextrader #daytrade #ouro #macroeconomia #fomc #federalreserve #xauusd #proptrading #rubimfx #tradingbrasil

---

O conteúdo está aprovado para seguir para design?
- "Aprovado" → segue para design visual
- "Ajustar slide [X]" → indica a mudança
- "Ajustar legenda" → indica a mudança
- "Refazer" → reescreve o carrossel
- "Trocar ângulo" → volta à seleção de ângulo
- "Trocar notícia" → volta à seleção de notícia
```

## Veto Conditions

- **Prosseguir sem aprovação explícita** — Nunca avançar para o Step 09 sem o usuário dizer explicitamente "Aprovado" ou equivalente claro.
- **Ignorar pedido de ajuste** — Toda solicitação de mudança deve ser implementada e reapresentada antes de seguir. Não pular ajustes "menores".

## Quality Criteria

- A apresentação deve ser escanável — o usuário deve conseguir revisar todo o conteúdo em menos de 2 minutos
- Cada slide deve ser resumido em no máximo 2 linhas na apresentação
- As opções de decisão devem ser claras e indicar para onde cada escolha leva no pipeline
- Ajustes devem ser aplicados imediatamente e reapresentados para nova aprovação
