---
id: write-hashtags
name: "Criar Set de Hashtags Estratégicas"
agent: leo-legenda
trigger: manual
input:
  - carousel_topic: string
  - caption_text: string
  - content_category: string (macro | forex | trading_education | ict_concepts | analysis)
output:
  format: markdown
  sections:
    - hashtag_set
    - hashtag_rationale
---

# Task: Criar Set de Hashtags Estratégicas

## Objetivo

Produzir um set de 5-15 hashtags estratégicas para o post do @rubimfx, equilibrando hashtags de nicho (alta relevância, menor volume), hashtags de categoria (volume médio) e hashtags amplas (alto volume, descoberta). O objetivo é maximizar alcance dentro do público-alvo de traders brasileiros.

## Process

### Passo 1 — Classificar o conteúdo
Identifique a categoria principal do post e os sub-temas:
- **Categoria principal**: ICT/Smart Money, Macro/Economia, Forex, Análise Técnica, Mindset de Trader
- **Sub-temas**: Conceitos específicos mencionados (order blocks, liquidity, NFP, FOMC, etc.)

### Passo 2 — Montar o mix de hashtags (3 camadas)
Selecione hashtags nas três camadas:
- **Nicho (3-5 tags)**: Termos específicos do conteúdo. Ex: #orderblocks, #smartmoneyconcepts, #fairvaluegap, #ictconcepts
- **Categoria (3-5 tags)**: Termos do segmento. Ex: #tradingbrasil, #forexbrasil, #analisetecnica, #priceaction, #daytrader
- **Amplas (2-4 tags)**: Termos de descoberta. Ex: #mercadofinanceiro, #investimentos, #educacaofinanceira, #trader

### Passo 3 — Validar e filtrar
Revise o set final:
- Remova hashtags banidas ou shadowbanned conhecidas
- Evite hashtags com mais de 10M de posts (muito genéricas, zero alcance orgânico)
- Evite hashtags com menos de 1K posts (muito nichadas, sem volume)
- Garanta que nenhuma hashtag contradiz o conteúdo
- Total entre 5 e 15 hashtags

## Output Format

```markdown
## Hashtags — [Tema do Post]

### Set Completo
[hashtags separadas por espaço, prontas para colar no Instagram]

### Breakdown por Camada

**Nicho (alta relevância)**
- #tag1 — motivo
- #tag2 — motivo

**Categoria (volume médio)**
- #tag3 — motivo
- #tag4 — motivo

**Ampla (descoberta)**
- #tag5 — motivo
- #tag6 — motivo

### Total: [N] hashtags
```

## Output Example

```markdown
## Hashtags — Order Blocks: O Mapa do Smart Money

### Set Completo
#orderblocks #smartmoneyconcepts #icttrading #fairvaluegap #priceaction #forexbrasil #tradingbrasil #analisetecnica #daytrader #mercadofinanceiro #educacaofinanceira #rubimfx

### Breakdown por Camada

**Nicho (alta relevância)**
- #orderblocks — termo central do post
- #smartmoneyconcepts — framework ICT usado no conteúdo
- #icttrading — comunidade ICT no Instagram
- #fairvaluegap — conceito complementar mencionado

**Categoria (volume médio)**
- #priceaction — método de análise base
- #forexbrasil — comunidade forex BR
- #tradingbrasil — comunidade trading BR
- #analisetecnica — categoria geral do conteúdo
- #daytrader — perfil do público-alvo

**Ampla (descoberta)**
- #mercadofinanceiro — descoberta por público amplo
- #educacaofinanceira — atrai iniciantes interessados
- #rubimfx — hashtag de marca do perfil

### Total: 12 hashtags
```

## Quality Criteria

1. Set contém entre 5 e 15 hashtags, com representação das 3 camadas
2. Hashtags de nicho são diretamente relevantes ao tema específico do post
3. Inclui a hashtag de marca #rubimfx em todo post
4. Nenhuma hashtag banida ou conhecidamente shadowbanned
5. Mix equilibrado: não mais que 40% de hashtags amplas

## Veto Conditions

1. **Hashtags irrelevantes**: Hashtags que não têm relação com o conteúdo do post (ex: #fitness em post de trading) — VETO, remover e substituir.
2. **Excesso de hashtags genéricas**: Mais de 50% do set sendo hashtags com +5M posts — VETO, substituir por hashtags de nicho mais relevantes.
3. **Hashtags em português traduzido forçado**: "#blocodeordem" em vez de "#orderblocks" — VETO, usar o termo como a comunidade realmente usa.
