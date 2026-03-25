---
task: find-news
order: 1
input:
  - context/research-focus.md
output:
  - artifacts/raw-news-list.md
---

# Task: Find News — Busca Ampla de Noticias

## Objetivo
Varrer fontes prioritarias e retornar 10-15 noticias candidatas sobre macro, economia, forex, ouro, indices e prop trading. Esta e a fase de amplitude — o filtro fino acontece em rank-stories.

## Process

### Step 1 — Ler o Foco de Pesquisa
Abrir `context/research-focus.md` e extrair:
- Topico principal (se definido) ou "cobertura geral do dia"
- Periodo de busca (padrao: ultimas 24 horas)
- Ativos em destaque (se especificados)
- Restricoes ou preferencias do usuario

### Step 2 — Buscar em Fontes Prioritarias
Executar buscas em pelo menos 5 fontes diferentes usando `web_search`:
- Termos em ingles: "FOMC", "Fed", "NFP", "CPI", "gold XAUUSD", "S&P500", "forex", "US dollar DXY", "tariffs trade war"
- Termos em portugues: "Selic COPOM", "economia brasileira mercado", "dolar real"
- Termos especificos: "prop trading news", "funded trader", nomes de prop firms relevantes
- Consultar calendario economico do dia/semana via ForexFactory ou Investing.com
- Para cada resultado relevante, usar `web_fetch` para confirmar data, extrair resumo e validar URL

### Step 3 — Compilar Lista Bruta
Montar a lista com 10-15 noticias, cada uma com todos os campos obrigatorios preenchidos. Descartar noticias que:
- Nao tem fonte verificavel
- Sao mais antigas que o periodo definido (salvo desdobramentos novos)
- Nao tem conexao com os ativos/mercados de @rubimfx
- Sao paywalled sem resumo acessivel

### Step 4 — Salvar Output
Gravar resultado em `artifacts/raw-news-list.md` no formato especificado abaixo.

## Output Format

```yaml
meta:
  search_date: "YYYY-MM-DD"
  period: "ultimas 24h | ultimas 48h | semana"
  focus: "topico do research-focus ou cobertura geral"
  total_found: 12
  sources_consulted:
    - Bloomberg
    - Reuters
    - Investing.com

stories:
  - id: 1
    title: "Titulo original da noticia"
    source: "Nome da Fonte"
    date: "YYYY-MM-DD"
    url: "https://..."
    summary: "Resumo de 2-3 linhas com dados concretos."
    assets_impacted:
      - XAUUSD
      - DXY
    category: "fed | macro-us | macro-br | geopolitics | commodities | prop-trading | crypto"
```

## Output Example

```yaml
meta:
  search_date: "2026-03-15"
  period: "ultimas 24h"
  focus: "cobertura geral — semana de FOMC"
  total_found: 13
  sources_consulted:
    - Bloomberg
    - Reuters
    - Financial Times
    - Valor Economico
    - ForexFactory
    - Investing.com

stories:
  - id: 1
    title: "Fed Expected to Hold Rates Amid Sticky Inflation Data"
    source: "Reuters"
    date: "2026-03-15"
    url: "https://reuters.com/markets/fed-hold-rates-2026-03-15"
    summary: "Mercado precifica 92% de chance de manutencao na reuniao de quarta. Core PCE em 2.8% mantem Fed cauteloso. Dot plot pode sinalizar apenas 1 corte em 2026."
    assets_impacted:
      - DXY
      - EUR/USD
      - S&P500
      - Nasdaq
    category: "fed"

  - id: 2
    title: "Ouro Renova Maxima Historica Acima de $3.200 com Demanda de Safe Haven"
    source: "Bloomberg"
    date: "2026-03-15"
    url: "https://bloomberg.com/gold-record-high-2026-03-15"
    summary: "XAUUSD ultrapassou $3.200 pela primeira vez, impulsionado por tensoes geopoliticas e compras de bancos centrais. China e India lideram demanda fisica."
    assets_impacted:
      - XAUUSD
      - DXY
    category: "commodities"

  - id: 3
    title: "COPOM Sinaliza Fim do Ciclo de Alta da Selic em 14.75%"
    source: "Valor Economico"
    date: "2026-03-14"
    url: "https://valoreconomico.com.br/copom-selic-fim-ciclo"
    summary: "Ata do COPOM indica que 14.75% deve ser o teto do ciclo. Mercado de juros futuros ja precifica cortes a partir do segundo semestre."
    assets_impacted:
      - USD/BRL
      - DXY
    category: "macro-br"
```

## Quality Criteria

1. **Volume:** minimo 10, maximo 15 noticias na lista bruta.
2. **Diversidade de fontes:** pelo menos 4 fontes diferentes representadas.
3. **Campos completos:** 100% das noticias com todos os campos do schema preenchidos (title, source, date, url, summary, assets_impacted, category).
4. **Resumo informativo:** cada summary deve conter pelo menos 1 dado numerico ou factual concreto.

## Veto Conditions

1. **Fonte nao verificavel:** se a URL nao funciona ou a fonte nao e identificavel, a noticia NAO entra na lista.
2. **Fora do escopo:** noticias sem conexao com forex, ouro, indices, macro ou prop trading sao descartadas mesmo que sejam trending.
3. **Duplicata:** se a mesma noticia aparece em multiplas fontes, manter apenas a versao da fonte de maior prioridade e citar as demais como confirmacao.
