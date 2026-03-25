---
id: generate-feedback
name: "Gerar Feedback Acionável"
agent: renata-revisao
trigger: auto (after score-content)
input:
  - score_result: object (output from score-content)
  - caption: string
  - hashtags: array
  - slide_visuals: array
output:
  format: markdown
  sections:
    - strengths
    - issues
    - action_items
---

# Task: Gerar Feedback Acionável

## Objetivo

Transformar o score do conteúdo em feedback detalhado e acionável, direcionado a cada agente responsável (Léo Legenda para texto, Diana Design para visuais). Cada item de feedback deve conter: o problema, por que é problema, e a ação exata para resolver.

## Process

### Passo 1 — Listar pontos fortes
Identifique 2-4 elementos que estão funcionando bem no conteúdo. Isso calibra o feedback — mostra que a avaliação é justa e reconhece qualidade. Seja específica: "O hook 'O mercado te mostra onde o smart money entrou' tem 58 caracteres e provoca curiosidade imediata" é melhor que "hook bom".

### Passo 2 — Identificar problemas por prioridade
Classifique cada problema encontrado:
- **BLOQUEANTE**: Impede publicação (erro factual, violação de compliance, dimensão errada)
- **IMPORTANTE**: Reduz qualidade significativamente (hook fraco, slide sobrecarregada, tom inconsistente)
- **MENOR**: Polimento (emoji a mais, hashtag subótima, ajuste fino de espaçamento)

### Passo 3 — Gerar action items direcionados
Para cada problema, crie um action item no formato:
- **Para quem**: Léo Legenda ou Diana Design
- **O quê**: Descrição específica da mudança
- **Por quê**: Impacto se não corrigir
- **Como**: Sugestão concreta de solução

### Passo 4 — Definir prioridade de execução
Ordene os action items por prioridade (bloqueantes primeiro) e agrupe por agente responsável. Isso permite que cada agente execute suas correções em paralelo.

## Output Format

```markdown
## Feedback — [Tema do Carrossel]

### Pontos Fortes
1. [Ponto forte específico]
2. [Ponto forte específico]
3. [Ponto forte específico]

### Problemas Encontrados

#### BLOQUEANTES
- **[Problema]**: [Descrição]. Agente: [nome]. Ação: [ação específica].

#### IMPORTANTES
- **[Problema]**: [Descrição]. Agente: [nome]. Ação: [ação específica].

#### MENORES
- **[Problema]**: [Descrição]. Agente: [nome]. Ação: [ação específica].

### Action Items por Agente

**Léo Legenda**
- [ ] [Ação 1]
- [ ] [Ação 2]

**Diana Design**
- [ ] [Ação 1]
- [ ] [Ação 2]

### Próximo Passo
[PUBLICAR / CORRIGIR E RE-SUBMETER / REESCREVER DO ZERO]
```

## Output Example

```markdown
## Feedback — Order Blocks: O Mapa do Smart Money

### Pontos Fortes
1. Hook da legenda ("O mercado te mostra onde o smart money entrou") tem 58 caracteres e gera curiosidade imediata — excelente uso do espaço pré-fold.
2. Definição de order block nos slides está tecnicamente precisa, incluindo a exigência de BOS para validação — diferencia de conteúdo genérico.
3. Palette visual consistente com dark mode #0A0A0F e accent azul #3B82F6 — identidade @rubimfx bem aplicada em todas as slides.
4. Disclaimer "Conteúdo educacional" presente na última slide e na legenda — compliance impecável.

### Problemas Encontrados

#### BLOQUEANTES
(Nenhum)

#### IMPORTANTES
- **Slide 4 com 92 palavras**: Excede o máximo de 80 palavras, prejudicando legibilidade mobile. Agente: Diana Design. Ação: Dividir o conteúdo entre slide 4 e uma nova slide 4b, ou remover o parágrafo de exemplo que repete informação do slide 3.
- **Legenda com 8 emojis**: Excede o máximo recomendado de 7. O emoji de foguete aparece 3 vezes sem função diferenciada. Agente: Léo Legenda. Ação: Remover 2 emojis de foguete duplicados, manter apenas 1 como marcador visual.

#### MENORES
- **Hashtag #trading muito genérica**: Tem +15M de posts, alcance orgânico praticamente zero. Agente: Léo Legenda. Ação: Substituir por #tradingbrasileiro ou #traderbrasileiro (volume médio, mais relevante).
- **Slide 6 sem alternância de background**: Usa mesmo #0A0A0F do slide 5, quebrando o ritmo visual. Agente: Diana Design. Ação: Trocar background do slide 6 para #111118.

### Action Items por Agente

**Léo Legenda**
- [ ] Remover 2 emojis de foguete duplicados na legenda (manter 1)
- [ ] Substituir #trading por #tradingbrasileiro no set de hashtags

**Diana Design**
- [ ] Reduzir slide 4 de 92 para ~70 palavras (remover parágrafo de exemplo redundante)
- [ ] Trocar background do slide 6 de #0A0A0F para #111118

### Próximo Passo
CORRIGIR E RE-SUBMETER — 4 ajustes rápidos, nenhum bloqueante. Score atual 8.6 deve subir para 9+ após correções.
```

## Quality Criteria

1. Todo problema identificado tem uma ação específica com agente responsável designado
2. Pontos fortes são específicos e mensuráveis, não elogios genéricos
3. Problemas estão corretamente classificados por prioridade (bloqueantes nunca são classificados como menores)
4. Action items são executáveis sem ambiguidade — o agente sabe exatamente o que fazer
5. Próximo passo está alinhado com o veredicto do score

## Veto Conditions

1. **Feedback sem ação**: Se um problema é listado mas não tem action item correspondente com agente designado — VETO, todo problema precisa de solução proposta.
2. **Bloqueante ignorado**: Se existe problema bloqueante mas o próximo passo é PUBLICAR — VETO, bloqueantes impedem publicação até serem resolvidos.
3. **Feedback destrutivo**: Crítica que ataca a qualidade geral sem apontar elementos específicos ("está tudo ruim") — VETO, reescrever com problemas e ações concretas.
