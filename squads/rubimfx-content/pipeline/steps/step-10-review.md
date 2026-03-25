---
execution: inline
agent: renata-revisao
inputFile: squads/rubimfx-content/output/carousel-visuals.md
outputFile: squads/rubimfx-content/output/review.md
---

# Step 10 — Review (Inline)

## Context Loading

- `squads/rubimfx-content/output/carousel-visuals.md` — carrossel visual completo (HTML de cada slide)
- `squads/rubimfx-content/output/carousel-draft.md` — texto aprovado do carrossel
- `squads/rubimfx-content/output/caption.md` — legenda e hashtags
- `squads/rubimfx-content/output/news-research.md` — notícia base (para verificação factual)
- `squads/rubimfx-content/output/style-guide.md` — style guide (para verificação de compliance visual)
- `company.md` — identidade da marca @rubimfx
- `agents/renata-revisao/agent.md` — configuração do agente de revisão
- `agents/renata-revisao/tasks/score-content.md` — task de scoring
- `agents/renata-revisao/tasks/generate-feedback.md` — task de feedback

## Instructions

Revisar todo o conteúdo produzido (texto, legenda, visual) e gerar scores e feedback detalhado antes da aprovação final.

### Processo

1. **Executar score-content.md** — Avaliar o conteúdo em 4 dimensões, cada uma com score de 1-10:

   **Dimensão 1: Precisão Factual (peso 3x)**
   - Todos os dados numéricos estão corretos e verificáveis?
   - As fontes são confiáveis?
   - Há afirmações sem base factual?
   - Os dados estão atualizados?
   - O bridge macro→trading é logicamente correto?

   **Dimensão 2: Tom e Voz (peso 2x)**
   - O tom está alinhado com a identidade @rubimfx?
   - A linguagem é acessível mas não simplista?
   - O estilo editorial @economesteter está presente?
   - Há consistência de tom entre slides e legenda?
   - A linguagem evita hype, clickbait vazio e promessas financeiras?

   **Dimensão 3: Qualidade Visual (peso 2x)**
   - O HTML renderiza corretamente em 1080x1350px?
   - A paleta segue o style guide?
   - A tipografia é legível e hierarquizada?
   - Há coesão visual entre todos os slides?
   - Os dados numéricos estão em destaque visual?

   **Dimensão 4: Compliance (peso 3x)**
   - Não há recomendação direta de compra/venda?
   - Não há promessa de retorno financeiro?
   - Não há informação que configure consultoria financeira?
   - Fontes estão creditadas quando necessário?
   - Disclaimers presentes quando necessário?

2. **Calcular score final** — Média ponderada das 4 dimensões:
   - Score Final = (Precisão x 3 + Tom x 2 + Visual x 2 + Compliance x 3) / 10

3. **Executar generate-feedback.md** — Para cada dimensão, gerar:
   - O que está bom (pontos fortes)
   - O que precisa melhorar (pontos fracos)
   - Sugestões específicas de correção (se score < 8)

4. **Classificar resultado** — Com base no score final:
   - **9-10:** Excelente, pronto para publicação
   - **7-8:** Bom, ajustes menores recomendados
   - **5-6:** Regular, ajustes necessários antes de publicar
   - **1-4:** Insuficiente, recomenda refazer

5. **Listar issues** — Criar lista priorizada de problemas encontrados:
   - **Crítico:** Erro factual, problema de compliance — DEVE ser corrigido
   - **Importante:** Problema de tom, legibilidade — deveria ser corrigido
   - **Menor:** Sugestão de melhoria, polish — pode ser ignorado

## Output Format

```markdown
# Review — [Título do Carrossel]

## Score Summary

| Dimensão | Score | Peso | Ponderado |
|----------|-------|------|-----------|
| Precisão Factual | X/10 | 3x | X |
| Tom e Voz | X/10 | 2x | X |
| Qualidade Visual | X/10 | 2x | X |
| Compliance | X/10 | 3x | X |
| **Score Final** | | | **X/10** |

## Classificação: [Excelente/Bom/Regular/Insuficiente]

## Feedback por Dimensão

### Precisão Factual (X/10)
**Pontos fortes:** [lista]
**Pontos fracos:** [lista]
**Sugestões:** [lista]

[repete para cada dimensão]

## Issues

### Críticas
- [issue 1]

### Importantes
- [issue 1]

### Menores
- [issue 1]

## Recomendação
[Aprovado para publicação / Ajustes necessários / Refazer]
```

## Output Example

```markdown
# Review — O Fed falou. O ouro ouviu.

## Score Summary

| Dimensão | Score | Peso | Ponderado |
|----------|-------|------|-----------|
| Precisão Factual | 9/10 | 3x | 27 |
| Tom e Voz | 8/10 | 2x | 16 |
| Qualidade Visual | 8/10 | 2x | 16 |
| Compliance | 9/10 | 3x | 27 |
| **Score Final** | | | **8.6/10** |

## Classificação: Bom

## Feedback por Dimensão

### Precisão Factual (9/10)
**Pontos fortes:**
- Dados do Fed verificados (taxa 5.25-5.50%, dot plot correto)
- Valor do ouro $2.385 e variação +2.3% conferem com Reuters
- Fluxo ETFs de $1.2bi alinhado com Bloomberg

**Pontos fracos:**
- Slide 6: "primeira vez em 2 meses" — verificar se DXY não tocou 103.9x em fevereiro

**Sugestões:**
- Confirmar a exatidão do dado "2 meses" no slide 6 antes de publicar

### Tom e Voz (8/10)
**Pontos fortes:**
- Tom editorial @economesteter bem capturado: direto, sem enrolação
- Bridge macro→trading natural, não forçado
- Linguagem acessível sem ser simplista

**Pontos fracos:**
- Slide 7: tom levemente técnico demais ("suporte", "resistência" sem explicação)
- Legenda poderia ter mais personalidade do Gabriel

**Sugestões:**
- Slide 7: adicionar breve contexto para quem não conhece suporte/resistência
- Legenda: incluir uma frase em primeira pessoa para humanizar

### Qualidade Visual (8/10)
**Pontos fortes:**
- Paleta consistente com style guide em todos os slides
- Hierarquia tipográfica clara (Inter/Space Mono)
- Dados numéricos bem destacados visualmente

**Pontos fracos:**
- Slide 5: fluxo "Juros → Dólar → Ouro" poderia ser mais visual
- Badge @rubimfx poderia ter mais presença nos slides centrais

**Sugestões:**
- Slide 5: usar cards com ícones maiores para cada etapa do fluxo
- Considerar adicionar marca d'água mais visível nos slides 3-6

### Compliance (9/10)
**Pontos fortes:**
- Nenhuma recomendação direta de compra/venda
- Slide 7 usa linguagem de "leitura" não de "recomendação"
- Sem promessas de retorno

**Pontos fracos:**
- Slide 7: "suporte em $2.350, alvo $2.450" pode ser interpretado como recomendação

**Sugestões:**
- Slide 7: reformular para "níveis de atenção: $2.350 (suporte) e $2.450 (resistência)" em vez de "alvo"
- Adicionar disclaimer sutil no slide 7: "Análise educacional, não recomendação"

## Issues

### Críticas
- Nenhuma issue crítica encontrada

### Importantes
- Slide 7: reformular linguagem de "alvo" para evitar interpretação como recomendação financeira
- Slide 6: verificar dado "primeira vez em 2 meses" para DXY abaixo de 104

### Menores
- Legenda: considerar adicionar frase em primeira pessoa para mais autenticidade
- Slide 5: melhorar visualização do fluxo macro→trading
- Watermark @rubimfx poderia ser mais presente nos slides intermediários

## Recomendação
**Bom para publicação com ajustes menores.** Corrigir o linguagem do slide 7 (compliance) e verificar dado do slide 6 antes de publicar. Score 8.6/10 indica conteúdo de alta qualidade.
```

## Veto Conditions

- **Erro factual crítico** — Se qualquer dado numérico principal estiver incorreto (preço de ativo, decisão de banco central, porcentagem), o conteúdo NÃO pode ser aprovado. Score de Precisão Factual automaticamente cai para 4/10 ou menos.
- **Violação de compliance** — Se houver linguagem que configure recomendação financeira direta ou promessa de retorno, o conteúdo NÃO pode ser aprovado. Score de Compliance automaticamente cai para 3/10 ou menos.

## Quality Criteria

- O review deve cobrir TODAS as 4 dimensões com feedback específico (não genérico)
- Cada dimensão deve ter pelo menos 2 pontos fortes e 1 sugestão de melhoria identificados
- Issues devem ser priorizadas (Crítica > Importante > Menor) com ação clara
- O score final deve refletir corretamente a média ponderada (verificar cálculo)
- A recomendação deve ser objetiva e acionável (não apenas "bom" ou "ruim")
- Sugestões de correção devem incluir texto alternativo concreto, não apenas "melhorar"
