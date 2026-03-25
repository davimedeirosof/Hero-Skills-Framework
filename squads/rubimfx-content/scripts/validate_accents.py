#!/usr/bin/env python3
"""
Validador de acentos do português brasileiro para slides HTML.
Detecta palavras que DEVEM ter acento mas não têm.

Uso:
  python validate_accents.py <pasta-html>
  python validate_accents.py ../output/posts/2026-03-16-ouro-5000/html/

Retorna exit code 1 se encontrar erros (bloqueia pipeline).
"""

import os
import sys
import re
import glob

# Mapa: palavra errada → correção
ACCENT_RULES = {
    # Verbos e palavras comuns
    r'\bnao\b': 'não',
    r'\bvoce\b': 'você',
    r'\bvoces\b': 'vocês',
    r'\btambem\b': 'também',
    r'\bate\b': 'até',
    r'\bja\b': 'já',
    r'\bso\b': 'só',
    r'\bapos\b': 'após',
    r'\bporem\b': 'porém',
    r'\bsera\b': 'será',
    r'\besta\b': 'está',
    r'\bestao\b': 'estão',
    r'\bfacil\b': 'fácil',
    r'\bdificil\b': 'difícil',
    r'\bpossivel\b': 'possível',
    r'\butil\b': 'útil',

    # Substantivos e adjetivos
    r'\bpadrao\b': 'padrão',
    r'\boperacao\b': 'operação',
    r'\boperacoes\b': 'operações',
    r'\bgestao\b': 'gestão',
    r'\banalise\b': 'análise',
    r'\bdecisao\b': 'decisão',
    r'\bconsequencia\b': 'consequência',
    r'\bcenario\b': 'cenário',
    r'\bdirecao\b': 'direção',
    r'\bpunicao\b': 'punição',
    r'\bcorrupcao\b': 'corrupção',
    r'\binflacao\b': 'inflação',
    r'\bmanipulacao\b': 'manipulação',
    r'\bsobrevivencia\b': 'sobrevivência',
    r'\bexperiencia\b': 'experiência',

    # Adjetivos
    r'\brigido\b': 'rígido',
    r'\bvolatil\b': 'volátil',
    r'\bnecessario\b': 'necessário',
    r'\bpublico\b': 'público',

    # Substantivos de nicho
    r'\bsalario\b': 'salário',
    r'\bjudiciario\b': 'judiciário',
    r'\bcompulsoria\b': 'compulsória',
    r'\bmagistrado\b': 'magistrado',  # sem acento, OK
    r'\binfracao\b': 'infração',
    r'\bgrafico\b': 'gráfico',
    r'\bruido\b': 'ruído',

    # Tempo
    r'\btercas\b': 'terças',
    r'\bmarco\b': 'março',  # cuidado: nome próprio Marco não leva acento

    # Pronomes
    r'\bninguem\b': 'ninguém',
    r'\balguem\b': 'alguém',

    # Substantivos financeiros/politicos
    r'\breducao\b': 'redução',
    r'\bisencao\b': 'isenção',
    r'\btributacao\b': 'tributação',
    r'\barrecadacao\b': 'arrecadação',
    r'\bproducao\b': 'produção',
    r'\bpopulacao\b': 'população',
    r'\bnacao\b': 'nação',
    r'\bprecos\b': 'preços',
    r'\bdecisoes\b': 'decisões',

    # Preposições e conectivos com acento
    r'\balem\b': 'além',
    r'\bporem\b': 'porém',
    r'\bentao\b': 'então',
}

# Contextos CSS/HTML a ignorar (não validar dentro de propriedades CSS)
CSS_PATTERNS = re.compile(
    r'(font-size|font-family|font-weight|line-height|letter-spacing|'
    r'background|border|margin|padding|color|display|position|'
    r'width|height|overflow|text-align|box-sizing|content|'
    r'class=|id=|src=|href=|style=|var\(--|rgba|#[0-9a-fA-F])',
    re.IGNORECASE
)


def is_text_line(line):
    """Verifica se a linha contém texto visível (não CSS/HTML puro)."""
    stripped = line.strip()
    # Pular linhas vazias, CSS puro, tags HTML sem texto
    if not stripped:
        return False
    if stripped.startswith('/*') or stripped.startswith('*') or stripped.startswith('//'):
        return False
    if stripped.startswith('<style') or stripped.startswith('</style'):
        return False
    if CSS_PATTERNS.search(stripped):
        return False
    # Tem texto alfanumérico?
    if re.search(r'[a-záéíóúâêôãõç]{3,}', stripped, re.IGNORECASE):
        return True
    return False


def validate_file(filepath):
    """Valida um arquivo HTML e retorna lista de erros."""
    errors = []
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_style = False
    for line_num, line in enumerate(lines, 1):
        # Rastrear blocos <style>
        if '<style' in line.lower():
            in_style = True
        if '</style' in line.lower():
            in_style = False
            continue
        if in_style:
            continue

        # Só validar linhas com texto visível
        if not is_text_line(line):
            continue

        # Extrair texto visível (fora de tags HTML)
        text = re.sub(r'<[^>]+>', ' ', line)
        text = text.lower()

        for pattern, correct in ACCENT_RULES.items():
            matches = list(re.finditer(pattern, text, re.IGNORECASE))
            for match in matches:
                word = match.group()
                # Ignorar se já tem acento (padrão regex pode pegar versão correta)
                if word == correct.lower():
                    continue
                errors.append({
                    'file': filename,
                    'line': line_num,
                    'word': word,
                    'correct': correct,
                    'context': line.strip()[:80],
                })

    return errors


def main():
    if len(sys.argv) < 2:
        print("Uso: python validate_accents.py <pasta-html>")
        print("Ex:  python validate_accents.py ../output/posts/2026-03-16-ouro-5000/html/")
        sys.exit(1)

    html_dir = os.path.abspath(sys.argv[1])
    html_files = sorted(glob.glob(os.path.join(html_dir, "slide-*.html")))

    if not html_files:
        print(f"❌ Nenhum slide-*.html encontrado em {html_dir}")
        sys.exit(1)

    print(f"🔍 Validando acentos em {len(html_files)} arquivos...\n")

    total_errors = []
    for filepath in html_files:
        errors = validate_file(filepath)
        total_errors.extend(errors)

    if total_errors:
        print(f"❌ {len(total_errors)} ERROS DE ACENTO ENCONTRADOS:\n")
        for err in total_errors:
            print(f"  {err['file']}:{err['line']} — '{err['word']}' → '{err['correct']}'")
            print(f"    {err['context']}")
            print()

        print(f"{'=' * 40}")
        print(f"❌ BLOQUEADO: Corrija {len(total_errors)} erros antes de renderizar.")
        print(f"\nDica: Use sed para corrigir em lote:")
        seen = set()
        for err in total_errors:
            key = (err['word'], err['correct'])
            if key not in seen:
                seen.add(key)
                print(f"  sed -i '' 's/\\b{err['word']}\\b/{err['correct']}/g' slide-*.html")
        sys.exit(1)
    else:
        print(f"✅ Todos os {len(html_files)} arquivos passaram na validação de acentos!")
        sys.exit(0)


if __name__ == "__main__":
    main()
