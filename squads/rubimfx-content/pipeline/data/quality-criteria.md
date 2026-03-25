# Quality Criteria — @rubimfx Content Pipeline

## Visao Geral

Todo carrossel produzido pela squad deve passar por TODOS os criterios abaixo antes de publicacao. Um unico criterio reprovado bloqueia a publicacao.

---

## 1. Precisao Factual

| Criterio | Requisito | Reprovacao automatica |
|---|---|---|
| Dados numericos | Conferidos com fonte primaria (BLS, Fed, BCB, Bloomberg) | Numero errado publicado |
| Datas | Verificadas com calendario economico | Data incorreta de evento |
| Atribuicao | Declaracoes atribuidas corretamente | Citar fala que nao existe |
| Contexto | Dados apresentados sem distorcao | Cherry-picking enganoso |
| Atualizacao | Informacao vigente no momento da publicacao | Dado desatualizado sem nota |

**Regra de ouro:** Na duvida, nao publica. Verifica primeiro.

---

## 2. Tom e Voz @rubimfx

| Criterio | Requisito |
|---|---|
| Tom default | Analitico Direto (ver tone-of-voice.md) |
| Linguagem | PT-BR com termos tecnicos em EN quando padrao do mercado |
| Termos mantidos em EN | FOMC, NFP, CPI, order flow, liquidity sweep, break of structure (BOS), fair value gap (FVG), order block (OB), stop hunt, smart money |
| Postura | Praticante que opera, nao comentarista de sofá |
| Autoridade | Demonstrada por analise, nao por autopromoção |
| Acessibilidade | Tecnico mas compreensivel para trader intermediario |

**Teste de tom:** Leia em voz alta. Soa como alguem que opera falando com alguem que opera? Se sim, aprovado.

---

## 3. Consistencia Visual

| Criterio | Requisito |
|---|---|
| Background | Dark mode (#0D1117 ou #1A1B2E) — NUNCA light mode |
| Tipografia headlines | Bold condensada (Montserrat Bold, Space Grotesk Bold) |
| Tipografia corpo | Regular sans-serif (Inter, DM Sans) |
| Cores de destaque | Gold (#F59E0B) ou Teal (#00D4AA) — consistente no carrossel inteiro |
| Gain/Loss | Verde (#22C55E) / Vermelho (#EF4444) |
| Header bar | Presente em TODOS os slides com @rubimfx + data |
| Formato | 3:4 portrait (1080x1440px) |
| Capa | Estilo magazine-cover com foto + titulo overlay |

**Referencia:** style-guide-economesteter.md

---

## 4. Estrutura do Carrossel

### Metricas por Slide

| Metrica | Minimo | Ideal | Maximo |
|---|---|---|---|
| Palavras por slide | 40 | 55-65 | 80 |
| Slides por carrossel | 8 | 9-10 | 12 |
| Palavras totais | 350 | 450-550 | 700 |

### Qualidade do Hook (Slide 1)

O hook deve passar o "teste do polegar" — o usuario pararia de rolar?

Checklist do hook:
- [ ] Cria curiosidade ou urgencia
- [ ] Especifico (nao generico)
- [ ] Relevante para trader BR
- [ ] Maximo 15 palavras no titulo principal

### Motivacao de Swipe

Cada slide deve terminar com um motivo para passar para o proximo:
- Pergunta aberta
- "Mas tem mais..."
- Dado parcial que sera completado
- Tensao narrativa

---

## 5. Caption

| Elemento | Requisito |
|---|---|
| Hook (primeiros 125 chars) | Para o scroll. Aparece antes do "mais" no Instagram |
| Corpo | 2-4 paragrafos curtos. Expande o tema do carrossel |
| CTA | Obrigatorio. Pergunta, "salve", "compartilhe", ou "comente" |
| Hashtags | 5-15 tags. Mix de alto volume (#trading, #forex) e nicho (#propfirm, #smc) |
| Tamanho total | 150-300 palavras |
| Emojis | Uso moderado (1-3 por paragrafo max). Nunca como substituto de texto |

### Hashtags Padrao @rubimfx

Sempre incluir 3-5 do banco fixo:
`#trading #forex #trader #mercadofinanceiro #propfirm #traderfinanceiro #smartmoney #rubimfx`

Complementar com 3-8 contextuais:
`#fomc #fed #selic #copom #ouro #dolar #eurusd #nfp #orderflow`

---

## 6. Compliance CVM/ANBIMA

### PROIBIDO (reprovacao imediata)

- Prometer retorno financeiro ("ganhe X por mes")
- Mostrar resultado especifico de trade como expectativa ("lucrei R$10k essa semana")
- Garantir performance futura ("esse setup sempre funciona")
- Recomendar compra/venda de ativo especifico como conselho financeiro
- Usar palavras: "garantido", "certeza", "impossivel perder", "renda extra facil"

### OBRIGATORIO quando aplicavel

- Disclaimer: "Conteudo educacional. Nao e recomendacao de investimento."
- Nota de risco quando mencionar operacoes alavancadas
- Resultados passados nao garantem resultados futuros (quando mostrar backtest)

### PERMITIDO

- Mostrar analise tecnica como estudo educacional
- Discutir cenarios e probabilidades
- Compartilhar framework de decisao
- Usar linguagem como "possivel", "cenario", "probabilidade", "historicamente"

---

## 7. BRIDGE (Conteudo Macro) — OPCIONAL

Quando o carrossel trata de evento macro/economia E existe conexao natural com trading:

| Criterio | Requisito |
|---|---|
| Presenca do BRIDGE | Opcional — incluir quando a conexao macro → trading for natural e genuina |
| Clareza da cadeia | Se presente: Evento → Impacto → Leitura → Setup |
| Especificidade | Se presente: Mencionar ativo e conceito tecnico especifico |

**Nota:** Posts puramente macro/economia NO ESTILO @economesteter (sem bridge para trading) sao perfeitamente validos para topo de funil. Nao forcar a ponte quando ela nao existe naturalmente.
| Praticidade | Trader consegue agir com a informacao |

**Reprovado se:** Carrossel macro termina sem nenhuma conexao com operacao.

---

## Scoring de Aprovacao

| Criterio | Peso | Nota (1-5) |
|---|---|---|
| Precisao factual | 5x | __ |
| Tom e voz | 3x | __ |
| Consistencia visual | 3x | __ |
| Estrutura carrossel | 4x | __ |
| Caption | 2x | __ |
| Compliance | 5x | __ |
| BRIDGE (se macro) | 4x | __ |

**Score minimo para publicacao:** 80% do maximo possivel.
**Compliance abaixo de 4:** Reprovacao automatica independente do score total.
