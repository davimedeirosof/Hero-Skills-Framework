#!/usr/bin/env python3
"""
Checklist pré-publicação para carrosséis Instagram.
Valida TUDO antes de publicar: PNGs, dimensões, acentos, caption, fontes.

Uso:
  python preflight_check.py <pasta-do-post>
  python preflight_check.py ../output/posts/2026-03-16-ouro-5000

Retorna exit code 1 se qualquer check falhar.
"""

import os
import sys
import re
import glob
import subprocess


class PreflightChecker:
    def __init__(self, post_dir):
        self.post_dir = os.path.abspath(post_dir)
        self.html_dir = os.path.join(self.post_dir, "html")
        self.png_dir = os.path.join(self.post_dir, "png")
        self.caption_file = os.path.join(self.post_dir, "POSTAR-AGORA.md")
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.errors = []

    def check(self, name, condition, error_msg=""):
        """Registra resultado de um check."""
        if condition:
            print(f"  ✅ {name}")
            self.passed += 1
        else:
            print(f"  ❌ {name} — {error_msg}")
            self.failed += 1
            self.errors.append(f"{name}: {error_msg}")

    def warn(self, name, msg):
        """Registra warning (não bloqueia)."""
        print(f"  ⚠️  {name} — {msg}")
        self.warnings += 1

    def run(self):
        """Executa todos os checks."""
        print(f"🔍 PRE-FLIGHT CHECK: {os.path.basename(self.post_dir)}")
        print(f"{'=' * 50}\n")

        self.check_structure()
        self.check_pngs()
        self.check_dimensions()
        self.check_caption()
        self.check_accents()
        self.check_font_sizes()
        self.check_placeholders()
        self.check_profile_photo()
        self.check_images_loaded()
        self.check_external_urls()

        self.print_summary()
        return self.failed == 0

    def check_structure(self):
        """1. Verifica estrutura de pastas."""
        print("📁 1. ESTRUTURA DE PASTAS")
        self.check("Pasta html/ existe", os.path.isdir(self.html_dir), "Pasta html/ não encontrada")
        self.check("Pasta png/ existe", os.path.isdir(self.png_dir), "Pasta png/ não encontrada")
        self.check("POSTAR-AGORA.md existe", os.path.isfile(self.caption_file), "Caption não encontrada")

        html_count = len(glob.glob(os.path.join(self.html_dir, "slide-*.html")))
        self.check(f"Slides HTML: {html_count} arquivos", html_count >= 6, f"Apenas {html_count} slides (mínimo 6)")
        print()

    def check_pngs(self):
        """2. Verifica se todos os PNGs existem."""
        print("🖼️  2. PNGs RENDERIZADOS")
        html_files = sorted(glob.glob(os.path.join(self.html_dir, "slide-*.html")))
        png_files = sorted(glob.glob(os.path.join(self.png_dir, "slide-*.png")))

        self.check(
            f"PNGs: {len(png_files)} arquivos",
            len(png_files) == len(html_files),
            f"{len(png_files)} PNGs para {len(html_files)} HTMLs"
        )

        for html_path in html_files:
            basename = os.path.basename(html_path).replace(".html", ".png")
            png_path = os.path.join(self.png_dir, basename)
            if not os.path.exists(png_path):
                self.check(f"  {basename}", False, "PNG não encontrado")
            else:
                size_kb = os.path.getsize(png_path) // 1024
                if size_kb < 100:
                    self.check(f"  {basename} ({size_kb}KB)", False, "PNG muito pequeno (render falhou?)")
        print()

    def check_dimensions(self):
        """3. Verifica dimensões de todos os PNGs."""
        print("📐 3. DIMENSÕES (1080x1350)")
        png_files = sorted(glob.glob(os.path.join(self.png_dir, "slide-*.png")))

        for png_path in png_files:
            result = subprocess.run(["file", png_path], capture_output=True, text=True)
            basename = os.path.basename(png_path)
            if "1080 x 1350" in result.stdout:
                self.check(f"  {basename}: 1080x1350", True)
            else:
                # Extrair dimensões reais
                dims = re.search(r'(\d+) x (\d+)', result.stdout)
                if dims:
                    self.check(f"  {basename}", False, f"Dimensão errada: {dims.group(1)}x{dims.group(2)}")
                else:
                    self.check(f"  {basename}", False, "Não foi possível verificar dimensão")
        print()

    def check_caption(self):
        """4. Verifica caption."""
        print("📝 4. CAPTION")

        if not os.path.isfile(self.caption_file):
            self.check("Caption existe", False, "POSTAR-AGORA.md não encontrado")
            print()
            return

        with open(self.caption_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extrair caption (após "## CAPTION")
        match = re.search(r'## CAPTION.*?\n\n(.+)', content, re.DOTALL)
        caption = match.group(1).strip() if match else content

        char_count = len(caption)
        self.check(f"Tamanho: {char_count} chars", 50 <= char_count <= 2200, f"Fora do limite (50-2200)")

        # Contar hashtags
        hashtags = re.findall(r'#\w+', caption)
        self.check(f"Hashtags: {len(hashtags)}", 5 <= len(hashtags) <= 30, f"{len(hashtags)} hashtags (ideal: 10-15)")

        # Verificar @rubimfx
        self.check("Menciona @rubimfx", "@rubimfx" in caption, "Sem menção ao @rubimfx")

        # Verificar CTA
        cta_words = ["segue", "salva", "comenta", "compartilha", "manda", "arrasta"]
        has_cta = any(word in caption.lower() for word in cta_words)
        self.check("Tem CTA (segue/salva/comenta)", has_cta, "Sem call-to-action")
        print()

    def check_accents(self):
        """5. Verifica acentos do português."""
        print("🇧🇷 5. ACENTOS DO PORTUGUÊS")

        # Usar o script validate_accents.py
        script_dir = os.path.dirname(os.path.abspath(__file__))
        validate_script = os.path.join(script_dir, "validate_accents.py")

        if os.path.exists(validate_script):
            result = subprocess.run(
                [sys.executable, validate_script, self.html_dir],
                capture_output=True, text=True,
            )
            if result.returncode == 0:
                self.check("Acentos OK", True)
            else:
                error_count = result.stdout.count("→")
                self.check("Acentos", False, f"{error_count} erros de acento encontrados")
                # Mostrar primeiros 3 erros
                lines = [l for l in result.stdout.split('\n') if '→' in l]
                for line in lines[:3]:
                    print(f"    {line.strip()}")
                if len(lines) > 3:
                    print(f"    ... e mais {len(lines) - 3} erros")
        else:
            self.warn("Acentos", "Script validate_accents.py não encontrado")
        print()

    def check_font_sizes(self):
        """6. Verifica tamanhos mínimos de fonte via validate_fonts_html.py."""
        print("🔤 6. TAMANHO DE FONTES (mín 22px)")

        # Usar o script validate_fonts_html.py que tem awareness de excecoes decorativas
        script_dir = os.path.dirname(os.path.abspath(__file__))
        validate_script = os.path.join(script_dir, "validate_fonts_html.py")

        if os.path.exists(validate_script):
            result = subprocess.run(
                [sys.executable, validate_script, self.html_dir, "--min", "22"],
                capture_output=True, text=True,
            )
            if result.returncode == 0:
                self.check("Fontes OK (≥ 22px, decorativos excluídos)", True)
            else:
                # Contar violacoes
                violation_lines = [l for l in result.stdout.split('\n') if ' -> ' in l and 'px' in l]
                error_count = len(violation_lines)
                self.check("Fontes mínimas", False, f"{error_count} fontes abaixo de 22px (não-decorativas)")
                for line in violation_lines[:5]:
                    print(f"    {line.strip()}")
                if len(violation_lines) > 5:
                    print(f"    ... e mais {len(violation_lines) - 5} erros")
        else:
            # Fallback: validacao simples (sem awareness de excecoes)
            self.warn("Fontes", "Script validate_fonts_html.py não encontrado — usando check básico")
            html_files = sorted(glob.glob(os.path.join(self.html_dir, "slide-*.html")))
            small_fonts = []
            for filepath in html_files:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                sizes = re.findall(r'font-size:\s*(\d+)px', content)
                for size in sizes:
                    if int(size) < 20:
                        small_fonts.append((os.path.basename(filepath), int(size)))
            if small_fonts:
                self.check(f"Fontes mínimas", False, f"{len(small_fonts)} fontes abaixo de 20px")
                for filename, size in small_fonts[:5]:
                    print(f"    {filename}: {size}px")
            else:
                self.check("Todas as fontes ≥ 20px", True)
        print()

    def check_placeholders(self):
        """7. Verifica se restou algum placeholder {{}}."""
        print("🔧 7. PLACEHOLDERS RESTANTES")

        html_files = sorted(glob.glob(os.path.join(self.html_dir, "slide-*.html")))
        leftover = []

        for filepath in html_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = re.findall(r'\{\{[A-Z_]+\}\}', content)
            if matches:
                leftover.append((os.path.basename(filepath), matches))

        if leftover:
            self.check("Sem placeholders", False, f"Placeholders não substituídos")
            for filename, placeholders in leftover:
                print(f"    {filename}: {', '.join(set(placeholders))}")
        else:
            self.check("Sem placeholders restantes", True)
        print()

    def check_profile_photo(self):
        """8. Verifica profile photo."""
        print("👤 8. PROFILE PHOTO")

        photo_path = os.path.join(self.html_dir, "profile-photo.jpeg")
        self.check("profile-photo.jpeg existe em html/", os.path.isfile(photo_path), "Copie de assets/")

        # Verificar que nenhum HTML usa ../
        html_files = sorted(glob.glob(os.path.join(self.html_dir, "slide-*.html")))
        bad_paths = []
        for filepath in html_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if '../profile-photo' in content:
                bad_paths.append(os.path.basename(filepath))

        self.check("Sem ../ no path da foto", len(bad_paths) == 0,
                    f"Arquivos com path errado: {', '.join(bad_paths)}")
        print()

    def check_images_loaded(self):
        """9. Verifica se imagens referenciadas existem."""
        print("🖼️  9. IMAGENS REFERENCIADAS")

        html_files = sorted(glob.glob(os.path.join(self.html_dir, "slide-*.html")))
        missing = []

        for filepath in html_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            # Encontrar src="xxx.jpg" ou src="xxx.jpeg" ou src="xxx.png"
            images = re.findall(r'src="([^"]+\.(?:jpg|jpeg|png|webp))"', content)
            for img in images:
                img_path = os.path.join(self.html_dir, img)
                if not os.path.isfile(img_path):
                    missing.append((os.path.basename(filepath), img))

        if missing:
            self.check("Todas as imagens existem", False, f"{len(missing)} imagens faltando")
            for filename, img in missing[:5]:
                print(f"    {filename} → {img}")
        else:
            self.check("Todas as imagens existem", True)
        print()

    def check_external_urls(self):
        """10. Verifica se há URLs externas (Unsplash, Pexels, CDNs) nos HTMLs."""
        print("🌐 10. URLs EXTERNAS (proibidas)")

        html_files = sorted(glob.glob(os.path.join(self.html_dir, "slide-*.html")))
        external_refs = []

        # Padroes de URLs externas proibidas
        blocked_patterns = [
            r'https?://images\.unsplash\.com',
            r'https?://unsplash\.com',
            r'https?://images\.pexels\.com',
            r'https?://www\.pexels\.com',
            r'https?://cdn\.pixabay\.com',
            r'https?://source\.unsplash\.com',
            r'https?://picsum\.photos',
            r'https?://via\.placeholder\.com',
        ]
        combined_pattern = '|'.join(blocked_patterns)

        for filepath in html_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = re.findall(combined_pattern, content)
            if matches:
                for url in matches:
                    external_refs.append((os.path.basename(filepath), url))

        if external_refs:
            self.check("Sem URLs externas", False,
                        f"{len(external_refs)} URLs externas encontradas (Unsplash/Pexels/CDN)")
            for filename, url in external_refs[:5]:
                print(f"    {filename} → {url}")
            if len(external_refs) > 5:
                print(f"    ... e mais {len(external_refs) - 5}")
        else:
            self.check("Sem URLs externas (Unsplash/Pexels/CDN)", True)
        print()

    def print_summary(self):
        """Imprime resumo final."""
        print(f"{'=' * 50}")
        print(f"📊 RESULTADO FINAL")
        print(f"{'=' * 50}")
        print(f"  ✅ Passou: {self.passed}")
        print(f"  ❌ Falhou: {self.failed}")
        print(f"  ⚠️  Avisos: {self.warnings}")
        print()

        if self.failed == 0:
            print(f"🟢 PRONTO PARA PUBLICAR!")
            print(f"   Rode: publicar via Playwright MCP")
        else:
            print(f"🔴 NÃO PUBLICAR — {self.failed} problemas encontrados:")
            for err in self.errors:
                print(f"   → {err}")
        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python preflight_check.py <pasta-do-post>")
        print("Ex:  python preflight_check.py ../output/posts/2026-03-16-ouro-5000")
        sys.exit(1)

    checker = PreflightChecker(sys.argv[1])
    success = checker.run()
    sys.exit(0 if success else 1)
