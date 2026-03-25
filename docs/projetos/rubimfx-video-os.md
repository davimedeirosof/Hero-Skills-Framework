# rubimfx-video — Squad de Vídeos Curtos

**Squad:** `rubimfx-video`
**Plataformas:** Instagram Reels (principal) + TikTok (secundária)
**Formato:** 9:16 vertical, 1080x1920px, 15-60 segundos
**Custo mensal:** ~R$350/mês (64% mais barato que avatar direto)

---

## Pipeline de produção (14 etapas)

```
PLANEJAMENTO
  1. Weekly Calendar (Cal)     → Plano 5-6 Reels semanais       ← checkpoint
  2. Trend Research (Tina)     → Formatos virais da semana

PRÉ-PRODUÇÃO
  3. Script Writing (Rex)      → Roteiro com hook + estrutura    ← checkpoint
  4. A/B Hook Test             → 2 variações de hook

PRODUÇÃO
  5. Voice Generation (Elia)   → Áudio via clone de voz
  6. B-Roll Curation (Bea)     → Materiais visuais de apoio
  7. Video Generation (Hugo)   → Vídeo com clone facial

PÓS-PRODUÇÃO
  8. Clone Validation          → Score mínimo 8/10
  9. Post Processing           → Upscale e correções
 10. Caption & Edit (Sam)      → Legendas animadas
 11. Thumbnail Generation      → Capas
 12. CTA Selection             → Call-to-action otimizado
 13. Quality Gate              → Validação final              ← checkpoint

DISTRIBUIÇÃO
 14. Publish (Pablo)           → Instagram Reels + TikTok
 15. Analytics (Ana)           → Métricas após 48h
```

---

## 10 Agentes do squad

### Rex Roteirista
Cria roteiros virais para trading/finanças. Estrutura universal: **Hook (0-3s) → Conteúdo (3-45s) → CTA (últimos 5-10s)**.
Regra crítica: hook deve aparecer como **TEXTO NA TELA + ser FALADO** ao mesmo tempo.

**10 formatos de vídeo:**

| Formato | Duração | Descrição |
|---------|---------|-----------|
| Clip Drop | 20-45s | Excerpt de mentoria com insight poderoso |
| Revelation Hook | 25-40s | Afirmação contrária + 3 pontos de suporte |
| Chart Explanation | 30-60s | Screen recording com narração de setup |
| Proof Reel | 15-30s | Resultados/pagamentos de prop firm |
| 3-Second Rule | 12-20s | Um conceito, texto mínimo |
| News + Analysis | 30-55s | Macro → conexão trading |
| Mindset Confession | 30-60s | Storytelling de erro real |
| Before/After Trade | 20-40s | Setup previsto vs. resultado |
| Ranking/List | 20-35s | Conteúdo numerado em ritmo acelerado |
| Student Result | 30-55s | Mini-documentário de aluno |

**Tipos de hook:** Loss Aversion, Curiosity Gap, Contrarian, Social Proof, Timeliness

---

### Hugo HeyGen
Gera o vídeo com clone facial em 3 etapas:

**1. Fotos via Nano Banana Pro 2** (`clone_image.py`)
- Rosto FRONTAL olhando direto para câmera
- Olhos totalmente visíveis e abertos
- Boca neutra ou levemente aberta
- Sem mãos cobrindo o rosto
- Fundo simples ou desfocado
- Iluminação uniforme, mín. 1080px largura

**2. Animação** (escolher conforme tipo):
| Ferramenta | Uso | Resolução | Custo |
|-----------|-----|-----------|-------|
| HeyGen Avatar IV | News/informacional | até 1280p | $24/mês |
| Hedra Character-3 | Storytelling emocional | 720p (upscalável) | $10-15/mês |
| OmniHuman API | Premium full-body, cinema | até 1080p | pay-per-use |

**3. Validação** (obrigatória antes de aprovar):
lip-sync alinhado, expressões naturais, sem artefatos, fundo estável, 1080p mín., sem watermarks, textura de pele natural.

**Custo por vídeo:** ~R$1-2 (com assinaturas mensais incluídas)

---

### Elia ElevenLabs
Clona a voz do Gabriel para narração.

- **Principal:** ElevenLabs Creator ($22/mês)
- **Alternativa:** Fish Audio Plus ($11/mês) — testar ambas
- **Setup:** 5-7 min de áudio em tom natural de mentoria (setup, análise gráfica, ensino)
- **Exportação:** 192kbps mínimo → entrega para HeyGen

Termos que o clone deve pronunciar corretamente:
Smart Money Concepts, FVG, Order Block, Displacement, Liquidity Sweep, Inducement, FOMC, NFP, CPI, Selic, stop loss, take profit, RR

---

### Bea B-Roll
Curadora de materiais visuais de apoio.

**Fontes (por prioridade):**
1. Pexels API (grátis) — trading/finance/tech
2. Screenshots de notícias reais via Firecrawl
3. Screen recordings de TradingView e MT5
4. Imagens IA via Nano Banana
5. Fotos pessoais via `clone_image.py`

**Categorias visuais:** monitores de trading, gestos de mão, distritos financeiros, moedas, headlines de notícias, animações de candlestick

---

### Sam Submagic
Legendas animadas e edição de vídeo.

- **Ferramenta:** Submagic Pro ($23/mês) — alternativas: CapCut, Captions.ai
- **Especificações:** 9:16, 1080x1920px, PT-BR com acentos, fonte mínima 48px
- **Estilos:** Bold Highlight, Karaoke sync, Minimal text
- **Posição:** centro-inferior (não cobrir o rosto)
- **Destaque:** palavras-chave em negrito ou cor contrastante
- **Termos em inglês:** manter ICT, FVG, stop loss no original
- **Contraste:** texto branco com outline preto ou highlight amarelo
- **Workflow:** Recebe vídeo do Hugo → Submagic → auto-detect PT → estilo trending → corrige terminologia técnica → exporta vertical

---

### Pablo Publisher
Publicação em Instagram Reels e TikTok.

**Horários otimizados:**
| Dia | Horário BRT |
|-----|-------------|
| Segunda | 6h-9h |
| Terça | 6h-9h |
| Quarta | 8h-11h |
| Quinta | 7h-10h |
| Sexta | 12h-14h |
| Evento macro | 30-90min após o evento |

**Frequência:** mínimo 4 Reels/semana, ideal 5-6, máximo 1/dia

**Mix semanal:** 3 educacionais (charts/conceitos) + 1 mentalidade + 1 resultados + 1 notícias

**Estrutura de legenda:**
- Captions educacionais: insight principal + 2-3 pontos expandidos + CTA + hashtags
- Captions narrativos: elemento emocional + contexto + engajamento direto

**Hashtags:** 1 marca (#RubimFX) + 2 nicho + 1-2 descoberta = 4-5 total

---

### Tina Trend
Caçadora de tendências virais semanais.

- Monitora Instagram Reels Explore, TikTok Creative Center
- Analisa concorrentes: @smcandict, @tradingcoachind
- Entrega 3-5 tendências/semana para Rex adaptar

**Metas de performance:**
- Completion rate > 80%
- Save rate > 5%
- Share rate > 3%
- Comment rate > 2%

---

### Cal Calendar
Planejamento editorial semanal (5-6 Reels).

**Distribuição por pilar:**
| Pilar | % | Vídeos/semana |
|-------|---|---------------|
| Macro/News | 40% | 2-3 |
| Educação ICT | 25% | 1-2 |
| Trade Analysis | 15% | 1 |
| Prop Firm | 10% | 0-1 |
| Mindset | 10% | 0-1 |

**Regras:** não repetir formatos em dias consecutivos, não repetir hooks em sequência, alternar "pesado" e "leve", máx. 2 vídeos do mesmo pilar seguidos.

Integra calendário econômico: NFP, FOMC, CPI, Copom, CAGED (padrão pré/durante/pós-evento).

---

### Ana Analytics
Performance tracker — relatório toda segunda-feira.

**Métricas primárias (48h após publicação):**
visualizações, salvamentos, compartilhamentos, comentários, taxa de conclusão, crescimento de seguidores

**Segmentações:**
- Por faixa horária: 6-8h, 11-13h, 17-19h, 20-22h, fins de semana
- Por tipo de hook: Loss Aversion, Curiosity Gap, Contrarian, Social Proof, Timeliness, Question

**Relatório semanal:** top 3 vídeos (análise causal) + pior desempenho + tendências + 3 ações específicas

**Regra crítica:** NUNCA tirar conclusão com menos de 5 vídeos de um formato.

---

### Rip Repurpose
Transforma conteúdo longo (mentorias, lives, webinars) em 5-10 vídeos curtos.

**Tags de identificação em transcrições:**
`[INSIGHT]` `[EMOTION]` `[POLÊMICA]` `[RESULTADO]` `[HISTÓRIA]` `[DICA_PRÁTICA]` `[FRASE_FORTE]`

**Scoring de clips:**
| Critério | Peso |
|----------|------|
| Hook Power | 3x |
| Valor standalone | 2x |
| Impacto emocional | 2x |
| Compartilhabilidade | 2x |
| Unicidade | 1x |

**Saída:** relatório priorizado — alto (>7/10), médio (5-7), baixo (<5) + sugestões de calendário

**Restrições:** 15-60s (ideal 25-40s), funcionar sem contexto externo, áudio limpo, sem conteúdo de área paga.

---

## Stack completa e custos

| Ferramenta | Uso | Custo |
|-----------|-----|-------|
| Nano Banana Pro 2 | Clone fotográfico | ~R$0,35/foto |
| HeyGen Avatar IV | Animação facial | $24/mês |
| Hedra Character-3 | Animação alternativa | $10-15/mês |
| ElevenLabs Creator | Clone de voz principal | $22/mês |
| Fish Audio Plus | Clone de voz alternativo | $11/mês |
| Submagic Pro | Legendas animadas | $23/mês |
| Pexels API | B-roll (grátis) | $0 |
| Firecrawl | Screenshots editoriais | variável |

**Total estimado:** ~R$350/mês para 20 vídeos
