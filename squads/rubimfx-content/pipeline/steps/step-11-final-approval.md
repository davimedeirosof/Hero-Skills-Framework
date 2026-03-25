---
type: checkpoint
---

# Step 11 — Final Approval (Checkpoint)

## Context Loading

- `squads/rubimfx-content/output/review.md` — scores e feedback da revisão (Step 10)
- `squads/rubimfx-content/output/carousel-visuals.md` — carrossel visual final (HTML)
- `squads/rubimfx-content/output/carousel-draft.md` — texto do carrossel
- `squads/rubimfx-content/output/caption.md` — legenda e hashtags

## Instructions

Este checkpoint final apresenta o carrossel completo com os resultados da revisão para aprovação definitiva do usuário antes da publicação.

### Processo

1. **Apresentar score da revisão** — Mostrar o resultado do Step 10 de forma resumida:
   > **Review Score: X/10 — [Classificação]**
   > Precisão: X/10 | Tom: X/10 | Visual: X/10 | Compliance: X/10

2. **Destacar issues encontradas** — Se houver issues críticas ou importantes, listar de forma clara:
   - Issues críticas em destaque (devem ser resolvidas)
   - Issues importantes como recomendação
   - Issues menores como sugestão

3. **Apresentar conteúdo final** — Mostrar resumo do carrossel:
   - Slides em formato compacto (número + tipo + hook/dado principal)
   - Legenda completa
   - Hashtags
   - Indicação de que o HTML visual está pronto para renderização

4. **Informar próximos passos pós-aprovação** — Explicar o que acontece depois:
   > Após aprovação:
   > 1. HTML dos slides será renderizado em imagens 1080x1350px
   > 2. Legenda e hashtags ficam prontos para copiar
   > 3. Conteúdo será arquivado no output da squad

5. **Solicitar decisão final** — Perguntar:
   > "Conteúdo final aprovado para publicação?"

   Opções:
   - **"Aprovado"** — carrossel é marcado como FINAL e está pronto para publicação
   - **"Corrigir [issue]"** — aplicar correção específica e reapresentar
   - **"Revisar slides"** — volta ao Step 06 para reescrever mantendo o ângulo
   - **"Revisar visual"** — volta ao Step 09 para refazer o design
   - **"Recomeçar"** — volta ao Step 01 para novo tema

6. **Processar correções** — Se o usuário pedir correções:
   - Aplicar as mudanças solicitadas
   - Re-executar apenas as partes afetadas (texto ou visual)
   - Reapresentar para nova aprovação
   - Não voltar para o Step 10 inteiro para correções menores

7. **Registrar aprovação final** — Quando aprovado:
   - Marcar todos os outputs como `## Status: FINAL`
   - Registrar timestamp de aprovação
   - Confirmar que o conteúdo está pronto para publicação

## Output Format

```
## Aprovação Final

### Review Score: X/10 — [Classificação]
| Precisão | Tom | Visual | Compliance |
|----------|-----|--------|------------|
| X/10     | X/10| X/10   | X/10       |

### Issues
[lista de issues se houver, ou "Nenhuma issue crítica"]

### Carrossel ([N] slides)
1. (Capa) "[hook]"
2. (Contexto) [resumo]
[...]
N. (CTA) "[CTA]"

### Legenda
[legenda completa]

### Hashtags ([contagem])
[hashtags]

---

Conteúdo final aprovado para publicação?
- "Aprovado" → pronto para publicar
- "Corrigir [issue]" → aplica correção
- "Revisar slides" → reescreve carrossel
- "Revisar visual" → refaz design
- "Recomeçar" → novo tema
```

## Output Example

```
## Aprovação Final

### Review Score: 8.6/10 — Bom
| Precisão | Tom | Visual | Compliance |
|----------|-----|--------|------------|
| 9/10     | 8/10| 8/10   | 9/10       |

### Issues
**Importantes (recomendado corrigir):**
- Slide 7: reformular "alvo $2.450" para "resistência em $2.450" (compliance)
- Slide 6: confirmar dado "primeira vez em 2 meses" para DXY < 104

**Menores (opcional):**
- Legenda: considerar frase em primeira pessoa
- Slide 5: fluxo visual macro→trading pode melhorar

### Carrossel (8 slides)
1. (Capa) "O Fed falou. O ouro ouviu."
2. (Contexto) Juros mantidos em 5.25-5.50%, dot plot muda
3. (Dados) Dot plot: maioria projeta corte em junho
4. (Dados) Ouro +2.3%, ATH em $2.385, ETFs +$1.2bi
5. (Bridge) Juros caem → Dólar enfraquece → Ouro sobe
6. (Dados) DXY perde 104.00
7. (Prático) Setups: ouro $2.350 suporte, EUR/USD > 1.0900
8. (CTA) Ouro ou dólar? Comenta e salva

### Legenda
O Fed manteve os juros. Nenhuma surpresa.

Mas o dot plot contou uma história diferente: a maioria dos membros já projeta corte em junho.

O ouro não esperou confirmação. Subiu 2.3% e renovou máxima histórica em $2.385.

O dólar perdeu o suporte de 104 que segurava há 2 meses.

Resumo rápido: o macro está falando. Quem opera precisa ouvir.

Passa os slides para entender o que mudou, por que o ouro reagiu assim e como isso pode impactar suas operações.

.
.
.

Comenta aqui: você está mais de olho no ouro ou no dólar essa semana?

Se esse conteúdo te ajudou a entender o cenário, salva e manda pra aquele amigo que opera sem olhar pro macro.

### Hashtags (14)
#forex #trading #mercadofinanceiro #investimentos #forextrader #daytrade #ouro #macroeconomia #fomc #federalreserve #xauusd #proptrading #rubimfx #tradingbrasil

---

Conteúdo final aprovado para publicação?
- "Aprovado" → pronto para publicar
- "Corrigir [issue]" → aplica correção
- "Revisar slides" → reescreve carrossel
- "Revisar visual" → refaz design
- "Recomeçar" → novo tema
```

## Veto Conditions

- **Issues críticas não resolvidas** — Se o Step 10 identificou issues críticas (erro factual, violação de compliance), alertar o usuário explicitamente antes de permitir aprovação. Perguntar: "Há issues críticas pendentes. Deseja corrigir antes de aprovar?"
- **Aprovação sem visualização** — O usuário deve ter visto o conteúdo completo (slides + legenda + hashtags) antes de aprovar. Não aceitar "aprovado" se o conteúdo não foi apresentado nesta sessão.

## Quality Criteria

- O score da revisão deve estar visível no topo da apresentação
- Issues devem estar claramente categorizadas por prioridade
- O carrossel resumido deve ser escanável em menos de 30 segundos
- A legenda deve ser apresentada completa (não resumida)
- As opções de decisão devem indicar claramente para onde cada escolha redireciona no pipeline
