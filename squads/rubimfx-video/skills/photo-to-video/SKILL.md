---
name: Photo to Video
description: Pipeline completo para transformar foto clone IA em video falando com lip sync
category: video-production
---

# Photo to Video — Clone em Foto → Video Falando

## O Pipeline

```
FOTOS REAIS (18 refs em assets/fotos-referencia/)
        |
NANO BANANA PRO 2 (clone_image.py)
  → Gera foto perfeita do clone em cenario profissional
  → Formato: vertical 9:16 (1080x1920) para Reels
  → Identity Header + anti-AI block
        |
ELEVENLABS / FISH AUDIO
  → Gera audio com clone de voz PT-BR
  → Formato: WAV 48kHz ou MP3 192kbps+
        |
HEYGEN / HEDRA / OMNIHUMAN
  → Anima a foto com o audio
  → Lip sync automatico
  → Saida: video MP4 720-1280p
        |
POS-PROCESSAMENTO
  → Upscale (Topaz se necessario)
  → Skin texture fix
  → Legendas (Submagic)
        |
PUBLICACAO
```

## Etapa 1: Gerar Foto Clone (Nano Banana)

### Comando:
```bash
cd squads/rubimfx-content
python3 scripts/clone_image.py assets/fotos-referencia/DSC04575.JPG \
  --multi assets/fotos-referencia/IMG_0521_jpg.JPG \
  <cenario-ou-preset> output.png
```

### Regras para Foto que ANIMA BEM:

REGRA CRITICA: Para animacao funcionar bem, a foto precisa:
- Rosto FRONTAL (olhando direto pra camera)
- Olhos ABERTOS e visiveis
- Boca levemente ABERTA ou posicao NEUTRA (facilita lip sync)
- Sem maos no rosto
- Fundo SIMPLES ou DESFOCADO (menos artefatos na animacao)
- Iluminacao UNIFORME no rosto (sem sombras pesadas)

### Prompts Otimizados para Animacao:

#### Trading Desk (Reels padrao):
```
Gabriel sitting at a professional trading desk, looking DIRECTLY at the camera
with a confident engaged expression, mouth slightly parted as if about to speak.
Three monitors with charts behind him (soft focus). Dark fitted shirt.
Warm key light from left, cool ambient from monitors. Shot on Canon R5 85mm f/1.4.
VERTICAL 9:16 composition, head and shoulders framing, face centered in upper third.
Natural skin texture, visible pores. 4:5 portrait aspect ratio.
```

#### Dark Studio (Podcast/YouTube):
```
Gabriel in a professional dark studio, looking DIRECTLY at camera with warm
confident expression, mouth in neutral relaxed position. Subtle blue rim light
from behind, soft key light from left creating gentle Rembrandt lighting.
Clean dark background with subtle depth. Dark fitted polo shirt.
VERTICAL 9:16, head and shoulders, face centered. Natural skin, visible pores.
Shot on Sony A7R V 85mm f/1.4. 4:5 portrait.
```

#### Casual/Street:
```
Gabriel standing outdoors in an urban environment, looking DIRECTLY at camera
with approachable smile, mouth slightly open. Wearing dark casual jacket.
Golden hour warm light from side. Blurred city background.
VERTICAL 9:16 composition, three-quarter body. Natural skin texture.
Shot on Fujifilm X100V 35mm f/2.0. 4:5 portrait.
```

#### Palco/Speaker:
```
Gabriel on a conference stage, looking DIRECTLY at camera (as if speaking to audience),
confident powerful expression, mouth open mid-speech. Spotlight from above,
blue fill from behind. Dark clothing. Stage background blurred.
VERTICAL 9:16, bust shot. Natural skin. Shot on Canon R1 85mm.
4:5 portrait.
```

## Etapa 2: Gerar Audio (ElevenLabs / Fish Audio)

### Via API ElevenLabs:
```python
# Exemplo de chamada
from elevenlabs import generate, Voice

audio = generate(
    text="Seu roteiro aqui em portugues",
    voice="Gabriel-Clone-ID",
    model="eleven_multilingual_v2"
)
```

### Via script (a implementar):
```bash
python3 scripts/generate_voice.py "texto do roteiro" output-audio.mp3
```

## Etapa 3: Animar Foto → Video

### Opcao A: HeyGen Avatar IV ($24/mes)
1. Acesse heygen.com
2. Create Avatar → Photo Avatar
3. Upload a foto do Nano Banana
4. Upload o audio do ElevenLabs
5. Gerar video
6. Exportar 1280p MP4

### Opcao B: Hedra Character-3 ($10-15/mes)
1. Acesse hedra.com
2. Upload foto + audio
3. Gerar com Character-3
4. Exportar 720p MP4
5. Melhor para conteudo emocional (mindset, confissao)

### Opcao C: OmniHuman API (pay-per-use)
1. API via Replicate ou WaveSpeed.ai
2. Upload foto + audio
3. Gerar full-body com gestos naturais
4. 1080p output
5. Melhor qualidade absoluta mas requer integracao tecnica

### Quando usar cada um:
| Tipo de conteudo | Ferramenta | Por que |
|---|---|---|
| Noticias / macro | HeyGen | Resolucao alta, tom neutro |
| Mindset / confissao | Hedra | Melhor expressao emocional |
| Conteudo premium | OmniHuman | Full-body, cinema quality |
| Teste / prototipo | Hedra free | Validar antes de investir |

## Etapa 4: Pos-Processamento

1. Clone Validator (checklist de qualidade)
2. Upscale com Topaz se < 1080p
3. Skin texture fix se pele plastica
4. Legendas via Submagic
5. Thumbnail via skill
6. Quality Gate final

## Custo por Video

| Componente | Custo |
|---|---|
| Foto clone (Nano Banana) | ~R$0.35 |
| Audio (ElevenLabs) | ~R$0.50 |
| Animacao (HeyGen Creator) | incluido no $24/mes |
| Legendas (Submagic) | incluido no $23/mes |
| **TOTAL por video** | **~R$1-2** (com planos mensais) |
