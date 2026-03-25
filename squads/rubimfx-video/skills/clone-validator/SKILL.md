---
name: Clone Validator
description: Checklist e script de validação de qualidade do clone de vídeo IA
category: quality-assurance
---

# Clone Validator — Validação de Qualidade do Clone

## Objetivo
Garantir que o vídeo gerado com clone IA (HeyGen/Argil) atinge um nível de realismo indistinguível de um vídeo real do Gabriel. O vídeo SÓ é aprovado com score mínimo de 8/10.

## Workflow de Validação Frame-a-Frame

### Preparação
1. Abrir o vídeo do clone em um player que permita avanço frame-a-frame (VLC: tecla "E")
2. Ter um vídeo real recente do Gabriel como referência lado a lado
3. Reproduzir em velocidade 0.5x para análise de lip sync
4. Usar tela grande (não celular) para detectar detalhes

### Etapa 1: Comparação de Tom de Pele (RGB Histogram)

**Método:**
1. Capturar frame do clone e frame do vídeo real com iluminação similar
2. Abrir ambos no Photoshop/GIMP
3. Comparar histograma RGB da região do rosto (sem cabelo/fundo)

**Critérios:**
| Aspecto | Aprovado | Reprovado |
|---------|----------|-----------|
| Tom geral | Diferença < 10% no histograma | Diferença > 15% (muito quente/frio) |
| Uniformidade | Tom varia naturalmente (bochechas mais rosadas) | Tom completamente uniforme (plástico) |
| Sombras | Sombras nas mesmas regiões que vídeo real | Sombras ausentes ou em posição errada |
| Brilho/Reflexo | Brilho sutil no nariz/testa | Sem brilho (matte) ou brilho excessivo |

**Score: ___/10**

### Etapa 2: Análise de Padrão de Piscadas

**Método:**
1. Assistir 30 segundos contando piscadas
2. Cronometrar intervalo entre piscadas
3. Comparar com padrão humano natural

**Critérios:**
| Aspecto | Aprovado | Reprovado |
|---------|----------|-----------|
| Frequência | 12-20 piscadas/minuto | < 8 ou > 25 (robótico ou nervoso) |
| Regularidade | Intervalos IRREGULARES (natural) | Intervalos idênticos (robótico) |
| Duração | Piscada dura 100-400ms | Muito rápida (< 50ms) ou lenta (> 500ms) |
| Completude | Olho fecha completamente | Piscada parcial/incompleta |
| Micro-movimentos | Olhos se movem entre piscadas | Olhos fixos como estátua |

**Score: ___/10**

### Etapa 3: Teste de Lip Sync (0.5x Speed)

**Método:**
1. Reproduzir o vídeo em 0.5x velocidade
2. Focar exclusivamente na boca
3. Verificar sincronização em cada tipo de fonema

**Critérios:**
| Fonema | O que verificar | Aprovado | Reprovado |
|--------|----------------|----------|-----------|
| P, B, M | Boca fecha totalmente | Lábios se tocam | Boca aberta nessas consoantes |
| A, E, O | Abertura proporcional | Boca abre adequadamente | Mesmo formato para todas as vogais |
| S, Z, CH | Posição dentes/lábios | Lábios semi-fechados, dentes visíveis | Boca aberta como vogal |
| Ã, EM, IM | Nasais do PT-BR | Formato específico (não é "A" puro) | Mesmo formato de vogal oral |
| Pausas | Boca em repouso | Boca parada/fechada | Boca se movendo sem som |
| Sync geral | Timing áudio-vídeo | Máximo 2-3 frames de diferença | > 5 frames de atraso/adiantamento |

**Score: ___/10**

### Etapa 4: Naturalidade de Movimento da Cabeça

**Método:**
1. Assistir o vídeo focando apenas na cabeça/pescoço
2. Comparar com vídeo real do Gabriel

**Critérios:**
| Aspecto | Aprovado | Reprovado |
|---------|----------|-----------|
| Micro-movimentos | Cabeça tem movimentos sutis constantes | Cabeça estática como manequim |
| Ênfase | Move a cabeça ao enfatizar pontos | Mesma posição durante toda a fala |
| Transições | Movimentos suaves e fluidos | Movimentos bruscos/robóticos |
| Pescoço | Pescoço acompanha naturalmente | Cabeça se move mas pescoço é rígido |
| Ombros | Ombros com micro-movimentos | Ombros congelados |

**Score: ___/10**

### Etapa 5: Teste de Identidade de Voz

**Método:**
1. Reproduzir 10 segundos do clone
2. Imediatamente reproduzir 10 segundos do vídeo real
3. Comparar lado a lado

**Critérios:**
| Aspecto | Aprovado | Reprovado |
|---------|----------|-----------|
| Timbre | Soa como O Gabriel | Soa como "alguém parecido" |
| Ritmo | Ritmo natural de fala do Gabriel | Muito rápido/lento/monótono |
| Respiração | Pausas naturais para respirar | Fala contínua sem respiração |
| Emoção | Variação emocional presente | Tom flat/robótico |
| Sotaque | PT-BR natural (sotaque do Gabriel) | Sotaque neutro/estrangeiro |
| Artefatos | Áudio limpo | Clicks, distorção, fade-outs |

**Score: ___/10**

## Cálculo do Score Final

```
Score Final = (Pele + Piscadas + Lip Sync + Movimento + Voz) / 5

APROVADO: Score >= 8.0
REPROVADO: Score < 8.0
```

### Ações por Score

| Score | Status | Ação |
|-------|--------|------|
| 9.0 - 10.0 | Excelente | Aprovar imediatamente |
| 8.0 - 8.9 | Aprovado | Aprovar, notar áreas de melhoria |
| 7.0 - 7.9 | Quase | Aplicar pós-processamento e re-testar |
| 6.0 - 6.9 | Reprovado | Re-gerar com parâmetros ajustados |
| < 6.0 | Reprovado | Revisar setup completo (prompt, áudio, foto base) |

## Relatório de Validação

```
=== RELATÓRIO DE VALIDAÇÃO DO CLONE ===
Data: [data]
Vídeo: [nome/identificador]
Duração: [X] segundos
Plataforma: [HeyGen / Argil]

SCORES:
  Tom de Pele:     [X]/10
  Piscadas:        [X]/10
  Lip Sync:        [X]/10
  Mov. Cabeça:     [X]/10
  Voz:             [X]/10
  ─────────────────────
  SCORE FINAL:     [X.X]/10

STATUS: [APROVADO / REPROVADO]

OBSERVAÇÕES:
- [detalhe 1]
- [detalhe 2]

AÇÕES NECESSÁRIAS:
- [ ] [ação se reprovado]
```

## Teste Humano (Validação Final)

Após aprovação técnica (score >= 8.0):
1. Mostrar o vídeo para alguém que conhece o Gabriel
2. **NÃO** dizer que é clone/IA
3. Perguntar: "Parece normal pra você?" e "Notou algo estranho?"
4. Se a pessoa identificar qualquer coisa artificial → voltar para pós-processamento
5. Se passar no teste humano → APROVADO FINAL

## Problemas Comuns e Soluções

| Problema | Causa Provável | Solução |
|----------|----------------|---------|
| Pele plástica/cerosa | Modelo IA suaviza demais | Pós-processamento com skin texture (Claid.ai) |
| Piscadas regulares | Padrão padrão do modelo | Re-gerar ou editar frames de piscada |
| Lip sync atrasado | Áudio não alinhado | MuseTalk para corrigir ou re-gerar |
| Cabeça estática | Prompt sem instrução de movimento | Adicionar "natural head movements" no prompt |
| Voz monótona | Clone de voz com pouca emoção | Re-gravar áudio com mais variação no ElevenLabs |
| Borda do cabelo | Hard edge no recorte | Upscale + feather edges no pós-processamento |
