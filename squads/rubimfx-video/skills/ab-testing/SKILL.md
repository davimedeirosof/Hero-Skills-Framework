---
name: A/B Testing
description: Framework de testes A/B para hooks, thumbnails e horários de publicação
category: optimization
---

# A/B Testing — Framework de Testes

## Objetivo
Testar sistematicamente variações de hooks, thumbnails e horários de publicação para descobrir o que funciona melhor para o @rubimfx, usando dados reais em vez de suposições.

## Tipos de Teste

### 1. Teste de Hook (A vs B)
Mesmo conteúdo, hooks diferentes.

**Como fazer:**
- Criar 2 versões do mesmo vídeo, mudando APENAS o hook (primeiros 3 segundos)
- Publicar Hook A e Hook B em dias diferentes (mesmo horário, mesmo dia da semana se possível)
- Medir após 48 horas

**Métricas de comparação:**
| Métrica | Peso | Por quê |
|---------|------|---------|
| Completion Rate | 3x | Hook bom = pessoa assiste até o fim |
| Views (após 48h) | 2x | Alcance orgânico |
| Saves | 2x | Valor percebido |
| Shares | 1x | Viralidade |

**Template de registro:**
```
TESTE DE HOOK #[N]
Data: [data]
Conteúdo: [tema do vídeo]

Hook A: "[texto do hook A]"
  Categoria: [Loss Aversion / Curiosity Gap / etc.]
  Views: [X]
  Completion: [X%]
  Saves: [X]
  Shares: [X]
  Score: [calculado]

Hook B: "[texto do hook B]"
  Categoria: [Loss Aversion / Curiosity Gap / etc.]
  Views: [X]
  Completion: [X%]
  Saves: [X]
  Shares: [X]
  Score: [calculado]

VENCEDOR: Hook [A/B]
MOTIVO: [análise de por quê]
APRENDIZADO: [o que aplicar nos próximos vídeos]
```

### 2. Teste de Thumbnail
Mesma thumbnail, textos diferentes (ou sem texto vs com texto).

**Variações comuns:**
- Texto grande vs sem texto
- Face focada vs ação/gráfico
- Cor quente vs cor fria
- Pergunta vs afirmação

**Como fazer:**
- Publicar o Reel com Thumbnail A
- Após 24h, trocar para Thumbnail B (Instagram permite editar capa)
- Comparar métricas de impressão → clique

### 3. Teste de Horário
Mesmo tipo de conteúdo em horários diferentes.

**Faixas para testar:**
- 7h vs 12h (manhã vs almoço)
- 12h vs 20h (almoço vs noite)
- Dia de semana vs fim de semana

**Regra:** Mínimo 3 vídeos em cada horário antes de concluir.

### 4. Teste de Formato
Mesmo tema, formatos diferentes.

**Exemplo:**
- Tema: "Erro mais comum em prop firm"
- Formato A: Revelation Hook (clone falando)
- Formato B: Ranking/List (texto na tela + voz)

## Significância Estatística

### Regras para Validação
1. **Mínimo de impressões:** 1.000+ impressões para cada variante
2. **Mínimo de amostras:** 3 testes do mesmo tipo antes de concluir padrão
3. **Diferença mínima:** Variação de 20%+ entre A e B para considerar significativo
4. **Fatores externos:** Descartar testes feitos em dias atípicos (feriados, breaking news)

### Quando NÃO confiar no resultado
- Menos de 500 views em uma das variantes
- Teste feito em dia de evento econômico grande (NFP, FOMC) vs dia normal
- Uma variante postada em horário de pico e outra fora
- Amostra de apenas 1 teste (precisa de pelo menos 3)

## Documentação de Resultados

### Banco de Vencedores
Manter registro atualizado em `_memory/ab-tests/`:

```
=== HOOKS VENCEDORES ===
1. Loss Aversion > Curiosity Gap (para conteúdo educacional) — 3 testes, +35% completion
2. Pergunta > Afirmação (para mindset) — 2 testes, +28% comments
3. ...

=== THUMBNAILS VENCEDORAS ===
1. Face + texto grande > apenas gráfico — 4 testes, +42% CTR
2. ...

=== HORÁRIOS VENCEDORES ===
1. 7h > 20h para News + Analysis — 3 testes, +25% views
2. 12h > 7h para educacional — 3 testes, +18% saves
3. ...
```

## Cadência de Testes

- **Semana 1-2:** Testar hooks (Loss Aversion vs Curiosity Gap)
- **Semana 3-4:** Testar horários (manhã vs noite)
- **Semana 5-6:** Testar thumbnails (texto vs sem texto)
- **Semana 7-8:** Testar formatos (clone vs texto na tela)
- **Depois:** Repetir ciclo com novas variações

## Regras

1. NUNCA testar mais de 1 variável por vez (muda hook = mantém tudo igual)
2. Documentar TODOS os testes, mesmo os inconclusivos
3. Compartilhar resultados com Ana Analytics para análise cruzada
4. Aplicar vencedores imediatamente no próximo vídeo
5. Re-testar vencedores a cada 2 meses (tendências mudam)
