---
name: Quality Gate
description: Checklist de validação de qualidade para vídeos de clone IA
category: quality-assurance
---

# Quality Gate — Validação de Clone

## Visual (verificar ANTES de publicar)
- [ ] Piscadas irregulares (não rítmicas/robóticas)
- [ ] Micro-movimentos dos olhos entre piscadas
- [ ] Boca + bochechas + queixo + sobrancelha coordenados
- [ ] Cabeça com movimento sutil e natural (não estática)
- [ ] Pele com textura visível (poros, linhas) — não plástica
- [ ] Perfil do rosto estável quando vira (orelha, mandíbula intactos)
- [ ] Borda do cabelo natural (não hard-edge/helmet)
- [ ] Iluminação consistente (sombras na mesma direção)
- [ ] Fundo estável sem flicker/pulso

## Lip Sync (reproduzir em 0.5x)
- [ ] Consoantes duras (p, b, m): boca fecha totalmente no frame certo
- [ ] Vogais abertas (a, e, o): abertura proporcional da boca
- [ ] Sibilantes (s, z, ch): posição de lábios/dentes correta
- [ ] Nasais PT-BR (ã, em, im): formato diferente de vogais puras
- [ ] Sync áudio-vídeo: máx 3 frames de diferença
- [ ] Boca parada quando não há fala

## Voz
- [ ] Ritmo natural de PT-BR (não neutro/estrangeiro)
- [ ] Respiração em pausas naturais (não meio de frase)
- [ ] Variação emocional (não monótono)
- [ ] Soa como O GABRIEL especificamente (não voz genérica)
- [ ] Sem artefatos (clicks, distorção, fade-outs)

## Teste Humano (mais importante)
- Mostrar para alguém SEM dizer que é IA
- Perguntar: "Parece real?" e "Algo parece estranho?"
- Se a pessoa identificar qualquer coisa → corrigir e re-testar
