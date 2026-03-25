---
id: write-caption
name: "Escrever Legenda para Instagram"
agent: leo-legenda
trigger: manual
input:
  - carousel_topic: string
  - slide_texts: array
  - target_audience: string (optional)
output:
  format: markdown
  sections:
    - hook
    - body
    - cta
---

# Task: Escrever Legenda para Instagram

## Objetivo

Criar uma legenda completa para Instagram que complementa o carrossel do @rubimfx, maximizando engajamento (saves, comments, shares) enquanto mantém o tom de autoridade praticante e compliance regulatório.

## Process

### Passo 1 — Analisar o carrossel e extrair o ângulo
Leia todos os slides do carrossel. Identifique: (a) o conceito central, (b) o insight mais forte, (c) o que NÃO foi dito nos slides mas o leitor precisa saber. A legenda deve cobrir o ponto (c) — complementar, não repetir.

### Passo 2 — Criar o hook (primeiros 125 caracteres)
Escreva 3 variações de hook usando uma destas estruturas:
- **Confronto**: Questione uma crença comum ("90% dos traders usam [X] errado")
- **Revelação**: Apresente um fato surpreendente ("O mercado te diz exatamente onde vai — você só não sabe ler")
- **Identificação**: Descreva uma dor do público ("Se você já tomou stop e não entendeu por quê, leia isso")
Selecione o hook mais forte.

### Passo 3 — Escrever o corpo da legenda
Desenvolva o corpo com 150-400 palavras contendo:
- Contexto ou mini-história que conecta ao tema
- 2-3 insights práticos com quebras de linha
- Termos técnicos em inglês onde natural
- Emojis como marcadores visuais (max 5-7 no total)

### Passo 4 — Criar o CTA de fechamento
Escreva um CTA que combine com o tema:
- Para posts educativos: "Salva pra revisar antes de operar"
- Para posts polêmicos: "Comenta o que você acha"
- Para posts de análise: "Marca quem precisa ver isso"
Inclua disclaimer sutil se necessário ("Conteúdo educacional, não recomendação de investimento").

### Passo 5 — Revisar e polir
Releia a legenda completa e verifique: hook cabe em 125 chars, sem promessas de retorno, estrutura escaneável, tom @rubimfx, CTA claro.

## Output Format

```markdown
## Legenda Instagram — [Tema]

### Hook
[Primeira linha — max 125 caracteres]

### Corpo
[Corpo da legenda com quebras de linha e formatação Instagram]

### CTA
[Call-to-action final]

### Disclaimer (se aplicável)
[Disclaimer regulatório]

### Métricas
- Caracteres do hook: [N]
- Palavras total: [N]
- Emojis usados: [N]
```

## Output Example

```markdown
## Legenda Instagram — Order Blocks: O Mapa do Smart Money

### Hook
O mercado te mostra onde o smart money entrou. Você só não sabe ler — ainda.

### Corpo
A maioria dos traders de varejo coloca ordem em suporte e resistência.

E toma stop.

Repetidamente.

Enquanto isso, o smart money opera em zonas específicas que deixam rastro no gráfico. Essas zonas têm nome: order blocks.

Não é indicador. Não é mágica.
É a leitura da pegada institucional no price action.

No meu operacional, eu identifico order blocks assim:
- Último candle de baixa antes de um movimento impulsivo de alta (bullish OB)
- Último candle de alta antes de um movimento impulsivo de baixa (bearish OB)
- Validação: o OB precisa ter causado um break of structure

O erro mais comum? Marcar qualquer zona de consolidação como OB.
Sem BOS, não é order block. É só ruído.

Desliza no carrossel que eu mostro os 3 filtros que uso pra separar OB válido de armadilha.

### CTA
Salva esse post e consulta antes de marcar seus OBs no gráfico.
Comenta "OB" se você já usa order blocks no seu operacional.

### Disclaimer
Conteúdo educacional sobre análise técnica. Não constitui recomendação de investimento.

### Métricas
- Caracteres do hook: 78
- Palavras total: 187
- Emojis usados: 0
```

## Quality Criteria

1. Hook tem no máximo 125 caracteres e provoca curiosidade imediata
2. Corpo contém pelo menos 2 insights práticos não presentes no carrossel
3. Tom consistente com @rubimfx — praticante, direto, sem guru vibes
4. Zero promessas de retorno financeiro ou linguagem de guru
5. Estrutura escaneável com parágrafos curtos e quebras estratégicas

## Veto Conditions

1. **Promessa de retorno**: Qualquer menção a ganhos financeiros específicos, "lucro garantido", "fique rico" — VETO IMEDIATO, reescrever do zero.
2. **Hook acima de 125 caracteres**: A primeira linha cortada pelo Instagram mata o engajamento — VETO, reescrever hook.
3. **Repetição do carrossel**: Se mais de 50% do conteúdo da legenda é cópia dos slides — VETO, a legenda deve complementar.
