---
id: score-content
name: "Pontuar Conteúdo do Carrossel"
agent: renata-revisao
trigger: manual
input:
  - caption: string
  - hashtags: array
  - slide_visuals: array (HTML or PNG paths)
  - carousel_topic: string
  - original_brief: string
output:
  format: markdown
  sections:
    - score_breakdown
    - overall_score
    - verdict
---

# Task: Pontuar Conteúdo do Carrossel

## Objetivo

Avaliar o pacote completo do carrossel @rubimfx (legenda + hashtags + slides visuais) em uma escala de 1-10, com breakdown por categoria. O score determina se o conteúdo está aprovado para publicação, precisa de ajustes menores ou requer retrabalho.

## Process

### Passo 1 — Avaliar Precisão Factual (peso 25%)
Revise todo o conteúdo textual (legenda + slides):
- Conceitos de trading estão corretamente definidos?
- Dados macroeconômicos estão corretos?
- Exemplos fazem sentido técnico?
- Não há simplificações que distorçam o conceito?
Score parcial: 1-10

### Passo 2 — Avaliar Tom e Voz @rubimfx (peso 20%)
Verifique aderência à identidade:
- Tom de praticante com autoridade (não guru, não acadêmico)?
- PT-BR com termos EN de trading onde natural?
- Hook forte nos primeiros 125 caracteres?
- CTA claro e engajador?
- Sem linguagem de coach motivacional?
Score parcial: 1-10

### Passo 3 — Avaliar Qualidade Visual (peso 20%)
Revise os slides:
- Dark mode consistente com palette?
- Header bar @rubimfx em todas as slides?
- Hierarquia tipográfica clara?
- 40-80 palavras por slide?
- Contraste e legibilidade adequados?
- Alternância visual entre slides?
Score parcial: 1-10

### Passo 4 — Avaliar Compliance Regulatório (peso 20%)
Verifique CVM/ANBIMA:
- Zero promessas de retorno financeiro?
- Sem linguagem de "lucro garantido" ou similar?
- Disclaimer presente quando necessário?
- Conteúdo posicionado como educacional?
Score parcial: 1-10

### Passo 5 — Avaliar Estrutura e Engajamento (peso 15%)
Analise a estrutura geral:
- Carrossel tem fluxo lógico (início, desenvolvimento, CTA)?
- Legenda complementa (não repete) o carrossel?
- Hashtags são relevantes e bem distribuídas?
- O conteúdo provoca save/comment/share?
Score parcial: 1-10

### Passo 6 — Calcular score final e emitir veredicto
Score final = media ponderada dos 5 critérios.
- >= 8.0: APROVADO
- 7.0 - 7.9: AJUSTES MENORES (publicável com correções rápidas)
- < 7.0: RETRABALHO (volta para agentes com feedback)

## Output Format

```markdown
## Score — [Tema do Carrossel]

### Breakdown

| Categoria              | Peso | Score | Nota                    |
|------------------------|------|-------|-------------------------|
| Precisão Factual       | 25%  | X/10  | [nota curta]            |
| Tom e Voz @rubimfx     | 20%  | X/10  | [nota curta]            |
| Qualidade Visual       | 20%  | X/10  | [nota curta]            |
| Compliance Regulatório | 20%  | X/10  | [nota curta]            |
| Estrutura/Engajamento  | 15%  | X/10  | [nota curta]            |

### Score Final: X.X/10

### Veredicto: [APROVADO / AJUSTES MENORES / RETRABALHO]

### Resumo
[2-3 frases sobre o estado geral do conteúdo]
```

## Output Example

```markdown
## Score — Order Blocks: O Mapa do Smart Money

### Breakdown

| Categoria              | Peso | Score | Nota                                          |
|------------------------|------|-------|-----------------------------------------------|
| Precisão Factual       | 25%  | 9/10  | Conceitos ICT corretos, BOS bem explicado      |
| Tom e Voz @rubimfx     | 20%  | 8/10  | Hook forte, CTA bom, leve excesso de emojis   |
| Qualidade Visual       | 20%  | 8/10  | Dark mode consistente, slide 4 com texto denso |
| Compliance Regulatório | 20%  | 10/10 | Sem promessas, disclaimer presente              |
| Estrutura/Engajamento  | 15%  | 8/10  | Fluxo lógico, hashtags bem distribuídas         |

### Score Final: 8.6/10

### Veredicto: APROVADO

### Resumo
Carrossel sólido com conceitos ICT bem apresentados e visual consistente. O hook da legenda é forte e o compliance está impecável. Sugestão menor: reduzir texto do slide 4 de 85 para ~70 palavras e trocar 2 emojis repetidos na legenda.
```

## Quality Criteria

1. Score final é a media ponderada correta dos 5 critérios (sem arredondamento arbitrário)
2. Cada categoria tem uma nota explicativa específica, não genérica
3. Compliance recebe 10/10 somente se zero problemas regulatórios encontrados
4. Veredicto está calibrado: 8+ = APROVADO, 7-7.9 = AJUSTES, <7 = RETRABALHO

## Veto Conditions

1. **Compliance falha**: Se a categoria Compliance Regulatório recebe score abaixo de 7, o veredicto DEVE ser RETRABALHO independente dos outros scores — compliance não é negociável.
2. **Erro factual grave**: Se um conceito central está factualmente errado (ex: definição invertida de bullish/bearish OB), o veredicto DEVE ser RETRABALHO — publicar erro técnico destrói credibilidade.
