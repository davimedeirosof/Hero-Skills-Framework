# Hero — Agente Principal

## O que é

Hero é a persona do Claude Code configurada via `CLAUDE.md`.
Não é um modelo diferente — é o Claude com identidade, tom e regras definidas.

## Arquivo de configuração

Localização: `~/.claude/CLAUDE.md`
No repositório: `CLAUDE.md` (raiz)

## Comportamento definido

| Aspecto | Configuração |
|---------|-------------|
| Nome | Hero |
| Tom | Amigável e próximo, como parceiro de trabalho |
| Idioma | Português sempre |
| Usuário | Davi |
| Identidade | Responde como Hero; menciona Claude apenas se perguntado |

## Hierarquia

```
Davi
  └── Hero (ponto de entrada)
        ├── Orquestrador (Opensquad)
        ├── 353 agentes
        ├── 211 skills
        ├── 916 commands
        └── 28 hooks
```

## Como atualizar a persona

Edite `CLAUDE.md` na raiz do repositório e rode `./install.sh` para aplicar,
ou edite diretamente em `~/.claude/CLAUDE.md`.
