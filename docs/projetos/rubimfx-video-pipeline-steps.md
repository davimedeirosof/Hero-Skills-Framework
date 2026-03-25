# rubimfx-video — Steps Detalhados do Pipeline

Pipeline completo de produção de vídeos curtos do squad `rubimfx-video` com 15 steps.

---

## Visão Geral do Pipeline

```
PLANEJAMENTO
  Step 01 — Weekly Calendar (Cal)        ← Plano 5-6 Reels semanais       [checkpoint]
  Step 02 — Trend Research (Tina)        ← Formatos virais da semana

PRÉ-PRODUÇÃO
  Step 03 — Script Writing (Rex)         ← Roteiro com hook + estrutura    [checkpoint]
  Step 04 — A/B Hook Test                ← 2 variações de hook

PRODUÇÃO
  Step 05 — Voice Generation (Elia)      ← Áudio via clone de voz          [checkpoint]
  Step 06 — B-Roll Curation (Bea)        ← Materiais visuais de apoio
  Step 07 — Video Generation (Hugo)      ← Vídeo com clone facial          [checkpoint]

PÓS-PRODUÇÃO
  Step 08 — Clone Validation             ← Score mínimo 8/10               [checkpoint]
  Step 09 — Post Processing              ← Upscale e correções (se necessário)
  Step 10 — Caption & Edit (Sam)         ← Legendas animadas
  Step 11 — Thumbnail                    ← Capa do Reel
  Step 12 — CTA Selection                ← Call-to-action otimizado
  Step 13 — Quality Gate                 ← Validação final completa         [checkpoint]

DISTRIBUIÇÃO
  Step 14 — Publish (Pablo)              ← Instagram Reels + TikTok         [checkpoint]
  Step 15 — Analytics (Ana)              ← Métricas após 48h
```

**Checkpoints (7):** Steps 01, 03, 05, 07, 08, 13 e 14 — requerem aprovação do usuário para prosseguir.

---

## Step 01 — Weekly Calendar (Calendário Semanal)

**Tipo:** Checkpoint

**Agente:** Cal Calendar — Planejador de Calendário de Conteúdo

**Objetivo:** Planejamento estratégico da semana de conteúdo, definindo quais vídeos serão produzidos, em quais formatos, com quais temas e horários.

**Inputs necessários:**
- Relatório de performance da semana anterior (Ana Analytics)
- Calendário econômico da semana (NFP, FOMC, Copom, CPI)
- Trends identificados pela Tina Trend (se disponíveis)
- Feedback do Gabriel sobre temas prioritários
- Backlog de temas pendentes

**Output produzido:**
- Calendário semanal com 5-6 Reels planejados
- Para cada dia: pilar, formato, tema, tipo de hook, horário de publicação
- Mix de conteúdo: 40% macro, 25% educação, 15% trade, 10% prop, 10% mindset

**Pergunta do checkpoint:** "Aprova o calendário da semana? Quer ajustar algum tema/formato?"

**Critérios de Qualidade:**
- 5-6 Reels planejados (mínimo 5)
- Nenhum formato repetido em dias consecutivos
- Eventos econômicos mapeados e cobertos
- Mix de pilares respeitado (tolerância +/- 10%)
- Horários de publicação definidos
- Pelo menos 1 formato diferente do mais usado na semana anterior

**Erros Comuns a Evitar:**
- Planejar só um tipo de conteúdo (ex: 5 News na mesma semana)
- Ignorar eventos econômicos importantes
- Não deixar espaço para breaking news
- Copiar exatamente o calendário da semana anterior

---

## Step 02 — Trend Research (Pesquisa de Tendências)

**Tipo:** Inline (sem checkpoint)

**Agente:** Tina Trend — Viral Trend Hunter

**Objetivo:** Pesquisa de formatos virais, sons trending e tendências no nicho de trading/finanças para a semana atual.

**Inputs:** Calendário semanal aprovado (Step 01), Instagram Explore, TikTok Creative Center, lista de concorrentes.

**Concorrentes monitorados:** @smcandict, @tradingcoachind, @newtraderu

**Output produzido:**
- 3-5 trends/formatos identificados
- Sons trending que combinam com o nicho
- Links de vídeos virais de referência
- Recomendações de quais trends adaptar para @rubimfx
- Alertas sobre formatos saturados (evitar)

**Critérios de Qualidade:**
- Mínimo 3 trends identificados com exemplos concretos
- Sons trending categorizados (hype, calma, news, motivacional)
- Verificação de que trends não estão saturados (> 3 semanas de pico)

**Erros Comuns a Evitar:**
- Sugerir trends sem relação com trading/finanças
- Indicar sons com letra (compete com a voz do Gabriel)
- Trends que já passaram do pico de viralidade
- Não verificar se trend funciona para vídeo com clone IA
- Ignorar concorrentes diretos no nicho ICT/SMC

---

## Step 03 — Script Writing (Criação de Roteiro)

**Tipo:** Checkpoint

**Agente:** Rex Roteirista — Roteirista de Reels e Vídeos Curtos

**Objetivo:** Criação do roteiro completo para o Reel, incluindo hook, desenvolvimento, CTA, indicações de B-roll e texto na tela.

**Inputs:**
- Briefing do Cal Calendar (tema, formato, tipo de hook)
- `hook-database.md` — Banco de hooks
- `tone-of-voice.md` — Guia de estilo de fala do Gabriel
- `anti-patterns.md` — Erros a evitar
- Trends da Tina Trend

**Output produzido:**
```
HOOK (0-3s):
  - Texto na tela
  - Frase falada

CONTEÚDO (3-45s):
  - Desenvolvimento com indicações de [CORTE], [B-ROLL], [FACE CÂMERA]

CTA (últimos 5-10s):
  - Call-to-action específico
```
- Tempo estimado (15-60 segundos)
- Indicação de formato (dos 10 formatos)
- Hook alternativo para A/B testing

**Pergunta do checkpoint:** "Aprova o roteiro? Quer ajustar algo?"

**Critérios de Qualidade:**
- Hook nos primeiros 3 segundos (obrigatório)
- Hook aparece como texto na tela E é falado simultaneamente
- Duração entre 15-60 segundos
- Tom de voz alinhado com o guia (expressões do Gabriel presentes)
- Termos técnicos em inglês (não traduzidos: FVG, SMC, order block)
- Português com acentos corretos
- CTA específico e contextual (não genérico)
- Indicações de B-roll/cortes claras
- Roteiro funciona para clone IA (não exige gestos complexos)

**Erros Comuns a Evitar:**
- Roteiro longo demais (> 60 segundos)
- Hook fraco ou genérico ("Fala, pessoal")
- Esquecer de incluir texto na tela para o hook
- Linguagem que não é do Gabriel ("Galera", "Bora lá")
- CTA genérico ("Curte e segue")
- Roteiro que exige gestos específicos (clone IA tem limitação)
- Prometer ganho fácil ou valores específicos
- Termos técnicos traduzidos ("lacuna de valor justo" em vez de "FVG")

---

## Step 04 — A/B Hook Test (Teste A/B de Hook)

**Tipo:** Inline (sem checkpoint)

**Skill:** A/B Testing Framework

**Objetivo:** Preparação de variações de hook para teste A/B comparando qual abertura gera mais engajamento.

**Inputs:**
- Roteiro aprovado (Step 03) com hook principal
- `hook-database.md`
- Histórico de testes A/B anteriores

**Output produzido:**
- Hook A (hook do roteiro aprovado)
- Hook B (variação alternativa de categoria diferente)
- Plano de teste: quando publicar cada versão
- Métricas a comparar após 48 horas
- Template de registro preenchido

**Critérios de Qualidade:**
- Duas variações claras e distintas (categorias diferentes de hook)
- Apenas 1 variável diferente entre A e B (hook, não conteúdo)
- Plano de publicação definido (mesmo horário, dias diferentes)
- Métricas de comparação definidas antecipadamente
- Teste documentado antes de executar

**Erros Comuns a Evitar:**
- Testar hooks muito parecidos (sem diferença real)
- Mudar mais de 1 variável entre A e B
- Não documentar o teste antes de publicar
- Tirar conclusão com menos de 1000 impressões
- Esquecer de registrar o resultado depois

---

## Step 05 — Voice Generation (Geração de Áudio)

**Tipo:** Checkpoint

**Agente:** Elia ElevenLabs — Especialista em Clone de Voz

**Objetivo:** Geração do áudio com clone de voz do Gabriel usando ElevenLabs, garantindo naturalidade, pronúncia correta e tom emocional adequado.

**Inputs:**
- Roteiro aprovado (Step 03) com texto completo da fala
- `tone-of-voice.md` — referência de ritmo, tom e expressões
- Parâmetros de voz configurados no ElevenLabs (stability, similarity, style)

**Output produzido:**
- Arquivo de áudio (MP3/WAV) com fala completa
- Duração do áudio (15-60 segundos)
- Notas sobre qualidade e pontos de atenção para lip sync
- Arquivo alternativo se primeira geração não ficou boa

**Pergunta do checkpoint:** "O áudio está natural? Pronúncia OK?"

**Critérios de Qualidade:**
- Soa como o Gabriel (não voz genérica)
- Ritmo de 130-150 palavras/minuto
- Pausas naturais antes de pontos de ênfase
- Variação emocional (não monótono)
- Respiração audível em pausas naturais
- Termos técnicos em inglês pronunciados corretamente
- Sem artefatos (clicks, distorção, fade-outs, robóticos)
- Sotaque PT-BR natural
- Duração entre 15-60 segundos

**Erros Comuns a Evitar:**
- Voz rápida demais (> 160 palavras/min) — soa artificial
- Voz monótona sem variação de tom
- Falta de respiração entre frases
- Pronúncia errada de termos em inglês (FVG, FOMC)
- Stability muito alta no ElevenLabs (voz robótica)
- Similarity muito baixa (perde identidade do Gabriel)

---

## Step 06 — B-Roll Curation (Curadoria de B-Roll)

**Tipo:** Inline (sem checkpoint)

**Agente:** Bea B-Roll — Curadora de Material de Apoio Visual

**Objetivo:** Seleção e preparação de vídeos e imagens de apoio (B-roll) para cobrir cortes, ilustrar conceitos e enriquecer visualmente o vídeo.

**Inputs:**
- Roteiro aprovado com indicações de [B-ROLL] e [CORTE PARA GRÁFICO]
- Tema e formato do vídeo
- Screenshots de notícias/gráficos se o formato exigir

**Output produzido:**
- Lista de clips/imagens de B-roll selecionados
- Timestamps de onde cada B-roll entra
- Arquivos organizados em pasta do projeto
- Screenshots de gráficos/notícias recortados e otimizados

**Fontes por prioridade:**
1. Pexels API (grátis) — trading/finance/tech
2. Screenshots de notícias reais via Firecrawl
3. Screen recordings de TradingView e MT5
4. Imagens IA via Nano Banana
5. Fotos pessoais via `clone_image.py`

**Critérios de Qualidade:**
- B-roll relevante ao tema (não genérico)
- Resolução mínima 1080p
- Formato vertical (9:16) ou adaptável
- Screenshots de notícias recortados (só a parte relevante)
- Gráficos legíveis em tela de celular
- Sem marcas d'água

**Erros Comuns a Evitar:**
- Fotos genéricas de Unsplash/Pexels como conteúdo principal
- Screenshots de páginas inteiras (ilegíveis em celular)
- B-roll com marca d'água
- Clips horizontais sem adaptar para vertical
- Gráficos com texto pequeno demais

---

## Step 07 — Video Generation (Geração de Vídeo com Clone)

**Tipo:** Checkpoint

**Agente:** Hugo HeyGen — Especialista em Clone Facial de Vídeo

**Objetivo:** Geração do vídeo com clone facial do Gabriel usando HeyGen (ou Argil), combinando o áudio aprovado com o avatar.

**Inputs:**
- Áudio aprovado (Step 05)
- Avatar/clone do Gabriel configurado no HeyGen
- Instruções de movimento (head movements, expressão)
- Fundo desejado (escritório, green screen, custom)

**Output produzido:**
- Vídeo MP4 com clone facial + áudio sincronizado
- Resolução mínima 1080x1920 (9:16 vertical)
- Duração correspondente ao áudio (15-60 segundos)
- Versão em máxima qualidade/bitrate para pós-processamento

**Pergunta do checkpoint:** "O vídeo do clone está realista? Lip sync OK?"

**Critérios de Qualidade:**
- Clone se parece com o Gabriel
- Lip sync alinhado com o áudio (máx. 3 frames de diferença)
- Movimentos de cabeça naturais (não estático)
- Piscadas irregulares (não robóticas)
- Pele com textura (não plástica/cerosa)
- Fundo estável (sem flicker)
- Borda do cabelo natural (não hard-edge)
- Iluminação consistente
- Formato vertical 9:16

**Ferramentas:**
| Ferramenta | Uso | Custo |
|-----------|-----|-------|
| HeyGen Avatar IV | News/informacional | $24/mês |
| Hedra Character-3 | Storytelling emocional | $10-15/mês |
| OmniHuman API | Premium full-body, cinema | pay-per-use |

**Erros Comuns a Evitar:**
- Usar avatar genérico em vez do clone personalizado
- Não incluir instrução de movimento natural no prompt
- Exportar em resolução baixa (< 1080p)
- Fundo com elementos que flickam
- Não verificar lip sync antes de enviar para pós-produção

---

## Step 08 — Clone Validation (Validação do Clone)

**Tipo:** Checkpoint (score mínimo 8/10)

**Skill:** Clone Validator — Checklist de Validação de Qualidade

**Objetivo:** Validação rigorosa da qualidade do vídeo gerado com clone IA em 5 dimensões. Score mínimo 8/10 para avançar.

**Inputs:**
- Vídeo gerado (Step 07)
- Vídeo real recente do Gabriel (comparação lado a lado)
- Player com reprodução frame-a-frame (VLC: tecla "E")

**5 scores parciais:**
- Tom de Pele (___/10)
- Padrão de Piscadas (___/10)
- Lip Sync (___/10)
- Movimento de Cabeça (___/10)
- Identidade de Voz (___/10)

**Status:** APROVADO (>= 8.0) ou REPROVADO (< 8.0)

**Pergunta do checkpoint:** "Score do clone atingiu 8/10? Aprovado?"

**Critérios de Qualidade:**
- Score final >= 8.0/10
- Nenhum score parcial abaixo de 6.0 (mesmo que média passe)
- Lip sync testado em velocidade 0.5x
- Piscadas verificadas por 30 segundos (irregulares?)
- Comparação visual com vídeo real do Gabriel feita

**Erros Comuns a Evitar:**
- Aprovar sem validação completa (pressa)
- Aceitar score 7.x "porque tá bom o suficiente"
- Não reproduzir em 0.5x para verificar lip sync
- Verificar apenas por 5 segundos em vez dos 30 completos
- Não comparar com vídeo real do Gabriel

---

## Step 09 — Post Processing (Pós-Processamento)

**Tipo:** Inline (sem checkpoint — executado apenas se necessário)

**Skill:** Post Processing Pipeline

**Objetivo:** Melhoria da qualidade visual do vídeo do clone através de upscaling, correção de textura de pele, ajuste de lip sync e color grading. Aplicar APENAS se necessário baseado no relatório do Clone Validator.

**Inputs:**
- Vídeo do clone (Step 07)
- Relatório de validação (Step 08) com áreas de melhoria
- Vídeo real do Gabriel (referência de cor e textura)

**Output produzido:**
- Vídeo pós-processado em alta qualidade
- Exportação: H.264/H.265 a 20-30Mbps para 1080p
- Log das operações aplicadas

**Ferramentas:** Topaz Video AI, MuseTalk, Claid.ai

**Critérios de Qualidade:**
- Pele com textura natural (poros e linhas visíveis)
- Cor de pele matching com vídeos reais do Gabriel
- Sem flicker na região do rosto
- Upscale sem artefatos
- Color grade consistente com estética real do Gabriel
- Exportação em qualidade máxima (20-30Mbps)

**Erros Comuns a Evitar:**
- Aplicar pós-processamento desnecessário
- Over-sharpen que cria artefatos
- Color grade que muda tom de pele drasticamente
- Compressão excessiva (< 10Mbps)
- Processar áudio e vídeo separados e dessincronizar

---

## Step 10 — Caption & Edit (Legendas e Edição)

**Tipo:** Inline (sem checkpoint — revisão final no Quality Gate)

**Agente:** Sam Submagic — Especialista em Legendas Animadas

**Objetivo:** Adição de legendas animadas, edição de cortes, inserção de B-roll nos pontos indicados e ajustes finais de ritmo.

**Inputs:**
- Vídeo pós-processado (Step 09)
- B-roll curado (Step 06)
- Roteiro com indicações de [CORTE], [B-ROLL], [TEXTO NA TELA]
- Estilo de legenda do @rubimfx

**Output produzido:**
- Vídeo editado com legendas animadas sincronizadas
- B-roll inserido nos pontos indicados
- Texto na tela nos momentos-chave (hook, dados, CTA)
- Transições suaves
- Arquivo pronto para thumbnail e publicação

**Especificações de legenda:**
- 9:16, 1080x1920px
- PT-BR com acentos
- Fonte mínima 48px
- Estilos: Bold Highlight, Karaoke sync, Minimal text
- Posição: centro-inferior (não cobrir o rosto)
- Palavras-chave em negrito ou cor contrastante
- Termos ICT/SMC em inglês (FVG, stop loss — manter no original)

**Critérios de Qualidade:**
- Legendas sincronizadas com áudio (máx. 1 frame de diferença)
- Fonte legível (mínimo 28px — ideal 48px+)
- Legendas não cobrem o rosto
- Palavras-chave destacadas
- B-roll inserido nos timestamps corretos
- Texto do hook nos primeiros 3 segundos
- Texto do CTA nos últimos 5 segundos
- Português com acentos corretos

**Erros Comuns a Evitar:**
- Legendas com fonte pequena (< 22px)
- Legendas cobrindo o rosto
- Acentos faltando ("voce", "e" ao invés de "é")
- B-roll que não corresponde ao que está sendo falado
- Cortes muito rápidos

---

## Step 11 — Thumbnail (Capa do Reel)

**Tipo:** Inline (sem checkpoint — revisão no Quality Gate)

**Skill:** Thumbnail Generator

**Objetivo:** Criação da capa/thumbnail otimizada para o Reel, garantindo CTR alto no grid do perfil e na aba Reels.

**Inputs:**
- Vídeo editado (Step 10)
- Formato do vídeo
- Frase-chave do hook
- Estilo recomendado (Text-Heavy, Face-Focus, Action-Shot)

**Output:** Thumbnail em 1080x1920 pixels (9:16), PNG ou JPG de alta qualidade

**Critérios de Qualidade:**
- Resolução 1080x1920 (9:16)
- Texto legível em miniatura (testar em 150x150px)
- Máximo 8 palavras no texto
- Contraste alto entre texto e fundo
- Rosto visível se estilo Face-Focus
- Dentro da zona segura do grid (sem cortes)
- Não conflita com ícones do Instagram (play, duração)
- Consistente com estética do perfil @rubimfx
- Diferente da thumbnail do vídeo anterior

**Erros Comuns a Evitar:**
- Texto pequeno demais (ilegível em miniatura)
- Muitas palavras (> 10) na thumbnail
- Clickbait que não corresponde ao conteúdo
- Foto genérica de banco de imagens
- Não testar a legibilidade em tamanho reduzido

---

## Step 12 — CTA Selection (Seleção de CTA)

**Tipo:** Inline — integrado ao roteiro (sem checkpoint)

**Skill:** CTA Optimizer

**Objetivo:** Seleção do Call-to-Action otimizado alinhando o pedido ao tipo de conteúdo e objetivo principal.

**Inputs:**
- Roteiro com tema e formato (Step 03)
- Tipo de conteúdo (educacional, opinião, resultado, notícia, mindset)
- Objetivo do vídeo (awareness, engagement, conversão)
- Histórico de CTAs usados recentemente (evitar repetição)

**Output produzido:**
- CTA primário selecionado (texto exato)
- CTA secundário como alternativa
- Justificativa da escolha
- Indicação de que o CTA deve ser FALADO + ESCRITO na tela

**Critérios de Qualidade:**
- CTA específico e contextual (não genérico)
- Apenas 1 CTA por vídeo
- CTA alinhado ao tipo de conteúdo:
  - Educacional → save
  - Opinião → comment
  - Resultado → follow
- Diferente do CTA do vídeo anterior
- Tom natural (soa como conversa)

**Erros Comuns a Evitar:**
- "Curte e segue" — genérico, zero impacto
- Pedir 2+ ações ao mesmo tempo
- CTA sem conexão com o conteúdo
- Repetir o mesmo CTA em vídeos consecutivos
- Usar linguagem de YouTube ("se inscreve no canal")
- CTA só falado mas não escrito na tela (ou vice-versa)

---

## Step 13 — Quality Gate (Validação Final)

**Tipo:** Checkpoint

**Skill:** Quality Gate — Checklist de Validação Completa

**Objetivo:** Checklist de validação final completa antes da publicação. Verifica todos os aspectos do vídeo.

**Inputs:**
- Vídeo final editado com legendas (Step 10)
- Thumbnail (Step 11)
- CTA definido (Step 12)
- `anti-patterns.md`
- Relatório de validação do clone (Step 08)

**Checklist completo:**

**Visual:**
- Clone realista (score >= 8/10 no Clone Validator)
- Pele com textura natural
- Piscadas irregulares e naturais
- Movimento de cabeça natural
- Fundo estável sem flicker
- Resolução 1080x1920 (9:16)

**Áudio:**
- Voz soa como o Gabriel
- Ritmo natural (130-150 palavras/min)
- Sem artefatos (clicks, distorção)
- Música (se houver) abaixo de 20% do volume da voz

**Legendas:**
- Sincronizadas com áudio
- Fonte legível (>= 28px)
- Português com acentos corretos
- Não cobrem o rosto
- Palavras-chave destacadas

**Conteúdo:**
- Hook nos primeiros 3 segundos (texto + fala)
- CTA específico nos últimos 5 segundos
- Formato diferente do vídeo anterior
- Sem promessas de ganho fácil
- Sem fotos genéricas como conteúdo principal

**Thumbnail:**
- Legível em miniatura
- Contraste alto
- Dentro da zona segura do grid

**Lip Sync:**
- Consoantes (p, b, m) com boca fechando
- Nasais (ã, em) diferenciadas
- Máximo 3 frames de diferença
- Boca parada quando não há fala

**Pergunta do checkpoint:** "Vídeo final passou no Quality Gate? Pronto para publicar?"

---

## Step 14 — Publish (Publicação)

**Tipo:** Checkpoint (confirmação final antes de publicar)

**Agente:** Pablo Publisher — Publicador Multiplataforma

**Objetivo:** Publicação do vídeo aprovado no Instagram Reels e TikTok.

**Inputs:**
- Vídeo final aprovado no Quality Gate (Step 13)
- Thumbnail aprovada (Step 11)
- CTA definido (Step 12)
- Horário de publicação do calendário (Step 01)
- Caption/descrição do post
- Hashtags relevantes

**Output produzido:**
- Post publicado no Instagram Reels
- Post publicado no TikTok (se aplicável)
- Link do post para tracking
- Screenshot de confirmação
- Registro com data, horário e formato para Ana Analytics

**Horários otimizados:**
| Dia | Horário BRT |
|-----|-------------|
| Segunda | 6h-9h |
| Terça | 6h-9h |
| Quarta | 8h-11h |
| Quinta | 7h-10h |
| Sexta | 12h-14h |
| Evento macro | 30-90min após o evento |

**Pergunta do checkpoint:** "Confirma publicação?"

**Critérios de Qualidade:**
- Vídeo no formato correto (9:16, 1080x1920)
- Thumbnail/capa selecionada corretamente
- Caption com CTA alinhado ao vídeo
- Hashtags relevantes (5-15 hashtags — estrutura: 1 marca #RubimFX + 2 nicho + 1-2 descoberta)
- Horário de publicação conforme calendário
- Compartilhamento no Stories ativado
- Publicação em ambas as plataformas (Instagram + TikTok)

**Erros Comuns a Evitar:**
- Publicar no horário errado
- Esquecer de selecionar thumbnail customizada (Instagram usa frame aleatório)
- Caption sem CTA
- Hashtags demais (> 20) ou genéricas
- Não verificar se o vídeo carregou em boa qualidade
- Publicar sem compartilhar nos Stories
- Esquecer de publicar no TikTok
- Não registrar data/horário para Analytics

---

## Step 15 — Analytics (Registro de Métricas)

**Tipo:** Inline (sem checkpoint — acontece 48h após publicação)

**Agente:** Ana Analytics — Analista de Performance de Vídeo

**Objetivo:** Coleta e registro de métricas de performance após 48 horas, alimentando o banco de dados para análises e melhoria contínua.

**Inputs:**
- Link do post publicado (Step 14)
- Dados do calendário: formato, pilar, tipo de hook, horário
- Acesso ao Instagram Insights / Meta Business Suite
- Planilha de tracking histórica

**Output produzido:**
Registro completo de métricas na planilha de tracking:
- Data, formato, hook type, horário
- Views, saves, shares, comments, completion%, followers+
- **Score calculado:** `(saves × 3) + (shares × 2) + comments + (completion% × views / 100)`
- Comparação com média histórica do mesmo formato
- Flag se o vídeo é outlier (positivo ou negativo)
- Alimentação do relatório semanal

**Metas de performance:**
- Completion rate > 80%
- Save rate > 5%
- Share rate > 3%
- Comment rate > 2%

**Critérios de Qualidade:**
- Métricas coletadas exatamente 48h após publicação
- Todas as 6 métricas primárias registradas
- Score calculado corretamente
- Comparação com média histórica feita
- Formato e tipo de hook registrados para análise cruzada
- Outliers flagged para investigação

**Erros Comuns a Evitar:**
- Coletar métricas antes de 48h (dados incompletos)
- Esquecer de registrar o formato e tipo de hook
- Tirar conclusões com 1 vídeo (precisa de mínimo 5 por formato)
- Não re-coletar métricas de vídeos que "explodem" depois de 48h
- Ignorar fatores externos (feriados, eventos) ao analisar outliers
- Não compartilhar insights com Cal Calendar para ajustar próxima semana
