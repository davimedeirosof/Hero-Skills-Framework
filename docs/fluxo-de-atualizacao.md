# Fluxo de Atualização do Framework

Guia para adicionar qualquer coisa nova ao Hero-Skills-Framework e subir para o GitHub.

---

## Fluxo padrão

```bash
cd /c/Users/Windows/DaviClaude

# 1. adiciona os arquivos novos ou modificados
git add .

# 2. cria o commit com descrição do que foi feito
git commit -m "descrição do que foi adicionado"

# 3. sobe para o GitHub
git push origin main
```

---

## Onde cada coisa vai

| O que adicionar | Pasta no repo | Instalar localmente também? |
|----------------|---------------|----------------------------|
| Novo agente | `agents/` | Sim — copiar para `~/.claude/agents/` |
| Nova skill | `skills/` | Sim — copiar para `~/.claude/skills/` |
| Novo command | `commands/` | Sim — copiar para `~/.claude/commands/` |
| Novo hook | `hooks/scripts/` | Sim — copiar para `~/.claude/hooks/scripts/` |
| Novo projeto | `docs/projetos/` | Não |
| Documentação | `docs/` | Não |
| Atualização da persona | `CLAUDE.md` | Sim — copiar para `~/.claude/CLAUDE.md` |

---

## Exemplos práticos

### Adicionando um novo agente
```bash
# 1. cria o arquivo do agente
# (ex: agents/meu-agente.md)

# 2. instala localmente
cp agents/meu-agente.md ~/.claude/agents/

# 3. documenta em docs/agentes/instalados/README.md

# 4. sobe para o GitHub
git add agents/meu-agente.md docs/agentes/instalados/README.md
git commit -m "Adiciona agente meu-agente"
git push origin main
```

### Adicionando uma nova skill
```bash
# 1. cria ou copia a pasta da skill
# (ex: skills/nova-skill/SKILL.md)

# 2. instala localmente
cp -r skills/nova-skill ~/.claude/skills/

# 3. documenta em docs/skills/README.md

# 4. sobe para o GitHub
git add skills/nova-skill docs/skills/README.md
git commit -m "Adiciona skill nova-skill"
git push origin main
```

### Registrando um projeto realizado
```bash
# 1. cria o arquivo do projeto
# (ex: docs/projetos/nome-do-projeto.md)

# 2. sobe para o GitHub
git add docs/projetos/nome-do-projeto.md
git commit -m "Registra projeto nome-do-projeto"
git push origin main
```

---

## Sobre os 5 agentes nativos do Claude Code

Os 5 agentes nativos (general-purpose, Explore, Plan, claude-code-guide, statusline-setup)
são código interno da Anthropic — não existem como arquivos.

- Não há nada para copiar ou subir
- Apenas a documentação deles fica em `docs/agentes/nativos/`
- Atualizar essa documentação apenas se a Anthropic lançar mudanças

---

## Verificar o que está pendente de subir

```bash
cd /c/Users/Windows/DaviClaude
git status
```

## Puxar atualizações do Gabriel (manual)

```bash
cd /c/Users/Windows/DaviClaude
git remote add upstream https://github.com/gabrielrbm-prog/claude-rubim-v2.git
git fetch upstream
git merge upstream/main
```
