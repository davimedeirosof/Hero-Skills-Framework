# GSD — Get Shit Done

## O que é

Sistema de desenvolvimento orientado por spec (spec-driven development).
Estrutura projetos com context engineering completo, tarefas organizadas
e fluxo de trabalho definido.

**Versão instalada:** v1.26.0

## Comandos principais

| Comando | Função |
|---------|--------|
| `/gsd:new-project` | Inicia um novo projeto com spec completa |
| `/gsd:task` | Cria e gerencia tasks |
| `/gsd:status` | Verifica status do projeto |
| `/gsd:context` | Gerencia contexto do projeto |

## Arquivos instalados

| Caminho | Descrição |
|---------|-----------|
| `~/.claude/commands/gsd/` | Comandos slash do GSD |
| `~/.claude/commands/get-shit-done/` | Comandos alternativos |
| `~/.claude/hooks/gsd-*.js` | Hooks do GSD (3 arquivos) |

## Hooks do GSD

| Hook | Função |
|------|--------|
| `gsd-check-update.js` | Verifica atualizações disponíveis |
| `gsd-context-monitor.js` | Monitora uso de contexto em tempo real |
| `gsd-statusline.js` | Exibe status do projeto na statusline |

## Como usar

1. Abra um diretório de projeto no Claude Code
2. Execute `/gsd:new-project`
3. Responda as perguntas de descoberta
4. O GSD gera a spec, tasks e contexto automaticamente
