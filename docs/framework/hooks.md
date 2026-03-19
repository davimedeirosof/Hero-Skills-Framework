# Hooks — Automações de Eventos

28 scripts JavaScript que disparam automaticamente em eventos do Claude Code.

---

## Hooks do GSD (raiz de `~/.claude/hooks/`)

| Hook | Evento | Função |
|------|--------|--------|
| `gsd-check-update.js` | sessão | Verifica atualizações do GSD |
| `gsd-context-monitor.js` | uso | Monitora tokens de contexto em tempo real |
| `gsd-statusline.js` | contínuo | Exibe status do projeto na statusline |

---

## Hooks de Scripts (`~/.claude/hooks/scripts/`)

### Proteção e segurança

| Hook | Evento | Função |
|------|--------|--------|
| `secret-scanner.js` | pre-tool | Detecta secrets/tokens antes de commits |
| `pre-push-check.js` | pre-tool | Valida antes de git push |
| `commit-guard.js` | pre-tool | Bloqueia commits fora do padrão |
| `block-dev-server.js` | pre-tool | Impede subir servidor dev acidentalmente |
| `block-md-creation.js` | pre-tool | Bloqueia criação de .md não solicitados |
| `anti-rationalization.js` | pre-tool | Detecta quando AI tenta justificar erros |
| `stop-check.js` | pre-tool | Valida condições antes de parar execução |
| `prompt-check.js` | pre-tool | Verifica qualidade do prompt antes de executar |

### Qualidade de código

| Hook | Evento | Função |
|------|--------|--------|
| `lint-fix.js` | post-edit | Roda lint automaticamente após edição |
| `async-lint-check.js` | post-edit | Lint assíncrono para não bloquear |
| `type-check.js` | post-edit | Verifica tipagem após edição |
| `post-edit-check.js` | post-edit | Validações gerais após edição |
| `bundle-check.js` | post-edit | Verifica impacto no bundle size |
| `auto-test.js` | post-edit | Roda testes relacionados automaticamente |

### Contexto e sessão

| Hook | Evento | Função |
|------|--------|--------|
| `context-loader.js` | session-start | Carrega contexto do projeto ao iniciar |
| `context-health-monitor.js` | contínuo | Monitora saúde do contexto |
| `session-start.js` | session-start | Inicialização da sessão |
| `session-end.js` | session-end | Finalização e limpeza da sessão |
| `pre-compact.js` | pre-compact | Prepara antes de compactar contexto |
| `pre-compact-save.js` | pre-compact | Salva estado antes da compactação |
| `post-compact-restore.js` | post-compact | Restaura estado após compactação |
| `suggest-compact.js` | contínuo | Sugere compactar quando contexto está alto |

### Observabilidade

| Hook | Evento | Função |
|------|--------|--------|
| `learning-log.js` | post-tool | Registra aprendizados da sessão |
| `notification-log.js` | post-tool | Log de notificações e eventos |
| `webhook-notify.js` | eventos | Envia notificações via webhook externo |

---

## Total

- 3 hooks GSD
- 25 hooks de scripts
- **28 hooks no total**
