# Framework — Visão Geral

O Hero Framework é composto por 5 camadas que trabalham juntas.

---

## Camadas

```
┌─────────────────────────────────────────┐
│  HERO  —  agente principal (CLAUDE.md)  │
├─────────────────────────────────────────┤
│  OPENSQUAD  —  orquestração de squads   │
├─────────────────────────────────────────┤
│  GSD  —  spec-driven development        │
├──────────────────┬──────────────────────┤
│  COMMANDS (916)  │  AGENTS (353)        │
├──────────────────┴──────────────────────┤
│  HOOKS (28)  —  automações de eventos   │
└─────────────────────────────────────────┘
```

---

## Documentação por componente

| Arquivo | Componente | Descrição |
|---------|-----------|-----------|
| `hero.md` | Hero | Persona, CLAUDE.md, comportamento |
| `opensquad.md` | Opensquad | Squads, pipelines, Orquestrador |
| `gsd.md` | GSD | Spec-driven development, comandos |
| `hooks.md` | Hooks | 28 scripts e quando disparam |
