# Style Guide @economesteter — @rubimfx Content Pipeline

## Visao Geral

Este guia define o padrao visual base para todos os carrosseis do @rubimfx, baseado no estilo editorial do @economesteter. Este e o documento de referencia inicial — Vitor Visual (designer da squad) atualiza conforme evolucao do branding.

**Ultima atualizacao:** Versao inicial
**Responsavel por atualizacoes:** Vitor Visual (designer da squad)

---

## Paleta de Cores

### Backgrounds

| Uso | Cor | Hex | Nota |
|---|---|---|---|
| Background primario | Navy escuro | `#0D1117` | Padrao para maioria dos slides |
| Background secundario | Charcoal | `#1A1B2E` | Alternancia visual entre slides |
| Background accent | Navy profundo | `#0A0E1A` | Slides de destaque |
| Background elevado | Cinza escuro | `#161B22` | Cards internos, tabelas |

**REGRA ABSOLUTA:** Background SEMPRE escuro. Light mode e proibido.

### Textos

| Uso | Cor | Hex |
|---|---|---|
| Texto primario | Branco | `#FFFFFF` |
| Texto secundario | Cinza claro | `#A0AEC0` |
| Texto terciario | Cinza medio | `#718096` |
| Texto sobre accent | Branco ou preto | Depende do contraste |

### Cores de Destaque (Accent)

| Uso | Cor | Hex | Quando usar |
|---|---|---|---|
| Accent primario | Gold | `#F59E0B` | Destaques, titulos accent, dados-chave |
| Accent alternativo | Teal | `#00D4AA` | Alternativa ao gold quando necessario |
| Accent secundario | Azul claro | `#3B82F6` | Links conceituais, complementar |

**Regra:** Escolher UM accent por carrossel (gold OU teal) e manter consistente em todos os slides.

### Cores Semanticas

| Uso | Cor | Hex |
|---|---|---|
| Positivo / Gain / Alta | Verde | `#22C55E` |
| Negativo / Loss / Queda | Vermelho | `#EF4444` |
| Neutro / Sem mudanca | Cinza | `#A0AEC0` |
| Alerta / Atencao | Amarelo | `#EAB308` |

---

## Tipografia

### Headlines / Titulos

- **Fontes:** Montserrat Bold, Space Grotesk Bold (primeira opcao), ou Inter Bold
- **Estilo:** CAPS ou Title Case
- **Peso:** Bold (700) ou Extra Bold (800)
- **Tamanho equivalente:** 28-40px (depende do comprimento do texto)
- **Tracking:** Levemente expandido (+0.5px a +1px)
- **Cor:** Branco (#FFFFFF) ou accent color

### Subtitulos

- **Fontes:** Montserrat Semi-Bold, Space Grotesk Medium
- **Estilo:** Title Case
- **Peso:** Semi-Bold (600)
- **Tamanho equivalente:** 20-24px
- **Cor:** Branco ou cinza claro (#A0AEC0)

### Corpo de Texto

- **Fontes:** Inter Regular, DM Sans Regular
- **Peso:** Regular (400) ou Medium (500)
- **Tamanho minimo equivalente:** 16px (nunca menor — legibilidade em mobile)
- **Line-height:** 1.5-1.6
- **Cor:** Branco (#FFFFFF) para texto principal, cinza (#A0AEC0) para secundario

### Dados e Numeros

- **Fontes:** Space Grotesk Bold, JetBrains Mono (para numeros tabulares)
- **Estilo:** Numeros sempre em destaque (tamanho maior ou cor accent)
- **Percentuais/valores:** Usar accent color ou semantico (verde/vermelho)

---

## Layout e Estrutura

### Dimensoes

- **Formato:** 3:4 portrait
- **Resolucao:** 1080 x 1440 px
- **Margem segura:** 60px em todas as bordas (conteudo nao encosta na borda)
- **Area util:** 960 x 1320 px

### Header Bar

Presente em TODOS os slides:

```
[Logo @rubimfx] .............. [Data do post]
-------------------------------------------
```

- Posicao: topo do slide
- Altura: ~80px
- Background: levemente mais escuro ou transparente
- Logo/handle: lado esquerdo
- Data: lado direito (formato: DD MMM YYYY)
- Separador: linha fina (#2D3748) ou fade

### Hierarquia por Slide

Cada slide tem exatamente 2 camadas visuais:

1. **Headline** — frase bold que resume o ponto do slide (1-2 linhas)
2. **Supporting text** — texto menor que desenvolve a headline (3-6 linhas)

Opcionalmente: elemento visual (grafico, tabela, icone) como terceira camada.

### Grid

- Layout em coluna unica para texto
- 2 colunas para comparacoes (antes/depois, bull/bear)
- Alinhamento: esquerda (nunca centralizado para corpo de texto)
- Headlines podem ser centralizadas em slides de impacto (capa, CTA)

---

## Tipos de Slide

### Slide 1 — Capa (Magazine Cover)

- Estilo magazine-cover editorial
- Elemento visual dominante: foto relevante (Powell, grafico, ativo) com overlay escuro
- Titulo bold overlay em branco ou accent
- Subtitulo menor abaixo
- Header bar com @rubimfx + data
- Tom: impactante, limpo, editorial

**Overlay escuro:** Gradiente de preto/navy com 60-80% opacidade sobre a imagem.

### Slides 2-8 — Conteudo

- Background solido (sem imagem de fundo)
- Headline + supporting text
- Dados em destaque (numeros grandes, accent color)
- Tabelas e listas quando aplicavel
- Graficos simplificados quando necessario

### Slides de Dados

- Tabelas com fundo levemente elevado (#161B22)
- Bordas sutis (#2D3748)
- Numeros em accent ou semantico (verde/vermelho)
- Sempre legivel em mobile (nao compactar demais)

### Slide Final — CTA

- @rubimfx centralizado
- CTA em texto grande
- Logos (ETF, Summit Prop) quando relevante
- Fundo pode ter accent sutil

---

## Elementos Visuais

### Graficos e Charts

- Estilo limpo, minimalista
- Linhas: 2-3px, accent color
- Background do grafico: transparente ou #0A0E1A
- Labels: cinza claro (#A0AEC0)
- Grid lines: muito sutis (#1A1B2E) ou ausentes
- Sem decoracao excessiva (sem sombras 3D, sem gradientes rainbow)

### Icones

- Estilo: line icons (nao preenchidos)
- Cor: cinza claro ou accent
- Tamanho: 24-32px
- Uso moderado (1-2 por slide maximo)

### Separadores

- Linhas finas (#2D3748)
- Ou espacamento generoso entre secoes
- Nunca ornamentos decorativos

### Setas e Indicadores

- Setas simples (→)
- Accent color para setas de destaque
- Usadas no BRIDGE para mostrar cadeia causal

---

## Branding

### Elementos Obrigatorios

1. **@rubimfx** no header bar de todos os slides
2. **Data** no header bar
3. **Disclaimer** quando conteudo envolve analise de ativos: "Conteudo educacional. Nao e recomendacao de investimento."

### Elementos Opcionais (quando relevante)

- Logo **ETF — Escola Trader Financiado** (slide CTA ou quando mencionar)
- Logo **Summit Prop** (quando mencionar prop firm)
- QR code para link (slide CTA, se aplicavel)

### Watermark

- @rubimfx em opacidade reduzida (20-30%) no canto inferior
- Alternativa: presente apenas no header bar (preferivel)

---

## Ritmo Visual (Alternancia de Slides)

Para manter engajamento visual ao longo do swipe:

| Slide | Background | Nota |
|---|---|---|
| 1 (Capa) | Imagem + overlay | Impacto visual maximo |
| 2 | #0D1117 (navy) | Padrao |
| 3 | #1A1B2E (charcoal) | Variacao sutil |
| 4 | #0D1117 (navy) | Volta ao padrao |
| 5 | Accent slide (dados) | #0A0E1A com accent color destaque |
| 6 | #1A1B2E (charcoal) | Variacao |
| 7 | #0D1117 (navy) | Padrao |
| 8 | #0A0E1A (profundo) | Slide de cenarios |
| 9 | #1A1B2E (charcoal) | Resumo |
| 10 | #0D1117 (navy) | CTA limpo |

A alternancia sutil entre backgrounds cria ritmo visual sem quebrar a consistencia.

---

## Anti-Patterns Visuais

- Background branco ou claro
- Fontes decorativas/script/serif
- Gradientes coloridos (rainbow, neon)
- Sombras pesadas / efeitos 3D
- Stock photos sem overlay
- Templates genericos de Canva
- Inconsistencia de accent color entre slides
- Texto menor que 16px equivalente
- Conteudo encostando nas bordas (sem margem)
- Mais de 2 accent colors no mesmo carrossel

---

## Notas de Implementacao

Este style guide e a BASE. Vitor Visual tem autonomia para:
- Ajustar valores especificos de cor dentro da paleta
- Adicionar novos elementos visuais que respeitem o sistema
- Criar variantes de layout para tipos especificos de conteudo
- Evoluir o branding mantendo a essencia dark/editorial

Qualquer mudanca estrutural (paleta, tipografia base, formato) deve ser documentada aqui.
