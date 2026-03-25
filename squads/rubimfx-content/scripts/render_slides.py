#!/usr/bin/env python3
"""
Renderiza slides HTML para PNG via http.server + npx playwright screenshot.
Dimensão: 1080x1350px (4:5 Instagram feed).

Uso:
  python render_slides.py <pasta-do-post>
  python render_slides.py ../output/posts/2026-03-16-ouro-5000

Ele:
1. Inicia http.server na pasta html/
2. Renderiza cada slide-XX.html como PNG 1080x1350
3. Salva em png/
4. Para o servidor
"""

import subprocess
import os
import sys
import glob
import time
import signal

WIDTH = 1080
HEIGHT = 1350  # 4:5 ratio — NUNCA usar 1440!
PORT = 8899


def find_free_port(start=8899):
    """Encontra porta livre."""
    import socket
    for port in range(start, start + 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    return start


def render_post(post_dir):
    """Renderiza todos os slides de um post."""
    post_dir = os.path.abspath(post_dir)
    html_dir = os.path.join(post_dir, "html")
    png_dir = os.path.join(post_dir, "png")

    if not os.path.isdir(html_dir):
        print(f"❌ Pasta html/ não encontrada em {post_dir}")
        sys.exit(1)

    os.makedirs(png_dir, exist_ok=True)

    # Encontrar slides
    html_files = sorted(glob.glob(os.path.join(html_dir, "slide-*.html")))
    if not html_files:
        print(f"❌ Nenhum slide-*.html encontrado em {html_dir}")
        sys.exit(1)

    print(f"🎨 Renderizando {len(html_files)} slides de: {os.path.basename(post_dir)}")
    print(f"📐 Dimensão: {WIDTH}x{HEIGHT}px (4:5)")

    # Iniciar servidor
    port = find_free_port(PORT)
    print(f"🌐 Iniciando servidor na porta {port}...")
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port)],
        cwd=html_dir,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1)

    success = 0
    errors = []

    try:
        for html_path in html_files:
            basename = os.path.basename(html_path).replace(".html", "")
            png_path = os.path.join(png_dir, f"{basename}.png")
            url = f"http://localhost:{port}/{os.path.basename(html_path)}"

            result = subprocess.run(
                ["npx", "playwright", "screenshot",
                 f"--viewport-size={WIDTH},{HEIGHT}", url, png_path],
                capture_output=True, text=True, timeout=30,
            )

            if result.returncode == 0 and os.path.exists(png_path):
                size_kb = os.path.getsize(png_path) // 1024
                print(f"  ✅ {basename}.png ({size_kb}KB)")
                success += 1
            else:
                print(f"  ❌ {basename} — erro no render")
                errors.append(basename)

    finally:
        server.terminate()
        server.wait()

    print(f"\n{'=' * 40}")
    print(f"✅ {success}/{len(html_files)} slides renderizados")
    if errors:
        print(f"❌ Erros: {', '.join(errors)}")
    print(f"📁 PNGs em: {png_dir}")

    # Validar dimensões
    print(f"\n🔍 Validando dimensões...")
    for png_file in sorted(glob.glob(os.path.join(png_dir, "slide-*.png"))):
        result = subprocess.run(
            ["file", png_file], capture_output=True, text=True
        )
        if f"{WIDTH} x {HEIGHT}" in result.stdout:
            print(f"  ✅ {os.path.basename(png_file)}: {WIDTH}x{HEIGHT}")
        else:
            print(f"  ⚠️  {os.path.basename(png_file)}: DIMENSÃO ERRADA — {result.stdout.strip()}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python render_slides.py <pasta-do-post>")
        print("Ex:  python render_slides.py ../output/posts/2026-03-16-ouro-5000")
        sys.exit(1)

    render_post(sys.argv[1])
