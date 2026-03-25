# Guia Completo — Content OS @rubimfx

> Tudo que você precisa saber para produzir carrosséis no padrão @rubimfx.
> Leia TUDO antes de criar o primeiro post.

---

## O QUE É ESSE PROJETO

Um sistema de produção de carrosséis para Instagram usando IA. Ele pesquisa notícias, gera imagens temáticas (clones do Gabriel + fotos bíblicas/editoriais), cria slides HTML, renderiza para PNG e publica automaticamente.

**Resultado:** 3-5 carrosséis por dia no @rubimfx com qualidade profissional.

---

## SETUP INICIAL (primeira vez)

### 1. Instalar dependências

```bash
# Node.js (para renderizar slides)
brew install node

# Playwright (para screenshots e publicação)
npm install playwright
npx playwright install chromium

# Python (para gerar imagens IA)
pip3 install google-genai
```

### 2. Configurar API Keys

Crie o arquivo `.env` na raiz do projeto:

```
GOOGLE_API_KEY=sua_chave_aqui
```

Para obter: https://aistudio.google.com/apikey (Google Gemini / Nano Banana)

### 3. Fotos de referência do Gabriel

Coloque pelo menos 3 fotos do Gabriel em:
```
squads/rubimfx-content/assets/fotos-referencia/
```

As principais usadas como referência são:
- `IMG_8579.JPG` (referência 1)
- `IMG_1092.JPG` (referência 2)
- `DSC04575.JPG` (referência 3)

Essas fotos NÃO estão no Git (são pessoais). Peça ao Gabriel.

### 4. Profile photo

Coloque a foto de perfil do Gabriel em:
```
squads/rubimfx-content/assets/profile-photo.jpeg
```

Essa foto aparece no header dos Tweet Cards (52px redondo).

---

## FLUXO DE PRODUÇÃO (passo a passo)

### Passo 1 — Pesquisar tema

Use o Claude Code com o agente `research-analyst` para buscar notícias virais:
- Fontes preferidas: Gazeta do Povo, Revista Oeste, O Antagonista, Jovem Pan, Poder360, CNN Brasil
- Gabriel tem viés conservador de direita — respeitar isso na seleção
- Priorizar: política, economia, geopolítica, escândalos, eleições

Para temas de mindset/fé:
- Disciplina > motivação
- Fé cristã (Bill Johnson, versículos, processo de Deus)
- Família e valores
- Solidão do topo, preço do sucesso

### Passo 2 — Gabriel escolhe tema + estilo

Apresentar 3-5 opções com potencial viral. Gabriel escolhe.

Estilos disponíveis (do favorito ao menos usado):

| Estilo | Quando usar | Impacto |
|--------|------------|---------|
| **Kaique Epic** ⭐ | Mindset, storytelling, fé, impacto máximo | ⭐⭐⭐⭐⭐ |
| **Twitter Dark** | Educativo, dados, impostos, economia | ⭐⭐⭐ |
| **Esteter Style** | Notícias com fontes, screenshots reais | ⭐⭐⭐ |
| **Hollyfield News** | Breaking news, foto hero gigante | ⭐⭐⭐⭐ |
| **Minimalista Premium** | Teaser InvisIA, manifesto, provocação | ⭐⭐⭐⭐ |
| **BrunoGPT Neon** | Tech, IA, futurista | ⭐⭐⭐ |

### Passo 3 — Gerar fotos

**REGRA DE OURO:** SEMPRE criar foto temática nova para a CAPA e pelo menos 1-2 slides-chave. Pode reusar fotos do book nos demais.

#### Foto clone do Gabriel (temática)

```bash
cd squads/rubimfx-content/

python3 scripts/clone_image.py \
  assets/fotos-referencia/IMG_8579.JPG \
  --multi assets/fotos-referencia/IMG_1092.JPG assets/fotos-referencia/DSC04575.JPG \
  "PROMPT DESCRITIVO AQUI" \
  output/posts/PASTA/fotos/nome-foto.png \
  --camera cinematic --color portra
```

**Presets de câmera:** editorial, cinematic, candid, luxury, dramatic, street, stage, warm

**Presets de cor:** portra, cinestill, chrome, bw, gold, natural, teal-orange

**12 cenários pré-definidos:** trading-desk, office-ceo, podcast-studio, stage-speaker, casual-street, teaching-whiteboard, results-celebration, rooftop-night, home-content, thinking-window, market-stress, walking-office

#### Foto bíblica/genérica (sem clone)

```python
# Usar generate_biblical.py como base
# Editar os prompts conforme o tema
python3 generate_biblical.py
```

#### Foto editorial real (de notícias)

Usar Firecrawl MCP para extrair og:image dos artigos:
```
mcp__firecrawl__firecrawl_scrape com formato JSON
→ extrair og:image
→ baixar via curl
```

**NUNCA usar:** fotos stock genéricas, Unsplash, Pexels. Sempre fotos reais ou geradas por IA.

### Passo 4 — Criar os 10 slides HTML

Estrutura padrão (Kaique Epic):

```
Slide 01 → EPIC COVER — Foto temática + headline gigante (Anton 80-96px)
Slide 02 → TWEET CARD — Profile header + texto + foto editorial
Slide 03 → TWEET CARD — Continuação do conteúdo
Slide 04 → EPIC COVER — Foto temática + dado/frase de impacto
Slide 05 → TWEET CARD — Conteúdo com lista ou dados
Slide 06 → TWEET CARD — Continuação
Slide 07 → EPIC COVER — Foto temática + frase forte
Slide 08 → TWEET CARD — Análise/cronologia/checklist
Slide 09 → QUOTE CARD — Frase de impacto (dark, Anton grande)
Slide 10 → CTA EPIC — "SEGUE @RUBIMFX" + profile photo + botão
```

**Alternância obrigatória:** Epic Cover (dark, foto full bleed) intercalado com Tweet Card (branco, profile header). NUNCA 3 slides do mesmo tipo seguidos.

### Passo 5 — Renderizar para PNG

```bash
cd output/posts/NOME-DO-POST/

# Copiar profile photo para html/
cp ../../assets/profile-photo.jpeg html/

# Iniciar server HTTP
python3 -m http.server 8899 &

# Renderizar com Playwright
cat > render.js << 'SCRIPT'
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1080, height: 1350 });
  for (let i = 1; i <= 10; i++) {
    const num = String(i).padStart(2, '0');
    await page.goto(`http://localhost:8899/html/slide-${num}.html`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    await page.screenshot({ path: `png/slide-${num}.png`, fullPage: false });
    console.log(`✓ slide-${num}.png`);
  }
  await browser.close();
})();
SCRIPT
node render.js
```

**IMPORTANTE:** O server HTTP deve rodar na pasta do POST (não na pasta html/) para que os paths relativos `../fotos/` funcionem.

### Passo 6 — Verificar visualmente

SEMPRE conferir os slides antes de mostrar ao Gabriel:
- Fotos aparecem? (não quebradas)
- Texto legível? (fontes grandes o suficiente)
- Acentos corretos?
- @rubimfx visível em todos?
- Variação de layouts? (mínimo 3 tipos)

### Passo 7 — Publicar no Instagram

```
1. Fechar Chrome: pkill -a "Google Chrome"
2. Abrir Instagram via Playwright
3. Criar → Postar → Selecionar do computador
4. Upload dos 10 PNGs
5. Selecionar corte 4:5
6. Avançar (sem filtro)
7. Avançar
8. Escrever legenda
9. Compartilhar
10. Aguardar "Post compartilhado"
```

---

## REGRAS VISUAIS (não negociáveis)

### Dimensões
- **Sempre:** 1080x1350px (4:5 Instagram)
- **Nunca:** quadrado, paisagem, ou qualquer outro formato

### Tipografia

| Elemento | Fonte | Tamanho | Peso |
|----------|-------|---------|------|
| Epic headline | Anton | 76-96px | 400 (Anton é bold por padrão) |
| Tweet headline | Inter | 44-56px | 900 |
| Body text | Inter | 28-34px | 450 |
| Labels/badges | Inter | 18-22px | 800 |
| Muted/sources | Inter | 20-22px | 500 |
| **MÍNIMO ABSOLUTO** | — | **20px** | — |

### Paleta de cores — Kaique Epic

| Elemento | Cor | Hex |
|----------|-----|-----|
| Destaque principal | Amarelo | `#FFD600` |
| Alerta/perigo | Vermelho | `#FF3B30` |
| Info/link | Azul | `#1D9BF0` |
| Sucesso | Verde | `#00BA7C` |
| Fundo card branco | Branco | `#FFFFFF` |
| Texto preto | Dark | `#0F1419` |
| Texto body | Gray | `#292F33` |
| Texto secondary | Gray | `#536471` |
| Border | Light | `#EFF3F4` |

### Paleta — Teaser InvisIA

| Elemento | Cor | Hex |
|----------|-----|-----|
| Fundo | Preto puro | `#000000` |
| Texto | Branco gelo | `#F5F5F5` |
| Acento | Roxo | `#7C3AED` |

### CSS dos overlays (Epic Cover)

```css
/* Gradient padrão sobre foto */
.bg-overlay {
  background: linear-gradient(180deg,
    rgba(0,0,0,0.4) 0%,
    rgba(0,0,0,0.15) 20%,
    rgba(0,0,0,0.25) 45%,
    rgba(0,0,0,0.8) 70%,
    rgba(0,0,0,0.97) 100%
  );
}
```

### Bottom bar (em todos os Epic Covers)

```html
<div class="bottom-bar">
  <div class="cta-arrasta">
    ARRASTA PRO LADO <span class="cta-arrows">&gt;&gt;&gt;</span>
  </div>
  <div class="handle">@RUBIMFX</div>
</div>
```

Arrows em amarelo (#FFD600), texto em rgba(255,255,255,0.7).

---

## TOM DA LEGENDA — COMO O GABRIEL ESCREVE

### Regras de estilo
- **Tudo minúscula** (exceto CAPS para ênfase)
- **Frases curtas.** Uma ideia por frase.
- **Parágrafos de 1-2 linhas** com espaço entre eles
- **Sem emoji** (ou máximo 2-3 por post)
- **Sem formalidade** — como se tivesse falando no WhatsApp com um amigo
- **Direto ao ponto** — sem enrolação, sem introdução longa
- **CTA no final** — sempre: "salva", "manda pra alguém", "comenta o número"

### Exemplo — Notícia política

```
vorcaro vai entregar 15 políticos.

e o mais absurdo? ele quer POUPAR o STF.

o cara tem mensagem no celular pra Moraes perguntando
"conseguiu bloquear?" na noite que foi preso.

e ele quer poupar esses caras?

André Mendonça já avisou: delação seletiva não vai rolar.

salva e manda pra todo mundo. as pessoas precisam saber
o que tá acontecendo nesse país.

#bancomaster #vorcaro #delação #stf #rubimfx
```

### Exemplo — Fé/espiritual

```
tá demorando?

por vezes a gente se questiona. "por que ainda não chegou?"

assisti um sermão do Bill Johnson essa semana que me quebrou.
ele falou uma coisa que eu precisava ouvir:

"no Reino, a demora SEMPRE traz ganho."

se tá demorando, não desiste. Deus não esqueceu de você.

salva e manda pra alguém que precisa ouvir isso hoje.

#fe #Deus #processo #rubimfx
```

### Exemplo — Pessoal/aniversário

```
37 anos hoje.

e eu poderia falar de conquistas, de números, de resultados...
mas não é sobre isso.

é sobre o que me sustenta quando ninguém tá vendo.

Deus. sempre foi Ele.

Thays. 14 anos do meu lado. essa mulher viu eu quebrar,
viu eu chorar — e ficou.

eu não nasci pronto. eu me construí.

Deus é fiel. sempre foi. sempre vai ser.

#aniversario #37anos #gratidao #rubimfx
```

---

## TEMAS QUE FUNCIONAM NO @RUBIMFX

### Notícias (virais, polêmicas)
- Banco Master / Vorcaro / delação
- Guerra Irã / petróleo / Ormuz
- Eleições 2026 (Flávio x Lula)
- Impostos / gastos do governo
- STF / escândalos / corrupção
- Caminhoneiros / diesel / greve
- **Fontes:** Gazeta do Povo, Revista Oeste, O Antagonista, Jovem Pan, Poder360

### Mindset / Disciplina
- Motivação é fraqueza — sistema > sentimento
- Verdades duras do mercado
- Protocolo diário do trader
- Preço do topo / solidão do topo
- **Tom:** provocativo, direto, sem motivação rasa

### Fé / Espiritual
- Tá demorando? Deus tá trabalhando
- 5 sinais que Deus tá te preparando
- A oração que mudou minha vida
- Deus, família e legado
- **Tom:** íntimo, guerreiro, vulnerável. Nunca religioso genérico.
- **Versículos favoritos:** Salmos 127:1, Habacuque 2:3, Tiago 1:12, Jeremias 29:11, Malaquias 3:3, Oséias 2:14, Provérbios 27:17

### Família / Pessoal
- Thays (esposa, 14 anos juntos, casamento restaurado)
- Cecília, Theo e Gael (3 filhos)
- Aniversário / datas especiais
- **Tom:** emocional, real, sem falar de trading

### Trading / Mercado
- SMC / ICT / Order Flow
- Mesa proprietária (Summit Prop)
- Gestão de risco
- **Tom:** practitioner, não teórico

### Teaser InvisIA (quando autorizado)
- Estilo minimalista premium (preto, branco, roxo)
- Sem revelar tudo — plantar curiosidade
- Público-alvo: empresários R$1M+/ano

---

## BOOKS DE FOTOS DISPONÍVEIS

### Book Minimalista (`output/book-minimalista/`)
| Foto | Estilo | Quando usar |
|------|--------|-------------|
| 01-linkedin-headshot.png | Blazer navy, fundo cinza | Negócios, autoridade |
| 02-personal-branding.png | Camiseta preta, fundo bege | Branding, stories |
| 03-trader-turtleneck.png | Gola alta, braços cruzados | Trading, autoridade |
| 04-editorial-rembrandt.png | Terno, luz dramática | Capas, editorial |
| 05-casual-camisa-branca.png | Camisa branca, fundo escuro | Casual, conteúdo |

### Book Impactante (`output/book-impactante/`)
| Foto | Estilo | Quando usar |
|------|--------|-------------|
| 01-close-dramatico.png | Metade rosto na luz | Slides de impacto máximo |
| 02-silhueta-poder.png | Contraluz P&B | Posts dark, mistério |
| 03-olhar-lateral.png | Editorial, pensativo | Reflexivos, fé |
| 04-bracos-cruzados.png | P&B, turtleneck | Autoridade, poder |
| 05-low-key-noir.png | Rosto na escuridão | Polêmicos, provocativos |
| 06-sorriso-natural.png | Meio sorriso, dramático | Acessível mas forte |

---

## IDENTIDADE DO GABRIEL RUBIM (para clones IA)

```
Subject: Gabriel Rubim, Brazilian male, early 30s
Face: light olive/fair skin, hazel-brown eyes, strong defined jawline,
      short well-trimmed dark beard and goatee, thick dark eyebrows
Hair: dark brown/black, short modern fade, slightly longer on top
Build: muscular athletic, broad shoulders, tattoo sleeve left arm
      (lion and geometric/religious motifs)
Style: professional-casual, dark fitted clothing, clean minimal
Distinctive: trading educator, tattoo sleeve, strong masculine presence
```

---

## CHECKLIST PRÉ-PUBLICAÇÃO

Antes de mostrar ao Gabriel ou publicar:

- [ ] Capa tem foto temática NOVA (não reusada de outro post)
- [ ] Todos os slides têm @rubimfx visível
- [ ] Mínimo 3 layouts diferentes (Epic + Tweet + Quote/Data)
- [ ] Fontes acima de 20px em TODOS os slides
- [ ] Acentos corretos em português (á, é, í, ó, ú, ã, õ, ç)
- [ ] Fotos aparecem corretamente (não quebradas)
- [ ] Texto legível sobre as fotos (gradient suficiente)
- [ ] CTA no último slide ("Segue @rubimfx")
- [ ] Legenda no tom informal do Gabriel (minúsculas, direto)
- [ ] Hashtags relevantes (5-10, sem exagero)
- [ ] Crop 4:5 selecionado antes de avançar no Instagram

---

## ESTRUTURA DE PASTAS

```
squads/rubimfx-content/
├── assets/
│   ├── profile-photo.jpeg          ← Foto de perfil (52px nos cards)
│   └── fotos-referencia/           ← Fotos reais do Gabriel (NÃO no Git)
├── templates/
│   ├── template-09-kaique-epic.html
│   ├── template-10-kaique-tweet.html
│   ├── MODELOS-COMPLETOS.md        ← Guia visual dos 6 estilos
│   ├── kaique-epic-reference.md
│   ├── hollyfield-news-reference.md
│   └── ...
├── scripts/
│   ├── clone_image.py              ← Clone PRO (12 cenários, 8 câmeras, 7 cores)
│   └── ...
├── agents/
│   └── *.agent.md                  ← 9 agentes com personas
├── output/
│   ├── book-minimalista/           ← 5 fotos book
│   ├── book-impactante/            ← 6 fotos book
│   └── posts/
│       └── YYYY-MM-DD-nome/
│           ├── html/               ← Slides HTML
│           │   └── profile-photo.jpeg
│           ├── fotos/              ← Fotos (editoriais + clones + temáticas)
│           └── png/                ← Slides renderizados (NÃO no Git)
├── GUIA-CONSISTENCIA.md            ← Regras resumidas
├── GUIA-COMPLETO-EQUIPE.md         ← ESTE ARQUIVO
├── squad.yaml
└── squad-party.csv
```

---

## PERGUNTAS FREQUENTES

**P: Posso usar a mesma foto de capa em dois posts diferentes?**
R: NÃO. Cada post deve ter foto temática nova na capa. Fotos do book podem ser reusadas nos slides internos.

**P: Quantos slides deve ter cada carrossel?**
R: 10. Sempre 10. A estrutura é: 3-4 Epic Covers + 5-6 Tweet Cards + 1 CTA.

**P: Gabriel quer postar sobre um tema novo que não está na lista. O que faço?**
R: Pesquisar o tema, manter o estilo Kaique Epic (favorito dele), e seguir as regras visuais. O tom da legenda é sempre informal.

**P: Como gero uma foto temática que não é clone?**
R: Use o generate_biblical.py como base. Edite o prompt para descrever a cena. Gemini gera imagens cinematográficas de qualidade.

**P: A foto ficou cortada no slide. Como resolvo?**
R: Use `object-fit: contain` em vez de `object-fit: cover`. Ou ajuste `object-position: top center` se só o topo importa.

**P: Gabriel não gostou de uma foto. O que faço?**
R: Regere com prompt diferente. Gabriel prefere fotos DRAMÁTICAS e MINIMALISTAS, fundo escuro, iluminação tipo Rembrandt. Evitar fotos "claras demais" ou "genéricas".

---

## CONTATO

- **Gabriel Rubim:** @rubimfx (Instagram)
- **Projeto:** Opensquad Content OS
- **Stack:** Claude Code + Gemini API + Playwright + HTML/CSS

---

*Documento criado em 23 de março de 2026.*
*Atualizar sempre que novas regras forem definidas.*
