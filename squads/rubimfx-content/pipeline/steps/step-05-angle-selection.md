---
type: checkpoint
---

# Step 05 — Angle Selection (Checkpoint)

## Context Loading

- `squads/rubimfx-content/output/angles.md` — 5 ângulos gerados no Step 04
- `squads/rubimfx-content/output/news-research.md` — notícia selecionada (para referência)

## Instructions

Este checkpoint apresenta os 5 ângulos editoriais e pede ao usuário que selecione UM para desenvolver como carrossel completo.

### Processo

1. **Recordar a notícia base** — Em 1 linha, lembrar qual notícia foi selecionada no Step 03:
   > Notícia: "[título da notícia selecionada]"

2. **Apresentar os 5 ângulos** — Para cada ângulo, mostrar de forma compacta:
   - Letra (A-E) + Nome
   - Tipo entre parênteses
   - Hook exato do slide 1 (entre aspas)
   - Tom predominante
   - Número de slides estimados

   Formato sugerido:
   > **A. "O Fed falou. O ouro ouviu."** (Bridge Macro→Trading)
   > Tom: Informativo + provocação | 8 slides
   > Conecta decisão do Fed com setup prático no ouro

3. **Destacar recomendação** — Indicar qual ângulo o pipeline considera mais forte e por quê, mas deixar claro que a decisão é do usuário:
   > Recomendação: Ângulo A — maior potencial de engagement e alinhamento com a marca @rubimfx.

4. **Solicitar seleção** — Perguntar:
   > "Qual ângulo você quer desenvolver? (A-E)"

   Opções adicionais:
   - **"Misturar"** — combinar elementos de 2 ângulos (ex: "A com tom do C")
   - **"Novo ângulo"** — se nenhum agradar, descrever o ângulo desejado
   - **"Gerar mais"** — volta ao Step 04 para gerar mais ângulos

5. **Confirmar escolha** — Repetir o ângulo selecionado com hook e estrutura resumida. Pedir confirmação antes de prosseguir.

6. **Registrar decisão** — Marcar no angles.md qual ângulo foi selecionado (`## Selected Angle`) para que o Step 06 saiba qual desenvolver.

## Output Format

```
## Ângulos para: [título da notícia]

**A. "[Hook]"** (Bridge Macro→Trading)
Tom: [tom] | [X] slides
[Descrição em 1 linha]

**B. "[Hook]"** (Educacional)
Tom: [tom] | [X] slides
[Descrição em 1 linha]

**C. "[Hook]"** (Contrarian)
Tom: [tom] | [X] slides
[Descrição em 1 linha]

**D. "[Hook]"** (Timeline)
Tom: [tom] | [X] slides
[Descrição em 1 linha]

**E. "[Hook]"** (Prático/Prop)
Tom: [tom] | [X] slides
[Descrição em 1 linha]

---
Recomendação: [ângulo] — [justificativa curta]

Qual ângulo você quer desenvolver? (A-E)
Ou: "Misturar A+C" | "Novo ângulo" | "Gerar mais"
```

## Output Example

```
## Ângulos para: Fed mantém juros mas sinaliza corte em junho

**A. "O Fed falou. O ouro ouviu."** (Bridge Macro→Trading)
Tom: Informativo + provocação | 8 slides
Conecta a decisão do Fed com o rally do ouro e como operar o setup

**B. "FOMC em 60 segundos"** (Educacional)
Tom: Didático, acessível | 8 slides
Explica o FOMC para quem está começando, alto potencial de save

**C. "Todo mundo virou bullish no ouro. Cuidado."** (Contrarian)
Tom: Provocativo, contrarian | 8 slides
Questiona o consenso, levanta riscos que ninguém está falando

**D. "Os 5 eventos que levaram o ouro ao ATH"** (Timeline)
Tom: Narrativo, cronológico | 9 slides
Storytelling mostrando a sequência de eventos por trás do rally

**E. "Como operar o Fed na mesa proprietária"** (Prático/Prop)
Tom: Prático, direto | 8 slides
Setup e gestão de risco para quem opera em conta funded

---
Recomendação: Ângulo A — maior potencial de engagement, forte bridge macro→trading, alinhado com DNA @rubimfx.

Qual ângulo você quer desenvolver? (A-E)
Ou: "Misturar A+C" | "Novo ângulo" | "Gerar mais"
```

## Veto Conditions

- **Prosseguir sem seleção clara** — Não avançar se o usuário der resposta ambígua. Confirmar explicitamente qual ângulo (ou combinação) foi escolhido.
- **Ignorar pedido de "Misturar"** — Se o usuário pedir combinação, registrar claramente quais elementos de cada ângulo serão usados e confirmar antes de seguir.

## Quality Criteria

- A apresentação deve ser escanável em menos de 20 segundos
- Cada ângulo deve ser distinguível dos demais em no máximo 2 linhas
- O hook entre aspas deve ser a frase exata que apareceria no slide 1
- A recomendação deve ter justificativa objetiva (não apenas "é o melhor")
