---
id: extract-style-guide
title: Compilar Guia de Estilo para Diana Design
agent: vitor-visual
trigger: on-demand
depends_on:
  - research-visual-trends
skills_required:
  - web_search
  - web_fetch
input:
  - trend-report.md
  - style-guide-anterior.md (se existente)
output: style-guide.md
---

# Task: Compilar Guia de Estilo para Diana Design

## Objetivo
Transformar o relatorio de tendencias em um guia de estilo pratico e completo que Diana Design usa diretamente para criar carrosseis de @rubimfx. O guia mantem @economesteter como base visual e incorpora tendencias relevantes identificadas na pesquisa.

## Process

### Step 1 — Consolidar Base @economesteter
Documentar o estilo base que nunca muda (apenas se refina):
- Fundos: dark #0D1117 ou navy #0F1729, opcao gradiente radial sutil
- Tipografia: sans-serif bold para headlines, regular para corpo
- Cores de destaque: gold #F59E0B (dados, numeros), teal #00D4AA (positivo, alta), red #EF4444 (negativo, queda)
- Header bar: faixa superior com logo @rubimfx e titulo da serie
- Primeira slide: estilo capa de revista editorial com foto do Gabriel Rubim, headline bold, subtitulo
- Densidade: alta informacao por slide, graficos e infograficos integrados
- Consistencia: mesmo grid e espacamento em todos os slides do carrossel

### Step 2 — Incorporar Tendencias Aprovadas
Do trend-report, selecionar apenas tendencias classificadas como "adotar agora" ou "testar" e documentar:
- Como aplicar a tendencia dentro da base @economesteter
- Em quais tipos de slide usar (capa, conteudo, dados, CTA)
- Limites de uso (ex: gradiente so em capa e CTA, nao em slides de dados)
- Data de validade estimada para reavaliar a tendencia

### Step 3 — Montar Especificacoes Tecnicas
Compilar todas as regras em formato de referencia rapida:
- Paleta de cores completa com hex, nome e uso recomendado
- Escala tipografica com fonte, peso, tamanho e uso por hierarquia
- Grid e espacamento (margens, gutters, padding)
- Templates de layout para cada tipo de slide
- Regras de uso de imagens e fotos
- Do's and Don'ts com exemplos descritivos

## Output Format

Arquivo Markdown estruturado como guia de referencia, com secoes claramente separadas, tabelas de especificacao e exemplos descritivos. Deve funcionar como documento standalone que Diana Design consulta sem precisar de contexto adicional.

## Output Example

```markdown
---
type: style-guide
version: "2026-W11"
base_reference: "@economesteter"
brand: "@rubimfx"
updated: "2026-03-15"
author: vitor-visual
status: active
---

# Guia de Estilo — Carrosseis @rubimfx

## 1. Base Visual (Imutavel)
Referencia principal: @economesteter. Todo carrossel @rubimfx segue este
estilo editorial profissional como fundacao.

## 2. Paleta de Cores

### Cores de Fundo
| Nome | Hex | Uso |
|------|-----|-----|
| Dark Primary | #0D1117 | Fundo principal padrao |
| Navy Deep | #0F1729 | Fundo alternativo, slides de dados |
| Dark Gradient Center | #0D1117 | Centro do gradiente radial |
| Dark Gradient Edge | #1A1040 | Borda do gradiente (tendencia atual) |

### Cores de Texto
| Nome | Hex | Uso |
|------|-----|-----|
| White Primary | #FFFFFF | Headlines e texto principal |
| White Secondary | #E5E7EB | Corpo de texto e descricoes |
| Gray Muted | #9CA3AF | Labels, footnotes, fonte de dados |

### Cores de Destaque
| Nome | Hex | Uso |
|------|-----|-----|
| Gold Accent | #F59E0B | Numeros, dados em destaque, KPIs |
| Teal Positive | #00D4AA | Indicadores positivos, alta, lucro |
| Red Negative | #EF4444 | Indicadores negativos, queda, prejuizo |
| Blue Info | #3B82F6 | Links, elementos informativos neutros |

## 3. Tipografia

| Nivel | Fonte | Peso | Tamanho | Uso |
|-------|-------|------|---------|-----|
| H1 - Headline Capa | Inter / Montserrat | ExtraBold 800 | 36-42pt | Titulo da primeira slide |
| H2 - Headline Slide | Inter / Montserrat | Bold 700 | 28-32pt | Titulo de cada slide |
| H3 - Subtitulo | Inter / Montserrat | SemiBold 600 | 20-24pt | Subtitulos e destaques |
| Body | Inter / Montserrat | Regular 400 | 16-18pt | Corpo de texto |
| Caption | Inter / Montserrat | Medium 500 | 12-14pt | Fontes, labels, rodape |
| Data Highlight | Inter / Montserrat | ExtraBold 800 | 48-64pt | Numeros em destaque |

**Regras**: caixa alta em headlines de capa. Tracking -0.01em em headlines.
Line-height 1.2 para headlines, 1.5 para corpo.

## 4. Templates de Layout

### Slide 1 — Capa Editorial
- Foto de Gabriel Rubim (lado esquerdo ou fundo com overlay escuro)
- Header bar com logo @rubimfx (topo, 48px altura, fundo #0D1117 100%)
- Headline bold caixa alta centralizada ou alinhada a direita
- Subtitulo em White Secondary abaixo da headline
- Elemento de cor accent como separador ou underline

### Slide 2-8 — Conteudo Informativo
- Header bar mantida no topo com titulo da serie
- Titulo do slide (H2) no topo, abaixo do header
- Area de conteudo com grid de 2 colunas quando necessario
- Graficos e infograficos integrados com cores da paleta
- Margem lateral: 40px | Margem topo/base: 60px | Gutter: 24px

### Slide Final — CTA
- Fundo gradiente radial (tendencia incorporada)
- Foto de Gabriel Rubim menor, circular ou recortada
- Headline de acao: "Siga @rubimfx" ou CTA do conteudo
- Icones de redes sociais em Gray Muted

## 5. Do's and Don'ts

### DO (Fazer)
- Usar fundo escuro como base em TODOS os slides
- Manter header bar consistente em todos os slides
- Usar Gold #F59E0B para destacar numeros e dados-chave
- Manter hierarquia tipografica rigida (H1 > H2 > H3 > Body)
- Incluir fonte de dados em Caption nos slides informativos
- Usar gradiente radial sutil apenas em capa e CTA

### DON'T (Nao Fazer)
- Usar fundo branco ou claro em nenhum slide
- Misturar mais de 2 cores de destaque por slide
- Usar fontes decorativas, scripts ou serif
- Reduzir corpo de texto abaixo de 14pt
- Colocar texto sobre areas de foto sem overlay escuro
- Usar mais de 3 niveis de hierarquia tipografica por slide
```

## Quality Criteria

- [ ] Base @economesteter documentada explicitamente como fundacao do estilo
- [ ] Paleta de cores completa com todos os hex codes e uso recomendado por cor
- [ ] Regras tipograficas com fonte, peso, tamanho e uso para cada nivel hierarquico
- [ ] Pelo menos 3 templates de layout (capa, conteudo, CTA) com especificacoes de margem e grid
- [ ] Secao Do's and Don'ts com minimo 5 itens em cada lista
- [ ] Tendencias incorporadas estao identificadas e separadas da base permanente
- [ ] Documento e auto-suficiente — Diana Design nao precisa de outra referencia

## Veto Conditions

- **Base @economesteter ausente ou diluida**: se o guia nao estabelece claramente o estilo @economesteter como base inegociavel, com fundos escuros, tipografia bold e layout editorial, deve ser reescrito
- **Especificacoes incompletas**: guia sem hex codes de cores, sem nomes de fontes ou sem medidas de espacamento nao pode ser entregue a Diana Design
- **Tendencias sem classificacao temporal**: elementos de tendencia incorporados sem data de validade estimada ou indicacao de que sao temporarios serao rejeitados para evitar que se tornem permanentes por inercao
