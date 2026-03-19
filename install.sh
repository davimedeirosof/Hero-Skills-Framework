#!/bin/bash
set -e

# ═══════════════════════════════════════════════════════
# Hero-Skills-Framework — Bootstrap Script
# Replica o setup completo em qualquer maquina
# ═══════════════════════════════════════════════════════

DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
BACKUP_DIR="$HOME/.claude-backup-$(date +%Y%m%d-%H%M%S)"

echo ""
echo "  Hero-Skills-Framework Installer"
echo "  ─────────────────────────"
echo ""

# ─── BACKUP ───
if [ -d "$CLAUDE_DIR" ]; then
  echo "  → Backup do ~/.claude existente em $BACKUP_DIR"
  cp -r "$CLAUDE_DIR" "$BACKUP_DIR"
fi

mkdir -p "$CLAUDE_DIR"
mkdir -p "$CLAUDE_DIR/commands"
mkdir -p "$CLAUDE_DIR/hooks/scripts"
mkdir -p "$CLAUDE_DIR/agents"
mkdir -p "$CLAUDE_DIR/skills"

# ─── 1. COMMANDS (937) ───
echo "  [1/10] Instalando slash commands..."
cp -r "$DOTFILES_DIR/commands/"* "$CLAUDE_DIR/commands/" 2>/dev/null || true
CMD_COUNT=$(find "$CLAUDE_DIR/commands" -name "*.md" | wc -l | tr -d ' ')
echo "         $CMD_COUNT commands instalados"

# ─── 2. AGENTS (344) ───
echo "  [2/10] Instalando agent personas..."
cp -r "$DOTFILES_DIR/agents/"* "$CLAUDE_DIR/agents/" 2>/dev/null || true
AGENT_COUNT=$(find "$CLAUDE_DIR/agents" -name "*.md" | wc -l | tr -d ' ')
echo "         $AGENT_COUNT agents instalados"

# ─── 3. SKILLS (211) ───
echo "  [3/10] Instalando skills..."
cp -r "$DOTFILES_DIR/skills/"* "$CLAUDE_DIR/skills/" 2>/dev/null || true
SKILL_COUNT=$(find "$CLAUDE_DIR/skills" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
echo "         $SKILL_COUNT skills instaladas"

# ─── 4. HOOKS (28) ───
echo "  [4/10] Instalando hook scripts..."
cp -r "$DOTFILES_DIR/hooks/scripts/"* "$CLAUDE_DIR/hooks/scripts/" 2>/dev/null || true
# Copy root-level hook files (GSD hooks)
for f in "$DOTFILES_DIR/hooks/"*.js; do
  [ -f "$f" ] && cp "$f" "$CLAUDE_DIR/hooks/"
done
HOOK_COUNT=$(find "$CLAUDE_DIR/hooks" -name "*.js" | wc -l | tr -d ' ')
echo "         $HOOK_COUNT hooks instalados"

# ─── 5. SETTINGS.JSON ───
echo "  [5/10] Configurando settings.json..."
if [ -f "$CLAUDE_DIR/settings.json" ]; then
  echo "         settings.json ja existe — merging..."
  node -e "
    const fs = require('fs');
    const existing = JSON.parse(fs.readFileSync('$CLAUDE_DIR/settings.json','utf8'));
    const template = JSON.parse(fs.readFileSync('$DOTFILES_DIR/settings.json','utf8'));
    existing.extraKnownMarketplaces = { ...existing.extraKnownMarketplaces, ...template.extraKnownMarketplaces };
    existing.enabledPlugins = { ...existing.enabledPlugins, ...template.enabledPlugins };
    if (!existing.hooks) existing.hooks = template.hooks;
    fs.writeFileSync('$CLAUDE_DIR/settings.json', JSON.stringify(existing, null, 2));
  " 2>/dev/null || cp "$DOTFILES_DIR/settings.json" "$CLAUDE_DIR/settings.json"
else
  cp "$DOTFILES_DIR/settings.json" "$CLAUDE_DIR/settings.json"
fi
echo "         settings.json configurado"

# ─── 5b. CLAUDE.MD (persona Hero) ───
echo "  [5b] Instalando persona Hero (CLAUDE.md)..."
if [ -f "$DOTFILES_DIR/CLAUDE.md" ]; then
  cp "$DOTFILES_DIR/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md"
  echo "         CLAUDE.md instalado — persona Hero ativa"
else
  echo "         CLAUDE.md nao encontrado — pulando"
fi

# ─── 6. MCP CONFIG ───
echo "  [6/10] Configurando .mcp.json..."
if [ -f "$HOME/.mcp.json" ]; then
  echo "         .mcp.json ja existe — preservando"
else
  cp "$DOTFILES_DIR/.mcp.json" "$HOME/.mcp.json" 2>/dev/null || true
  echo "         .mcp.json configurado"
fi

# ─── 7. PROJECT RULES ───
echo "  [7/10] Preparando rules template..."
echo "         Rules disponiveis em $DOTFILES_DIR/project-rules/"
echo "         Copie para seu projeto: cp -r project-rules/ .claude/rules/"

# ─── 8. OPENSQUAD ───
echo "  [8/10] Instalando Opensquad..."
if [ -d "$DOTFILES_DIR/_opensquad" ]; then
  mkdir -p "$HOME/_opensquad"
  cp -r "$DOTFILES_DIR/_opensquad/"* "$HOME/_opensquad/" 2>/dev/null || true
  mkdir -p "$HOME/_opensquad/_memory"
  mkdir -p "$HOME/_opensquad/_browser_profile"
  mkdir -p "$HOME/squads"
  echo "         Opensquad instalado"
else
  echo "         Opensquad nao encontrado — pulando"
fi

# ─── 9. GSD ───
echo "  [9/10] Instalando GSD (Get Shit Done)..."
if command -v npx &>/dev/null; then
  npx get-shit-done-cc --claude --global 2>/dev/null && echo "         GSD instalado" || echo "         GSD: falhou (rode manualmente: npx get-shit-done-cc --claude --global)"
else
  echo "         npx nao encontrado — instale Node.js primeiro"
fi

# ─── 10. EXTERNAL TOOLS ───
echo "  [10/10] Verificando ferramentas externas..."
if command -v brew &>/dev/null; then
  echo "         Instalando Dippy..."
  brew tap ldayton/dippy 2>/dev/null && brew install dippy 2>/dev/null && echo "         Dippy instalado" || echo "         Dippy: ja instalado ou falhou"

  echo "         Instalando Claude Squad..."
  brew install claude-squad 2>/dev/null && echo "         Claude Squad instalado" || echo "         Claude Squad: ja instalado ou falhou"
else
  echo "         brew nao encontrado — instale manualmente:"
  echo "         brew tap ldayton/dippy && brew install dippy"
  echo "         brew install claude-squad"
fi

# ─── RESUMO ───
echo ""
echo "  ═══════════════════════════════════════"
echo "  Instalacao completa!"
echo "  ═══════════════════════════════════════"
echo ""
echo "  Totais:"
echo "    Commands:  $CMD_COUNT"
echo "    Agents:    $AGENT_COUNT"
echo "    Skills:    $SKILL_COUNT"
echo "    Hooks:     $HOOK_COUNT"
echo ""
echo "  Proximos passos (rodar dentro do Claude Code):"
echo ""
echo "  /plugin install planning-with-files@planning-with-files"
echo "  /plugin install claude-hud"
echo "  /claude-hud:setup"
echo "  /plugin install oh-my-claudecode"
echo "  /omc-setup"
echo ""
echo "  Para projetos, copie as rules:"
echo "  cp -r $DOTFILES_DIR/project-rules/ seu-projeto/.claude/rules/"
echo ""
