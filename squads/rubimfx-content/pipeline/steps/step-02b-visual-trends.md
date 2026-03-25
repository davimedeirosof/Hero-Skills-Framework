---
execution: subagent
agent: vitor-visual
outputFile: squads/rubimfx-content/output/style-guide.md
model_tier: fast
---

# Step 02b — Visual Trends Research (Subagent, parallel)

## Context Loading

- `company.md` — identidade visual @rubimfx, paleta de cores, tipografia base
- `agents/vitor-visual/agent.md` — configuração e capabilities do agente visual
- `agents/vitor-visual/tasks/research-visual-trends.md` — task de pesquisa de tendências visuais
- `agents/vitor-visual/tasks/extract-style-guide.md` — task de extração de style guide
- `squads/rubimfx-content/output/style-guide.md` — style guide anterior (se existir, para atualização incremental)

## Instructions

Este step roda em paralelo com o Step 02. O agente Vitor pesquisa tendências visuais atuais no Instagram, especialmente no nicho de finanças/trading, e atualiza o style guide da marca.

### Processo

1. **Carregar referências** — Ler company.md para entender a identidade visual atual. Consultar o style guide anterior (se existir) para manter consistência evolutiva.

2. **Executar research-visual-trends.md** — Pesquisar tendências visuais atuais:
   - Perfis de referência: @economesteter, @primorico, @thiagofinancas, @investidorsardinha
   - Tendências de design no Instagram para nicho financeiro
   - Padrões de carrossel que performam bem (layouts, tipografia, cores)
   - Elementos visuais em alta (gradientes, glassmorphism, data viz, ícones)
   - Formatos de slide que geram mais saves e shares

3. **Executar extract-style-guide.md** — Compilar descobertas em um style guide atualizado:
   - Paleta de cores primária e secundária
   - Tipografia (fontes, tamanhos, hierarquia)
   - Layout grid para carrossel (margens, espaçamentos)
   - Elementos gráficos (ícones, separadores, badges)
   - Padrões de slide (capa, conteúdo, dados, CTA)
   - Referência visual @economesteter (editorial, clean, dados em destaque)

4. **Comparar com anterior** — Se existir style guide prévio, destacar o que mudou e por quê.

5. **Validar coerência** — Garantir que o style guide mantém a identidade @rubimfx mesmo incorporando tendências novas.

## Output Format

```markdown
# Style Guide — @rubimfx
## Atualizado em: [data]

### Referências Visuais
- [perfil 1]: [o que absorver]
- [perfil 2]: [o que absorver]

### Paleta de Cores
- Primária: [hex codes]
- Secundária: [hex codes]
- Texto: [hex codes]
- Background: [hex codes]

### Tipografia
- Títulos: [fonte, peso, tamanho]
- Corpo: [fonte, peso, tamanho]
- Dados/Destaque: [fonte, peso, tamanho]

### Layout Carrossel
- Dimensões: [tamanho]
- Grid: [especificações]
- Margens: [valores]

### Padrões de Slide
[tipos de slide com descrição]

### Tendências Atuais
[lista de tendências incorporadas]
```

## Output Example

```markdown
# Style Guide — @rubimfx
## Atualizado em: 2026-03-15

### Referências Visuais
- @economesteter: Layout editorial limpo, dados em destaque com background contrastante, uso de ícones minimalistas
- @primorico: Tipografia bold para hooks, slides com pouco texto e alto impacto
- @thiagofinancas: Uso de gráficos simplificados, cores quentes para urgência

### Paleta de Cores
- Primária: #1A1A2E (deep navy), #E94560 (accent red), #0F3460 (dark blue)
- Secundária: #16213E (mid navy), #533483 (purple accent), #F5C518 (gold highlight)
- Texto: #FFFFFF (primary), #B8B8D0 (secondary), #E94560 (emphasis)
- Background: #0A0A1A (dark base), #1A1A2E (card bg), linear-gradient(135deg, #0A0A1A, #1A1A2E)

### Tipografia
- Títulos: Inter Bold, 700, 36-48px — impacto máximo, sem serifa
- Corpo: Inter Regular, 400, 18-22px — legibilidade em mobile
- Dados/Destaque: Space Mono Bold, 700, 28-36px — números e dados econômicos
- Labels: Inter Medium, 500, 12-14px — tags, datas, categorias

### Layout Carrossel
- Dimensões: 1080x1350px (4:5 ratio, maximiza espaço no feed)
- Grid: 12 colunas, 60px margens laterais, 40px gutter
- Margens: 60px lateral, 80px top, 60px bottom
- Safe zone: 960x1190px (conteúdo principal)

### Padrões de Slide

#### Slide Capa (Tipo A)
- Hook em 2-3 linhas, tipografia bold
- Ícone ou emoji representativo do tema
- Badge de categoria (MACRO, FOREX, OURO, PROP)
- Background: gradiente escuro com sutil textura

#### Slide Contexto (Tipo B)
- Título do tópico + corpo explicativo
- Máximo 4 linhas de texto
- Separador visual entre título e corpo
- Ícone à esquerda do título

#### Slide Dados (Tipo C)
- Número grande centralizado (Space Mono)
- Label acima do número (o que é)
- Variação percentual com cor (verde/vermelho)
- Fonte dos dados no rodapé

#### Slide Bridge (Tipo D)
- Divisão visual: macro (topo) → trading (base)
- Seta ou conector visual entre as duas seções
- Ativo + direção + emoji indicativo
- Background levemente diferenciado

#### Slide CTA (Tipo E)
- Pergunta engajadora ou call to action
- Menção @rubimfx
- "Salve para consultar depois" ou "Comenta o ativo que você opera"
- Logo ou marca d'água sutil

### Tendências Atuais (Q1 2026)
- **Glassmorphism sutil** — cards com blur leve sobre background gradiente
- **Data visualization** — mini charts e sparklines inline com texto
- **Micro-animações** — setas e indicadores com sensação de movimento (via design estático que sugere motion)
- **Color blocking** — blocos de cor sólida para separar seções
- **Editorial minimalism** — influência de @economesteter: menos é mais, dados falam
```

## Veto Conditions

- **Perda de identidade** — O style guide não pode desviar radicalmente da identidade visual existente da @rubimfx. Tendências devem ser incorporadas como evolução, não revolução.
- **Ilegibilidade** — Qualquer combinação de cores que não passe no teste de contraste WCAG AA para texto sobre background deve ser rejeitada.
- **Excesso de tendências** — Máximo de 3-4 tendências novas por atualização. Incorporar tudo ao mesmo tempo dilui a identidade.

## Quality Criteria

- A paleta de cores deve ter no mínimo 4 cores definidas com hex codes
- A tipografia deve especificar fonte, peso e tamanho para pelo menos 3 níveis hierárquicos
- Pelo menos 3 perfis de referência devem ser analisados
- Os padrões de slide devem cobrir no mínimo: capa, conteúdo, dados e CTA
- O style guide deve ser implementável diretamente em HTML/CSS sem ambiguidade
