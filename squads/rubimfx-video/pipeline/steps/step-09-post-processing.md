# Step 09 — Post Processing (Pós-Processamento)

## Descrição
Melhoria da qualidade visual do vídeo do clone através de upscaling, correção de textura de pele, ajuste de lip sync e color grading. Aplicar APENAS se necessário baseado no relatório do Clone Validator.

## Skill Responsável
**Post Processing** — Pipeline de Pós-Processamento

## Input Necessário
- Vídeo do clone (Step 07)
- Relatório de validação (Step 08) com áreas de melhoria identificadas
- Vídeo real do Gabriel (referência de cor e textura)

## Output Produzido
- Vídeo pós-processado em alta qualidade
- Exportação: H.264/H.265 a 20-30Mbps para 1080p
- Log das operações aplicadas
- Comparação antes/depois (se mudanças significativas)

## Checkpoint
**Não** — Etapa técnica automática baseada no relatório de validação.

## Critérios de Qualidade
- [ ] Pele com textura natural (poros e linhas visíveis)
- [ ] Cor de pele matching com vídeos reais do Gabriel
- [ ] Sem flicker na região do rosto
- [ ] Upscale sem artefatos (sem noise, sem blur excessivo)
- [ ] Lip sync corrigido (se era problema)
- [ ] Color grade consistente com estética real do Gabriel
- [ ] Exportação em qualidade máxima (20-30Mbps)

## Erros Comuns a Evitar
- Aplicar pós-processamento desnecessário (se clone já está bom)
- Over-sharpen que cria artefatos
- Color grade que muda tom de pele drasticamente
- Compressão excessiva na exportação (< 10Mbps)
- Processar áudio e vídeo separados e dessincronizar
- Não verificar o resultado do pós-processamento
