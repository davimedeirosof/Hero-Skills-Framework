# Kaique Epic — Referência Visual Completa

> Baseado em @kaique.editor (237K seguidores). Estilo FAVORITO do Gabriel.
> Capas cinematográficas com fotos IA épicas + tweet cards brancos.

---

## QUANDO USAR
- Conteúdo de mindset/motivação
- Storytelling pessoal
- Temas bíblicos/espirituais
- Disciplina e protocolo
- Qualquer tema que precise de IMPACTO VISUAL máximo

## QUANDO NÃO USAR
- Notícias factuais que precisam de screenshots de reportagem
- Conteúdo puramente educacional/dados

---

## 2 TIPOS DE CARD

### TIPO A — EPIC COVER (full bleed, headline gigante)

```
┌─────────────────────────────────┐
│                                 │
│    FOTO IA ÉPICA FULLSCREEN     │  ← Foto cobre 100% do slide
│    (cenário cinematográfico)    │     object-fit: cover
│                                 │
│                                 │
│  ┌── gradiente escuro ───────┐  │
│  │                           │  │  ← Gradiente: transparent → 0.92
│  │ HEADLINE GIGANTE          │  │  ← 80-96px, UPPERCASE, bold 900
│  │ COM PALAVRAS EM           │  │     text-shadow pesado
│  │ AMARELO OU VERMELHO       │  │     .yellow { #FFD600 }
│  │                           │  │     .red { #FF3B30 }
│  │ Subtítulo/fontes          │  │  ← 22px, rgba(255,255,255,0.7)
│  │                           │  │
│  │ ARRASTA PRO LADO >>> │ @rubimfx │  ← Bottom bar com border-top
│  │ ● ○ ○ ○ ○ ○ ○ ○ ○ ○     │  │  ← Dots (active = branco)
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

**CSS essencial:**
```css
body { width: 1080px; height: 1350px; position: relative; overflow: hidden; }
.bg-image { position: absolute; inset: 0; z-index: 1; }
.bg-image img { width: 100%; height: 100%; object-fit: cover; }
.bg-overlay { position: absolute; inset: 0; z-index: 2;
  background: linear-gradient(180deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.15) 20%,
  rgba(0,0,0,0.25) 45%, rgba(0,0,0,0.7) 70%, rgba(0,0,0,0.92) 100%); }
.content { position: relative; z-index: 10; width: 100%; height: 100%;
  display: flex; flex-direction: column; justify-content: flex-end; padding: 0 56px 48px; }
.headline { font-size: 86px; font-weight: 900; line-height: 0.95; text-transform: uppercase;
  text-shadow: 0 2px 8px rgba(0,0,0,0.6), 0 4px 24px rgba(0,0,0,0.4); }
```

**Usar para:** Slides 01, 04, 07, 10 (capas e CTA)

---

### TIPO B — TWEET CARD (branco top + foto bottom)

```
┌─────────────────────────────────┐
│ ┌─ FUNDO BRANCO ─────────────┐  │
│ │ 📷 Gabriel Rubim ✓         │  │  ← Profile row (52px avatar)
│ │    @rubimfx                │  │
│ │                            │  │
│ │ HEADLINE BOLD              │  │  ← 52px, UPPERCASE, preto #0F1419
│ │ EM CIMA (AZUL/VERMELHO)    │  │     .blue { #1D9BF0 }
│ │                            │  │     .red { #F4212E }
│ │ Texto do conteúdo aqui     │  │  ← 28px, #292F33, line-height 1.45
│ │ com palavras em bold       │  │     strong { #0F1419, weight 800 }
│ │                            │  │
│ ├────────────────────────────┤  │
│ │                            │  │
│ │    FOTO IA TEMÁTICA        │  │  ← flex: 1, object-fit cover
│ │    (ilustra o conceito)    │  │     Gradiente 120px no bottom
│ │                            │  │
│ │ ARRASTA >>> │ @rubimfx     │  │  ← Bar sobre foto (z-index 10)
│ │ ○ ○ ● ○ ○ ○ ○ ○ ○ ○      │  │  ← Dots na foto
│ └────────────────────────────┘  │
└─────────────────────────────────┘
```

**CSS essencial:**
```css
body { width: 1080px; height: 1350px; background: #FFFFFF;
  display: flex; flex-direction: column; overflow: hidden; }
.top-section { flex-shrink: 0; padding: 40px 52px 0; }
.headline { font-size: 52px; font-weight: 900; text-transform: uppercase; color: #0F1419; }
.body-text { font-size: 28px; color: #292F33; line-height: 1.45; }
.bottom-section { flex: 1; position: relative; overflow: hidden; }
.bottom-section img { width: 100%; height: 100%; object-fit: cover; }
.bottom-section::after { height: 120px; background: linear-gradient(transparent, rgba(0,0,0,0.7)); }
```

**Usar para:** Slides 02, 03, 05, 06, 08, 09 (conteúdo)

---

## PALETA DE CORES

| Elemento | Cor | Hex |
|---|---|---|
| Destaque principal | Amarelo | `#FFD600` |
| Alerta/perigo | Vermelho | `#FF3B30` |
| Info/link | Azul | `#1D9BF0` |
| Texto branco | White | `#FFFFFF` |
| Texto muted | Light gray | `rgba(255,255,255,0.7)` |
| Fundo card branco | White | `#FFFFFF` |
| Texto preto (card) | Dark | `#0F1419` |
| Texto body (card) | Gray | `#292F33` |
| Texto secondary | Gray | `#536471` |
| Border card | Light | `#EFF3F4` |

---

## ESTRUTURA PADRÃO — 10 SLIDES

```
Slide 01 → TIPO A — Epic Cover (foto épica + headline)
Slide 02 → TIPO B — Tweet Card (ponto 1)
Slide 03 → TIPO B — Tweet Card (ponto 2)
Slide 04 → TIPO A — Epic (foto épica + dado impactante)
Slide 05 → TIPO B — Tweet Card (ponto 3)
Slide 06 → TIPO B — Tweet Card (ponto 4)
Slide 07 → TIPO A — Epic (foto épica + frase forte)
Slide 08 → TIPO B — Tweet Card (ponto 5)
Slide 09 → TIPO B — Tweet Card (ponto 6 / protocolo)
Slide 10 → TIPO A — Epic CTA (SEGUE @rubimfx)
```

---

## REGRAS DE FOTOS

### Para Epic Covers (Tipo A):
- Fotos IA ÉPICAS, cinematográficas, nível poster de filme
- Prompts com: volumetric light, god-rays, epic scale, cinematic
- Clones do Gabriel em poses de PODER (braços cruzados, hilltop, backlight)
- Temas que funcionam: guerreiro, campo de batalha, montanha, tempestade, nascer do sol
- Camera: RED cinema, ARRI Alexa, anamorphic lens
- Color: teal and orange, golden hour, Cinestill 800T

### Para Tweet Cards (Tipo B):
- Fotos temáticas que ILUSTRAM o conceito do texto
- Podem ser IA ou reais
- Devem combinar com o texto acima
- Escudo + espada = protocolo/proteção
- Campo de batalha = guerra/disciplina
- Correntes quebradas = liberdade/vitória

---

## REGRAS DE TIPOGRAFIA

| Elemento | Tamanho | Peso | Fonte |
|---|---|---|---|
| Epic headline | 80-96px | 900 | System sans-serif |
| Epic subtitle | 22px | 500 | System sans-serif |
| Tweet headline | 52px | 900 | System sans-serif |
| Tweet body | 28px | 450 | System sans-serif |
| Profile name | 26px | 700 | System sans-serif |
| Handle | 22px | 400 | System sans-serif |
| CTA/arrasta | 22px | 700 | System sans-serif, uppercase |
| NADA abaixo | 20px | — | — |

---

## BOTTOM BAR (em todos os slides)

```html
<div class="bottom-bar">
  <div class="cta">ARRASTA PRO LADO <span class="arrows">&gt;&gt;&gt;</span></div>
  <div class="handle">@RUBIMFX</div>
</div>
```

- Arrows em amarelo (#FFD600)
- Texto em rgba(255,255,255,0.7) para Epic, rgba(255,255,255,0.8) para Tweet
- border-top: 1px solid rgba(255,255,255,0.15) no Epic
- Sobre gradiente escuro no Tweet card

---

## EXEMPLOS DE PROMPTS ÉPICOS QUE FUNCIONARAM

### Guerreiro na terra prometida:
```
Hyper-realistic cinematic photograph of a lone warrior standing at the edge of a cliff
overlooking a vast promised land — green valleys, rivers, mountains in golden sunset light.
Dramatic volumetric god-rays breaking through storm clouds. Biblical epic scale,
Lord of the Rings atmosphere. Shot on RED cinema camera, 35mm anamorphic, golden hour.
4:5 portrait. No text.
```

### Muralhas caindo:
```
Hyper-realistic cinematic photograph of ancient walls crumbling and falling in a massive
explosion of dust and stone, with divine light piercing through the destruction from above.
Dramatic biblical scene of victory through faith. Massive scale, earthquake effect.
Shot on RED V-Raptor, 24mm wide angle, volumetric dust particles in golden light.
4:5 portrait. No text.
```

### Clone guerreiro:
```
Gabriel standing like a warrior commander on a hilltop at golden hour, wearing a dark
fitted shirt, arms at his sides with fists clenched. Dramatic backlight creating powerful
rim lighting silhouette. Epic leadership pose, conqueror energy. Cinematic Hollywood poster feel.
```

---

## TEMPLATES HTML

- `template-09-kaique-epic.html` — Epic Cover (Tipo A)
- `template-10-kaique-tweet.html` — Tweet Card (Tipo B)
