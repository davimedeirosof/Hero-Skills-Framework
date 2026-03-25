---
execution: inline
agent: leo-legenda
inputFile: squads/rubimfx-content/output/carousel-draft.md
outputFile: squads/rubimfx-content/output/caption.md
---

# Step 07 — Write Caption (Inline)

## Context Loading

- `squads/rubimfx-content/output/carousel-draft.md` — carrossel completo do Step 06
- `squads/rubimfx-content/output/news-research.md` — notícia base com dados
- `company.md` — tom de voz @rubimfx, público-alvo, identidade
- `agents/leo-legenda/agent.md` — configuração do agente de legendas
- `agents/leo-legenda/tasks/write-caption.md` — task de escrita de legenda
- `agents/leo-legenda/tasks/write-hashtags.md` — task de seleção de hashtags

## Instructions

Escrever a legenda do post e selecionar hashtags otimizadas para o carrossel produzido no Step 06.

### Processo

1. **Analisar o carrossel** — Ler todos os slides para entender: tema central, tom, dados-chave, CTA. A legenda deve complementar o carrossel, não repetir o mesmo conteúdo.

2. **Executar write-caption.md** — Escrever a legenda seguindo a estrutura @rubimfx:

   **Estrutura da legenda:**
   - **Linha 1 (Hook):** Frase de impacto que complementa o hook do slide 1. Deve fazer sentido mesmo sem ver o carrossel. Máximo 1 linha.
   - **Corpo (3-5 linhas):** Contexto adicional que o carrossel não cobriu. Pode incluir opinião pessoal do Gabriel, conexão com eventos futuros, ou call to action expandido.
   - **Quebra visual:** Linha em branco ou "." para separar
   - **CTA (1-2 linhas):** Pergunta engajadora ou instrução direta (salvar, compartilhar, comentar). Diferente do CTA do último slide.
   - **Quebra visual**
   - **Hashtags:** Em bloco separado

   **Regras de copywriting:**
   - Tom: editorial, direto, como se estivesse conversando com um trader amigo
   - Sem emojis em excesso (máximo 3-4 na legenda inteira)
   - Usar quebras de linha para legibilidade no mobile
   - Menção de @rubimfx pelo menos 1 vez
   - Não usar linguagem de vendas ou hype

3. **Executar write-hashtags.md** — Selecionar hashtags em 3 camadas:
   - **Camada 1 (3-4 hashtags):** Alto volume, gerais — #forex #trading #mercadofinanceiro #investimentos
   - **Camada 2 (3-4 hashtags):** Médio volume, nicho — #forextrader #daytrade #ouro #macroeconomia
   - **Camada 3 (3-4 hashtags):** Baixo volume, específicas — #fomc #federalreserve #xauusd #proptrading
   - **Camada 4 (2-3 hashtags):** Marca — #rubimfx #tradingbrasileiro
   - Total: 12-15 hashtags (não exceder 15)

4. **Verificar compliance** — Garantir que a legenda não contém:
   - Promessas de retorno financeiro
   - Recomendação direta de compra/venda
   - Linguagem que possa ser interpretada como consultoria financeira
   - Informações desatualizadas ou incorretas

5. **Revisão final** — Ler a legenda em voz alta (mentalmente) para verificar fluidez e naturalidade.

## Output Format

```markdown
# Caption — [Título do Carrossel]

## Legenda

[texto completo da legenda pronto para copiar e colar]

## Hashtags

[bloco de hashtags]

## Metadata
- Caracteres: [contagem]
- Hashtags: [contagem]
- CTA tipo: [pergunta/instrução/debate]
```

## Output Example

```markdown
# Caption — O Fed falou. O ouro ouviu.

## Legenda

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

## Hashtags

#forex #trading #mercadofinanceiro #investimentos #forextrader #daytrade #ouro #macroeconomia #fomc #federalreserve #xauusd #proptrading #rubimfx #tradingbrasil

## Metadata
- Caracteres: 687
- Hashtags: 14
- CTA tipo: Pergunta + instrução de compartilhamento
```

## Veto Conditions

- **Legenda com mais de 2.200 caracteres** — Limite do Instagram é 2.200. Se exceder, cortar sem perder a essência.
- **Promessas financeiras** — Frases como "Compre ouro agora", "Garantia de lucro", "Você vai ganhar dinheiro" são proibidas. Reformular para linguagem educacional.
- **Repetição do carrossel** — Se a legenda repete exatamente os mesmos pontos dos slides sem adicionar valor, reescrever com perspectiva complementar.

## Quality Criteria

- O hook da legenda deve funcionar sozinho (fazer sentido sem ver o carrossel)
- A legenda deve adicionar pelo menos 1 informação ou perspectiva que não está nos slides
- O CTA deve ser diferente do CTA do último slide do carrossel
- As hashtags devem estar distribuídas nas 3 camadas de volume (alta, média, baixa)
- O total de hashtags deve estar entre 12 e 15
- A legenda deve ter entre 400 e 1.500 caracteres para engajamento ideal
