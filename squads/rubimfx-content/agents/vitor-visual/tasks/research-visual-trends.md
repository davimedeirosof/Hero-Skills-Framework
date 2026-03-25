---
id: research-visual-trends
title: Pesquisar Tendencias Visuais de Carrosseis
agent: vitor-visual
trigger: scheduled
frequency: weekly
skills_required:
  - web_search
  - web_fetch
input:
  - periodo: "ultima semana"
  - contas_referencia:
      - "@economesteter"
      - "@visualcap"
      - "@newtraderu"
      - "@smcandict"
      - "@zcfxofficial"
output: trend-report.md
---

# Task: Pesquisar Tendencias Visuais de Carrosseis

## Objetivo
Identificar tendencias atuais de design visual em carrosseis de Instagram no nicho de financas, economia e trading. Monitorar contas concorrentes e catalogar padroes emergentes de layout, cor, tipografia e composicao.

## Process

### Step 1 — Coleta de Dados por Conta
Para cada conta de referencia, pesquisar os posts mais recentes (ultimos 7 dias) e registrar:
- Tipo de conteudo (carrossel, imagem unica, reel cover)
- Paleta de cores predominante (hex codes quando identificaveis)
- Estilo tipografico (serif, sans-serif, peso, caixa alta/baixa)
- Layout e composicao (grid, full-bleed, split, overlay)
- Elementos graficos (icones, charts, separadores, gradientes)
- Estilo da primeira slide (capa editorial, titulo bold, foto, ilustracao)
- Engajamento observavel (likes, comentarios como proxy de eficacia visual)

### Step 2 — Identificacao de Padroes
Cruzar as observacoes entre contas para identificar:
- Elementos que aparecem em 3+ contas (tendencia confirmada)
- Elementos novos que nao estavam presentes na semana anterior (tendencia emergente)
- Elementos que desapareceram de contas que os usavam (tendencia em declinio)
- Diferenciais unicos de cada conta que merecem atencao

### Step 3 — Classificacao e Prioridade
Classificar cada tendencia identificada:
- **Relevancia para @rubimfx**: alta / media / baixa
- **Compatibilidade com base @economesteter**: sim / parcial / nao
- **Maturidade**: emergente / estabelecida / em declinio
- **Esforco de implementacao**: baixo / medio / alto

### Step 4 — Documentacao Detalhada
Para cada tendencia relevante, criar ficha com:
- Nome descritivo da tendencia
- Descricao visual detalhada
- Exemplos de contas e posts onde foi observada
- Cores, fontes e dimensoes especificas
- Recomendacao de adocao (adotar agora / testar / monitorar / ignorar)

## Output Format

Arquivo Markdown estruturado com header YAML, tabela resumo e fichas detalhadas por tendencia. Cada ficha deve ter descricao visual suficiente para um designer reproduzir o estilo sem ver o post original.

## Output Example

```markdown
---
type: trend-report
date: "2026-03-15"
period: "2026-03-08 a 2026-03-15"
analyst: vitor-visual
accounts_monitored: 5
trends_identified: 4
---

# Relatorio de Tendencias Visuais — Semana 11/2026

## Resumo Executivo
Observadas 4 tendencias relevantes no periodo. Destaque para adocao crescente
de gradientes sutis em fundos escuros e uso de micro-animacoes em carrosseis
estaticos (efeito simulado por composicao de slides).

## Tabela Resumo

| Tendencia | Relevancia | Compatibilidade | Maturidade | Recomendacao |
|-----------|-----------|-----------------|------------|--------------|
| Gradiente radial sutil em fundo | Alta | Sim | Estabelecida | Adotar agora |
| Tipografia condensed extra-bold | Media | Parcial | Emergente | Testar |
| Barra lateral colorida como separador | Alta | Sim | Estabelecida | Adotar agora |
| Icones outline monocromaticos | Baixa | Sim | Estabelecida | Monitorar |

## Fichas de Tendencia

### 1. Gradiente Radial Sutil em Fundo
- **Descricao**: fundo com gradiente radial do centro para bordas, variando
  de #0D1117 (centro) para #1A1040 (bordas), criando profundidade sem
  distrair do conteudo
- **Observado em**: @economesteter (3 posts), @visualcap (2 posts), @newtraderu (1 post)
- **Cores**: base #0D1117, variacao navy #0F1729, variacao purple-dark #1A1040
- **Compatibilidade**: totalmente compativel com base @economesteter
- **Recomendacao**: adotar como variacao do fundo solido atual, usar em
  slides de destaque (capa e CTA)

### 2. Tipografia Condensed Extra-Bold
- **Descricao**: headlines usando fontes condensed (ex: Inter Tight, Barlow
  Condensed) em peso 800-900, caixa alta, tracking -0.02em
- **Observado em**: @newtraderu (5 posts), @smcandict (2 posts)
- **Fontes identificadas**: Barlow Condensed 800, Inter Tight ExtraBold
- **Compatibilidade**: parcial — funciona para headlines mas contrasta com
  a tipografia atual mais aberta
- **Recomendacao**: testar em 2-3 posts como headline principal, manter
  fonte atual para corpo de texto
```

## Quality Criteria

- [ ] Pelo menos 5 contas de referencia monitoradas com registros individuais
- [ ] Cada tendencia tem minimo 3 exemplos de posts reais como evidencia
- [ ] Cores especificadas em hex codes, fontes com nome e peso exatos
- [ ] Classificacao de relevancia, compatibilidade e maturidade para cada tendencia
- [ ] Recomendacao clara e acionavel (adotar / testar / monitorar / ignorar)
- [ ] Periodo de observacao e data de pesquisa documentados no header

## Veto Conditions

- **Dados insuficientes**: relatorio com menos de 3 contas monitoradas ou menos de 10 posts analisados no total deve ser refeito com pesquisa mais ampla
- **Tendencias sem evidencia**: qualquer tendencia listada sem pelo menos 2 exemplos concretos de posts deve ser removida do relatorio
- **Ausencia de @economesteter**: relatorio que nao inclua analise especifica de @economesteter como conta base e automaticamente rejeitado
