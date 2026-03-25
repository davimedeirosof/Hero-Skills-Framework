---
name: Lip Sync Fix
description: Correção de lip sync usando MuseTalk e Wav2Lip para fonemas PT-BR
category: video-production
---

# Correção de Lip Sync

## Quando usar
- Lip sync do HeyGen falhou em fonemas específicos
- Consoantes duras (p, b, m) não fecham a boca
- Nasais PT-BR (ã, em) com formato errado
- Dessincronização áudio-vídeo > 3 frames

## MuseTalk (Recomendado)
- GitHub: github.com/TMElyralab/MuseTalk
- Baseado em difusão (Tencent)
- 30+ FPS em GPU
- Resolução: 256x256 na face (depois upscale)
- Melhor que Wav2Lip para: dentes, bordas, consistência

## Wav2Lip (Alternativa)
- Mais simples de configurar
- Menor resolução (96x96 face)
- Comunidade maior, mais tutoriais
- Usar quando MuseTalk não estiver disponível

## Workflow
1. Identificar o trecho com lip sync ruim
2. Extrair o áudio do trecho
3. Rodar MuseTalk/Wav2Lip no trecho
4. Substituir o trecho no vídeo final
5. Verificar transição entre trechos (sem corte visível)

## Fonemas Problemáticos em PT-BR
| Fonema | Problema Comum | Solução |
|---|---|---|
| ã, em, im | Boca igual a vogal pura | Regenerar com MuseTalk |
| rr (carro) | Vibração não aparece | Aceitar — difícil de corrigir |
| lh, nh | Língua não visível | Aceitar — imperceptível |
| p, b, m | Boca não fecha | Regenerar com MuseTalk |
| s, z, ch | Dentes/lábios errados | Regenerar com MuseTalk |
