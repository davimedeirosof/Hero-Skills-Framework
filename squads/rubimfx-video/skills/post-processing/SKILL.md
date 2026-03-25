---
name: Post Processing
description: Pipeline de pós-processamento para melhorar qualidade do clone
category: video-production
---

# Pós-Processamento de Vídeo Clone

## Sequência de Operações (NESTA ORDEM)
1. Gerar vídeo no HeyGen/Argil
2. Exportar na máxima resolução/bitrate
3. Skin texture enhancement (se pele plástica)
4. Eye contact correction (se olhar desalinhado)
5. Upscale com Topaz Video AI (2x ou 4K)
6. Temporal denoising (eliminar flicker)
7. Color grade (match com estética real do Gabriel)
8. Reconectar áudio se processado separado
9. Exportar H.264/H.265 a 20-30Mbps para 1080p

## Ferramentas

### Upscaling
- **Topaz Video AI** ($300/ano) — melhor qualidade
- Modelo Proteus para uso geral
- Modelo Gaia para qualidade máxima
- Aplicar anti-flicker forte na região do rosto

### Skin Texture
- **Claid.ai** — restaura poros e textura
- **LetsEnhance Prime** — adiciona detalhe sem drift
- Usar quando pele parecer cerosa/plástica

### Eye Contact
- **BIGVU** — correção de olhar
- **Kapwing** — ajuste de direção do olhar
- Usar se avatar olhar levemente fora do centro

### Lip Sync (se necessário)
- **MuseTalk** (open source, Tencent) — melhor qualidade 2026
- 30+ FPS, difusão, dentes nítidos
- Usar para corrigir fonemas específicos que falharam

### Color Grade
- Match com tom de pele real do Gabriel
- Warmth consistente com gravações reais
- Contraste e saturação naturais
