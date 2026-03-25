# Hollyfield News — Referência Visual Completa

> Baseado em @hollyfield.ia (108K seguidores).
> Estilo jornalístico editorial com fotos hero gigantes.

---

## QUANDO USAR
- Notícias de mercado/economia
- Breaking news
- Macro (Copom, Fed, petróleo)
- Qualquer notícia factual com foto editorial forte

## QUANDO NÃO USAR
- Mindset/motivação (preferir Kaique Epic)
- Conteúdo educacional puro (preferir Twitter Dark)

---

## ESTRUTURA DO CARD

```
┌─────────────────────────────┐
│ @rubimfx │ Categoria │ © │ R │  ← Header bar (fino, escuro, laranja)
├─────────────────────────────┤
│                             │
│     FOTO REAL GIGANTE       │  ← 70-80% do slide = foto hero
│     (editorial/jornalística)│     object-fit: cover, full bleed
│                             │
│  ┌─ gradiente 55% ────────┐ │  ← Escurece de baixo pra cima
│  │                        │ │
│  │ 🟠 Gabriel Rubim ✓    │ │  ← Brand row (ícone laranja 40px)
│  │    @rubimfx            │ │
│  │                        │ │
│  │ HEADLINE EDITORIAL     │ │  ← 42-44px, bold 800, branco
│  │ SOBRE A FOTO           │ │     Direto, factual, jornalístico
│  │                        │ │
│  │ Subtítulo/CTA          │ │  ← 22px, muted
│  └────────────────────────┘ │
└─────────────────────────────┘
```

---

## PALETA DE CORES

| Elemento | Cor | Hex |
|---|---|---|
| Background | Near-black | `#0a0a0a` |
| Header bg | Dark transparent | `rgba(10,10,10,0.85)` |
| Accent (logo, ícones) | Laranja | `#FF6B00` |
| Accent light | Laranja claro | `#FF8C33` |
| Texto principal | Branco | `#FFFFFF` |
| Texto muted | Light gray | `rgba(255,255,255,0.6)` |
| Border | Sutil | `rgba(255,255,255,0.08)` |

---

## HEADER BAR

```html
<div class="header-bar">
  <div class="header-handle">@rubimfx</div>
  <div class="header-category">Macro</div>
  <div class="header-right">
    <div class="header-copyright">Copyright © 2026</div>
    <div class="header-logo">R</div>  <!-- Círculo laranja 44px -->
  </div>
</div>
```

- Altura: ~72px
- Padding: 14px 40px
- flex-shrink: 0
- border-bottom: 1px solid rgba(255,255,255,0.08)

---

## FOTO HERO

- Ocupa TODO o espaço restante (flex: 1)
- `object-fit: cover` — preenche sem distorcer
- Gradiente por cima: 55% de altura, de transparent a #0a0a0a

```css
.photo-area::after {
  height: 55%;
  background: linear-gradient(180deg,
    transparent 0%,
    rgba(10,10,10,0.3) 30%,
    rgba(10,10,10,0.75) 60%,
    rgba(10,10,10,0.95) 85%,
    #0a0a0a 100%
  );
}
```

---

## TEXT AREA (sobre o gradiente)

```css
.text-area {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  z-index: 10;
  padding: 0 48px 32px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
```

### Brand Row
- Ícone circular laranja 40px + nome + ✓ + @handle
- 22px para nome, 20px para handle

### Headline
- 42-44px, bold 800, branco
- Tom jornalístico direto (não clickbait)
- line-height: 1.15
- letter-spacing: -0.5px

### CTA
- 22px, muted, informativo
- Ex: "Estreito de Ormuz bloqueado. 20% do petróleo mundial parado."

---

## VARIAÇÕES PARA SLIDES SEM FOTO

### Data Card (slides 04, 07)
- Sem foto hero
- Fundo escuro com métricas grandes
- Números em cores de destaque (vermelho, azul, verde)
- Stats chips no bottom

### Texto Puro (slide 06, 09)
- Sem foto
- Fundo escuro
- Bullets/lista com ícones
- Warning bars laranjas

### CTA Final (slide 10)
- Gradiente laranja/preto
- Profile photo grande (160px)
- "SEGUE @RUBIMFX" em bold
- Botão "follow" estilizado

---

## ESTRUTURA PADRÃO — 10 SLIDES

```
Slide 01 → FOTO HERO — Capa (foto principal da notícia)
Slide 02 → FOTO HERO — Contexto 1 (foto editorial)
Slide 03 → FOTO HERO — Contexto 2 (foto editorial)
Slide 04 → DATA CARD — Números impactantes
Slide 05 → FOTO HERO — Contexto 3 (foto editorial)
Slide 06 → TEXTO PURO — Análise/efeito dominó
Slide 07 → DATA CARD — Dado principal (dólar, etc.)
Slide 08 → FOTO HERO — Contexto 4 (foto ou IA)
Slide 09 → TEXTO PURO — Checklist/o que fazer
Slide 10 → CTA — Segue @rubimfx
```

---

## FONTES DE FOTOS

### Fotos editoriais reais (PREFERIR):
1. Firecrawl scrape → extrair og:image da matéria
2. Baixar via curl
3. São fotos Reuters, AFP, AP — qualidade profissional

### Fotos IA (para capas épicas):
- Nano Banana com prompts cinematográficos
- War room, telas de trading, explosões, etc.

---

## TEMPLATE HTML

- `template-11-hollyfield-news.html`
