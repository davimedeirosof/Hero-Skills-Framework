---
task: rank-stories
order: 2
input:
  - artifacts/raw-news-list.md
output:
  - artifacts/news-brief.md
---

# Task: Rank Stories — Ranking e Selecao Final

## Objetivo
Receber a lista bruta de 10-15 noticias do find-news e aplicar um sistema de pontuacao em 4 criterios para selecionar as top 5 historias. Cada historia selecionada recebe uma sugestao de angulo para carrossel.

## Process

### Step 1 — Carregar e Validar Lista Bruta
Abrir `artifacts/raw-news-list.md` e validar que:
- Ha pelo menos 10 noticias na lista
- Todos os campos obrigatorios estao preenchidos
- As noticias estao dentro do periodo de busca definido
Se a lista tiver menos de 8 noticias, sinalizar ao usuario e prosseguir com o disponivel.

### Step 2 — Pontuar Cada Noticia
Aplicar 4 criterios de pontuacao (1-5 cada, total maximo 20):

**Criterio 1: Relevancia Forex/Ouro/Indices (peso 1-5)**
- 5 = Impacto direto em XAUUSD, EUR/USD, DXY, S&P500 ou Nasdaq
- 3 = Impacto indireto ou de segundo grau
- 1 = Conexao tangencial

**Criterio 2: Impacto no Publico @rubimfx (peso 1-5)**
- 5 = Afeta diretamente a operacao de traders brasileiros (Selic, dolar, prop firms)
- 3 = Relevante para educacao/contexto de mercado
- 1 = Interessante mas distante do dia-a-dia do publico

**Criterio 3: Potencial de Carrossel (peso 1-5)**
- 5 = Dados visualizaveis + debate + antes/depois ou comparacao
- 3 = Tem dados ou tem debate, mas nao ambos
- 1 = Dificil de transformar em conteudo visual

**Criterio 4: Atualidade (peso 1-5)**
- 5 = Publicado nas ultimas 6 horas ou evento acontecendo agora
- 4 = Publicado nas ultimas 12 horas
- 3 = Publicado nas ultimas 24 horas
- 2 = Publicado nas ultimas 48 horas
- 1 = Mais antigo (so entra se houver desdobramento novo)

### Step 3 — Selecionar Top 5 e Sugerir Angulos
Ordenar por pontuacao total (desempate pelo Criterio 1). Selecionar as top 5 e para cada uma:
- Definir um angulo de carrossel em 1 frase (ex: "Comparacao antes/depois do dot plot do Fed")
- Sugerir o formato visual (dados, timeline, vs., checklist, mapa)
- Indicar o hook potencial para o primeiro slide

### Step 4 — Salvar Briefing Final
Gravar em `artifacts/news-brief.md` no formato abaixo.

## Output Format

```yaml
meta:
  brief_date: "YYYY-MM-DD"
  stories_evaluated: 13
  stories_selected: 5
  focus: "topico do research-focus"

ranked_stories:
  - rank: 1
    title: "Titulo da noticia"
    source: "Fonte"
    date: "YYYY-MM-DD"
    url: "https://..."
    summary: "Resumo com dados concretos."
    scores:
      relevance: 5
      audience_impact: 5
      carousel_potential: 4
      timeliness: 5
      total: 19
    carousel_angle: "Descricao do angulo em 1 frase"
    visual_format: "dados | timeline | versus | checklist | mapa | infografico"
    hook_suggestion: "Frase de hook para o primeiro slide"
    assets_impacted:
      - XAUUSD
      - DXY
```

## Output Example

```yaml
meta:
  brief_date: "2026-03-15"
  stories_evaluated: 13
  stories_selected: 5
  focus: "cobertura geral — semana de FOMC"

ranked_stories:
  - rank: 1
    title: "Fed Expected to Hold Rates Amid Sticky Inflation Data"
    source: "Reuters"
    date: "2026-03-15"
    url: "https://reuters.com/markets/fed-hold-rates-2026-03-15"
    summary: "Mercado precifica 92% de manutencao. Core PCE em 2.8%. Dot plot pode sinalizar apenas 1 corte em 2026."
    scores:
      relevance: 5
      audience_impact: 5
      carousel_potential: 5
      timeliness: 5
      total: 20
    carousel_angle: "O que o Fed decide amanha e como isso mexe no ouro, dolar e indices"
    visual_format: "timeline"
    hook_suggestion: "O Fed decide amanha. Voce esta preparado?"
    assets_impacted:
      - DXY
      - EUR/USD
      - XAUUSD
      - S&P500
      - Nasdaq

  - rank: 2
    title: "Ouro Renova Maxima Historica Acima de $3.200"
    source: "Bloomberg"
    date: "2026-03-15"
    url: "https://bloomberg.com/gold-record-high-2026-03-15"
    summary: "XAUUSD ultrapassou $3.200 pela primeira vez. Tensoes geopoliticas e compras de bancos centrais impulsionam."
    scores:
      relevance: 5
      audience_impact: 4
      carousel_potential: 5
      timeliness: 5
      total: 19
    carousel_angle: "Timeline do ouro de $1.800 a $3.200 — o que esta por tras da alta historica"
    visual_format: "dados"
    hook_suggestion: "O ouro acabou de bater $3.200. Isso nunca aconteceu antes."
    assets_impacted:
      - XAUUSD
      - DXY

  - rank: 3
    title: "COPOM Sinaliza Fim do Ciclo de Alta da Selic em 14.75%"
    source: "Valor Economico"
    date: "2026-03-14"
    url: "https://valoreconomico.com.br/copom-selic-fim-ciclo"
    summary: "Ata indica 14.75% como teto. Mercado de juros futuros ja precifica cortes no segundo semestre."
    scores:
      relevance: 4
      audience_impact: 5
      carousel_potential: 4
      timeliness: 4
      total: 17
    carousel_angle: "Selic no topo — o que muda para o dolar e para o trader brasileiro"
    visual_format: "versus"
    hook_suggestion: "A Selic parou de subir. E agora?"
    assets_impacted:
      - USD/BRL
      - DXY
```

## Quality Criteria

1. **Ranking justificado:** cada nota de 1-5 deve ser coerente com os criterios definidos. Nenhuma nota sem logica aparente.
2. **Diversidade tematica:** as top 5 devem cobrir pelo menos 3 categorias diferentes (fed, macro-br, commodities, geopolitics, prop-trading, etc).
3. **Angulos acionaveis:** cada carousel_angle deve ser especifico o suficiente para um roteirista comecar a trabalhar sem pesquisa adicional.
4. **Hook concreto:** cada hook_suggestion deve ser uma frase curta, direta, que gere curiosidade — no estilo de conteudo de @rubimfx.

## Veto Conditions

1. **Nota inflada:** se uma noticia recebe total acima de 16 mas nao tem dados concretos no resumo, revisar as notas para baixo.
2. **Monocultura tematica:** se 4 ou mais das top 5 sao sobre o mesmo tema/ativo, substituir a de menor nota por uma de categoria diferente.
3. **Hook generico:** hooks como "Veja o que aconteceu no mercado hoje" sao vetados. Devem ser especificos e conter o gancho da noticia.
