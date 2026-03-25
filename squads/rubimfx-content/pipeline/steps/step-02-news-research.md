---
execution: subagent
agent: nara-noticia
inputFile: squads/rubimfx-content/pipeline/data/research-focus.md
outputFile: squads/rubimfx-content/output/news-research.md
model_tier: powerful
---

# Step 02 — News Research (Subagent)

## Context Loading

- `squads/rubimfx-content/pipeline/data/research-focus.md` — foco e horizonte temporal definidos pelo usuário
- `company.md` — identidade @rubimfx, público-alvo (traders brasileiros), tom editorial
- `agents/nara-noticia/agent.md` — configuração e capabilities do agente de pesquisa
- `agents/nara-noticia/tasks/find-news.md` — task de busca de notícias
- `agents/nara-noticia/tasks/rank-stories.md` — task de ranqueamento de histórias

## Instructions

O agente Nara executa pesquisa de notícias com base no foco definido no Step 01, buscando histórias relevantes para o universo @rubimfx.

### Processo

1. **Carregar contexto** — Ler o research-focus.md para entender tema, horizonte temporal e palavras-chave. Ler company.md para alinhar com a identidade da marca.

2. **Executar find-news.md** — Buscar notícias usando as palavras-chave e o horizonte temporal definidos. Fontes prioritárias:
   - Reuters, Bloomberg, Financial Times (macro global)
   - Investing.com, ForexFactory (dados econômicos e forex)
   - InfoMoney, Valor Econômico (perspectiva brasileira)
   - Twitter/X de analistas reconhecidos
   - Relatórios de bancos centrais e instituições

3. **Executar rank-stories.md** — Ranquear as notícias encontradas com os seguintes critérios:
   - **Relevância para trading** (peso 3x) — A notícia afeta diretamente algum ativo operável?
   - **Potencial de engajamento** (peso 2x) — O público @rubimfx vai se interessar?
   - **Bridge macro→trading** (peso 2x) — É possível conectar o macro com operação prática?
   - **Frescor** (peso 1x) — A notícia ainda é relevante no ciclo de atenção?
   - **Originalidade do ângulo** (peso 1x) — Outros perfis já cobriram exaustivamente?

4. **Compilar resultado** — Selecionar as 5 melhores histórias e formatar conforme output.

5. **Validar qualidade** — Verificar que todas as 5 histórias têm fonte, dados concretos e potencial de bridge macro→trading.

## Output Format

```markdown
# News Research — [Foco]

## Metodologia
- Fontes consultadas: [lista]
- Horizonte: [período]
- Data da pesquisa: [timestamp]

## Top 5 Stories

### 1. [Título da Notícia]
- **Fonte:** [nome e link]
- **Data:** [data de publicação]
- **Resumo:** [2-3 frases]
- **Dados-chave:** [números, porcentagens, valores]
- **Ativos impactados:** [lista de ativos]
- **Bridge macro→trading:** [como conectar com operação]
- **Score:** [X/10]

[repete para stories 2-5]
```

## Output Example

```markdown
# News Research — FOMC

## Metodologia
- Fontes consultadas: Reuters, Bloomberg, ForexFactory, Fed.gov
- Horizonte: Últimas 24h
- Data da pesquisa: 2026-03-15T10:30:00-03:00

## Top 5 Stories

### 1. Fed mantém juros em 5.25% mas sinaliza corte em junho
- **Fonte:** Reuters (https://reuters.com/...)
- **Data:** 2026-03-14
- **Resumo:** O Federal Reserve manteve a taxa de juros inalterada pela quinta reunião consecutiva, mas o dot plot revisado mostra que a maioria dos membros agora projeta um corte de 25bps em junho. Powell destacou "progresso substancial" na inflação.
- **Dados-chave:** Taxa mantida em 5.25-5.50%; dot plot mediano aponta 4.75% no final de 2026; inflação PCE em 2.4%
- **Ativos impactados:** DXY, EUR/USD, XAU/USD, US500, US30
- **Bridge macro→trading:** Corte em junho = dólar mais fraco = ouro bullish. Setup: compra de XAU/USD em pullback para 2.300, alvo 2.400
- **Score:** 9.5/10

### 2. Ouro renova máxima histórica após decisão do Fed
- **Fonte:** Bloomberg (https://bloomberg.com/...)
- **Data:** 2026-03-14
- **Resumo:** O ouro subiu 2.3% nas horas seguintes à decisão do Fed, renovando máxima histórica em $2.385/oz. Fluxo para ETFs de ouro atingiu o maior nível em 3 meses.
- **Dados-chave:** XAU/USD em $2.385; +2.3% no dia; fluxo ETFs: $1.2bi em 24h
- **Ativos impactados:** XAU/USD, XAG/USD, GDX, mineradoras
- **Bridge macro→trading:** Rompimento de ATH com volume = momentum forte. Setup: retest do $2.350 como suporte
- **Score:** 9.0/10

### 3. DXY perde suporte de 104 pela primeira vez em 2 meses
- **Fonte:** ForexFactory / Investing.com
- **Data:** 2026-03-14
- **Resumo:** O índice do dólar (DXY) caiu abaixo de 104.00 pela primeira vez desde janeiro, pressionado pela sinalização dovish do Fed. EUR/USD rompeu 1.0900.
- **Dados-chave:** DXY em 103.75; EUR/USD em 1.0920; GBP/USD em 1.2780
- **Ativos impactados:** DXY, EUR/USD, GBP/USD, USD/JPY
- **Bridge macro→trading:** Dólar fraco favorece pares EUR e GBP. Risco: reversão se dados de emprego surpreenderem
- **Score:** 8.5/10

### 4. China anuncia estímulo fiscal de $500bi para infraestrutura
- **Fonte:** Financial Times (https://ft.com/...)
- **Data:** 2026-03-14
- **Resumo:** O governo chinês anunciou um pacote de estímulo de 3.6 trilhões de yuan focado em infraestrutura e tecnologia verde.
- **Dados-chave:** 3.6 trilhões de yuan (~$500bi); foco em infraestrutura; implementação Q2 2026
- **Ativos impactados:** AUD/USD, NZD/USD, cobre, minério de ferro
- **Bridge macro→trading:** China comprando commodities = AUD bullish. Correlação com pares de moeda commodity
- **Score:** 7.5/10

### 5. NFP da próxima semana pode definir ritmo de cortes do Fed
- **Fonte:** Investing.com / analistas
- **Data:** 2026-03-15
- **Resumo:** O relatório de emprego (NFP) da próxima sexta-feira é considerado decisivo para confirmar ou negar a expectativa de corte em junho. Consenso: 180K vagas.
- **Dados-chave:** Consenso NFP: 180K; anterior: 275K; taxa de desemprego esperada: 3.8%
- **Ativos impactados:** DXY, ouro, S&P 500, todos os pares USD
- **Bridge macro→trading:** Se NFP < 150K = confirma corte = ouro sobe. Se NFP > 200K = adia corte = dólar recupera
- **Score:** 7.0/10
```

## Veto Conditions

- **Notícias sem fonte verificável** — Toda história deve ter fonte primária identificável. Rumores de redes sociais sem confirmação são excluídos.
- **Score abaixo de 5/10** — Se nenhuma notícia atingir score 5+, informar o orchestrator que o tema pode não render conteúdo e sugerir novo foco.
- **Sem bridge macro→trading** — Cada notícia DEVE ter uma conexão com trading prático. Notícias puramente políticas sem impacto em ativos são excluídas.

## Quality Criteria

- Todas as 5 histórias devem ter dados numéricos concretos (não apenas narrativas vagas)
- Pelo menos 3 das 5 histórias devem ter score 7+ no ranking
- Cada história deve listar pelo menos 2 ativos impactados
- As fontes devem ser diversificadas (não todas do mesmo veículo)
- O bridge macro→trading deve ser específico (mencionar ativo, direção e setup quando possível)
