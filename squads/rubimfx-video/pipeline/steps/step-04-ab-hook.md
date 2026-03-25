# Step 04 — A/B Hook Test (Teste A/B de Hook)

## Descrição
Preparação de variações de hook para teste A/B, permitindo comparar qual abertura gera mais engajamento no mesmo tipo de conteúdo.

## Skill Responsável
**A/B Testing** — Framework de Testes A/B

## Input Necessário
- Roteiro aprovado (Step 03) com hook principal
- `hook-database.md` — Para selecionar hook alternativo
- Histórico de testes A/B anteriores (se existir)

## Output Produzido
- Hook A (o do roteiro aprovado)
- Hook B (variação alternativa, categoria diferente)
- Plano de teste: quando publicar cada versão
- Métricas a comparar após 48 horas
- Template de registro preenchido

## Checkpoint
**Não** — Etapa de preparação que não requer aprovação.

## Critérios de Qualidade
- [ ] Duas variações claras e distintas (categorias diferentes de hook)
- [ ] Apenas 1 variável diferente entre A e B (hook, não conteúdo)
- [ ] Plano de publicação definido (mesmo horário, dias diferentes)
- [ ] Métricas de comparação definidas antecipadamente
- [ ] Teste documentado antes de executar

## Erros Comuns a Evitar
- Testar hooks muito parecidos (sem diferença real)
- Mudar mais de 1 variável entre A e B (hook + horário)
- Não documentar o teste antes de publicar
- Tirar conclusão com menos de 1000 impressões
- Esquecer de registrar o resultado depois
