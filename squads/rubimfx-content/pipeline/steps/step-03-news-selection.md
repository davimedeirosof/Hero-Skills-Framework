---
type: checkpoint
---

# Step 03 — News Selection (Checkpoint)

## Context Loading

- `squads/rubimfx-content/output/news-research.md` — lista ranqueada de 5 notícias do Step 02
- `squads/rubimfx-content/pipeline/data/research-focus.md` — foco original do usuário

## Instructions

Este checkpoint apresenta as 5 notícias ranqueadas e pede ao usuário que selecione UMA para produzir o conteúdo.

### Processo

1. **Apresentar resumo da pesquisa** — Informar quantas fontes foram consultadas, o horizonte temporal coberto e o foco original.

2. **Listar as 5 notícias** — Para cada notícia, apresentar de forma compacta:
   - Número + Título
   - Score (X/10)
   - Resumo em 1-2 linhas
   - Ativos impactados (lista curta)
   - Bridge macro→trading em 1 frase

   Formato sugerido:
   > **1. [Título]** (Score: 9.5/10)
   > Resumo curto. Ativos: DXY, XAU/USD, EUR/USD.
   > Bridge: Corte de juros em junho = dólar fraco = ouro bullish.

3. **Solicitar seleção** — Perguntar:
   > "Qual notícia você quer transformar em carrossel? (1-5)"

   Incluir opções adicionais:
   - **"Pesquisar mais"** — volta ao Step 02 com o mesmo foco ou foco ajustado
   - **"Combinar notícias"** — se o usuário quiser juntar 2 notícias relacionadas, registrar ambas

4. **Confirmar seleção** — Após a escolha, repetir a notícia selecionada com detalhes completos e pedir confirmação:
   > "Confirmado: vamos criar um carrossel sobre [título]. Correto?"

5. **Registrar decisão** — Salvar a notícia selecionada no news-research.md com uma marcação `## Selected Story` no topo, para que os próximos steps saibam qual notícia usar.

## Output Format

A interação com o usuário deve seguir este formato:

```
## Pesquisa Concluída

Foco: [tema]
Fontes: [X fontes consultadas]
Período: [horizonte]

---

### Top 5 Notícias

**1. [Título]** (Score: X/10)
[Resumo] | Ativos: [lista] | Bridge: [frase]

**2. [Título]** (Score: X/10)
[Resumo] | Ativos: [lista] | Bridge: [frase]

[...]

---

Qual notícia você quer transformar em carrossel? (1-5)
Ou: "Pesquisar mais" | "Combinar notícias"
```

## Output Example

```
## Pesquisa Concluída

Foco: FOMC — Decisão de juros do Federal Reserve
Fontes: 8 fontes consultadas (Reuters, Bloomberg, ForexFactory, Fed.gov, Investing.com, FT, InfoMoney, analistas X)
Período: Últimas 24h

---

### Top 5 Notícias

**1. Fed mantém juros mas sinaliza corte em junho** (Score: 9.5/10)
Dot plot revisado mostra maioria projetando corte de 25bps em junho. Powell fala em "progresso substancial" na inflação.
Ativos: DXY, EUR/USD, XAU/USD, US500 | Bridge: Corte confirmado = dólar fraco = ouro e euro bullish

**2. Ouro renova máxima histórica após Fed** (Score: 9.0/10)
XAU/USD +2.3% para $2.385/oz. Fluxo para ETFs de ouro em alta de 3 meses.
Ativos: XAU/USD, XAG/USD, GDX | Bridge: ATH + volume = momentum de alta. Retest $2.350 como suporte

**3. DXY perde suporte de 104** (Score: 8.5/10)
Índice do dólar abaixo de 104.00 pela primeira vez em 2 meses. EUR/USD rompe 1.0900.
Ativos: DXY, EUR/USD, GBP/USD, USD/JPY | Bridge: Dólar fraco favorece pares EUR e GBP long

**4. China anuncia estímulo de $500bi** (Score: 7.5/10)
Pacote de 3.6T yuan para infraestrutura e tech verde. Implementação no Q2.
Ativos: AUD/USD, NZD/USD, cobre | Bridge: Demanda chinesa por commodities = AUD bullish

**5. NFP da próxima semana será decisivo** (Score: 7.0/10)
Relatório de emprego pode confirmar ou negar expectativa de corte em junho. Consenso: 180K.
Ativos: DXY, XAU/USD, S&P 500 | Bridge: NFP fraco = confirma corte = ouro sobe

---

Qual notícia você quer transformar em carrossel? (1-5)
Ou: "Pesquisar mais" | "Combinar notícias"
```

## Veto Conditions

- **Seleção fora do range** — Se o usuário escolher um número fora de 1-5 ou algo incompreensível, pedir novamente de forma clara.
- **Prosseguir sem confirmação** — Não avançar para o Step 04 sem que o usuário confirme explicitamente a notícia selecionada.

## Quality Criteria

- A apresentação deve ser escanável em menos de 30 segundos (formato compacto, não paredes de texto)
- Cada notícia deve mostrar score, resumo, ativos e bridge em no máximo 3 linhas
- A opção "Pesquisar mais" deve estar visível para não forçar escolha insatisfatória
- A confirmação final deve repetir a notícia selecionada com detalhes suficientes para o usuário validar
