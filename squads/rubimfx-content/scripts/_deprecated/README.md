# Scripts Deprecados

Estes scripts foram movidos para ca porque estao obsoletos e **nao devem ser usados**.

## generate_slide.py
- Gera slides com dimensao errada (1080x1440 em vez de 1080x1350)
- Usa Google Fonts via URL externa (CDN) nos HTMLs, o que causa falha no render offline
- Substituido pelo sistema de templates em `templates/` + slides escritos diretamente em HTML

## fetch_images.py
- Busca imagens via Unsplash/Pexels APIs (URLs externas)
- URLs externas sao proibidas nos slides (check 10 do preflight_check.py)
- Imagens devem ser locais, copiadas para a pasta html/ do post
