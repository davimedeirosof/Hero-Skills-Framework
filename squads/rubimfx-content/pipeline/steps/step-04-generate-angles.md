---
execution: inline
agent: iago-instagram
inputFile: squads/rubimfx-content/output/news-research.md
outputFile: squads/rubimfx-content/output/angles.md
---

# Step 04 — Generate Angles (Inline)

## Context Loading

- `squads/rubimfx-content/output/news-research.md` — notícia selecionada (marcada como Selected Story)
- `company.md` — tom de voz @rubimfx, público-alvo, valores da marca
- `agents/iago-instagram/agent.md` — configuração do agente de conteúdo Instagram
- `agents/iago-instagram/tasks/generate-angles.md` — task de geração de ângulos
- `squads/rubimfx-content/output/style-guide.md` — style guide atualizado (do Step 02b)

## Instructions

Gerar 5 ângulos editoriais distintos para transformar a notícia selecionada em carrossel Instagram. Cada ângulo deve oferecer uma perspectiva diferente sobre o mesmo evento.

### Processo

1. **Analisar a notícia selecionada** — Extrair:
   - Fato central e dados-chave
   - Ativos impactados
   - Contexto macro (o que veio antes, o que vem depois)
   - Bridge macro→trading já identificado

2. **Executar generate-angles.md** — Criar exatamente 5 ângulos, cada um com abordagem distinta. Sugestões de tipos (adaptar conforme a notícia):

   - **Ângulo A: Explicativo/Educacional** — Explica o conceito por trás da notícia no estilo @economesteter. Ex: "O que é o FOMC e por que ele move o mercado?"

   - **Ângulo B: Contrarian/Provocativo** — Apresenta o lado que ninguém está falando. Ex: "Todo mundo está bullish no ouro, mas e se o NFP surpreender?"

   - **Ângulo C: Bridge Macro→Trading** (OPCIONAL — incluir quando a conexão for natural) — Conecta o evento macro com operação prática. Ex: "NFP fraco → dólar caiu → liquidity sweep no EUR/USD → setup ativado"

   - **Ângulo D: Timeline/Sequência** — Conta a história cronologicamente. Ex: "Os 5 eventos que levaram o ouro para máxima histórica"

   - **Ângulo E: Impacto Prático** — Impacto direto na vida do trader/investidor. Ex: "Selic subiu — o que muda no seu bolso e nos seus trades"

3. **Formatar cada ângulo** — Para cada um, incluir:
   - Nome do ângulo (A-E)
   - Tipo (bridge, educacional, contrarian, timeline, prático)
   - Hook do slide 1 (frase de impacto)
   - Estrutura de slides (resumo em bullet points)
   - Tom predominante (informativo, provocativo, didático, urgente)
   - Estimativa de slides (6-10)

4. **Ordenar por potencial** — Classificar do mais forte ao mais fraco com base em: engajamento estimado, alinhamento com a marca, originalidade.

5. **Validar diversidade** — Garantir que os 5 ângulos são genuinamente diferentes, não variações do mesmo approach.

## Output Format

```markdown
# Ângulos — [Título da Notícia]

## Notícia Base
[resumo da notícia selecionada]

## Ângulo A: [Nome] (BRIDGE MACRO→TRADING)
- **Tipo:** Bridge
- **Hook:** "[frase de impacto para slide 1]"
- **Estrutura:**
  1. [slide 1 — hook]
  2. [slide 2 — contexto]
  [...]
- **Tom:** [tom predominante]
- **Slides estimados:** [número]
- **Por que funciona:** [justificativa]

[repete para B-E]
```

## Output Example

```markdown
# Ângulos — Fed mantém juros mas sinaliza corte em junho

## Notícia Base
O Federal Reserve manteve juros em 5.25-5.50% mas o dot plot revisado mostra maioria projetando corte de 25bps em junho. Ouro renovou ATH em $2.385. DXY perdeu 104.

## Ângulo A: "O Fed falou. O ouro ouviu." (BRIDGE MACRO→TRADING)
- **Tipo:** Bridge macro→trading
- **Hook:** "O Fed manteve os juros. O ouro subiu 2.3%. Coincidência? Nunca."
- **Estrutura:**
  1. Hook — frase de impacto + dado do ouro
  2. O que o Fed decidiu (fatos, números)
  3. O que o dot plot revelou (projeção de corte)
  4. Por que o ouro reage a juros (relação inversa)
  5. O que aconteceu no gráfico (XAU/USD, DXY)
  6. Bridge: como operar isso na prática
  7. Setup ou leitura: suporte, resistência, cenários
  8. CTA: "Qual ativo você está de olho?"
- **Tom:** Informativo com pitada de provocação
- **Slides estimados:** 8
- **Por que funciona:** Conecta macro (Fed) com trading (ouro) de forma direta, dados fortes, público adora gold

## Ângulo B: "FOMC em 60 segundos" (EDUCACIONAL)
- **Tipo:** Explicativo/Educacional
- **Hook:** "O FOMC decidiu ontem. Você sabe o que é o FOMC?"
- **Estrutura:**
  1. Hook — pergunta direta
  2. O que é o FOMC (explicação simples)
  3. Por que ele é o evento mais importante do mercado
  4. O que foi decidido ontem (resumo)
  5. Dot plot: o que é e o que mostrou
  6. Impacto nos ativos (DXY, ouro, bolsa)
  7. Próximos passos: o que observar
  8. CTA: "Salva pra não esquecer antes do próximo FOMC"
- **Tom:** Didático, acessível
- **Slides estimados:** 8
- **Por que funciona:** Atrai iniciantes, alto potencial de save, evergreen parcial

## Ângulo C: "Todo mundo virou bullish no ouro. Cuidado." (CONTRARIAN)
- **Tipo:** Contrarian/Provocativo
- **Hook:** "Ouro em ATH. Todo mundo comprando. É aí que mora o perigo."
- **Estrutura:**
  1. Hook — provocação contra o consenso
  2. O que todo mundo está dizendo (narrativa bullish)
  3. Mas o que ninguém está falando (riscos)
  4. NFP na próxima semana pode mudar tudo
  5. Cenário bear: e se os dados surpreenderem?
  6. Histórico: outras vezes que "todo mundo" estava errado
  7. A leitura equilibrada (bullish com ressalvas)
  8. CTA: "Você está comprado ou vendido em ouro?"
- **Tom:** Provocativo, contrarian
- **Slides estimados:** 8
- **Por que funciona:** Gera debate nos comments, engagement alto, diferencia de outros perfis

## Ângulo D: "Os 5 eventos que levaram o ouro ao ATH" (TIMELINE)
- **Tipo:** Timeline/Sequência
- **Hook:** "O ouro não subiu do nada. Foram 5 eventos em sequência."
- **Estrutura:**
  1. Hook — ouro em ATH não é acaso
  2. Evento 1: Inflação caindo (dados PCE)
  3. Evento 2: Bancos centrais comprando ouro
  4. Evento 3: Tensões geopolíticas (China/Taiwan)
  5. Evento 4: Dot plot dovish do Fed
  6. Evento 5: Fluxo para ETFs de ouro
  7. O resultado: $2.385 e contando
  8. O que vem depois: cenários
  9. CTA: "Qual desses eventos te surpreendeu?"
- **Tom:** Narrativo, cronológico
- **Slides estimados:** 9
- **Por que funciona:** Storytelling forte, educativo, mostra profundidade de análise

## Ângulo E: "Como operar o Fed na mesa proprietária" (PRÁTICO/PROP)
- **Tipo:** Prático/Prop Trading
- **Hook:** "O Fed decidiu. Quem opera em mesa prop sabe: é hora de ter plano."
- **Estrutura:**
  1. Hook — conexão Fed + prop trading
  2. Por que decisões do Fed são perigosas para contas funded
  3. Regra de ouro: não operar durante o comunicado
  4. Oportunidades pós-Fed (gaps, momentum)
  5. Setup: ouro após comunicado dovish (com gestão de risco)
  6. Gestão de risco: drawdown, lot size, regras da prop
  7. Checklist pré-notícia para prop traders
  8. CTA: "Você opera notícia ou espera o poeira baixar?"
- **Tom:** Prático, direto, específico
- **Slides estimados:** 8
- **Por que funciona:** Público @rubimfx opera em prop, conteúdo hiper-relevante e acionável
```

## Veto Conditions

- **Sem diversidade de perspectiva** — Os 5 ângulos devem oferecer visões genuinamente diferentes da mesma notícia. Se a notícia tem conexão natural com trading, incluir um ângulo Bridge. Se não tem, não forçar — focar em ângulos informativos, educacionais e de impacto.
- **Ângulos repetitivos** — Se 3+ ângulos seguem a mesma estrutura ou tom, reescrever até haver diversidade genuína.
- **Hook fraco** — Nenhum hook pode ser genérico ("Entenda o que aconteceu", "Notícia importante"). Deve ser específico, com dado ou provocação.

## Quality Criteria

- Cada ângulo deve ter hook de no máximo 15 palavras, direto e impactante
- A estrutura de slides deve ter entre 6-10 slides para cada ângulo
- Os 5 ângulos devem cobrir pelo menos 3 tons diferentes (informativo, provocativo, didático, urgente, prático)
- Cada ângulo deve ter justificativa ("por que funciona") baseada em engagement do público-alvo
- O ângulo Bridge (A) deve mencionar pelo menos 1 ativo específico e 1 direção de trade
