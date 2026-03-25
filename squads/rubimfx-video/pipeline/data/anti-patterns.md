# Anti-Patterns — Erros a Evitar na Produção de Vídeo

Lista de erros aprendidos na produção de carrosséis e vídeos. Cada erro inclui: o que é, por que é ruim e como evitar.

---

## Design e Visual

### 1. Fontes Pequenas (< 22px)
- **Problema:** Texto ilegível em telas de celular
- **Regra:** Headlines mínimo 64-80px, body mínimo 28-34px, labels mínimo 22px
- **NADA abaixo de 20px em nenhuma circunstância**
- **Teste:** Se não dá pra ler com o celular a 50cm do rosto, tá pequeno demais

### 2. Fotos Genéricas de Banco de Imagens
- **Problema:** Unsplash/Pexels para conteúdo principal destrói credibilidade
- **Regra:** Usar prints reais, screenshots de notícias, gráficos reais
- **Exceção:** B-roll de apoio pode usar banco de imagens (com moderação)
- **Alternativa:** Screenshots de manchetes de jornal para credibilidade

### 3. Screenshots de Páginas Inteiras
- **Problema:** Ilegível quando reduzido para caber no vídeo
- **Regra:** Cortar apenas a parte relevante da screenshot
- **Zoom in** na área que importa
- **Destacar** com borda/seta o texto-chave

### 4. Layouts Repetitivos
- **Problema:** Todos os vídeos/slides com a mesma aparência = monotonia
- **Regra:** Alternar entre pelo menos 3-4 estilos visuais diferentes
- **Variação:** Mudar cores, posição de texto, tipo de fundo, estilo de legenda

---

## Texto e Idioma

### 5. Acentos Faltando no Português
- **Problema:** "voce" em vez de "você", "e" em vez de "é"
- **Regra:** TODOS os acentos corretos (é, á, ã, õ, ç, ê, ô)
- **Verificar:** Passar o texto por corretor ortográfico ANTES de renderizar
- **Exemplos críticos:** análise, técnica, você, também, padrão, ação

### 6. URLs Externas em HTML
- **Problema:** Links externos quebram em produção/renderização
- **Regra:** Todos os assets (fontes, imagens, CSS) devem ser locais
- **Nunca:** Referenciar CDNs ou URLs externas em templates HTML

---

## Áudio e Voz

### 7. Voz de Robô (Rápido Demais, Sem Emoção)
- **Problema:** Clone de voz falando rápido demais e sem variação emocional
- **Regra:** 130-150 palavras/minuto, com pausas e variação de tom
- **Solução:** Ajustar parâmetros de stability e similarity no ElevenLabs
- **Teste:** Ouvir de olhos fechados — se soa artificial, refazer

### 8. Música Mais Alta que a Voz
- **Problema:** Trilha sonora compete com a mensagem
- **Regra:** Música no máximo 20% do volume da voz
- **Em trechos com fala:** Música quase imperceptível
- **Em trechos sem fala:** Música pode subir para 40-60%

---

## Clone de Vídeo

### 9. Pele Plástica no Clone
- **Problema:** Modelo IA suaviza demais a pele, fica aspecto ceroso/artificial
- **Solução:** Pós-processamento com skin texture enhancement (Claid.ai)
- **Prevenção:** Usar foto base com boa textura de pele
- **Verificação:** Comparar com vídeo real do Gabriel lado a lado

### 10. Lip Sync Errado nas Nasais (ã, em)
- **Problema:** Clone não diferencia nasais de vogais orais do PT-BR
- **Solução:** MuseTalk para corrigir fonemas específicos
- **Verificação:** Reproduzir em 0.5x focando na boca
- **Fonemas críticos:** "ã" em "padrão", "em" em "também", "ão" em "ação"

### 11. Cabeça Estática
- **Problema:** Clone com cabeça parada como manequim enquanto fala
- **Solução:** Adicionar instrução de movimento no prompt do HeyGen
- **Natural:** Micro-movimentos, acenos sutis ao enfatizar
- **Verificação:** Comparar com vídeo real — Gabriel move a cabeça constantemente

### 12. Piscadas Regulares/Robóticas
- **Problema:** Clone pisca em intervalos exatos (a cada 3 segundos, por exemplo)
- **Solução:** Re-gerar até conseguir padrão irregular
- **Natural:** Humanos piscam 12-20x/min com intervalos VARIÁVEIS
- **Verificação:** Contar piscadas por 30 segundos e verificar irregularidade

---

## Publicação e Processo

### 13. Publicar Sem Revisão
- **Problema:** Erros óbvios que poderiam ser pegos com uma revisão simples
- **Regra:** SEMPRE passar pelo Quality Gate antes de publicar
- **Checklist mínimo:** áudio OK, visual OK, texto sem erro, CTA presente
- **Ideal:** Mostrar para outra pessoa antes de publicar

### 14. CTA Genérico ou Ausente
- **Problema:** "Curte e segue" não gera ação real. Sem CTA = oportunidade perdida
- **Regra:** 1 CTA específico por vídeo, alinhado ao tipo de conteúdo
- **Exemplos bons:** "Salva esse setup pra amanhã", "Comenta se já passou por isso"
- **Exemplo ruim:** "Deixa seu like", "Se inscreve"

### 15. Mesmo Formato Todo Dia
- **Problema:** Audiência enjoa, algoritmo penaliza repetição
- **Regra:** Nunca repetir formato em dias consecutivos
- **Mix semanal:** 40% macro, 25% educacional, 15% trade, 10% prop, 10% mindset
- **Variação:** Pelo menos 3-4 formatos diferentes por semana

---

## Checklist Rápido Anti-Padrão

Antes de publicar QUALQUER vídeo, verificar:

- [ ] Fontes legíveis (mínimo 22px em qualquer texto)
- [ ] Sem fotos genéricas como conteúdo principal
- [ ] Screenshots cortadas e legíveis
- [ ] Visual diferente do último vídeo
- [ ] Acentos corretos em todo o texto
- [ ] Sem URLs externas
- [ ] Voz natural (não robótica)
- [ ] Música baixa (< 20% volume)
- [ ] Pele com textura (não plástica)
- [ ] Lip sync OK (testar em 0.5x)
- [ ] Cabeça com movimento natural
- [ ] Piscadas irregulares
- [ ] Revisão feita por humano
- [ ] CTA específico presente
- [ ] Formato diferente do dia anterior
