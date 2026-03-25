# Toolkit do Squad de Carrosséis @rubimfx

## Scripts Disponíveis

### 1. Busca de Imagens
```bash
cd squads/rubimfx-content
python3 scripts/fetch_images.py search "federal reserve juros"
python3 scripts/fetch_images.py search "economia brasil inflação"
python3 scripts/fetch_images.py download "https://url-da-imagem.jpg" "capa.jpg"
python3 scripts/fetch_images.py list
python3 scripts/fetch_images.py topics  # ver temas mapeados
```

**Configuração necessária:**
```bash
export UNSPLASH_ACCESS_KEY=sua_chave   # https://unsplash.com/developers
export PEXELS_API_KEY=sua_chave        # https://www.pexels.com/api/
```

**Temas mapeados:** economia, fed, dolar, ouro, brasil, mercado, petroleo, crypto, eleicoes, inflacao, guerra, china, tecnologia, trump, juros

### 2. Gerador de Slides
```bash
python3 scripts/generate_slide.py  # gera 6 slides de teste
```

**Tipos de slide disponíveis:**
- `generate_cover()` — Capa com foto + overlay
- `generate_context()` — Contexto/explicação com highlight
- `generate_data()` — Dado estatístico com número grande
- `generate_comparison()` — Comparativo lado a lado
- `generate_bridge()` — Setup operacional macro→trading
- `generate_cta()` — Call to action final

### 3. Renderizador PNG
```bash
python3 scripts/render_slides.py              # renderiza test-*.html
python3 scripts/render_slides.py "slide-*.html"  # renderiza slides específicos
```

**Output:** PNGs 1080x1440px em `output/slides/png/`

## Fluxo Completo de Produção

```
1. Pesquisar notícia do dia (web_search)
2. Buscar imagens relevantes (fetch_images.py)
3. Gerar slides HTML (generate_slide.py)  
4. Renderizar para PNG (render_slides.py)
5. Revisar qualidade visual
6. Publicar no Instagram
```

## Onde Buscar Fotos (Referência @economesteter)

### Fontes Gratuitas:
- **Unsplash** (unsplash.com) — Fotos editoriais alta qualidade
- **Pexels** (pexels.com) — Alternativa ao Unsplash
- **Pixabay** (pixabay.com) — Sem atribuição necessária

### Fontes de Dados/Gráficos:
- **TradingView** — Screenshots de gráficos (com overlay)
- **Trading Economics** — Dados macro globais
- **IBGE/BCB** — Dados Brasil oficiais
- **Bloomberg/Reuters** — Manchetes + fotos jornalísticas

### Como @economesteter faz:
1. **Capa**: Foto jornalística (agências) + overlay escuro 70% + título bold
2. **Slides internos**: Print de tweet/thread no X (dark mode) com dados
3. **Dados**: Screenshots de matérias originais + cards com números
4. **Gráficos**: TradingView customizado ou gráficos simplificados
5. **Fotos**: Reuters, AFP, Getty (via Google Images com uso editorial)

### Dica prática para foto da capa:
```bash
# Buscar no Google Images e baixar
python3 scripts/fetch_images.py search "jerome powell federal reserve"
# Ou baixar direto de URL
python3 scripts/fetch_images.py download "https://url-foto.jpg" "capa-powell.jpg"
```

## Melhorias Identificadas (Roadmap)

### Prioridade Alta:
- [ ] Ocupar melhor o espaço vertical dos slides
- [ ] Adicionar mini-gráficos/sparklines nos slides de dados
- [ ] Pictogramas (ícones pessoas) para dados percentuais
- [ ] Texturas/gradientes sutis no background

### Prioridade Média:
- [ ] Integração automática com TradingView para gráficos
- [ ] Template de "tweet card" estilo X/Twitter dark mode
- [ ] Sistema de temas por editoria (macro, trading, brasil, crypto)
- [ ] Auto-resize de texto baseado em comprimento

### Prioridade Baixa:
- [ ] Publicação automática via Instagram API
- [ ] A/B testing de capas
- [ ] Analytics de performance por tipo de slide
