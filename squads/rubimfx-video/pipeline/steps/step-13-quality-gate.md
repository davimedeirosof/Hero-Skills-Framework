# Step 13 — Quality Gate (Validação Final)

## Descrição
Checklist de validação final completa antes da publicação. Verifica todos os aspectos do vídeo: visual, áudio, legendas, thumbnail, CTA e alinhamento com anti-patterns.

## Skill Responsável
**Quality Gate** — Checklist de Validação de Qualidade

## Input Necessário
- Vídeo final editado com legendas (Step 10)
- Thumbnail (Step 11)
- CTA definido (Step 12)
- `anti-patterns.md` — Checklist de erros a evitar
- Relatório de validação do clone (Step 08)

## Output Produzido
- Relatório de Quality Gate com status para cada item
- Status final: APROVADO ou REPROVADO
- Lista de correções necessárias se reprovado
- Vídeo marcado como pronto para publicação se aprovado

## Checkpoint
**Sim** — Última verificação antes de publicar. Precisa de aprovação.

**Pergunta do checkpoint:** "Vídeo final passou no Quality Gate? Pronto para publicar?"

## Critérios de Qualidade

### Visual
- [ ] Clone realista (score >= 8/10 no Clone Validator)
- [ ] Pele com textura natural
- [ ] Piscadas irregulares e naturais
- [ ] Movimento de cabeça natural
- [ ] Fundo estável sem flicker
- [ ] Resolução 1080x1920 (9:16)

### Áudio
- [ ] Voz soa como o Gabriel
- [ ] Ritmo natural (130-150 palavras/min)
- [ ] Sem artefatos (clicks, distorção)
- [ ] Música (se houver) abaixo de 20% do volume da voz

### Legendas
- [ ] Sincronizadas com áudio
- [ ] Fonte legível (>= 28px)
- [ ] Português com acentos corretos
- [ ] Não cobrem o rosto
- [ ] Palavras-chave destacadas

### Conteúdo
- [ ] Hook nos primeiros 3 segundos (texto + fala)
- [ ] CTA específico nos últimos 5 segundos
- [ ] Formato diferente do vídeo anterior
- [ ] Sem promessas de ganho fácil
- [ ] Sem fotos genéricas como conteúdo principal

### Thumbnail
- [ ] Legível em miniatura
- [ ] Contraste alto
- [ ] Dentro da zona segura do grid

### Lip Sync
- [ ] Consoantes (p, b, m) com boca fechando
- [ ] Nasais (ã, em) diferenciadas
- [ ] Máximo 3 frames de diferença
- [ ] Boca parada quando não há fala

## Erros Comuns a Evitar
- Aprovar por pressa sem verificar cada item
- Ignorar detalhes "pequenos" que acumulam sensação de artificialidade
- Não assistir o vídeo inteiro antes de aprovar
- Não testar em tela de celular (só em monitor grande)
- Publicar sem mostrar para pelo menos 1 pessoa
