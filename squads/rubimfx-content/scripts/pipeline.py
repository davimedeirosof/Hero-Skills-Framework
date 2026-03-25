#!/usr/bin/env python3
"""
Pipeline completo de producao de carrossel Instagram.
Executa validacao, render e preflight em sequencia.

Uso:
  python pipeline.py <pasta-do-post>
  python pipeline.py ../output/posts/2026-03-17-proteja-sanidade

Passos:
  1. Verifica/copia profile-photo.jpeg para html/
  2. Valida fontes (validate_fonts_html.py)
  3. Valida acentos (validate_accents.py)
  4. Renderiza slides (render_slides.py)
  5. Preflight check (preflight_check.py)
  6. Imprime resumo de sucesso
"""

import os
import sys
import shutil
import subprocess


def run_step(step_num, description, cmd, cwd=None):
    """Executa um passo do pipeline. Sai com erro se falhar."""
    print(f"\n{'=' * 50}")
    print(f"PASSO {step_num}: {description}")
    print(f"{'=' * 50}\n")

    result = subprocess.run(cmd, cwd=cwd)

    if result.returncode != 0:
        print(f"\n{'=' * 50}")
        print(f"PIPELINE PARADO no passo {step_num}: {description}")
        print(f"Corrija os erros acima e rode novamente.")
        print(f"{'=' * 50}")
        sys.exit(1)

    return True


def main():
    if len(sys.argv) < 2:
        print("Uso: python pipeline.py <pasta-do-post>")
        print("Ex:  python pipeline.py ../output/posts/2026-03-17-proteja-sanidade")
        sys.exit(1)

    post_dir = os.path.abspath(sys.argv[1])
    html_dir = os.path.join(post_dir, "html")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(os.path.dirname(script_dir), "assets")

    if not os.path.isdir(html_dir):
        print(f"Pasta html/ nao encontrada em {post_dir}")
        sys.exit(1)

    print(f"PIPELINE DE PRODUCAO — {os.path.basename(post_dir)}")
    print(f"{'=' * 50}")

    # ── Passo 1: profile-photo.jpeg ──
    print(f"\n{'=' * 50}")
    print(f"PASSO 1: Verificar profile-photo.jpeg")
    print(f"{'=' * 50}\n")

    photo_dest = os.path.join(html_dir, "profile-photo.jpeg")
    photo_source = os.path.join(assets_dir, "profile-photo.jpeg")

    if os.path.isfile(photo_dest):
        print(f"  OK: profile-photo.jpeg ja existe em html/")
    elif os.path.isfile(photo_source):
        shutil.copy2(photo_source, photo_dest)
        print(f"  COPIADO: assets/profile-photo.jpeg -> html/profile-photo.jpeg")
    else:
        print(f"  ERRO: profile-photo.jpeg nao encontrada em assets/ nem em html/")
        print(f"  Coloque o arquivo em: {photo_source}")
        sys.exit(1)

    # ── Passo 2: Validar fontes ──
    run_step(
        2, "Validar tamanhos de fonte (min 22px)",
        [sys.executable, os.path.join(script_dir, "validate_fonts_html.py"), html_dir, "--min", "22"]
    )

    # ── Passo 3: Validar acentos ──
    run_step(
        3, "Validar acentos do portugues",
        [sys.executable, os.path.join(script_dir, "validate_accents.py"), html_dir]
    )

    # ── Passo 4: Renderizar slides ──
    run_step(
        4, "Renderizar slides HTML -> PNG (1080x1350)",
        [sys.executable, os.path.join(script_dir, "render_slides.py"), post_dir]
    )

    # ── Passo 5: Preflight check ──
    run_step(
        5, "Preflight check completo",
        [sys.executable, os.path.join(script_dir, "preflight_check.py"), post_dir]
    )

    # ── Sucesso ──
    print(f"\n{'=' * 50}")
    print(f"READY TO PUBLISH")
    print(f"{'=' * 50}")
    print(f"  Post: {os.path.basename(post_dir)}")
    print(f"  HTML: {html_dir}")
    print(f"  PNG:  {os.path.join(post_dir, 'png')}")
    print(f"  Todos os 5 passos passaram com sucesso.")
    print(f"  Proximo: publicar via Playwright MCP")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
