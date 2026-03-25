---
execution: inline
agent: diana-design
inputFile: squads/rubimfx-content/output/carousel-draft.md
outputFile: squads/rubimfx-content/output/carousel-visuals.md
---

# Step 09 — Create Visuals (Inline)

## Context Loading

- `squads/rubimfx-content/output/carousel-draft.md` — carrossel aprovado com texto e notas de design
- `squads/rubimfx-content/output/style-guide.md` — style guide visual atualizado (do Step 02b)
- `company.md` — identidade visual @rubimfx
- `agents/diana-design/agent.md` — configuração do agente de design
- `agents/diana-design/tasks/create-carousel-visuals.md` — task de criação visual

## Instructions

Gerar o código HTML/CSS completo para cada slide do carrossel, pronto para renderização e captura de screenshot em 1080x1350px.

### Processo

1. **Carregar style guide** — Ler o style guide do Step 02b para obter: paleta de cores, tipografia, layout grid, padrões de slide. Toda decisão visual deve seguir o style guide.

2. **Analisar notas de design** — Para cada slide do carousel-draft.md, ler as notas de design que indicam: tipo de slide, layout sugerido, elementos visuais, cores de destaque.

3. **Executar create-carousel-visuals.md** — Para cada slide, gerar HTML/CSS completo:

   **Regras de implementação:**
   - Dimensão fixa: 1080x1350px (4:5 Instagram)
   - Fontes: usar Google Fonts (Inter, Space Mono) via import
   - Cores: seguir paleta do style guide exatamente
   - Layout: CSS Grid ou Flexbox, margens conforme style guide
   - Responsividade: não necessária (dimensão fixa)
   - Animação: nenhuma (output estático)
   - Imagens: usar gradientes, formas CSS e ícones Unicode/emoji em vez de imagens externas
   - Cada slide é um arquivo HTML autocontido (inline CSS)

   **Padrões de slide:**
   - **Capa:** Background gradiente, texto centralizado bold, badge de categoria no topo
   - **Contexto:** Título no topo, corpo centralizado, separador visual
   - **Dados:** Número grande centralizado (Space Mono), label acima, variação com cor
   - **Bridge:** Divisão visual macro/trading com conector (seta ou linha)
   - **CTA:** Texto centralizado, espaçamento generoso, @rubimfx em destaque

4. **Garantir consistência visual** — Todos os slides devem:
   - Usar a mesma paleta de cores base
   - Manter tipografia consistente entre slides
   - Ter o mesmo estilo de margens e espaçamento
   - Seguir o grid definido no style guide
   - Ter transição visual coesa (parecer um conjunto, não slides soltos)

5. **Adicionar elementos de marca** — Em cada slide:
   - Marca d'água sutil @rubimfx (canto inferior direito, opacidade baixa) nos slides de conteúdo
   - Badge de categoria no slide de capa
   - Numeração de slide discreta (ex: "3/8" no canto) — opcional conforme style guide

6. **Validar renderização** — Verificar que o HTML é válido, CSS não tem conflitos, e o resultado visual é clean e legível.

## Output Format

```markdown
# Carousel Visuals — [Título]

## Metadata
- Slides: [número]
- Dimensão: 1080x1350px
- Fontes: [lista]
- Paleta: [cores principais usadas]

## Slide 1 — [Tipo]

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    [CSS completo inline]
  </style>
</head>
<body>
  [HTML do slide]
</body>
</html>
```

[repete para todos os slides]
```

## Output Example

```markdown
# Carousel Visuals — O Fed falou. O ouro ouviu.

## Metadata
- Slides: 8
- Dimensão: 1080x1350px
- Fontes: Inter (400, 500, 700), Space Mono (700)
- Paleta: #0A0A1A, #1A1A2E, #E94560, #F5C518, #FFFFFF, #B8B8D0

## Slide 1 — Capa

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1080px;
      height: 1350px;
      background: linear-gradient(135deg, #0A0A1A 0%, #1A1A2E 100%);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-family: 'Inter', sans-serif;
      color: #FFFFFF;
      position: relative;
      overflow: hidden;
    }
    .badge {
      position: absolute;
      top: 60px;
      left: 60px;
      background: #E94560;
      color: #FFFFFF;
      font-family: 'Inter', sans-serif;
      font-weight: 700;
      font-size: 14px;
      padding: 8px 20px;
      border-radius: 4px;
      letter-spacing: 2px;
      text-transform: uppercase;
    }
    .icon {
      font-size: 64px;
      margin-bottom: 40px;
    }
    .hook {
      font-family: 'Inter', sans-serif;
      font-weight: 700;
      font-size: 48px;
      line-height: 1.2;
      text-align: center;
      max-width: 800px;
    }
    .hook span {
      display: block;
    }
    .watermark {
      position: absolute;
      bottom: 40px;
      right: 60px;
      font-size: 14px;
      color: rgba(255,255,255,0.25);
      font-weight: 500;
    }
  </style>
</head>
<body>
  <div class="badge">MACRO</div>
  <div class="icon">🥇</div>
  <div class="hook">
    <span>O Fed falou.</span>
    <span>O ouro ouviu.</span>
  </div>
  <div class="watermark">@rubimfx</div>
</body>
</html>
```

## Slide 2 — Contexto

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1080px;
      height: 1350px;
      background: #0A0A1A;
      display: flex;
      flex-direction: column;
      padding: 80px 60px 60px 60px;
      font-family: 'Inter', sans-serif;
      color: #FFFFFF;
      position: relative;
    }
    .title {
      font-weight: 700;
      font-size: 36px;
      line-height: 1.3;
      margin-bottom: 40px;
    }
    .separator {
      width: 80px;
      height: 4px;
      background: #E94560;
      margin-bottom: 40px;
    }
    .body-text {
      font-weight: 400;
      font-size: 24px;
      line-height: 1.6;
      color: #B8B8D0;
      max-width: 900px;
    }
    .highlight {
      font-family: 'Space Mono', monospace;
      font-weight: 700;
      font-size: 40px;
      color: #F5C518;
      margin: 40px 0;
    }
    .watermark {
      position: absolute;
      bottom: 40px;
      right: 60px;
      font-size: 14px;
      color: rgba(255,255,255,0.2);
      font-weight: 500;
    }
    .page {
      position: absolute;
      bottom: 40px;
      left: 60px;
      font-size: 14px;
      color: rgba(255,255,255,0.3);
    }
  </style>
</head>
<body>
  <div class="title">Juros mantidos.<br>Mas o recado mudou.</div>
  <div class="separator"></div>
  <div class="body-text">O Fed manteve a taxa pela quinta vez seguida.</div>
  <div class="highlight">5.25 — 5.50%</div>
  <div class="body-text">Até aí, esperado. O que surpreendeu foi o dot plot.</div>
  <div class="watermark">@rubimfx</div>
  <div class="page">2/8</div>
</body>
</html>
```
```

## Veto Conditions

- **Desvio do style guide** — Cores, fontes ou layouts que não seguem o style guide do Step 02b devem ser corrigidos. Não improvisar estilos fora do guia.
- **HTML inválido ou mal-formado** — Todo HTML deve ser válido e renderizável em qualquer browser moderno. Tags não fechadas, CSS com syntax errors ou imports quebrados devem ser corrigidos.
- **Texto ilegível** — Contraste insuficiente entre texto e background, fontes pequenas demais (abaixo de 18px para corpo), ou excesso de elementos visuais que dificultem a leitura.

## Quality Criteria

- Cada slide HTML deve renderizar corretamente em 1080x1350px sem scroll ou overflow
- A paleta de cores deve ser consistente em todos os slides (mesmas variáveis)
- Tipografia deve seguir a hierarquia definida no style guide (títulos, corpo, dados, labels)
- Elementos de marca (@rubimfx, badge) devem estar presentes conforme especificado
- O conjunto de slides deve ter coesão visual (parecer uma peça única, não slides aleatórios)
- Dados numéricos devem estar em destaque visual (tamanho maior, cor diferenciada, Space Mono)
