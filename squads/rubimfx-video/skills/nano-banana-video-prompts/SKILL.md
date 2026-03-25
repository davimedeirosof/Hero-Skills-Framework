---
name: Nano Banana Video Prompts
description: Prompts otimizados para gerar fotos de clone que animam bem em video (frontal, olhos abertos, boca neutra, vertical 9:16)
category: ai-generation
---

# Nano Banana Video Prompts — Fotos Otimizadas para Animacao

## Regras Universais (aplicar em TODOS os prompts)

Toda foto gerada para animacao DEVE ter:
1. **DIRECTLY at the camera** — olhar frontal
2. **mouth slightly parted** ou **neutral relaxed position** — facilita lip sync
3. **eyes open and visible** — sem oculos escuros, sem olhos fechados
4. **no hands near face** — maos fora do frame do rosto
5. **simple or blurred background** — menos artefatos na animacao
6. **uniform lighting on face** — sem sombras pesadas
7. **VERTICAL 9:16** — formato Reels/TikTok
8. **face centered in upper third** — composicao ideal para video
9. **Natural skin texture, visible pores** — anti-AI realismo
10. **head and shoulders framing** — enquadramento ideal para lip sync

---

## 10 Cenarios Pre-Definidos

### 1. trading-desk-video
```
Gabriel sitting at a professional trading desk, looking DIRECTLY at the camera
with a confident engaged expression, mouth slightly parted as if about to speak.
Three monitors with financial charts behind him (soft focus, green and red candlesticks).
Dark fitted shirt, sleeves rolled up. Warm key light from left, cool blue ambient
from monitors. Shot on Canon R5 85mm f/1.4, shallow depth of field.
VERTICAL 9:16 composition, head and shoulders framing, face centered in upper third.
Natural skin texture, visible pores, subtle stubble. No hands in frame.
```

### 2. dark-studio-video
```
Gabriel in a professional dark studio, looking DIRECTLY at camera with warm
confident expression, mouth in neutral relaxed position ready to speak.
Subtle blue rim light from behind creating hair separation, soft key light
from 45 degrees left creating gentle Rembrandt lighting pattern on face.
Clean dark background with subtle depth and texture. Dark fitted polo shirt.
VERTICAL 9:16, head and shoulders, face centered in upper third.
Natural skin, visible pores, realistic skin imperfections.
Shot on Sony A7R V 85mm f/1.4, ISO 400. No hands visible.
```

### 3. casual-street-video
```
Gabriel standing outdoors in a modern urban environment, looking DIRECTLY at camera
with approachable warm smile, mouth slightly open as if greeting someone.
Wearing dark casual jacket over fitted t-shirt. Golden hour warm sunlight
from camera right creating beautiful skin tones. Blurred city street background
with bokeh from car lights and storefronts.
VERTICAL 9:16 composition, three-quarter body but face large in frame.
Natural skin texture, warm tones. Shot on Fujifilm X100V 35mm f/2.0.
Face centered in upper third. No hands near face.
```

### 4. stage-speaker-video
```
Gabriel on a professional conference stage, looking DIRECTLY at camera
as if speaking confidently to a large audience. Powerful engaged expression,
mouth open mid-speech showing natural speaking position.
Dramatic spotlight from above, blue-purple fill light from behind creating
cinematic rim light. Dark clothing, professional look. Stage background
blurred with subtle LED panels. VERTICAL 9:16, bust shot framing.
Natural skin texture under stage lighting. Shot on Canon R1 85mm f/1.2.
Face centered in upper third. No hands in frame.
```

### 5. podcast-studio-video
```
Gabriel sitting in a professional podcast studio, looking DIRECTLY at camera
with engaged conversational expression, mouth in relaxed neutral position.
Large broadcast microphone visible but NOT blocking face (positioned to the side).
Acoustic panels and warm ambient lighting in background (blurred).
Wearing dark henley shirt. Soft diffused key light from front-left,
warm practical lights in background. VERTICAL 9:16, head and shoulders.
Natural skin, visible pores. Shot on Sony A7S III 50mm f/1.4.
Face centered in upper third. Hands resting on desk, NOT near face.
```

### 6. home-office-video
```
Gabriel sitting at a clean modern home office desk, looking DIRECTLY at camera
with focused professional expression, mouth slightly parted ready to explain.
Minimalist desk setup with one monitor showing charts (blurred), plant in corner.
Wearing smart casual dark button-up shirt, top button open. Natural window light
from left side creating soft even illumination on face, warm tone.
VERTICAL 9:16, head and shoulders framing. Natural skin texture.
Shot on Canon R6 85mm f/1.8. Face centered in upper third.
Clean uncluttered background. No hands near face.
```

### 7. news-desk-video
```
Gabriel at a professional news-style desk, looking DIRECTLY at camera with
serious authoritative expression, mouth in neutral position as if about to
deliver breaking news. Clean modern desk with subtle branding.
Professional broadcast lighting: soft key from front-left, fill from right,
blue backlight for separation. Dark suit jacket over fitted shirt.
VERTICAL 9:16, bust shot. Sharp focus on face, background slightly soft.
Natural skin, realistic texture. Shot on Canon C70 85mm.
Face centered in upper third. Hands on desk but NOT near face.
```

### 8. outdoor-rooftop-video
```
Gabriel standing on a modern building rooftop terrace, looking DIRECTLY at camera
with confident relaxed expression, mouth slightly open with approachable energy.
City skyline blurred in background with blue sky. Wearing dark fitted jacket.
Natural daylight with slight overcast creating beautifully diffused soft light
on face, no harsh shadows. Wind slightly moving hair for realism.
VERTICAL 9:16, head and shoulders. Natural skin with warm outdoor tones.
Shot on Sony A7R V 85mm f/1.4. Face centered in upper third.
No hands near face. Architectural elements blurred behind.
```

### 9. classroom-teaching-video
```
Gabriel standing in front of a modern classroom whiteboard, looking DIRECTLY
at camera with enthusiastic teaching expression, mouth slightly open as if
explaining a concept. Whiteboard behind with trading-related diagrams (blurred).
Wearing dark fitted polo shirt, professional educator look.
Even fluorescent lighting supplemented with soft key from left.
VERTICAL 9:16, three-quarter body but face prominent. Natural skin.
Shot on Canon R5 35mm f/1.4. Face centered in upper third.
One hand gesturing low (waist level), NOT near face.
Clean educational environment.
```

### 10. gym-fitness-video
```
Gabriel in a modern gym environment, looking DIRECTLY at camera with energetic
motivated expression, mouth slightly open with determined look.
Wearing fitted dark athletic shirt showing fit build. Gym equipment
blurred in background with warm industrial lighting. Subtle sweat glow
on skin for realism. Key light from front-left, warm ambient from gym lights.
VERTICAL 9:16, head and upper body. Natural skin texture with athletic glow.
Shot on Sony A7 IV 50mm f/1.4. Face centered in upper third.
Arms at sides or crossed at chest level, NOT near face.
```

---

## Como Usar

### Com clone_image.py:
```bash
cd squads/rubimfx-content
python3 scripts/clone_image.py assets/fotos-referencia/DSC04575.JPG \
  --multi assets/fotos-referencia/IMG_0521_jpg.JPG \
  "COLE O PROMPT ACIMA AQUI" output-video-ready.png
```

### Checklist Pos-Geracao (ANTES de animar):
- [ ] Rosto frontal, olhando para camera
- [ ] Olhos abertos e visiveis
- [ ] Boca neutra ou levemente aberta
- [ ] Sem maos no frame do rosto
- [ ] Fundo simples/desfocado
- [ ] Iluminacao uniforme no rosto
- [ ] Resolucao >= 1080px de largura
- [ ] Formato vertical 9:16
- [ ] Identidade consistente com Gabriel real

**Se QUALQUER item falhar, gerar nova foto com prompt ajustado.**
