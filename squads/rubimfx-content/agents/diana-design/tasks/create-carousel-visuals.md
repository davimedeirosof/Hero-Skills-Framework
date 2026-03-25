---
id: create-carousel-visuals
name: "Criar Visuais do Carrossel"
agent: diana-design
trigger: manual
skills_required:
  - image-creator
input:
  - carousel_topic: string
  - slide_contents: array
  - num_slides: integer
  - accent_color: string (optional)
output:
  format: html + png
  dimensions: 1080x1440px
---

# Task: Criar Visuais do Carrossel

## Objetivo

Produzir HTML/CSS auto-contido para cada slide do carrossel do @rubimfx, seguindo o style guide editorial dark mode inspirado no @economesteter. Cada HTML é renderizado em PNG 1080x1440px via skill image-creator (Playwright).

## Process

### Passo 1 — Definir a estrutura visual do carrossel
Analise o conteúdo de todos os slides e defina:
- Accent color principal (azul, verde, vermelho, dourado ou roxo — ou o especificado no input)
- Sequência de backgrounds alternados (ex: slide 1 = #0A0A0F, slide 2 = #111118, slide 3 = #0F172A)
- Tipo de cada slide: cover, conceito, lista, comparação, dados, CTA final
- Layout base para cada tipo

### Passo 2 — Criar o HTML/CSS de cada slide
Para cada slide, produza HTML inline completo:
- Dimensões fixas: `width: 1080px; height: 1440px`
- Header bar: barra superior com "@rubimfx", height ~70px, background semi-transparente ou tom mais escuro
- Headline: sans-serif bold, 48-64px, cor branca ou accent
- Body text: sans-serif regular, 22-26px, cor #E2E8F0 ou similar
- Accent highlights: palavras-chave em accent color com `font-weight: bold`
- Padding: mínimo 40px em todos os lados (60px recomendado)
- Fontes: usar system fonts (`-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`) para garantir renderização

### Passo 3 — Slide cover (primeira slide)
O cover precisa de impacto máximo:
- Headline grande (56-72px) com o título do carrossel
- Subtítulo opcional em accent color
- Elemento visual de destaque (linha decorativa, ícone em CSS, número grande)
- Branding @rubimfx proeminente
- Texto "Deslize >>>" ou seta indicando carrossel

### Passo 4 — Slide CTA (última slide)
Fechamento com call-to-action:
- "Salva esse carrossel" / "Siga @rubimfx para mais" / "Comenta sua dúvida"
- Branding reforçado
- Visual limpo, não sobrecarregado
- Disclaimer se necessário: "Conteúdo educacional"

### Passo 5 — Renderizar via image-creator
Use a skill image-creator para converter cada HTML em PNG:
- Resolução: 1080x1440px
- Formato: PNG
- Nomeação: `slide-01.png`, `slide-02.png`, etc.

## Output Format

```markdown
## Carrossel Visual — [Tema]

### Design Notes
- Accent color: [cor]
- Background rotation: [cores]
- Tipografia: [fonte], [tamanhos]
- Total slides: [N]

### Slide [N] — [Tipo: cover/conceito/lista/CTA]

```html
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0; padding:0; width:1080px; height:1440px; background:#0A0A0F; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; color:#F1F5F9; overflow:hidden;">
  <!-- slide content -->
</body>
</html>
```

**Renderizado**: slide-[N].png
```

## Output Example

```markdown
## Carrossel Visual — Order Blocks: O Mapa do Smart Money

### Design Notes
- Accent color: #3B82F6 (azul)
- Background rotation: #0A0A0F, #111118, #0F172A
- Tipografia: system sans-serif, headlines 56px bold, body 24px
- Total slides: 7

### Slide 1 — Cover

```html
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;width:1080px;height:1440px;background:#0A0A0F;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#F1F5F9;overflow:hidden;display:flex;flex-direction:column;">
  <div style="background:#13131A;padding:16px 40px;display:flex;align-items:center;justify-content:space-between;">
    <span style="font-size:20px;font-weight:700;color:#3B82F6;">@rubimfx</span>
    <span style="font-size:16px;color:#64748B;">Educacional</span>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:60px;">
    <div style="font-size:120px;font-weight:900;color:#3B82F6;line-height:1;margin-bottom:24px;">OB</div>
    <h1 style="font-size:56px;font-weight:800;line-height:1.15;margin:0 0 20px 0;">Order Blocks:<br>O Mapa do<br><span style="color:#3B82F6;">Smart Money</span></h1>
    <p style="font-size:24px;color:#94A3B8;margin:0;">Como identificar as zonas onde o institucional realmente opera</p>
    <div style="margin-top:48px;display:flex;align-items:center;gap:8px;">
      <span style="font-size:20px;color:#64748B;">Deslize para aprender</span>
      <span style="font-size:24px;color:#3B82F6;">→→→</span>
    </div>
  </div>
</body>
</html>
```

**Renderizado**: slide-01.png
```

## Quality Criteria

1. Cada HTML renderiza corretamente em exatamente 1080x1440px sem overflow ou corte
2. Header bar com @rubimfx presente em todas as slides
3. Contraste texto/background passa WCAG AA (4.5:1 mínimo)
4. Máximo 80 palavras de texto por slide
5. HTML auto-contido — zero dependências externas (sem CDN, sem imagens externas, sem JS)
6. Alternância visual de background entre slides consecutivas

## Veto Conditions

1. **Dimensões incorretas**: Qualquer slide que não seja exatamente 1080x1440px — VETO, corrigir dimensões antes de renderizar.
2. **Dependências externas**: HTML que referencia fontes CDN, imagens externas ou scripts — VETO, converter para inline/system fonts.
3. **Background claro**: Qualquer slide com fundo branco, bege ou pastel — VETO, substituir por dark mode conforme palette.
