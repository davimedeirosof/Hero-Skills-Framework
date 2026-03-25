---
type: checkpoint
outputFile: squads/rubimfx-content/pipeline/data/research-focus.md
---

# Step 01 — Research Focus (Checkpoint)

## Context Loading

- `company.md` — identidade da marca @rubimfx, tom editorial, público-alvo
- `squads/rubimfx-content/squad.md` — configuração da squad e pipeline

## Instructions

Este checkpoint coleta do usuário o direcionamento editorial antes de iniciar a pesquisa de notícias.

### Processo

1. **Cumprimentar e contextualizar** — Informar que estamos iniciando o pipeline de conteúdo @rubimfx e que precisamos definir o foco da pesquisa.

2. **Perguntar o foco da pesquisa** — Apresentar a pergunta principal:
   > "Qual o foco da pesquisa hoje?"

   Oferecer exemplos organizados por categoria:
   - **Política monetária:** FOMC, BCE, COPOM, decisão de juros
   - **Dados econômicos:** NFP, CPI, PIB, PMI
   - **Commodities:** Ouro, petróleo, prata
   - **Geopolítica:** guerras comerciais, tarifas, sanções
   - **Mercado forex:** DXY, pares principais, correlações
   - **Mesa proprietária:** desafios, regras, psicologia de trading
   - **Evergreen:** conceitos atemporais de macro/trading

3. **Perguntar o horizonte temporal** — Após o foco, perguntar:
   > "Qual o período de cobertura?"

   Opções:
   - **Últimas 24h** — notícias do dia, ideal para conteúdo quente
   - **Últimos 7 dias** — visão semanal, bom para resumos
   - **Último mês** — tendências de médio prazo
   - **Evergreen** — sem limite temporal, conteúdo atemporal

4. **Confirmar e registrar** — Repetir a escolha do usuário para confirmação antes de gravar.

## Output Format

O arquivo `research-focus.md` deve conter:

```markdown
# Research Focus

## Foco
[Tema escolhido pelo usuário]

## Horizonte Temporal
[Período selecionado]

## Palavras-chave
- [keyword 1]
- [keyword 2]
- [keyword 3]

## Notas do Usuário
[Qualquer contexto adicional fornecido]

## Data de Criação
[timestamp]
```

## Output Example

```markdown
# Research Focus

## Foco
FOMC — Decisão de juros do Federal Reserve e impacto no DXY e ouro

## Horizonte Temporal
Últimas 24h

## Palavras-chave
- FOMC
- Federal Reserve
- taxa de juros
- DXY
- ouro
- Jerome Powell

## Notas do Usuário
Quero focar na reação do mercado após a decisão, especialmente no ouro e no dólar.

## Data de Criação
2026-03-15T10:00:00-03:00
```

## Veto Conditions

- **Foco vago demais** — Se o usuário responder algo como "qualquer coisa" ou "tanto faz", insistir educadamente por um direcionamento mais específico.
- **Tema fora do escopo** — Se o foco não tiver relação com macro/economia/trading/forex, alertar que o conteúdo @rubimfx é focado em mercado financeiro e sugerir alternativas.
- **Sem horizonte temporal** — Não prosseguir sem definir o período de cobertura.

## Quality Criteria

- O foco deve ser específico o suficiente para direcionar a pesquisa (não apenas "economia")
- O horizonte temporal deve estar claramente definido
- As palavras-chave devem ser derivadas logicamente do foco escolhido
- O registro deve incluir qualquer nuance ou preferência expressa pelo usuário
