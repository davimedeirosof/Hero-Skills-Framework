# rubimfx-content — Tasks Detalhadas dos Agentes

Tasks detalhadas de cada agente do squad de conteúdo (`squads/rubimfx-content/agents/`).

---

## Nara Notícia — Pesquisadora de Notícias

### Task: find-news — Busca Ampla de Notícias

**Objetivo:** Varrer fontes prioritárias e retornar 10-15 notícias candidatas sobre macro, economia, forex, ouro, índices e prop trading. Fase de amplitude — o filtro fino acontece em rank-stories.

**Processo:**

1. **Step 1 — Ler o Foco de Pesquisa:** Abrir `context/research-focus.md` e extrair tópico principal, período de busca (padrão: últimas 24h), ativos em destaque e restrições.

2. **Step 2 — Buscar em Fontes Prioritárias:** Executar buscas em pelo menos 5 fontes usando `web_search`:
   - Termos em inglês: "FOMC", "Fed", "NFP", "CPI", "gold XAUUSD", "S&P500", "forex", "US dollar DXY", "tariffs trade war"
   - Termos em português: "Selic COPOM", "economia brasileira mercado", "dolar real"
   - Termos específicos: "prop trading news", "funded trader", nomes de prop firms
   - Consultar calendário econômico via ForexFactory ou Investing.com
   - Para cada resultado, usar `web_fetch` para confirmar data, extrair resumo e validar URL

3. **Step 3 — Compilar Lista Bruta:** Montar lista com 10-15 notícias. Descartar notícias sem fonte verificável, mais antigas que o período definido (salvo desdobramentos novos), sem conexão com @rubimfx ou paywalled sem resumo acessível.

4. **Step 4 — Salvar Output:** Gravar em `artifacts/raw-news-list.md`.

**Output Format (YAML):**
```yaml
meta:
  search_date: "YYYY-MM-DD"
  period: "ultimas 24h | ultimas 48h | semana"
  focus: "topico do research-focus ou cobertura geral"
  total_found: 12
  sources_consulted:
    - Bloomberg
    - Reuters

stories:
  - id: 1
    title: "Titulo original da noticia"
    source: "Nome da Fonte"
    date: "YYYY-MM-DD"
    url: "https://..."
    summary: "Resumo de 2-3 linhas com dados concretos."
    assets_impacted:
      - XAUUSD
      - DXY
    category: "fed | macro-us | macro-br | geopolitics | commodities | prop-trading | crypto"
```

**Critérios de Qualidade:**
- Volume: mínimo 10, máximo 15 notícias
- Diversidade de fontes: pelo menos 4 fontes diferentes
- Campos completos: 100% das notícias com todos os campos do schema
- Resumo informativo: cada summary com pelo menos 1 dado numérico concreto

**Veto Conditions:**
1. Fonte não verificável: URL não funciona ou fonte não identificável — NOT entra na lista
2. Fora do escopo: sem conexão com forex, ouro, índices, macro ou prop trading
3. Duplicata: manter apenas a versão da fonte de maior prioridade

---

### Task: rank-stories — Ranking e Seleção Final

**Objetivo:** Receber a lista bruta de 10-15 notícias e aplicar sistema de pontuação em 4 critérios para selecionar as top 5 histórias, cada uma com sugestão de ângulo para carrossel.

**Processo:**

1. **Step 1 — Carregar e Validar Lista Bruta:** Abrir `artifacts/raw-news-list.md`, validar que há pelo menos 10 notícias e todos os campos estão preenchidos. Se houver menos de 8, sinalizar e prosseguir.

2. **Step 2 — Pontuar Cada Notícia (1-5 cada critério, total máximo 20):**
   - **Critério 1: Relevância Forex/Ouro/Índices (peso 1-5):** 5=impacto direto em XAUUSD/EUR/USD/DXY/S&P500, 3=impacto indireto, 1=conexão tangencial
   - **Critério 2: Impacto no Público @rubimfx (peso 1-5):** 5=afeta diretamente traders brasileiros, 3=relevante para educação, 1=interessante mas distante
   - **Critério 3: Potencial de Carrossel (peso 1-5):** 5=dados visualizáveis + debate + antes/depois, 3=tem dados OU debate, 1=difícil de transformar em visual
   - **Critério 4: Atualidade (peso 1-5):** 5=últimas 6h, 4=últimas 12h, 3=últimas 24h, 2=últimas 48h, 1=mais antigo

3. **Step 3 — Selecionar Top 5 e Sugerir Ângulos:** Ordenar por pontuação total (desempate pelo Critério 1). Para cada uma: definir ângulo de carrossel em 1 frase, sugerir formato visual (dados, timeline, vs., checklist, mapa) e indicar hook potencial.

4. **Step 4 — Salvar Briefing Final:** Gravar em `artifacts/news-brief.md`.

**Output Format (YAML):**
```yaml
ranked_stories:
  - rank: 1
    title: "Titulo da noticia"
    scores:
      relevance: 5
      audience_impact: 5
      carousel_potential: 4
      timeliness: 5
      total: 19
    carousel_angle: "Descricao do angulo em 1 frase"
    visual_format: "dados | timeline | versus | checklist | mapa | infografico"
    hook_suggestion: "Frase de hook para o primeiro slide"
    assets_impacted:
      - XAUUSD
```

**Critérios de Qualidade:**
- Ranking justificado: cada nota 1-5 deve ser coerente
- Diversidade temática: top 5 deve cobrir pelo menos 3 categorias diferentes
- Ângulos acionáveis: específicos o suficiente para roteirista começar sem pesquisa adicional
- Hook concreto: frase curta e direta, no estilo @rubimfx

**Veto Conditions:**
1. Nota inflada: total acima de 16 sem dados concretos no resumo — revisar
2. Monocultura temática: se 4+ das top 5 são do mesmo tema, substituir a de menor nota
3. Hook genérico: "Veja o que aconteceu no mercado hoje" é vetado

---

## Iago Instagram — Criador de Conteúdo Instagram

### Task: generate-angles — Gerar 5 Ângulos Editoriais

**Objetivo:** Gerar 5 ângulos editoriais distintos a partir de uma única notícia, cada um reposicionando a informação por diferentes lentes emocionais e estratégicas.

**Inputs:** `news_story` (string), `pillar` (macro|ict-education|trade-analysis|summit-prop|orderflow-mindset), `context` (opcional)

**Output:** Lista de 5 objetos de ângulo

**Processo:**

1. **Step 1 — Desconstruir a Notícia:** Extrair fato central, implicação de mercado, relevância para a audiência e conexões ICT/SMC.

2. **Step 2 — Gerar 5 Ângulos:**
   - **Medo/Urgência:** Enquadrar como ameaça ou alerta
   - **Oportunidade:** Enquadrar como janela de oportunidade
   - **Educacional:** Usar a notícia como veículo pedagógico para conceitos ICT/SMC
   - **Contrário:** Tomar posição oposta ao consenso com honestidade intelectual
   - **Ponte Macro→Trading:** Ângulo signature conectando headline macro através de cadeia causal até setup específico

3. **Step 3 — Pontuar e Ranquear:** Atribuir Hook Strength, Swipe Potential e Bridge Clarity (1-5 cada). Marcar top 1-2 como recomendados.

**Critérios de Qualidade:**
- Exatamente 5 ângulos (um por lente)
- Máximo 12 palavras por título
- Enquadramento emocional distinto em todos os ângulos
- Pelo menos um ângulo marcado como recomendado com justificativa

**Veto Conditions:**
- VETO se menos de 5 ângulos ou qualquer lente pulada
- VETO se o ângulo Ponte não contém par/instrumento específico e tipo de setup
- VETO se algum título ultrapassa 12 palavras

---

### Task: create-instagram-feed — Criar Carrossel Instagram

**Objetivo:** Produzir carrosseis Instagram com formato estruturado de 8-10 slides.

**Input necessário:** Ângulo selecionado, notícia, pilar de conteúdo e referência de trade (opcional)

**Estrutura de Output — 8-10 slides:**
- Slide 1: Capa (headline apenas, âncora visual)
- Slides 2-3: Hook + contexto estabelecendo tensão
- Slides 4-6: Desenvolvimento progressivo do argumento
- Slides 7-8: Bridge macro→trading e síntese
- Slide 9: Takeaway claro
- Slide 10: Call-to-action

**Restrições críticas:**
- Slides de conteúdo: entre 40-80 palavras
- Carrosseis: exatamente 8-10 slides
- Conteúdo macro requer ponte explícita para setup de trading
- Slide de capa: apenas headline, sem corpo de texto

**Verificação de qualidade:** word counts, disciplina de uma ideia por slide, marcação de palavras-chave accent, ritmo visual através de alternância de backgrounds, originalidade da legenda.

---

### Task: optimize-instagram-feed — Otimizar Carrossel Instagram

**Objetivo:** Refinar drafts de carrossel em 4 dimensões de otimização: força do hook, fluxo de swipe-through, densidade de informação e highlights de palavras-chave accent.

**Fases:**

1. **Audit Phase:** Avalia hook impact (Slide 1), transition flow (Slides 2-9), conformidade de word count (40-80 palavras) e qualidade de keyword selection.

2. **Optimization Phase:** Reescreve headlines fracas, adiciona swipe-bridges ao final dos slides, ajusta densidade, refina keywords, sugere ajustes de ritmo de cor. Todas as modificações recebem tags `[CHANGED]`.

3. **A/B Variant Creation:** Desenvolve cover alternativa usando estratégias de hook estruturalmente diferentes — afirmação vs. pergunta, números vs. emoção.

4. **Reporting:** Entrega scores de audit (antes/após), lista de mudanças, carrossel completo otimizado e justificativa do A/B.

**Checkpoints obrigatórios:**
- Todos os edits requerem markup visível
- Scores antes/após devem mostrar diferenciação significativa
- Variantes A/B devem usar abordagens genuinamente distintas
- Cada transição precisa de swipe-flow scoring >= 6/10
- Palavras-chave accent devem capturar todos os termos ICT/SMC críticos

**Veto Conditions:**
- Relatórios sem scores antes/após
- Variantes A/B repetindo a estratégia de headline original
- Slides otimizados fora dos parâmetros de word-count

---

## Diana Design — Designer Visual

### Task: create-carousel-visuals — Criar Visuais do Carrossel

**Objetivo:** Gerar visuais de carrossel dark-mode para Instagram do @rubimfx, produzindo HTML/CSS auto-contido renderizável como PNG de 1080x1440px.

**Especificações de design:**
- Dimensões fixas: 1080×1440 pixels
- Header bar: "@rubimfx" (~70px de altura)
- Headlines: 48-72px bold sans-serif, branco ou cor accent
- Corpo de texto: 22-26px, cinza claro (#E2E8F0)
- Padding mínimo: 40px (60px recomendado)
- Apenas system fonts (sem dependências CDN externas)

**Tipos de slide:**
- Cover: abertura de alto impacto
- Concept: desenvolvimento de conceito
- List: listas estruturadas
- Comparison: comparações
- Data: dados em destaque
- CTA: call-to-action de fechamento

**Rotação de backgrounds (3 tons escuros alternados):** `#0A0A0F`, `#111118`, `#0F172A`

**Veto Conditions:**
1. Dimensões incorretas de pixels
2. Dependências externas (CDN fonts, imagens externas, scripts)
3. Backgrounds claros violando requisitos de dark mode

---

## Leo Legenda — Copywriter de Legendas

### Task: write-caption — Escrever Legenda para Instagram

**Objetivo:** Criar legenda completa para Instagram que complementa o carrossel do @rubimfx, maximizando engajamento (saves, comments, shares) com tom de autoridade praticante e compliance regulatório.

**Processo:**

1. **Passo 1 — Analisar o carrossel:** Identificar conceito central, insight mais forte e o que NÃO foi dito nos slides. A legenda cobre o ponto (c) — complementar, não repetir.

2. **Passo 2 — Criar o hook (primeiros 125 caracteres):** Escrever 3 variações usando uma dessas estruturas:
   - **Confronto:** "90% dos traders usam [X] errado"
   - **Revelação:** "O mercado te diz exatamente onde vai — você só não sabe ler"
   - **Identificação:** "Se você já tomou stop e não entendeu por quê, leia isso"

3. **Passo 3 — Escrever o corpo (150-400 palavras):** Contexto ou mini-história, 2-3 insights práticos, termos técnicos em inglês onde natural, emojis como marcadores visuais (máx. 5-7 no total).

4. **Passo 4 — Criar o CTA de fechamento:**
   - Posts educativos: "Salva pra revisar antes de operar"
   - Posts polêmicos: "Comenta o que você acha"
   - Posts de análise: "Marca quem precisa ver isso"

5. **Passo 5 — Revisar:** Hook cabe em 125 chars, sem promessas de retorno, estrutura escanável, tom @rubimfx, CTA claro.

**Critérios de Qualidade:**
- Hook máximo 125 caracteres, provoca curiosidade imediata
- Corpo contém pelo menos 2 insights práticos não presentes no carrossel
- Tom consistente: praticante, direto, sem guru vibes
- Zero promessas de retorno financeiro

**Veto Conditions:**
1. **Promessa de retorno:** Qualquer menção a ganhos financeiros específicos — VETO IMEDIATO
2. **Hook acima de 125 caracteres** — VETO, reescrever hook
3. **Repetição do carrossel:** mais de 50% do conteúdo copiado dos slides — VETO

---

### Task: write-hashtags — Criar Set de Hashtags Estratégicas

**Objetivo:** Produzir set de 5-15 hashtags estratégicas para o post do @rubimfx, equilibrando hashtags de nicho (alta relevância), categoria (volume médio) e amplas (descoberta).

**Processo:**

1. **Passo 1 — Classificar o conteúdo:** Identificar categoria principal (ICT/Smart Money, Macro/Economia, Forex, Análise Técnica, Mindset de Trader) e sub-temas.

2. **Passo 2 — Montar mix de 3 camadas:**
   - **Nicho (3-5 tags):** Termos específicos — `#orderblocks`, `#smartmoneyconcepts`, `#fairvaluegap`, `#ictconcepts`
   - **Categoria (3-5 tags):** Termos do segmento — `#tradingbrasil`, `#forexbrasil`, `#analisetecnica`, `#priceaction`
   - **Amplas (2-4 tags):** Descoberta — `#mercadofinanceiro`, `#investimentos`, `#educacaofinanceira`

3. **Passo 3 — Validar e filtrar:**
   - Remover hashtags banidas ou shadowbanned
   - Evitar hashtags com mais de 10M de posts (muito genéricas)
   - Evitar hashtags com menos de 1K posts (muito nichadas)
   - Total entre 5 e 15 hashtags

**Critérios de Qualidade:**
- Set com entre 5 e 15 hashtags, representação das 3 camadas
- Hashtags de nicho diretamente relevantes ao tema
- Sempre incluir `#rubimfx`
- Mix equilibrado: não mais que 40% de hashtags amplas

**Veto Conditions:**
1. Hashtags irrelevantes ao conteúdo do post — VETO
2. Mais de 50% de hashtags com +5M posts — VETO
3. Termos em português traduzido forçado (`#blocodeordem` em vez de `#orderblocks`) — VETO

---

## Renata Revisão — Analista de Qualidade

### Task: score-content — Pontuar Conteúdo do Carrossel

**Objetivo:** Sistema de avaliação ponderada em 5 dimensões para determinar prontidão para publicação.

**Dimensões de avaliação (total 10.0):**
1. **Precisão Factual (peso 25%):** Valida conceitos de trading, dados macroeconômicos e exemplos técnicos
2. **Voz & Tom (peso 20%):** Verifica autoridade praticante sem posicionamento de guru; hooks fortes nos primeiros 125 caracteres
3. **Qualidade Visual (peso 20%):** Revisa consistência dark mode, hierarquia tipográfica, word count dos slides (40-80)
4. **Compliance Regulatório (peso 20%):** Verifica ausência de promessas de retorno garantido e posicionamento educacional adequado
5. **Estrutura & Engajamento (peso 15%):** Avalia fluxo lógico e potencial de saves/shares/comments

**Thresholds de decisão:**
- **>= 8.0:** Aprovado para publicação
- **7.0-7.9:** Ajustes menores aceitáveis
- **< 7.0:** Retrabalho necessário

**Veto Conditions (automáticas):**
- Falhas de compliance abaixo de 7/10 → rework automático
- Erros factuais graves em conceitos core → rework automático (proteger credibilidade prevalece sobre outros scores)

---

### Task: generate-feedback — Gerar Feedback Acionável

**Objetivo:** Transformar avaliações de conteúdo em orientações específicas dirigidas aos agentes Leo Legenda (texto) e Diana Design (visuais).

**Processo:**

1. **Listar pontos fortes** (2-4 elementos com detalhes mensuráveis)

2. **Identificar problemas** classificados como:
   - **Bloqueantes:** impedem publicação, devem ser resolvidos
   - **Importantes:** devem ser corrigidos se possível
   - **Menores:** opcionais

3. **Gerar action items** com designação de agente responsável, descrição da ação, impacto esperado e solução proposta

4. **Definir prioridade** e agrupar por responsável (Leo Legenda ou Diana Design)

**Critérios de Qualidade:**
- Todo problema identificado tem uma ação específica com agente responsável
- Ações são executáveis sem ambiguidade

**Veto Conditions:**
- Problemas sem ações propostas
- Classificação incorreta de bloqueantes
- Crítica genérica sem elementos específicos

---

## Vitor Visual — Pesquisador de Tendências Visuais

### Task: research-visual-trends — Pesquisar Tendências Visuais

**Objetivo:** Identificar tendências atuais de design visual em carrosseis de Instagram no nicho de finanças, economia e trading.

**Contas de referência monitoradas:**
- @economesteter (obrigatório — base visual do @rubimfx)
- @visualcap
- @newtraderu
- @smcandict
- @zcfxofficial

**Processo de 4 etapas:**

1. **Coleta de dados:** Documentar elementos de carrossel por conta (paleta de cores com hex codes, estilos tipográficos, layouts, elementos gráficos)

2. **Identificação de padrões:** Cruzar observações para identificar tendências confirmadas (3+ contas), emergentes, em declínio e diferenciais únicos

3. **Classificação e prioridade:** Ranquear por relevância para @rubimfx, compatibilidade com estética @economesteter, maturidade e esforço de implementação

4. **Documentação detalhada:** Criar cards individuais de tendências com descrições visuais que permitam designers replicar os estilos independentemente

**Output:** `trend-report.md` em formato Markdown com header YAML

**Critérios de Qualidade:**
- Mínimo 3 tendências identificadas, cada uma com exemplo concreto
- Hex codes de cores e nomes/pesos de fontes específicos
- Análise de @economesteter obrigatória — relatório sem ela é automaticamente rejeitado
- Mínimo 3 contas monitoradas e 10+ posts analisados

---

### Task: extract-style-guide — Compilar Guia de Estilo para Diana Design

**Objetivo:** Transformar o relatório de tendências em guia de estilo prático e completo que Diana Design usa diretamente para criar carrosseis de @rubimfx, mantendo @economesteter como base visual.

**Processo:**

1. **Step 1 — Consolidar Base @economesteter (imutável):**
   - Fundos: dark `#0D1117` ou navy `#0F1729`, opção gradiente radial sutil
   - Tipografia: sans-serif bold para headlines, regular para corpo
   - Cores de destaque: gold `#F59E0B` (dados, números), teal `#00D4AA` (positivo, alta), red `#EF4444` (negativo, queda)
   - Header bar: faixa superior com logo @rubimfx e título da série
   - Primeira slide: estilo capa de revista editorial com foto do Gabriel Rubim
   - Densidade: alta informação por slide, gráficos e infográficos integrados

2. **Step 2 — Incorporar Tendências Aprovadas:** Do trend-report, selecionar apenas tendências "adotar agora" ou "testar". Documentar como aplicar dentro da base @economesteter, em quais tipos de slide usar e data de validade estimada.

3. **Step 3 — Montar Especificações Técnicas:**
   - Paleta de cores completa com hex, nome e uso recomendado
   - Escala tipográfica com fonte, peso, tamanho e uso por hierarquia
   - Grid e espaçamento (margens, gutters, padding)
   - Templates de layout para cada tipo de slide
   - Do's and Don'ts com exemplos descritivos

**Critérios de Qualidade:**
- Base @economesteter documentada explicitamente como fundação
- Paleta de cores completa com hex codes e uso recomendado
- Regras tipográficas com fonte, peso, tamanho e uso por nível hierárquico
- Pelo menos 3 templates de layout (capa, conteúdo, CTA) com especificações
- Seção Do's and Don'ts com mínimo 5 itens em cada lista
- Documento auto-suficiente — Diana Design não precisa de outra referência

**Veto Conditions:**
- Base @economesteter ausente ou diluída — reescrever
- Especificações incompletas (sem hex codes, sem nomes de fontes ou sem medidas)
- Tendências sem classificação temporal — rejeitadas para evitar que se tornem permanentes

---

## Referência do Style Guide @economesteter

*Arquivo: `squads/rubimfx-content/pipeline/data/style-guide-economesteter.md`*

### Paleta de Cores

**Backgrounds:**

| Nome | Hex | Uso |
|------|-----|-----|
| Navy escuro | `#0D1117` | Background primário padrão |
| Charcoal | `#1A1B2E` | Background secundário alternante |
| Navy profundo | `#0A0E1A` | Slides de destaque |
| Cinza escuro | `#161B22` | Cards internos, tabelas |

**REGRA ABSOLUTA:** Background SEMPRE escuro. Light mode é proibido.

**Textos:**

| Nome | Hex |
|------|-----|
| Branco | `#FFFFFF` |
| Cinza claro | `#A0AEC0` |
| Cinza médio | `#718096` |

**Accent:**

| Nome | Hex | Quando usar |
|------|-----|-------------|
| Gold | `#F59E0B` | Destaques, títulos accent, dados-chave |
| Teal | `#00D4AA` | Alternativa ao gold quando necessário |
| Azul claro | `#3B82F6` | Links conceituais, complementar |

**Semânticas:**

| Nome | Hex | Uso |
|------|-----|-----|
| Verde | `#22C55E` | Positivo / Gain / Alta |
| Vermelho | `#EF4444` | Negativo / Loss / Queda |
| Amarelo | `#EAB308` | Alerta / Atenção |

### Tipografia

- **Headlines/Títulos:** Montserrat Bold, Space Grotesk Bold ou Inter Bold — CAPS ou Title Case, 700-800 — 28-40px
- **Subtítulos:** Montserrat Semi-Bold ou Space Grotesk Medium — Semi-Bold 600 — 20-24px
- **Corpo:** Inter Regular ou DM Sans Regular — Regular 400 — mínimo 16px, line-height 1.5-1.6
- **Dados/Números:** Space Grotesk Bold, JetBrains Mono — accent color ou semântico (verde/vermelho)

### Layout

- **Formato:** 3:4 portrait, 1080x1440px
- **Margem segura:** 60px em todas as bordas
- **Área útil:** 960x1320px
- **Header Bar:** obrigatório em todos os slides — @rubimfx à esquerda, data à direita, separador linha fina `#2D3748`
- **Hierarquia por slide:** exatamente 2 camadas visuais (Headline + Supporting text) + elemento visual opcional

### Tipos de Slide

- **Slide 1 — Capa (Magazine Cover):** Elemento visual dominante (foto Powell, gráfico, ativo) com overlay escuro 60-80%, título bold overlay, header bar
- **Slides 2-8 — Conteúdo:** Background sólido, headline + supporting text, dados em destaque
- **Slide Final — CTA:** @rubimfx centralizado, CTA em texto grande, logos (ETF, Summit Prop) quando relevante

### Anti-Patterns Visuais
- Background branco ou claro
- Fontes decorativas/script/serif
- Gradientes coloridos (rainbow, neon)
- Inconsistência de accent color entre slides
- Texto menor que 16px equivalente
- Conteúdo encostando nas bordas
- Mais de 2 accent colors no mesmo carrossel
