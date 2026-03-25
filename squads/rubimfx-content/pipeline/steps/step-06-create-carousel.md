---
execution: inline
agent: iago-instagram
format: instagram-feed
inputFile: squads/rubimfx-content/output/angles.md
outputFile: squads/rubimfx-content/output/carousel-draft.md
---

# Step 06 — Create Carousel (Inline)

## Context Loading

- `squads/rubimfx-content/output/angles.md` — ângulo selecionado (marcado como Selected Angle)
- `squads/rubimfx-content/output/news-research.md` — notícia base com dados completos
- `squads/rubimfx-content/output/style-guide.md` — style guide visual atualizado
- `company.md` — tom de voz @rubimfx, identidade da marca
- `agents/iago-instagram/agent.md` — configuração do agente
- `agents/iago-instagram/tasks/create-instagram-feed.md` — task de criação de carrossel
- `agents/iago-instagram/tasks/optimize-instagram-feed.md` — task de otimização

## Instructions

Criar o carrossel completo slide por slide, com todo o texto, hierarquia e indicações visuais. O resultado deve ser um draft pronto para design.

### Processo

1. **Carregar ângulo e dados** — Ler o ângulo selecionado, seus slides planejados, hook e tom. Ler os dados completos da notícia base para garantir precisão factual.

2. **Executar create-instagram-feed.md** — Escrever cada slide seguindo regras:
   - **Slide 1 (Capa):** Hook exato do ângulo selecionado. Máximo 12 palavras. Deve parar o scroll. Incluir badge de categoria.
   - **Slides 2-7 (Conteúdo):** Cada slide com 1 ideia central. Máximo 40 palavras por slide. Hierarquia: título (bold) + corpo (regular) + destaque (accent). Dados numéricos devem estar em tamanho grande.
   - **Slide final (CTA):** Pergunta engajadora ou call to action. Menção @rubimfx. Incentivo a salvar/compartilhar/comentar.

   Regras de copywriting @rubimfx:
   - Linguagem direta, sem enrolação
   - Dados concretos sempre que possível
   - Explicar jargão na primeira menção
   - Tom editorial inspirado em @economesteter
   - Sem clickbait vazio — toda promessa do hook deve ser entregue
   - Bridge macro→trading deve ser explícito e acionável

3. **Executar optimize-instagram-feed.md** — Revisar e otimizar:
   - Cortar palavras desnecessárias (cada slide deve ser ~30% mais enxuto que o primeiro draft)
   - Verificar fluxo narrativo (slide N deve conectar naturalmente com slide N+1)
   - Garantir que o hook é entregue até o slide final
   - Adicionar transições visuais entre slides (indicações de layout)
   - Verificar que dados estão corretos e com fonte

4. **Adicionar indicações visuais** — Para cada slide, incluir notas de design:
   - Tipo de slide (capa, contexto, dados, bridge, CTA)
   - Layout sugerido (centralizado, split, full-bleed)
   - Elementos visuais (ícone, gráfico, separador, badge)
   - Cor de destaque se diferente do padrão

5. **Revisão final** — Ler o carrossel completo em sequência e verificar: narrativa coesa, dados corretos, tom consistente, CTA forte.

## Output Format

```markdown
# Carousel Draft — [Título]

## Metadata
- Ângulo: [nome e tipo]
- Total de slides: [número]
- Tom: [tom predominante]
- Notícia base: [título]

## Slide 1 — Capa
**Tipo:** Capa
**Layout:** [indicação]
**Badge:** [categoria]

### Texto
**[HOOK EM DESTAQUE]**

### Notas de Design
- [indicação visual 1]
- [indicação visual 2]

---

## Slide 2 — [Título do slide]
**Tipo:** [tipo]
**Layout:** [indicação]

### Texto
**[Título]**
[Corpo do slide]

### Notas de Design
- [indicações]

---
[repete para todos os slides]
```

## Output Example

```markdown
# Carousel Draft — O Fed falou. O ouro ouviu.

## Metadata
- Ângulo: A — Bridge Macro→Trading
- Total de slides: 8
- Tom: Informativo com pitada de provocação
- Notícia base: Fed mantém juros mas sinaliza corte em junho

## Slide 1 — Capa
**Tipo:** Capa
**Layout:** Centralizado, texto sobre gradiente escuro
**Badge:** MACRO

### Texto
**O Fed falou.**
**O ouro ouviu.**

### Notas de Design
- Background: gradiente #0A0A1A → #1A1A2E
- Badge "MACRO" no canto superior esquerdo (#E94560)
- Emoji ou ícone de ouro centralizado acima do texto
- Tipografia: Inter Bold 44px, 2 linhas

---

## Slide 2 — O que o Fed decidiu
**Tipo:** Contexto
**Layout:** Título topo + corpo centro + dado destaque base

### Texto
**Juros mantidos. Mas o recado mudou.**

O Fed manteve a taxa em 5.25-5.50% pela quinta vez seguida.

Até aí, esperado. O que surpreendeu foi o dot plot.

### Notas de Design
- Título em Inter Bold 28px
- "5.25-5.50%" em Space Mono Bold 36px com cor #F5C518
- Ícone de banco/prédio ao lado do título

---

## Slide 3 — O que é o dot plot
**Tipo:** Dados/Educacional
**Layout:** Centralizado com número grande

### Texto
**Dot Plot: o mapa dos juros**

Cada ponto = a projeção de 1 membro do Fed.

A maioria agora aponta para corte em junho.

### Notas de Design
- Representação visual simplificada de dot plot (6-8 pontos)
- Destaque no cluster que aponta corte
- Label: "Projeção mediana: 4.75% ao fim de 2026"

---

## Slide 4 — A reação do ouro
**Tipo:** Dados
**Layout:** Número grande centralizado + contexto abaixo

### Texto
**+2.3%**

O ouro subiu para $2.385/oz — nova máxima histórica.

Fluxo para ETFs de ouro: $1.2 bilhão em 24h.

### Notas de Design
- "+2.3%" em Space Mono Bold 56px, cor #F5C518
- "$2.385" em destaque secundário
- Seta para cima indicando ATH
- Background card com leve glassmorphism

---

## Slide 5 — Por que ouro sobe quando juros caem
**Tipo:** Educacional/Bridge
**Layout:** Split vertical — juros à esquerda, ouro à direita

### Texto
**Juros caem → Dólar enfraquece → Ouro sobe**

O ouro não paga juros. Quando os títulos americanos rendem menos, o ouro fica mais atrativo.

É a relação inversa mais famosa do mercado.

### Notas de Design
- Fluxo visual com setas: Juros ↓ → DXY ↓ → XAU ↑
- Cada etapa em um card com ícone
- Conexão visual entre os 3 elementos

---

## Slide 6 — O que aconteceu no DXY
**Tipo:** Dados
**Layout:** Número + contexto

### Texto
**DXY perdeu 104.00**

Primeira vez abaixo desse nível em 2 meses.

Dólar fraco = combustível para ouro e euro.

### Notas de Design
- "104.00" em Space Mono Bold, riscado com linha vermelha
- Seta para baixo em #E94560
- Mini representação de suporte sendo rompido

---

## Slide 7 — Bridge: como operar isso
**Tipo:** Bridge/Prático
**Layout:** Card com setup estruturado

### Texto
**E na prática?**

Se o cenário de corte em junho se confirmar:
- Ouro: suporte em $2.350, alvo $2.450
- EUR/USD: acima de 1.0900, momentum comprador
- DXY: abaixo de 104, viés baixista

Atenção: NFP da próxima semana pode mudar tudo.

### Notas de Design
- Card estilo "setup" com borda #F5C518
- Cada ativo em linha separada com ícone de direção (↑ ↓)
- Warning banner para NFP em #E94560
- Disclaimer sutil: "Não é recomendação de investimento"

---

## Slide 8 — CTA
**Tipo:** CTA
**Layout:** Centralizado, clean

### Texto
**E você?**

Está de olho no ouro ou no dólar?

Comenta o ativo que você está operando.

Salva esse post para consultar antes do NFP.

@rubimfx

### Notas de Design
- Texto centralizado, espaçamento generoso
- @rubimfx em destaque
- Ícone de bookmark/salvar
- Background igual ao slide 1 para fechar o ciclo visual
```

## Veto Conditions

- **Dados incorretos ou inventados** — Todo número, porcentagem e dado deve vir diretamente da pesquisa do Step 02. Não inventar estatísticas.
- **Mais de 50 palavras por slide** — Carrossel Instagram é visual-first. Se um slide tem mais de 50 palavras, deve ser dividido em dois.
- **Hook não entregue** — Se o slide 1 promete algo ("O ouro ouviu"), os slides seguintes devem entregar a explicação completa.
- **Sem bridge macro→trading** — Se o ângulo selecionado for Bridge (A), deve haver pelo menos 1 slide com setup prático. Para outros ângulos, pelo menos 1 slide conectando macro com operação.

## Quality Criteria

- O carrossel deve ter entre 6 e 10 slides (sweet spot do Instagram)
- Cada slide deve ter no máximo 40 palavras (exceto slides educacionais que podem ter até 50)
- O fluxo de slides deve seguir uma narrativa lógica: hook → contexto → dados → bridge → CTA
- Pelo menos 2 slides devem conter dados numéricos concretos
- O CTA final deve ter pergunta engajadora que incentive comentários
- Notas de design devem ser específicas o suficiente para guiar o Step 09
