# rubimfx-content — Steps Detalhados do Pipeline

Pipeline completo de conteúdo do squad `rubimfx-content` com 12 steps (step-01 a step-11 + step-02b).

---

## Visão Geral do Pipeline

```
PLANEJAMENTO
  Step 01 — Research Focus (Checkpoint)     ← Define foco da pesquisa com o usuário
  Step 02 — News Research (Inline)          ← Nara busca e ranqueia notícias
  Step 02b — Visual Trends (Inline)         ← Vitor pesquisa tendências visuais

SELEÇÃO
  Step 03 — News Selection (Checkpoint)     ← Usuário seleciona 1 notícia das top 5
  Step 04 — Generate Angles (Inline)        ← Iago gera 5 ângulos editoriais
  Step 05 — Angle Selection (Checkpoint)    ← Usuário seleciona 1 ângulo

CRIAÇÃO DE CONTEÚDO
  Step 06 — Create Carousel (Inline)        ← Iago cria e otimiza o carrossel
  Step 07 — Write Caption (Inline)          ← Leo escreve legenda e hashtags
  Step 08 — Content Approval (Checkpoint)   ← Usuário aprova conteúdo textual

PRODUÇÃO VISUAL
  Step 09 — Create Visuals (Inline)         ← Diana gera HTML/CSS dos slides
  Step 10 — Review (Inline)                 ← Renata revisa e pontua tudo
  Step 11 — Final Approval (Checkpoint)     ← Usuário aprova para publicação
```

**Checkpoints (5):** Steps 01, 03, 05, 08 e 11 — requerem aprovação do usuário para prosseguir.

---

## Step 01 — Research Focus (Checkpoint)

**Tipo:** Checkpoint — requer input do usuário

**Objetivo:** Coletar direcionamento editorial antes de iniciar a pesquisa de notícias.

**Arquivos de contexto carregados:**
- `company.md` — identidade da marca @rubimfx, tom editorial, público-alvo
- `squads/rubimfx-content/squad.md` — configuração da squad e pipeline

**Processo:**

1. **Cumprimentar e contextualizar** — Informar que estamos iniciando o pipeline de conteúdo @rubimfx e precisamos definir o foco.

2. **Perguntar o foco da pesquisa:**
   > "Qual o foco da pesquisa hoje?"

   Categorias sugeridas:
   - Política monetária: FOMC, BCE, COPOM, decisão de juros
   - Dados econômicos: NFP, CPI, PIB, PMI
   - Commodities: Ouro, petróleo, prata
   - Geopolítica: guerras comerciais, tarifas, sanções
   - Mercado forex: DXY, pares principais, correlações
   - Mesa proprietária: desafios, regras, psicologia de trading
   - Evergreen: conceitos atemporais de macro/trading

3. **Perguntar o horizonte temporal:**
   > "Qual o período de cobertura?"
   - Últimas 24h — notícias do dia, ideal para conteúdo quente
   - Últimos 7 dias — visão semanal
   - Último mês — tendências de médio prazo
   - Evergreen — sem limite temporal

4. **Confirmar e registrar** — Repetir a escolha do usuário para confirmação antes de gravar.

**Output:** `research-focus.md` com tópico, horizonte temporal, palavras-chave e notas do usuário.

**Veto Conditions:**
- Foco vago demais ("qualquer coisa") — insistir por direcionamento específico
- Tema fora do escopo (sem relação com macro/economia/trading/forex) — alertar e sugerir alternativas
- Sem horizonte temporal — não prosseguir

---

## Step 02 — News Research (Inline)

**Tipo:** Inline — executado automaticamente pelo agente Nara Notícia

**Agente:** Nara Notícia

**Arquivos de contexto:**
- `squads/rubimfx-content/pipeline/data/research-focus.md` — foco definido no Step 01
- `company.md` — identidade da marca

**Tasks executadas:**
- `find-news` — busca ampla em 5+ fontes (Reuters, Bloomberg, ForexFactory, InfoMoney, Banco Central)
- `rank-stories` — ranking com critérios ponderados (relevância trading 3x, potencial de engajamento, bridge macro→trading, atualidade, originalidade)

**Critérios de ranking:** Cada notícia pontuada em 4 dimensões (1-5). Peso triplo para relevância de trading.

**Output:** Top 5 notícias em `output/news-research.md` com:
- Fonte verificada com link
- Data de publicação
- Resumo de 2-3 frases com dado numérico chave
- Ativos impactados
- Bridge macro→trading (setup específico)
- Score de relevância 0-10

**Quality Gate:** Mínimo 3 notícias com score >= 7 e diversidade de fontes.

---

## Step 02b — Visual Trends (Inline)

**Tipo:** Inline — executado em paralelo ao Step 02

**Agente:** Vitor Visual

**Objetivo:** Atualizar o style guide com tendências visuais atuais para carrosseis de Instagram no nicho de finanças.

**Contas monitoradas:** @economesteter (obrigatório), @visualcap, @newtraderu, @smcandict, @zcfxofficial

**Tasks executadas:**
- `research-visual-trends` — identifica tendências confirmadas (3+ contas), emergentes, em declínio
- `extract-style-guide` — compila guia de estilo prático para Diana Design

**Output:** `output/style-guide.md` — guia de estilo atualizado baseado na referência @economesteter + tendências da semana.

**Nota:** O style guide de referência base está em `squads/rubimfx-content/pipeline/data/style-guide-economesteter.md`.

---

## Step 03 — News Selection (Checkpoint)

**Tipo:** Checkpoint — requer seleção do usuário

**Objetivo:** Apresentar as 5 notícias ranqueadas e pedir ao usuário que selecione UMA para produzir o conteúdo.

**Processo:**

1. **Apresentar resumo da pesquisa** — fontes consultadas, horizonte temporal coberto, foco original.

2. **Listar as 5 notícias** em formato compacto:
   > **1. [Título]** (Score: 9.5/10)
   > Resumo curto. Ativos: DXY, XAU/USD, EUR/USD.
   > Bridge: Corte de juros em junho = dólar fraco = ouro bullish.

3. **Solicitar seleção:** "Qual notícia você quer transformar em carrossel? (1-5)"
   - Opções adicionais: "Pesquisar mais" | "Combinar notícias"

4. **Confirmar seleção** — repetir a notícia selecionada com detalhes completos.

5. **Registrar decisão** — Salvar no news-research.md com marcação `## Selected Story`.

**Veto Conditions:**
- Seleção fora do range (1-5) — pedir novamente
- Prosseguir sem confirmação explícita — não avançar para Step 04

---

## Step 04 — Generate Angles (Inline)

**Tipo:** Inline — executado automaticamente

**Agente:** Iago Instagram

**Arquivos carregados:**
- Notícia selecionada (marked as Selected Story)
- `company.md` — tom de voz @rubimfx
- `agents/iago-instagram/tasks/generate-angles.md`
- `output/style-guide.md` — style guide do Step 02b

**Objetivo:** Gerar 5 ângulos editoriais distintos para a notícia selecionada.

**Tipos de ângulo (adaptar conforme a notícia):**
- **A: Explicativo/Educacional** — Explica conceito por trás da notícia no estilo @economesteter
- **B: Contrarian/Provocativo** — Apresenta o lado que ninguém está falando
- **C: Bridge Macro→Trading** (incluir quando a conexão for natural) — Conecta evento macro com operação prática
- **D: Timeline/Sequência** — Conta a história cronologicamente
- **E: Impacto Prático** — Impacto direto na vida do trader/investidor

**Para cada ângulo:**
- Nome (A-E) e tipo
- Hook do slide 1 (frase de impacto)
- Estrutura de slides (bullets)
- Tom predominante (informativo, provocativo, didático, urgente)
- Estimativa de slides (6-10)
- Justificativa ("por que funciona")

**Validação de diversidade:** Garantir que os 5 ângulos são genuinamente diferentes.

**Output:** `output/angles.md`

**Veto Conditions:**
- Sem diversidade de perspectiva — 5 ângulos devem ter visões genuinamente diferentes
- Ângulos repetitivos — se 3+ seguem mesma estrutura ou tom, reescrever
- Hook fraco ou genérico ("Entenda o que aconteceu") — vetado

---

## Step 05 — Angle Selection (Checkpoint)

**Tipo:** Checkpoint — requer seleção do usuário

**Objetivo:** Apresentar os 5 ângulos e pedir ao usuário que selecione UM para desenvolver como carrossel completo.

**Processo:**

1. **Recordar a notícia base** — em 1 linha.

2. **Apresentar os 5 ângulos** em formato compacto:
   > **A. "[Hook]"** (Bridge Macro→Trading)
   > Tom: Informativo + provocação | 8 slides
   > Conecta decisão do Fed com setup prático no ouro

3. **Destacar recomendação** — indicar qual o pipeline considera mais forte e por quê.

4. **Solicitar seleção:** "Qual ângulo você quer desenvolver? (A-E)"
   - Opções: "Misturar" | "Novo ângulo" | "Gerar mais"

5. **Confirmar** — repetir ângulo selecionado com hook e estrutura resumida.

6. **Registrar** — marcar no angles.md com `## Selected Angle`.

**Veto Conditions:**
- Prosseguir sem seleção clara — confirmar explicitamente antes de avançar
- Ignorar pedido de "Misturar" — registrar claramente os elementos combinados

---

## Step 06 — Create Carousel (Inline)

**Tipo:** Inline — executado automaticamente

**Agente:** Iago Instagram

**Arquivos carregados:**
- Notícia selecionada e ângulo selecionado
- `company.md`
- `agents/iago-instagram/tasks/create-instagram-feed.md`
- `agents/iago-instagram/tasks/optimize-instagram-feed.md`
- `output/style-guide.md`

**Processo:**

1. Gerar carrossel com 6-10 slides estruturados: cover slide (hook, máx. 12 palavras) + 2-7 content slides (máx. 40 palavras cada) + CTA slide.

2. Otimizar o draft: reescrever headlines fracas, adicionar swipe-bridges, ajustar densidade, criar variante A/B de cover.

3. Adicionar especificações de design para cada slide: tipo, layout sugerido, elementos visuais, notas de cor.

**Regras de copywriting:** linguagem direta sem enchimento, dados concretos, bridge macro→trading explícito quando ângulo Bridge.

**Output:** `output/carousel-draft.md` — carrossel completo com texto e notas de design.

**Veto Conditions:**
- Inventar estatísticas não verificadas
- Ultrapassar limites de word count
- Não conectar macro a setups quando ângulo Bridge

---

## Step 07 — Write Caption (Inline)

**Tipo:** Inline — executado automaticamente

**Agente:** Leo Legenda

**Tasks executadas:**
- `write-caption` — escreve legenda estruturada
- `write-hashtags` — seleciona 12-15 hashtags em 3 camadas

**Estrutura da legenda:**
- **Linha 1 (Hook):** Frase de impacto complementando o hook do slide 1 — máximo 1 linha, funciona sem ver o carrossel
- **Corpo (3-5 linhas):** Contexto adicional não coberto nos slides. Tom editorial, direto.
- **Quebra visual:** linha em branco ou "."
- **CTA (1-2 linhas):** Pergunta engajadora ou instrução direta — DIFERENTE do CTA do último slide
- **Hashtags:** Bloco separado

**Regras:** sem emojis em excesso (máx. 3-4), quebras de linha para legibilidade mobile, menção @rubimfx, sem linguagem de vendas ou hype.

**Hashtags em 4 camadas:**
- Camada 1 (3-4 tags): Alto volume — `#forex`, `#trading`, `#mercadofinanceiro`, `#investimentos`
- Camada 2 (3-4 tags): Médio volume, nicho — `#forextrader`, `#daytrade`, `#ouro`, `#macroeconomia`
- Camada 3 (3-4 tags): Baixo volume, específicas — `#fomc`, `#federalreserve`, `#xauusd`, `#proptrading`
- Camada 4 (2-3 tags): Marca — `#rubimfx`, `#tradingbrasil`
- Total: 12-15 hashtags (não exceder 15)

**Output:** `output/caption.md`

**Veto Conditions:**
- Legenda com mais de 2.200 caracteres (limite Instagram)
- Promessas financeiras — reformular para linguagem educacional
- Repetição do carrossel sem adicionar valor

---

## Step 08 — Content Approval (Checkpoint)

**Tipo:** Checkpoint — requer aprovação do usuário

**Objetivo:** Apresentar TODO o conteúdo textual produzido para aprovação antes de seguir para design visual.

**Apresentação:**
- Overview: tema, ângulo, número de slides, tom
- Carrossel slide por slide (formato compacto)
- Legenda completa
- Hashtags com contagem

**Decisão solicitada:** "O conteúdo está aprovado para seguir para design?"

**Opções:**
- **"Aprovado"** → Step 09 (design visual)
- **"Ajustar [slide X]"** → ajuste pontual e reapresentação
- **"Ajustar legenda"** → ajuste e reapresentação
- **"Refazer"** → volta ao Step 06 (mantendo o ângulo)
- **"Trocar ângulo"** → volta ao Step 05
- **"Trocar notícia"** → volta ao Step 03

**Quando aprovado:** marcar carousel-draft.md e caption.md com `## Status: APPROVED` e timestamp.

**Veto Conditions:**
- Prosseguir sem aprovação explícita do usuário — NUNCA avançar para Step 09 sem "Aprovado"
- Ignorar pedido de ajuste — toda solicitação deve ser implementada e reapresentada

---

## Step 09 — Create Visuals (Inline)

**Tipo:** Inline — executado automaticamente

**Agente:** Diana Design

**Arquivos carregados:**
- `output/carousel-draft.md` — carrossel aprovado com texto e notas de design
- `output/style-guide.md` — style guide do Step 02b
- `company.md` — identidade visual @rubimfx
- `agents/diana-design/tasks/create-carousel-visuals.md`

**Processo:**

1. **Carregar style guide** — paleta de cores, tipografia, layout grid, padrões de slide. Toda decisão visual segue o style guide.

2. **Analisar notas de design** — para cada slide, ler o tipo, layout sugerido, elementos visuais e cores de destaque.

3. **Gerar HTML/CSS completo** para cada slide:
   - Dimensão fixa: 1080x1350px (4:5 Instagram)
   - Fontes via Google Fonts (Inter, Space Mono)
   - Cada slide é um arquivo HTML autocontido com CSS inline
   - Sem animações (output estático)

4. **Garantir consistência visual** — mesma paleta, tipografia e margens em todos os slides.

5. **Adicionar elementos de marca:**
   - Marca d'água sutil @rubimfx (canto inferior direito, baixa opacidade)
   - Badge de categoria no slide de capa
   - Numeração discreta (ex: "3/8") — opcional

**Output:** `output/carousel-visuals.md` — HTML completo de todos os slides

**Veto Conditions:**
- Desvio do style guide — cores/fontes/layouts fora do guia devem ser corrigidos
- HTML inválido ou mal-formado
- Texto ilegível (contraste insuficiente, fontes abaixo de 18px)

---

## Step 10 — Review (Inline)

**Tipo:** Inline — executado automaticamente

**Agente:** Renata Revisão

**Tasks executadas:**
- `score-content` — pontuação ponderada em 5 dimensões
- `generate-feedback` — feedback acionável por agente responsável

**Dimensões de avaliação:**
1. Precisão Factual (3x peso)
2. Tom & Voz (2x peso)
3. Qualidade Visual (2x peso)
4. Compliance (3x peso)
5. Estrutura & Engajamento

**Classificação final:**
- 9-10: Excelente, pronto para publicar
- 7-8: Bom, ajustes menores recomendados
- 5-6: Regular, revisões necessárias
- 1-4: Insuficiente, recomenda reescrita

**Veto Triggers automáticos:**
- Erros factuais em dados primários — desqualificação automática
- Violações de compliance — desqualificação automática (proteger credibilidade prevalece)

**Issues priorizadas como:** Critical (deve corrigir), Important (deveria corrigir), Minor (melhorias opcionais)

**Output:** `output/review.md` — scores, feedback e recomendação final

---

## Step 11 — Final Approval (Checkpoint)

**Tipo:** Checkpoint — requer aprovação definitiva do usuário

**Objetivo:** Apresentar o carrossel completo com resultados da revisão para aprovação definitiva antes da publicação.

**Apresentação:**
- Review Score: X/10 com breakdown por dimensão
- Issues encontradas (categorizadas por prioridade)
- Carrossel resumido (número + tipo + hook/dado principal)
- Legenda completa
- Hashtags

**Próximos passos pós-aprovação:**
1. HTML dos slides será renderizado em imagens 1080x1350px
2. Legenda e hashtags ficam prontos para copiar
3. Conteúdo arquivado no output da squad

**Decisão solicitada:** "Conteúdo final aprovado para publicação?"

**Opções:**
- **"Aprovado"** → carrossel marcado como FINAL, pronto para publicação
- **"Corrigir [issue]"** → aplicar correção específica e reapresentar
- **"Revisar slides"** → volta ao Step 06
- **"Revisar visual"** → volta ao Step 09
- **"Recomeçar"** → volta ao Step 01

**Quando aprovado:** marcar todos os outputs como `## Status: FINAL` com timestamp.

**Veto Conditions:**
- Issues críticas não resolvidas — alertar explicitamente antes de permitir aprovação
- Aprovação sem visualização — usuário deve ter visto o conteúdo completo nesta sessão
