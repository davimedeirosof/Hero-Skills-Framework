# 🎨 Modelos de Carrossel — Guia Visual Completo

> 6 estilos testados e documentados. Cada um com estrutura, paleta, CSS e exemplos.
> Criado em 19 de março de 2026 por @rubimfx com Claude Code.

---

## 📋 Índice dos Modelos

| # | Modelo | Referência | Status | Posts feitos |
|---|---|---|---|---|
| 1 | [Twitter Dark](#1-twitter-dark) | @economesteter / modelo Dino | ✅ Aprovado | 4 posts |
| 2 | [Esteter Style](#2-esteter-style) | @economesteter | ✅ Aprovado | 3 posts |
| 3 | [Hollyfield News](#3-hollyfield-news) | @hollyfield.ia | ✅ Aprovado | 1 post |
| 4 | [Kaique Epic](#4-kaique-epic) | @kaique.editor | ⭐ FAVORITO | 3 posts |
| 5 | [BrunoGPT Neon](#5-brunogpt-neon) | @brun0gpt | 🔲 Não testado | 0 |
| 6 | [Minimal Clean](#6-minimal-clean) | Minimalista | 🔲 Não testado | 0 |

---

## 1. Twitter Dark

### Origem
Padrão aprovado original, baseado nos posts "Dino vs Juízes" e "24 Impostos Lula".

### Estrutura Visual
```
7 tipos de card DIFERENTES em 10 slides:
├── Cover (tweet card + foto bottom)
├── Article Card (branco com foto lateral)
├── Cycle/Diagram (visual com boxes + setas)
├── Screenshot/Quote (citação grande)
├── Tweet Thread (bullets com borda vermelha)
├── Comparison (2 colunas: antes vs depois)
├── Data Card (número grande centralizado)
├── Tweet Insight (tweet limpo sem foto)
├── Protocol Card (lista com ícones)
└── CTA Final (gradiente + segue)
```

### Paleta
| Elemento | Hex |
|---|---|
| Background | `#000000` |
| Cards | `#16181C` |
| Borders | `#2F3336` |
| Red | `#F4212E` |
| Blue | `#1D9BF0` |
| Green | `#00BA7C` |
| Text | `#E7E9EA` |
| Muted | `#71767B` |

### Headlines: 52-80px | Body: 28-34px | Min: 22px

### Referência completa: `twitter-dark-reference.md`
### Posts feitos: Sanidade Mental, Ciclo do Invisível, Impostos Lula, Dino

---

## 2. Esteter Style

### Origem
@economesteter (159K). Tweet thread numerado com screenshots reais.

### Estrutura Visual
```
5 tipos de slide:
├── Type A — CAPA (badge + headline + fotos reais)
├── Type B — TWEET THREAD (1️⃣ numerado + screenshot)
├── Type C — FULL SCREENSHOT (print de matéria)
├── Type D — DATA/STATS (número grande + stats bar)
└── Type E — CTA FINAL (gradiente + segue)
```

### Layout do Tweet Thread (mais usado):
```
┌─────────────────────────┐
│ ← Post         X.com   │  ← Chrome do Twitter
├─────────────────────────┤
│ 📷 Gabriel Rubim ✓      │
│    @rubimfx             │
│ Show translation        │
│                         │
│ 1️⃣ Título da seção     │  ← 32px bold
│                         │
│ Texto do conteúdo com   │  ← 30px, keywords em bold
│ palavras em BOLD        │
│                         │
│ 14:30 · 18/03/26        │
│ 💬 1.2K 🔁 4.8K ❤️ 18K │  ← Engagement bar
├─────────────────────────┤
│ 📰 Fonte original       │
│ ┌─────────────────────┐ │
│ │ FOTO EDITORIAL REAL │ │  ← og:image da matéria
│ │ + gradiente escuro   │ │     opacity 0.6
│ │ FONTE · headline     │ │     nome da fonte + headline
│ └─────────────────────┘ │
└─────────────────────────┘
```

### Paleta
| Elemento | Hex |
|---|---|
| Background | `#0A0A0A` |
| Card | `#16181C` |
| Border | `#2F3336` |
| Blue accent | `#1D9BF0` |
| Red alert | `#F4212E` |
| Green | `#00BA7C` |
| Text | `#E7E9EA` |

### Fotos: SEMPRE editoriais reais (og:image das matérias), NUNCA screenshots de página inteira
### Referência completa: `esteter-style-reference.md`
### Posts feitos: Banco Master, Petróleo, Choque Macro v1

---

## 3. Hollyfield News

### Origem
@hollyfield.ia (108K). News cards com foto hero gigante.

### Estrutura Visual
```
┌──────────────────────────────┐
│ @rubimfx │ Categoria │ © │ R │  ← Header bar laranja
├──────────────────────────────┤
│                              │
│      FOTO HERO GIGANTE       │  ← 80% do slide
│      (editorial/IA)          │     full bleed, object-fit cover
│                              │
│  ┌── gradiente 55% ───────┐  │
│  │ 🟠 Gabriel Rubim ✓     │  │  ← Brand com ícone laranja
│  │                         │  │
│  │ HEADLINE EDITORIAL      │  │  ← 42px, bold, jornalístico
│  │                         │  │
│  │ Subtítulo/CTA           │  │
│  └─────────────────────────┘  │
└──────────────────────────────┘
```

### Paleta
| Elemento | Hex |
|---|---|
| Background | `#0a0a0a` |
| Accent (LARANJA) | `#FF6B00` |
| Header bg | `rgba(10,10,10,0.85)` |
| Text | `#FFFFFF` |
| Muted | `rgba(255,255,255,0.6)` |

### Diferencial: Foto ENORME como hero, header bar fino no topo, tom jornalístico
### Referência completa: `hollyfield-news-reference.md`
### Post feito: Choque Macro 2026

---

## 4. Kaique Epic ⭐ FAVORITO

### Origem
@kaique.editor (237K). Capas cinematográficas épicas.

### Estrutura Visual — 2 Tipos

#### TIPO A — Epic Cover (impacto máximo)
```
┌─────────────────────────────┐
│                             │
│   FOTO IA ÉPICA FULLSCREEN  │  ← Guerreiro, campo de batalha,
│   (nível poster de filme)   │     muralhas, nascer do sol
│                             │
│  ┌── gradiente ──────────┐  │
│  │                       │  │
│  │ HEADLINE GIGANTE      │  │  ← 80-96px, UPPERCASE
│  │ COM PALAVRAS EM       │  │     .yellow { #FFD600 }
│  │ AMARELO               │  │     .red { #FF3B30 }
│  │                       │  │
│  │ Subtítulo             │  │
│  │ ARRASTA >>> │ @RUBIMFX│  │
│  │ ● ○ ○ ○ ○ ○ ○ ○ ○ ○  │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
```

#### TIPO B — Tweet Card (conteúdo)
```
┌─────────────────────────────┐
│ ┌── BRANCO ───────────────┐ │
│ │ 📷 Gabriel Rubim ✓      │ │
│ │ HEADLINE BOLD PRETO     │ │  ← 52px uppercase
│ │ Texto conteúdo          │ │  ← 28px
│ ├──────────────────────────┤ │
│ │ FOTO IA TEMÁTICA        │ │  ← flex:1
│ │ ARRASTA >>> │ @RUBIMFX  │ │
│ └──────────────────────────┘ │
└─────────────────────────────┘
```

### Paleta
| Elemento | Hex |
|---|---|
| Destaque principal | Amarelo `#FFD600` |
| Alerta | Vermelho `#FF3B30` |
| Info | Azul `#1D9BF0` |
| Card background | Branco `#FFFFFF` |
| Texto preto | `#0F1419` |

### Diferencial: Fotos IA ÉPICAS cinematográficas, headlines GIGANTES, impacto visual máximo
### Dica: Prompts com "hyper-realistic, LORD OF THE RINGS atmosphere, volumetric god-rays, epic scale"
### Referência completa: `kaique-epic-reference.md`
### Posts feitos: 7 Verdades Disciplina, Terra Prometida, (e variações)

---

## 5. BrunoGPT Neon

### Origem
@brun0gpt. Covers neon vibrantes.

### Estrutura
- Background escuro com efeitos neon (azul/roxo/verde)
- Headline com glow effect
- Cards com bordas neon sutis

### Paleta
| Elemento | Hex |
|---|---|
| Background | `#0a0a0a` |
| Neon Blue | `#00D4FF` |
| Neon Purple | `#7C3AED` |
| Neon Green | `#00FF88` |

### Status: Templates criados, NÃO testado em produção
### Templates: `template-12-brunogpt-cover.html`, `template-13-brunogpt-content.html`

---

## 6. Minimal Clean

### Origem
Estilo minimalista universal.

### Estrutura
- Fundo branco ou claro
- Texto grande preto
- Ultra limpo, sem distrações
- Ideal para listas e dados

### Paleta
| Elemento | Hex |
|---|---|
| Background | `#FFFFFF` |
| Texto | `#0F1419` |
| Accent | `#1D9BF0` |
| Border | `#EFF3F4` |

### Status: Template criado, NÃO testado em produção
### Template: `template-04-minimal-clean.html`

---

## 📊 Comparativo Rápido

| Aspecto | Twitter Dark | Esteter | Hollyfield | Kaique Epic |
|---|---|---|---|---|
| Foto | Média (30%) | Média + screenshots | GRANDE (80%) | GRANDE (100%) |
| Texto | Muito | Médio | Pouco | Médio |
| Tom | Informativo | Jornalístico | Editorial | Cinematográfico |
| Fundo | Preto | Near-black | Near-black | Foto full |
| Accent | Azul/vermelho | Azul/vermelho | Laranja | Amarelo/vermelho |
| Melhor para | Educativo/dados | Notícias + fontes | Breaking news | Mindset/storytelling |
| Impacto visual | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🔧 Regras Universais (TODOS os estilos)

1. **Dimensão:** 1080x1350px (4:5 Instagram)
2. **Fonte mínima:** 22px (NADA abaixo de 20px)
3. **Português:** Acentos corretos SEMPRE (á, é, í, ó, ú, ã, õ, ç)
4. **Fotos:** Reais ou IA épica (NUNCA stock/Unsplash genérico)
5. **Profile:** profile-photo.jpeg apenas para avatar (48-52px)
6. **URLs:** Zero dependências externas
7. **HTML:** Cada slide é standalone
8. **@rubimfx:** Visível em TODOS os slides
9. **CTA:** Último slide SEMPRE com "Segue @rubimfx"
10. **Variação:** Mínimo 3 layouts diferentes no carrossel

---

*Documentação atualizada em 19 de março de 2026.*
