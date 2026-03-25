# Step 07 — Video Generation (Geração de Vídeo com Clone)

## Descrição
Geração do vídeo com clone facial do Gabriel usando HeyGen (ou Argil), combinando o áudio aprovado com o avatar para criar um vídeo realista de fala.

## Agente Responsável
**Hugo HeyGen** — Especialista em Clone Facial de Vídeo

## Input Necessário
- Áudio aprovado (Step 05)
- Avatar/clone do Gabriel configurado no HeyGen
- Instruções de movimento (head movements, expressão)
- Fundo desejado (escritório, green screen, custom)

## Output Produzido
- Vídeo MP4 com clone facial + áudio sincronizado
- Resolução mínima 1080x1920 (9:16 vertical)
- Duração correspondente ao áudio (15-60 segundos)
- Versão em máxima qualidade/bitrate para pós-processamento

## Checkpoint
**Sim** — O Gabriel precisa verificar se o clone está realista antes de prosseguir.

**Pergunta do checkpoint:** "O vídeo do clone está realista? Lip sync OK?"

## Critérios de Qualidade
- [ ] Clone se parece com o Gabriel (rosto, corpo, proporções)
- [ ] Lip sync alinhado com o áudio (máx 3 frames de diferença)
- [ ] Movimentos de cabeça naturais (não estático)
- [ ] Piscadas irregulares (não robóticas)
- [ ] Pele com textura (não plástica/cerosa)
- [ ] Fundo estável (sem flicker)
- [ ] Borda do cabelo natural (não hard-edge)
- [ ] Iluminação consistente com sombras corretas
- [ ] Formato vertical 9:16

## Erros Comuns a Evitar
- Usar avatar genérico em vez do clone personalizado do Gabriel
- Não incluir instrução de movimento natural no prompt
- Exportar em resolução baixa (< 1080p)
- Fundo com elementos que flickam ou pulsam
- Não verificar lip sync antes de enviar para pós-produção
- Gerar vídeo horizontal e depois cortar (perda de qualidade)
