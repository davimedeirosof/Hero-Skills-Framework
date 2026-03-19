# Opensquad — Orquestração Multi-Agente

## O que é

Sistema que cria e executa squads — equipes de agentes que trabalham em
pipeline para tarefas complexas. Cada agente executa uma etapa e passa
o resultado para o próximo.

## Componentes

| Componente | Arquivo | Função |
|-----------|---------|--------|
| Orquestrador | `_opensquad/core/architect.agent.yaml` | Monta o squad e define o pipeline |
| Pipeline Runner | `_opensquad/core/runner.pipeline.md` | Executa o pipeline passo a passo |
| Skills Engine | `_opensquad/core/skills.engine.md` | Gerencia skills dos agentes |
| Memória | `_opensquad/_memory/` | Contexto persistente entre sessões |

## Fluxo de execução

```
Davi faz uma demanda
  └── Hero recebe e avalia complexidade
        └── Orquestrador monta o squad
              └── Pipeline Runner executa
                    ├── Agente 1 → output 1
                    ├── Agente 2 recebe output 1 → output 2
                    ├── Agente 3 recebe output 2 → output 3
                    └── Resultado final entregue ao Davi
```

## Squads

Squads ficam em `~/squads/`. Cada squad tem:
- `squad.yaml` — configuração do squad
- `squad-party.csv` — lista de agentes e papéis
- `pipeline/pipeline.yaml` — etapas de execução
- `output/` — resultados por execução (formato: YYYY-MM-DD-HHmmss)
- `_memory/memories.md` — memória do squad

## Como iniciar um squad

No Claude Code:
```
@Orquestrador crie um squad para [descrição da tarefa]
```

## Arquivos locais

| Caminho | Descrição |
|---------|-----------|
| `~/_opensquad/` | Instalação do Opensquad |
| `~/squads/` | Squads criados |
| `~/_opensquad/_memory/` | Memória global |
| `~/_opensquad/_browser_profile/` | Perfil de browser para skills web |
