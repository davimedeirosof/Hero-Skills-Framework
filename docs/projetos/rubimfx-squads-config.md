# rubimfx — Configuração dos Squads

Arquivos de configuração (`squad.yaml` e `squad-party.csv`) dos squads em `squads/`.

---

## rubimfx-content

**Path:** `squads/rubimfx-content/`
**Performance mode:** alta-performance
**Idioma:** Português (Brasil)

### squad.yaml (resumo)

```yaml
name: "RubimFX Content OS"
code: rubimfx-content
description: "Squad de produção de conteúdo Instagram para @rubimfx — carrosséis de
  notícias macro/economia no estilo @economesteter, conectando eventos globais a
  forex, ouro, índices americanos e mesa proprietária."
language: "Português (Brasil)"
performance_mode: alta-performance
```

### Agentes

| id | Nome | Ícone | Execução |
|----|------|-------|----------|
| nara-noticia | Nara Notícia | 🔍 | subagent |
| vitor-visual | Vitor Visual | 🎨 | subagent |
| iago-instagram | Iago Instagram | 💡 | inline |
| leo-legenda | Léo Legenda | ✍️ | inline |
| diana-design | Diana Design | 🖼️ | inline |
| renata-revisao | Renata Revisão | ✅ | inline |

### Skills usadas
- `web_search` (nativo)
- `web_fetch` (nativo)
- `image-creator`

### Dados carregados (pipeline/data/)
- `research-brief.md`
- `domain-framework.md`
- `quality-criteria.md`
- `output-examples.md`
- `anti-patterns.md`
- `tone-of-voice.md`
- `style-guide-economesteter.md`

### Formato
- `instagram-feed`

### Pipeline (12 steps)
```
step-01-research-focus
step-02-news-research         ← Nara (subagent)
step-02b-visual-trends        ← Vitor (subagent)
step-03-news-selection        ← checkpoint
step-04-generate-angles       ← Iago
step-05-angle-selection       ← checkpoint
step-06-create-carousel       ← Diana + Iago
step-07-write-caption         ← Léo
step-08-content-approval      ← checkpoint ⏸️
step-09-create-visuals        ← Diana
step-10-review                ← Renata
step-11-final-approval        ← checkpoint ⏸️
```

### Estrutura de diretórios
```
squads/rubimfx-content/
├── GUIA-COMPLETO-EQUIPE.md   ← Guia detalhado da equipe
├── GUIA-CONSISTENCIA.md      ← Guia de consistência visual
├── README.md
├── TOOLKIT.md                ← Ferramentas e recursos
├── _investigations/          ← Análises Sherlock (gitkeep)
├── _memory/                  ← Memória persistente do squad
├── agents/                   ← Arquivos .agent.md dos agentes
├── generate_biblical.py      ← Script de geração bíblica
├── pipeline/
│   ├── pipeline.yaml
│   ├── data/                 ← Arquivos de dados (research-brief, etc.)
│   └── steps/                ← Steps do pipeline
├── scripts/                  ← Scripts auxiliares (clone_image.py, etc.)
├── squad-party.csv
├── squad.yaml
└── templates/                ← Templates HTML dos 6+ estilos visuais
```

---

## rubimfx-video

**Path:** `squads/rubimfx-video/`
**Versão:** 3.0
**Plataforma:** Instagram Reels, TikTok
**Conteúdo:** Short-form video (15-60s)

### squad.yaml (resumo)

```yaml
name: rubimfx-video
description: "Squad profissional de producao de videos curtos (Reels/TikTok) com clone
  de voz e imagem para @rubimfx — Pipeline: Nano Banana foto clone + HeyGen/Hedra animacao"
brand: "@rubimfx"
platform: "Instagram Reels, TikTok"
content_type: "Short-form video (15-60s)"
version: "3.0"
```

### Agentes

| Nome | Arquivo | Execução |
|------|---------|----------|
| Rex Roteirista | agents/rex-roteirista.agent.md | inline |
| Hugo HeyGen | agents/hugo-heygen.agent.md | inline |
| Elia ElevenLabs | agents/elia-elevenlabs.agent.md | inline |
| Sam Submagic | agents/sam-submagic.agent.md | inline |
| Bea B-Roll | agents/bea-broll.agent.md | inline |
| Pablo Publisher | agents/pablo-publisher.agent.md | inline |
| Tina Trend | agents/tina-trend.agent.md | inline |
| Ana Analytics | agents/ana-analytics.agent.md | inline |
| Cal Calendar | agents/cal-calendar.agent.md | inline |
| Rip Repurpose | agents/rip-repurpose.agent.md | inline |

### Skills (13 específicas do squad)
```
skills/
├── ab-testing/
├── clone-validator/
├── cta-optimizer/
├── lip-sync-fix/
├── nano-banana-video-prompts/
├── photo-to-video/
├── post-processing/
├── prompt-engineering-video/
├── quality-gate/
├── recording-guide/
├── thumbnail-generator/
├── trending-sounds/
└── voice-training/
```

### Dados carregados (pipeline/data/)
- `hook-database.md`
- `tone-of-voice.md`
- `anti-patterns.md`
- `clone-perfection-guide.md`
- `photo-to-video-reference.md`

### Ferramentas declaradas no squad.yaml

| Ferramenta | Uso |
|-----------|-----|
| Nano Banana Pro 2 | Clone foto via `clone_image.py` |
| HeyGen Avatar IV | Animação primária (até 1280p) |
| Hedra Character-3 | Animação emocional (720p) |
| OmniHuman (ByteDance/Replicate) | Premium full-body, cinema |
| ElevenLabs Creator / Fish Audio | Clone de voz |
| Submagic Pro | Legendas animadas |
| Pexels API | B-roll (grátis) |
| Playwright MCP | Publicação (grátis) |
| Instagram Insights API | Analytics |
| OpusClip / WayinVideo / Descript | Repurposing |

**Custo total:** ~$70/mês (64% mais barato que avatar direto)

### Estrutura de diretórios
```
squads/rubimfx-video/
├── README.md
├── _investigations/
├── _memory/
├── agents/                   ← 10 arquivos .agent.md
├── pipeline/
│   ├── pipeline.yaml
│   └── data/                 ← hook-database, tone-of-voice, etc.
├── skills/                   ← 13 skills específicas
├── squad-party.csv
└── squad.yaml
```

---

## squad-party.csv — rubimfx-content

```csv
id,name,icon,path,execution
nara-noticia,Nara Notícia,🔍,./agents/nara-noticia.agent.md,subagent
vitor-visual,Vitor Visual,🎨,./agents/vitor-visual.agent.md,subagent
iago-instagram,Iago Instagram,💡,./agents/iago-instagram.agent.md,inline
leo-legenda,Léo Legenda,✍️,./agents/leo-legenda.agent.md,inline
diana-design,Diana Design,🖼️,./agents/diana-design.agent.md,inline
renata-revisao,Renata Revisão,✅,./agents/renata-revisao.agent.md,inline
```

## squad-party.csv — rubimfx-video

```csv
name,role,agent_file,execution
Rex Roteirista,Roteirista de Reels,agents/rex-roteirista.agent.md,inline
Hugo HeyGen,Clone Video Specialist,agents/hugo-heygen.agent.md,inline
Elia ElevenLabs,Voice Clone Engineer,agents/elia-elevenlabs.agent.md,inline
Sam Submagic,Caption & Edit Specialist,agents/sam-submagic.agent.md,inline
Bea B-Roll,B-Roll Curator,agents/bea-broll.agent.md,inline
Pablo Publisher,Social Media Publisher,agents/pablo-publisher.agent.md,inline
Tina Trend,Viral Trend Hunter,agents/tina-trend.agent.md,inline
```
