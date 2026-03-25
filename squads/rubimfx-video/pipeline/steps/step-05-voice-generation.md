# Step 05 — Voice Generation (Geração de Áudio)

## Descrição
Geração do áudio com clone de voz do Gabriel usando ElevenLabs, garantindo naturalidade, pronúncia correta e tom emocional adequado ao conteúdo.

## Agente Responsável
**Elia ElevenLabs** — Especialista em Clone de Voz

## Input Necessário
- Roteiro aprovado (Step 03) com texto completo da fala
- `tone-of-voice.md` — Referência de ritmo, tom e expressões
- Parâmetros de voz configurados no ElevenLabs (stability, similarity, style)

## Output Produzido
- Arquivo de áudio (MP3/WAV) com a fala completa
- Duração do áudio (deve ser 15-60 segundos)
- Notas sobre qualidade: pontos de atenção para lip sync
- Arquivo alternativo se primeira geração não ficou boa

## Checkpoint
**Sim** — O Gabriel precisa ouvir e aprovar o áudio antes de gerar o vídeo.

**Pergunta do checkpoint:** "O áudio está natural? Pronúncia OK?"

## Critérios de Qualidade
- [ ] Soa como O Gabriel (não voz genérica)
- [ ] Ritmo de 130-150 palavras/minuto
- [ ] Pausas naturais antes de pontos de ênfase
- [ ] Variação emocional (não monótono)
- [ ] Respiração audível em pausas naturais
- [ ] Termos técnicos em inglês pronunciados corretamente
- [ ] Sem artefatos (clicks, distorção, fade-outs, robôs)
- [ ] Sotaque PT-BR natural
- [ ] Duração entre 15-60 segundos

## Erros Comuns a Evitar
- Voz rápida demais (> 160 palavras/min) — soa artificial
- Voz monótona sem variação de tom
- Falta de respiração entre frases
- Pronúncia errada de termos em inglês (FVG, FOMC)
- Stability muito alta no ElevenLabs (voz robótica)
- Similarity muito baixa (perde identidade do Gabriel)
- Não testar o áudio antes de enviar para o HeyGen
