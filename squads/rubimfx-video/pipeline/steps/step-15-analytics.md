# Step 15 — Analytics (Registro de Métricas)

## Descrição
Coleta e registro de métricas de performance do vídeo publicado após 48 horas, alimentando o banco de dados para análises de tendência e melhoria contínua.

## Agente Responsável
**Ana Analytics** — Analista de Performance de Vídeo

## Input Necessário
- Link do post publicado (Step 14)
- Dados do calendário: formato, pilar, tipo de hook, horário
- Acesso ao Instagram Insights / Meta Business Suite
- Planilha de tracking histórica

## Output Produzido
- Registro completo de métricas na planilha de tracking:
  - Data, formato, hook type, horário, views, saves, shares, comments, completion%, followers+
- Score calculado: `(saves × 3) + (shares × 2) + comments + (completion% × views / 100)`
- Comparação com média histórica do mesmo formato
- Flag se o vídeo é outlier (positivo ou negativo)
- Alimentação do relatório semanal

## Checkpoint
**Não** — Etapa de coleta de dados que acontece 48h após publicação.

## Critérios de Qualidade
- [ ] Métricas coletadas exatamente 48h após publicação
- [ ] Todas as 6 métricas primárias registradas (views, saves, shares, comments, completion, followers)
- [ ] Score calculado corretamente
- [ ] Comparação com média histórica feita
- [ ] Formato e tipo de hook registrados para análise cruzada
- [ ] Outliers flagged para investigação

## Erros Comuns a Evitar
- Coletar métricas antes de 48h (dados incompletos)
- Esquecer de registrar o formato e tipo de hook (impossibilita análise cruzada)
- Tirar conclusões com 1 vídeo (precisa de mínimo 5 por formato)
- Não re-coletar métricas de vídeos que "explodem" depois de 48h
- Ignorar fatores externos (feriados, eventos) ao analisar outliers
- Não compartilhar insights com Cal Calendar para ajustar próxima semana
