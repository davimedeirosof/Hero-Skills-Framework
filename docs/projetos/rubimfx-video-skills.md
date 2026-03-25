# rubimfx-video — Skills do Squad

Skills em `squads/rubimfx-video/skills/`. Todas específicas para produção de vídeo com clone de IA.

---

## Lista de skills (13 total)

| Skill | Categoria | Função |
|-------|-----------|--------|
| `ab-testing` | optimization | Testes A/B de hooks, thumbnails e horários |
| `clone-validator` | quality-assurance | Checklist de validação frame-a-frame do clone |
| `cta-optimizer` | engagement | Seleção de CTAs por objetivo e tipo de conteúdo |
| `lip-sync-fix` | video-production | Correção de lip sync com MuseTalk e Wav2Lip |
| `nano-banana-video-prompts` | ai-generation | Prompts otimizados para fotos que animam bem |
| `photo-to-video` | video-production | Pipeline completo foto clone → vídeo falando |
| `post-processing` | video-production | Pós-processamento para melhorar qualidade |
| `prompt-engineering-video` | ai-generation | Prompts de cenários e backgrounds via IA |
| `quality-gate` | quality-assurance | Checklist visual + lip sync antes de publicar |
| `recording-guide` | video-production | Guia de gravação para clone facial IA |
| `thumbnail-generator` | design | Capas otimizadas para Reels e TikTok |
| `trending-sounds` | audio | Seleção de trilha sonora por tipo de conteúdo |
| `voice-training` | voice-production | Guia de gravação de áudio para clone de voz |

---

## ab-testing

Framework de testes A/B para hooks, thumbnails e horários de publicação.

### Tipos de teste

**Teste de Hook (A vs B)**
- Mesmo conteúdo, hooks diferentes nos primeiros 3 segundos
- Publicar em dias diferentes, mesmo horário e dia da semana
- Medir após 48h

**Métricas por peso:**
| Métrica | Peso |
|---------|------|
| Completion Rate | 3x |
| Views (48h) | 2x |
| Saves | 2x |
| Shares | 1x |

---

## clone-validator

Checklist e workflow de validação de qualidade do clone. **Score mínimo 8/10** para aprovação.

### Workflow frame-a-frame
1. Abrir vídeo no VLC (tecla "E" para avanço frame-a-frame)
2. Ter vídeo real recente do Gabriel como referência lado a lado
3. Reproduzir em 0.5x para análise de lip sync
4. Usar tela grande (não celular)

### Checklist visual
- [ ] Piscadas irregulares (não rítmicas/robóticas)
- [ ] Micro-movimentos dos olhos entre piscadas
- [ ] Boca + bochechas + queixo + sobrancelha coordenados
- [ ] Cabeça com movimento sutil e natural (não estática)
- [ ] Pele com textura visível (poros, linhas) — não plástica
- [ ] Perfil do rosto estável quando vira
- [ ] Borda do cabelo natural (não hard-edge)
- [ ] Iluminação consistente
- [ ] Fundo estável sem flicker

### Comparação de tom de pele
1. Capturar frame do clone e frame do vídeo real com iluminação similar
2. Comparar histograma RGB da região do rosto no Photoshop/GIMP
- Aprovado: diferença < 10% no histograma
- Reprovado: diferença > 15%

---

## cta-optimizer

Seleção de CTAs por objetivo e tipo de conteúdo.

### Regra de ouro
**NUNCA usar "Curte e segue"** — CTAs específicos e contextuais performam 3-5x melhor.

### CTAs por objetivo

**SAVE — conteúdo educacional de alto valor**
- "Salva esse vídeo antes de operar amanhã"
- "Salva pra revisar antes do pregão"
- "Salva esse setup — ele aparece toda semana"
- "Guarda esse vídeo, você vai precisar dele"
- "Salva e assiste de novo com calma"

Formatos ideais: Chart Explanation, 3-Second Rule, Ranking/List, Revelation Hook

**COMMENT — interação e comunidade**
- Pergunta específica do nicho

**SHARE — viralidade**
- Conteúdo polêmico, surpreendente ou de utilidade universal

**FOLLOW — crescimento**
- Prometer conteúdo futuro específico

---

## lip-sync-fix

Correção de lip sync usando MuseTalk e Wav2Lip para fonemas PT-BR.

### Quando usar
- Lip sync falhou em fonemas específicos
- Consoantes duras (p, b, m) não fecham a boca
- Nasais PT-BR (ã, em) com formato errado
- Dessincronização áudio-vídeo > 3 frames

### MuseTalk (Recomendado)
- GitHub: github.com/TMElyralab/MuseTalk
- Baseado em difusão (Tencent)
- 30+ FPS em GPU
- Resolução: 256x256 na face (depois upscale)
- Melhor que Wav2Lip para: dentes, bordas, consistência

### Wav2Lip (Alternativa)
- Mais simples de configurar
- Menor resolução (96x96 face)
- Usar quando MuseTalk não estiver disponível

### Workflow
1. Identificar trecho com lip sync ruim
2. Extrair áudio do trecho
3. Aplicar MuseTalk/Wav2Lip ao segmento
4. Reintegrar ao vídeo original

---

## nano-banana-video-prompts

Prompts otimizados para gerar fotos de clone que animam bem em vídeo.

### Regras universais (aplicar em TODOS os prompts)
1. **DIRECTLY at the camera** — olhar frontal
2. **mouth slightly parted** ou **neutral relaxed position** — facilita lip sync
3. **eyes open and visible** — sem óculos escuros, sem olhos fechados
4. **no hands near face** — mãos fora do frame do rosto
5. **simple or blurred background** — menos artefatos na animação
6. **uniform lighting on face** — sem sombras pesadas
7. **VERTICAL 9:16** — formato Reels/TikTok
8. **face centered in upper third** — composição ideal
9. **Natural skin texture, visible pores** — anti-AI realismo
10. **head and shoulders framing** — enquadramento ideal para lip sync

### 10 cenários pré-definidos

| Cenário | Uso |
|---------|-----|
| `trading-desk-video` | News/informacional |
| `dark-studio` | Padrão, neutro |
| `business-casual` | Autoridade |
| `outdoor-natural` | Storytelling casual |
| `white-background` | Minimalista/profissional |
| `conference-room` | Educacional formal |
| `home-office` | Conteúdo pessoal/mindset |
| `street-urban` | Conteúdo jovem/dinâmico |
| `prop-firm-results` | Prova social |
| `close-up-emotional` | Storytelling emocional |

### Template de prompt base
```
Gabriel sitting at [SETTING], looking DIRECTLY at the camera
with a confident engaged expression, mouth slightly parted as if about to speak.
Natural skin texture, visible pores. No hands near face. Simple blurred background.
Uniform lighting on face. Vertical 9:16 format. Head and shoulders framing.
```

---

## photo-to-video

Pipeline completo para transformar foto clone IA em vídeo falando.

### Pipeline
```
FOTOS REAIS (refs em assets/)
        ↓
NANO BANANA PRO 2 (clone_image.py)
  → Foto clone em cenário profissional
  → Formato: vertical 9:16 (1080x1920)
        ↓
ELEVENLABS / FISH AUDIO
  → Áudio com clone de voz PT-BR
  → Formato: WAV 48kHz ou MP3 192kbps+
        ↓
HEYGEN / HEDRA / OMNIHUMAN
  → Animação da foto com o áudio
  → Lip sync automático
  → Saída: MP4 720-1280p
        ↓
PÓS-PROCESSAMENTO (se necessário)
  → Upscale (Topaz)
  → Skin texture fix
```

### Escolha de ferramenta de animação
| Ferramenta | Uso |
|-----------|-----|
| HeyGen Avatar IV | Uso diário, noticiário |
| Hedra Character-3 | Conteúdo emocional |
| OmniHuman (Replicate) | Máxima qualidade |

---

## post-processing

Pipeline de pós-processamento para melhorar qualidade do clone.

### Sequência de operações (NESTA ORDEM)
1. Gerar vídeo no HeyGen/Hedra
2. Exportar na máxima resolução/bitrate
3. Skin texture enhancement (se pele plástica)
4. Eye contact correction (se olhar desalinhado)
5. Upscale com Topaz Video AI (2x ou 4K)
6. Temporal denoising (eliminar flicker)
7. Color grade (match com estética real do Gabriel)
8. Reconectar áudio se processado separado
9. Exportar H.264/H.265 a 20-30Mbps para 1080p

### Ferramentas

**Upscaling**
- Topaz Video AI ($300/ano) — melhor qualidade
  - Modelo Proteus: uso geral
  - Modelo Gaia: qualidade máxima
  - Anti-flicker forte na região do rosto

**Skin Texture**
- Claid.ai — restaura poros e textura
- LetsEnhance Prime — adiciona detalhe sem drift

---

## prompt-engineering-video

Engenharia de prompts para gerar cenários e backgrounds de clone via IA.

### Estrutura do prompt para background
```
[STYLE] + [SETTING] + [LIGHTING] + [CAMERA] + [MOOD] + [ASPECT RATIO]
```

### Cenários pré-aprovados

**Trading Desk**
```
Professional modern trading desk setup with 3 ultrawide monitors showing
candlestick charts and market data, dark room illuminated by screen glow
and subtle blue neon ambient. Clean minimalist desk. Shot at eye level.
Cinematic, professional, 9:16 vertical.
```

**Dark Studio (Padrão)**
```
Clean professional dark studio background, subtle gradient from dark gray
to black, minimal ambient lighting. Shot at eye level, 9:16 vertical.
```

---

## quality-gate

Checklist de validação antes de publicar. **Score mínimo 8/10.**

### Visual
- [ ] Piscadas irregulares (não rítmicas/robóticas)
- [ ] Micro-movimentos dos olhos entre piscadas
- [ ] Boca + bochechas + queixo + sobrancelha coordenados
- [ ] Cabeça com movimento sutil e natural
- [ ] Pele com textura visível (poros, linhas) — não plástica
- [ ] Perfil do rosto estável quando vira
- [ ] Borda do cabelo natural
- [ ] Iluminação consistente
- [ ] Fundo estável sem flicker/pulso

### Lip Sync (reproduzir em 0.5x)
- [ ] Consoantes duras (p, b, m): boca fecha totalmente no frame certo
- [ ] Vogais abertas (a, e, o): abertura proporcional
- [ ] Sibilantes (s, z, ch): posição de lábios/dentes correta
- [ ] Nasais PT-BR (ã, em, im): formato diferente de vogais puras
- [ ] Sync áudio-vídeo: máx 3 frames de diferença
- [ ] Boca parada quando não há fala

### Voz
- [ ] Ritmo natural de PT-BR
- [ ] Respiração em pausas naturais (não meio de frase)
- [ ] Terminologia técnica pronunciada corretamente (FVG, SMC, Order Block)
- [ ] Velocidade adequada (130-150 palavras/min)

### Formato
- [ ] 9:16 vertical, mín 720p
- [ ] Duração 15-60s (ideal 25-40s)
- [ ] Sem watermarks de ferramenta
- [ ] Legendas corretas em PT-BR com acentos

---

## recording-guide

Guia completo de gravação para criar material base para clone facial.

### Câmera
- Mínimo: 1080p 30fps | Ideal: 4K 60fps
- Lente: 85-105mm equivalente (sem distorção)
- Distância: 1.5-2 metros
- Enquadramento: cabeça + ombros, 2/3 do frame
- Olhar: DIRETO na lente (não no preview)

### Iluminação 3 pontos
1. **Key Light** (45° lado, 15-20° acima): Softbox difusa, 100%
2. **Fill Light** (lado oposto, nível da câmera): 50-60% da key
3. **Backlight** (atrás, no cabelo/ombros): 70-80% da key

### Fundo
- Sólido, neutro (cinza, branco, azul escuro)
- Mínimo 1.2m de distância do fundo
- Sem padrões, logos, objetos distrativos

### Duração
- 5-10 minutos contínuos sem cortes
- Variação emocional: confiança, preocupação, empolgação
- Incluir: setup de trade, análise de gráfico, ensino de conceito

---

## thumbnail-generator

Criação de capas/thumbnails otimizadas para Reels e TikTok.

### Specs técnicas
- **Resolução:** 1080x1920px (9:16 vertical)
- **Área segura:** 1080x1350 (zona central, y=285 a y=1635)
- **Formato:** PNG ou JPG
- **Peso máximo:** 5MB

### Grid do Instagram
- Reel aparece como 1080x1350 (4:5) no grid — topo e base cortados
- Todo texto e elemento importante deve estar na zona central

### 3 estilos de thumbnail

**Estilo 1: Text-Heavy (Educacional, listas)**
- Fundo escuro ou gradiente
- Texto em 2-3 linhas, fonte bold (mínimo 72px)
- Cores: branco/amarelo sobre fundo escuro

**Estilo 2: Face + Text (Storytelling, mindset)**
- Clone em destaque (60-70% do frame)
- Texto sobreposto em área segura
- Expressão facial intensa/curiosa

**Estilo 3: Chart/Proof (Análise técnica, resultados)**
- Screenshot de gráfico ou comprovante como fundo
- Título curto (máx 5 palavras) em overlay

---

## trending-sounds

Seleção de trilha sonora por tipo de conteúdo.

### Categorias de som por tipo de vídeo

| Categoria | Quando usar | BPM | Exemplos |
|-----------|-------------|-----|---------|
| Hype/Energia | Resultados, provas sociais, listas | 120-140 | trap beats, phonk suave |
| Calma/Mindset | Storytelling, confissões, reflexões | 60-90 | lo-fi, piano, acoustic |
| News/Urgência | Análise de notícia, breaking news | — | sons de noticiário, tensão |
| Educacional | Chart Explanation, 3-Second Rule | 90-110 | neutro, sem destaque |
| Emocional | Mindset Confession, Student Result | 70-100 | cinematic, inspiracional |

### Regra de volume
- Música: máx 20% do volume da voz (voz SEMPRE em primeiro plano)
- 85% dos usuários assistem sem som — legendas compensam

---

## voice-training

Guia de gravação de áudio para clone de voz perfeito em PT-BR.

### Setup de microfone
- Mínimo: Rode NT-USB Mini ($100)
- Ideal: Audio-Technica AT2020 XLR + Focusrite Scarlett Solo ($300)
- NUNCA usar microfone do laptop
- Distância: 20cm (2 punhos), levemente fora do eixo central
- Pop filter SEMPRE entre boca e mic
- Microfone na altura da boca

### Ambiente
- Sala menor possível (armário funciona)
- Cobertores/cortinas nas paredes
- DESLIGAR: ar condicionado, ventilador, eletrônicos
- Fechar portas e janelas
- SNR > 30dB

### Conteúdo a gravar (5-7 minutos)
- Conteúdo natural: explicar setup, analisar gráfico, ensinar conceito
- NÃO ler roteiro de forma rígida
- Variação emocional: empolgação, preocupação, confiança
- Incluir terminologia técnica: FVG, Order Block, SMC, prop firm, take profit, stop loss

### Termos que o clone deve pronunciar corretamente
Smart Money Concepts, FVG, Order Block, Displacement, Liquidity Sweep, Inducement, FOMC, NFP, CPI, Selic, stop loss, take profit, RR

### Formato de exportação
- ElevenLabs: WAV 44.1kHz mínimo
- Fish Audio: WAV ou MP3 192kbps+
