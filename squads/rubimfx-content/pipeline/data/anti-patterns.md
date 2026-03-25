# Anti-Patterns — @rubimfx Content Pipeline

## O que sao anti-patterns

Erros recorrentes que reduzem qualidade, engajamento ou criam risco regulatorio. Cada item abaixo inclui o erro, por que e um problema, e como corrigir.

---

## 1. Hook Generico

**Erro:**
> "Hoje vamos falar sobre o FOMC"
> "Voce sabe o que e o NFP?"

**Por que e ruim:** Nao para o scroll. Zero curiosidade. Parece aula de faculdade, nao conteudo de Instagram.

**Como corrigir:**
> "O Fed acabou de sinalizar algo que o mercado nao esperava."
> "Esse dado de emprego pode derrubar o dolar essa semana."

**Regra:** O hook precisa criar tensao, curiosidade ou urgencia em menos de 15 palavras.

---

## 2. Slides Superficiais (< 40 palavras)

**Erro:** Slides com 15-30 palavras que parecem tweets colados num carrossel.

**Por que e ruim:** Transmite falta de profundidade. O seguidor sente que nao aprendeu nada. Reduz saves (a metrica mais importante para o algoritmo).

**Como corrigir:** Cada slide deve ter entre 40-80 palavras. Se tem menos de 40, ou o slide nao deveria existir, ou falta desenvolvimento da ideia.

**Excecao:** Slide de capa (10-20 palavras) e slide de CTA (20-40 palavras).

---

## 3. Ausencia de BRIDGE (Macro sem Conexao)

**Erro:** Carrossel sobre FOMC que termina no slide 7 com "e isso que aconteceu" sem conectar a nenhum trade ou setup.

**Por que e ruim:** O seguidor do @rubimfx e trader, nao economista. Ele quer saber: "E dai? O que eu faco com essa informacao?"

**Como corrigir:** Sempre incluir o BRIDGE:
```
Evento Macro → Impacto no Ativo → Leitura Tecnica → Setup
```

Se nao consegue fazer o BRIDGE, a pauta provavelmente nao serve para @rubimfx.

---

## 4. Promessa de Retorno (Violacao CVM)

**Erro:**
> "Esse setup da 80% de acerto"
> "Ganhe R$5.000/mes operando"
> "Lucrei 200 pontos ontem"
> "Com esse metodo voce vai viver de trading"

**Por que e ruim:** Violacao da regulacao CVM/ANBIMA. Risco de processo, multa, e perda de credibilidade. Alem disso, promessas irreais atraem seguidores errados e geram churn.

**Como corrigir:**
> "Historicamente, esse padrao tem uma relacao risco/retorno favoravel"
> "Esse framework ajuda a identificar oportunidades"
> "Conteudo educacional. Nao e recomendacao de investimento."

**Regra absoluta:** NUNCA prometer, garantir ou sugerir retorno financeiro especifico.

---

## 5. Estetica Canva Stock

**Erro:** Templates coloridos do Canva com fundos gradientes claros, icones genericos, fontes decorativas, backgrounds stock photo.

**Por que e ruim:** Destroi a autoridade visual. Parece conta amadora, nao analista profissional. Incoerente com o posicionamento @economesteter.

**Como corrigir:** Seguir rigorosamente o style-guide-economesteter.md:
- Dark mode SEMPRE
- Tipografia bold condensada
- Paleta restrita (navy/charcoal + branco + 1 accent)
- Hierarquia visual limpa
- Header bar consistente

---

## 6. Hashtag Spam

**Erro:** 30 hashtags incluindo genericas como #instagood #photooftheday #lifestyle #motivation #success.

**Por que e ruim:** Hashtags irrelevantes diluem o sinal para o algoritmo. O Instagram penaliza hashtag stuffing. Alem disso, parece desesperado.

**Como corrigir:**
- 5-15 hashtags maximo
- 3-5 do banco fixo @rubimfx (#trading #forex #mercadofinanceiro #propfirm #rubimfx)
- 3-8 contextuais relacionadas ao tema especifico
- Zero hashtags genericas de lifestyle

---

## 7. Caption sem CTA

**Erro:** Caption que termina com a ultima frase do conteudo e nenhuma chamada para acao.

**Por que e ruim:** Sem CTA, o seguidor consome e vai embora. Nao salva, nao comenta, nao compartilha. O algoritmo interpreta como baixo engajamento.

**Como corrigir:** Sempre terminar com um CTA especifico:
- Pergunta que gera comentario: "Voce opera macro ou so tecnico?"
- Comando de salvar: "Salva pra consultar no proximo FOMC."
- Compartilhamento: "Manda pra aquele amigo que ignora macro."
- Combinacao: "Salva e comenta: qual par voce ta operando essa semana?"

---

## 8. Inconsistencia Visual Entre Slides

**Erro:** Slide 1 com fundo navy, slide 3 com fundo cinza claro, slide 5 com accent amarelo, slide 7 com accent azul.

**Por que e ruim:** Quebra a experiencia de swipe. Parece que cada slide foi feito por uma pessoa diferente. Reduz a percepcao de profissionalismo.

**Como corrigir:**
- Definir paleta ANTES de comecar o design
- Usar o mesmo accent color em TODOS os slides
- Variar sutilmente o background (dark → slightly lighter → accent dark) mas manter a familia cromatica
- Header bar identico em todos os slides

---

## 9. Light Mode / Fundos Claros

**Erro:** Background branco ou pastel.

**Por que e ruim:** A marca @rubimfx/@economesteter e dark mode. Light mode quebra o branding, reduz reconhecimento visual no feed, e parece fora do padrao editorial.

**Como corrigir:** Background SEMPRE dark:
- Primary: #0D1117 (navy escuro)
- Secondary: #1A1B2E (charcoal)
- Nunca usar branco ou cores claras como background

**Unica excecao:** Elemento interno (tabela, destaque de dado) pode ter fundo levemente mais claro para contraste, mas dentro do slide dark.

---

## 10. Jargao sem Explicacao (TOPO DE FUNIL)

**Erro:**
> "O preco fez um BOS apos sweep do SSL com displacement para o OB que confluencia com o FVG do H4."

**Por que e ruim:** Parte da audiencia e topo de funil — sabe o basico de trading mas nao domina terminologia ICT/SMC. Se nao entende, nao salva, nao engaja, nao converte.

**Como corrigir:**
- Usar o termo tecnico + explicacao na primeira vez:
  > "Break of structure (BOS) — quando o preco rompe uma estrutura anterior, sinalizando mudanca de direcao"
- Apos explicar uma vez no carrossel, pode usar a sigla
- Manter no maximo 3-4 termos tecnicos novos por carrossel
- Para conteudo muito tecnico, adicionar "nivel: intermediario/avancado" no caption

---

## 11. Frequencia Irregular

**Erro:** Postar 5 carrosseis na semana do FOMC e sumir por 2 semanas.

**Por que e ruim:** O algoritmo do Instagram penaliza inconsistencia. Seguidores esquecem. Momentum perdido.

**Como corrigir:** Manter cadencia de 3-4 posts/semana, independente de ter evento macro ou nao. Semanas fracas de macro = conteudo educacional, storytelling, ou conceito tecnico.

---

## 12. Copiar Formato de Outro Nicho

**Erro:** Usar estrutura de carrossel de coach de vendas, influencer de lifestyle, ou perfil motivacional.

**Por que e ruim:** O publico de trading detecta imediatamente conteudo generico revestido de terminologia financeira. Perde credibilidade.

**Como corrigir:** A referencia visual e editorial e SEMPRE o @economesteter e perfis de analise macro (Hedgeye, The Kobeissi Letter, MacroAlf). Nunca coach/guru de vendas.

---

## Checklist Rapido Anti-Patterns

Antes de publicar, confirmar que NENHUM destes esta presente:

- [ ] Hook generico que nao para scroll
- [ ] Slide com menos de 40 palavras (exceto capa/CTA)
- [ ] Conteudo macro sem BRIDGE
- [ ] Promessa de retorno ou resultado
- [ ] Estetica Canva/stock/light mode
- [ ] Mais de 15 hashtags
- [ ] Sem CTA no caption
- [ ] Visual inconsistente entre slides
- [ ] Jargao sem explicacao
- [ ] Background claro
