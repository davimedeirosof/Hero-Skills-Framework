# Domain Framework — @rubimfx Content Pipeline

## Objetivo

Produzir carrosseis de Instagram para @rubimfx no estilo editorial do @economesteter — a forma como ele conta notícias, estrutura argumentos, simplifica dados econômicos e constrói narrativas. Quando a notícia conecta naturalmente a forex/ouro/índices, fazer a ponte para trading. Quando não, entregar conteúdo macro de qualidade puro (topo de funil).

---

## Pipeline Operacional (7 Etapas)

### Etapa 1 — Monitoramento de Notícias Macro

Fontes prioritárias:
- **EUA:** FOMC (decisão de juros, dot plot, ata), NFP (payroll), CPI/PPI, PCE, ISM, GDP
- **Brasil:** COPOM/Selic, IPCA, PIB, fiscal, balança comercial
- **Global:** BCE, BoJ, BoE, tensões geopolíticas, OPEC
- **Ativos-chave:** DXY, ouro (XAU/USD), S&P 500, Nasdaq, petróleo (WTI/Brent)
- **Pares forex:** EUR/USD, GBP/USD, USD/JPY, USD/BRL
- **Derivativos BR:** WDO (mini dólar), WIN (mini índice)

Frequência: diária (scanning) + tempo real em dias de evento.

### Etapa 2 — Seleção da Pauta

Critérios de prioridade (peso 1-5):
1. **Impacto no mercado forex/futuros** (peso 5) — moveu ou vai mover preço?
2. **Relevância para a audiência** (peso 4) — traders BR de prop firm se importam?
3. **Timing** (peso 4) — ainda é novidade ou já saturou?
4. **Potencial de BRIDGE** (peso 2, opcional) — consigo conectar naturalmente a um setup? (não obrigatório)
5. **Potencial de viralização** (peso 2) — tem elemento de surpresa/polêmica?

Score mínimo para produção: 14/25.

### Etapa 3 — Geração de Ângulos

Para cada pauta, gerar no mínimo 3 ângulos:

| Tipo de Ângulo | Exemplo |
|---|---|
| **Medo / Alerta** | "O Fed sinalizou algo que ninguém percebeu" |
| **Oportunidade** | "Esse dado cria a melhor janela do mês para operar ouro" |
| **Educacional** | "Como ler o dot plot do Fed em 5 minutos" |
| **Contrário** | "Todo mundo espera corte. Aqui está por que estão errados" |
| **BRIDGE macro→trade** | "FOMC → DXY → setup no EUR/USD" |

Selecionar o ângulo com maior intersecção de relevância + viralização.

### Etapa 4 — Criação do Carrossel (8-10 slides)

Estrutura padrão:

| Slide | Função | Palavras |
|---|---|---|
| 1 (Capa) | Hook visual + título impactante | 10-20 |
| 2 | Contexto do evento / O que aconteceu | 50-70 |
| 3 | Dados / números relevantes | 40-60 |
| 4 | Por que isso importa (análise) | 50-80 |
| 5 | Impacto no mercado / ativos | 50-70 |
| 6 | **BRIDGE** — Conexão macro → setup | 50-80 |
| 7 | Setup / confluência técnica | 40-70 |
| 8 | O que esperar / cenários | 50-70 |
| 9 | Resumo / takeaway | 40-60 |
| 10 | CTA + branding | 20-40 |

### Etapa 5 — Caption

Estrutura:
- **Primeiros 125 caracteres:** Hook que para o scroll (aparece antes do "mais")
- **Corpo:** 2-4 parágrafos curtos expandindo o tema
- **CTA:** Pergunta ou chamada para ação (salvar, compartilhar, comentar)
- **Hashtags:** 5-15 relevantes, mix de volume alto e nicho

### Etapa 6 — Design Visual

Seguir o style-guide-economesteter.md rigorosamente:
- Dark mode obrigatório
- Tipografia bold condensada para headlines
- Hierarquia visual de 2 camadas por slide
- Formato 3:4 (1080x1440px)
- Header bar consistente com @rubimfx

### Etapa 7 — Revisão Final

Checklist:
- [ ] Dados e números conferidos com fonte primária
- [ ] Tom alinhado com tone-of-voice.md (default: Analítico Direto)
- [ ] Sem promessa de retorno ou resultado (compliance CVM/ANBIMA)
- [ ] Disclaimer presente quando necessário
- [ ] BRIDGE presente em conteúdo macro
- [ ] Visual consistente em todos os slides
- [ ] Caption com hook + CTA + hashtags

---

## Conceito BRIDGE

O diferencial do @rubimfx é o BRIDGE — a ponte entre macro e trade.

**Fórmula:**
```
Evento Macro → Impacto no Ativo → Leitura Técnica/Order Flow → Setup Ativado
```

**Exemplo completo:**
```
Fed manteve juros (macro)
→ Dólar enfraqueceu (impacto)
→ Ouro fez liquidity sweep acima de high anterior (leitura)
→ Retração para OB + confirmação de BOS (setup)
```

O BRIDGE transforma notícia genérica em conteúdo acionável para traders.

---

## Cadência de Publicação

- **Dias de evento macro (FOMC, NFP, COPOM):** Carrossel no mesmo dia ou D+1
- **Semanas normais:** 3-4 carrosseis/semana
- **Horários ideais:** 7h-9h ou 18h-20h (BRT)

---

## Dependências

- `style-guide-economesteter.md` — padrão visual
- `tone-of-voice.md` — tom de comunicação
- `quality-criteria.md` — critérios de aprovação
- `anti-patterns.md` — erros a evitar
- `output-examples.md` — referências concretas
