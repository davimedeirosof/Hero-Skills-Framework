# rubimfx-video — Squad de Producao de Videos com Clone IA

Squad para producao automatizada de videos curtos (Reels/TikTok) usando clone de voz e imagem.

## Pipeline Principal: Foto Clone → Video Falando

```
Fotos Reais (18 refs) → Nano Banana (foto clone) → ElevenLabs (audio) → HeyGen/Hedra (animacao) → Video Final
```

### Por que este pipeline?
- **64% mais barato** que avatar direto ($70/mes vs $194/mes)
- **Cenarios infinitos** — muda roupa, fundo, iluminacao via prompt
- **Sem gravacao** — usa fotos de referencia existentes
- **Controle total** — clone_image.py ja calibrado com Identity Header

## Stack Tecnologica
| Ferramenta | Funcao | Custo |
|---|---|---|
| Nano Banana Pro 2 | Foto clone (via clone_image.py) | ~R$0.35/foto |
| HeyGen Avatar IV | Animacao foto → video (lip sync) | $24/mes |
| Hedra Character-3 | Animacao emocional (alternativa) | $10-15/mes |
| OmniHuman | Animacao premium full-body | Pay-per-use |
| ElevenLabs | Clone de voz PT-BR | $22/mes |
| Submagic Pro | Legendas animadas | $23/mes |
| Pexels API | B-roll gratis | $0 |
| Playwright MCP | Publicacao | $0 |

### Custo Total Estimado
- **Com HeyGen Creator:** ~$70/mes (~R$350) para 20 videos
- **Com Hedra:** ~$56/mes (~R$280) para 20 videos
- **Custo por video:** ~R$1-2

## Agentes
- **Rex Roteirista** — Cria roteiros virais (10 formatos)
- **Hugo HeyGen** — Pipeline foto clone → animacao video (Nano Banana + HeyGen/Hedra/OmniHuman)
- **Elia ElevenLabs** — Clona a voz em PT-BR
- **Sam Submagic** — Legendas e edicao
- **Bea B-Roll** — Curadoria de videos/imagens de apoio
- **Pablo Publisher** — Publicacao Instagram + TikTok
- **Tina Trend** — Pesquisa tendencias virais
- **Cal Calendar** — Calendario editorial
- **Ana Analytics** — Metricas e otimizacao
- **Rip Repurpose** — Reaproveitamento de conteudo

## Skills Novas (v3.0)
- **Photo to Video** — Pipeline completo Nano Banana → HeyGen/Hedra
- **Nano Banana Video Prompts** — 10 cenarios pre-definidos otimizados para animacao

## Como Usar
```bash
/opensquad run rubimfx-video
```

## Formatos de Video
1. Clip Drop (corte de mentoria)
2. Revelation Hook (declaracao contraria)
3. Chart Explanation (tela + voiceover)
4. Proof Reel (resultado prop firm)
5. 3-Second Rule (insight ultra-curto)
6. News + Analysis (macro do dia)
7. Mindset Confession (storytelling)
8. Before/After Trade (replay)
9. Ranking/List (top 3/5)
10. Student Result (prova social)

## Quando Usar Cada Ferramenta de Animacao
| Tipo de conteudo | Ferramenta | Por que |
|---|---|---|
| Noticias / macro | HeyGen | Resolucao alta, tom neutro |
| Mindset / confissao | Hedra | Melhor expressao emocional |
| Conteudo premium | OmniHuman | Full-body, cinema quality |
| Teste / prototipo | Hedra free | Validar antes de investir |
