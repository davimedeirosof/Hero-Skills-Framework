# Step 08 — Clone Validation (Validação do Clone)

## Descrição
Validação rigorosa da qualidade do vídeo gerado com clone IA, verificando tom de pele, piscadas, lip sync, movimento de cabeça e identidade de voz. O vídeo só avança com score mínimo de 8/10.

## Skill Responsável
**Clone Validator** — Checklist de Validação de Qualidade do Clone

## Input Necessário
- Vídeo gerado (Step 07)
- Vídeo real recente do Gabriel (para comparação lado a lado)
- Player que permita reprodução frame-a-frame (VLC: tecla "E")

## Output Produzido
- Relatório de validação com 5 scores parciais:
  - Tom de Pele (___/10)
  - Padrão de Piscadas (___/10)
  - Lip Sync (___/10)
  - Movimento de Cabeça (___/10)
  - Identidade de Voz (___/10)
- **Score Final (___/10)** — média dos 5 scores
- Status: APROVADO (>= 8.0) ou REPROVADO (< 8.0)
- Lista de ações corretivas se reprovado

## Checkpoint
**Sim** — Score precisa atingir 8/10 para prosseguir.

**Pergunta do checkpoint:** "Score do clone atingiu 8/10? Aprovado?"

## Critérios de Qualidade
- [ ] Score final >= 8.0/10
- [ ] Nenhum score parcial abaixo de 6.0 (mesmo que média passe)
- [ ] Lip sync testado em velocidade 0.5x
- [ ] Piscadas verificadas por 30 segundos (irregulares?)
- [ ] Comparação visual com vídeo real do Gabriel feita
- [ ] Tom de pele comparado via histograma RGB

## Erros Comuns a Evitar
- Aprovar vídeo sem fazer a validação completa (pressa)
- Aceitar score 7.x "porque tá bom o suficiente"
- Não reproduzir em 0.5x para verificar lip sync
- Verificar apenas por 5 segundos em vez dos 30 completos
- Não comparar com vídeo real do Gabriel
- Ignorar pele plástica porque "ninguém vai perceber"
