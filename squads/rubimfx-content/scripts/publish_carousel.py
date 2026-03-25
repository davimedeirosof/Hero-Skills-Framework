#!/usr/bin/env python3
"""
Publicador automático de carrosséis no Instagram via Instagrapi.
Uso: python publish_carousel.py <pasta-do-post> [username] [--confirm]
  --confirm   Pula confirmação interativa
  Senha via: IG_PASSWORD env var ou prompt interativo
Exemplo: IG_PASSWORD=xxx python publish_carousel.py ../output/posts/2026-03-16-ouro-5000 --confirm
"""

import sys
import os
import re
import json
from pathlib import Path
from getpass import getpass

from instagrapi import Client

# Diretório para salvar sessão do Instagram
SCRIPT_DIR = Path(__file__).parent
SESSION_FILE = SCRIPT_DIR / "ig_session.json"


def load_or_login(username: str) -> Client:
    """Carrega sessão salva ou faz login novo."""
    cl = Client()
    cl.delay_range = [1, 3]  # delay entre requests (anti-ban)

    if SESSION_FILE.exists():
        print(f"📂 Carregando sessão salva de {SESSION_FILE.name}...")
        try:
            cl.load_settings(SESSION_FILE)
            cl.login(username, "")  # relogin com sessão
            cl.get_timeline_feed()  # teste de conexão
            print("✅ Sessão válida!")
            return cl
        except Exception as e:
            print(f"⚠️  Sessão expirada ({e}). Fazendo login novo...")

    password = os.environ.get("IG_PASSWORD") or getpass(f"🔑 Senha do Instagram (@{username}): ")
    verification_code = os.environ.get("IG_2FA_CODE", "")
    try:
        cl.login(username, password, verification_code=verification_code)
    except Exception as e:
        if "two-factor" in str(e).lower() and not verification_code:
            print("⚠️  2FA ativado. Rode novamente com IG_2FA_CODE=<codigo>")
            print("  Exemplo: IG_PASSWORD='xxx' IG_2FA_CODE=123456 python publish_carousel.py ...")
            sys.exit(1)
        raise
    cl.dump_settings(SESSION_FILE)
    print(f"✅ Login OK! Sessão salva em {SESSION_FILE.name}")
    return cl


def extract_caption(post_dir: Path) -> str:
    """Extrai caption do arquivo POSTAR-AGORA.md."""
    postar_file = post_dir / "POSTAR-AGORA.md"
    if not postar_file.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {postar_file}")

    text = postar_file.read_text(encoding="utf-8")

    # Extrai tudo entre "## CAPTION" e o fim do arquivo
    match = re.search(r"## CAPTION.*?\n\n(.+)", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Fallback: pega tudo depois do primeiro bloco de metadados
    lines = text.strip().split("\n")
    caption_lines = []
    in_caption = False
    for line in lines:
        if line.startswith("## CAPTION"):
            in_caption = True
            continue
        if in_caption:
            caption_lines.append(line)
    return "\n".join(caption_lines).strip()


def get_png_files(post_dir: Path) -> list[Path]:
    """Retorna PNGs ordenados numericamente."""
    png_dir = post_dir / "png"
    if not png_dir.exists():
        raise FileNotFoundError(f"Pasta png/ não encontrada em {post_dir}")

    files = sorted(png_dir.glob("slide-*.png"))
    if not files:
        raise FileNotFoundError(f"Nenhum slide-*.png encontrado em {png_dir}")

    return files


def publish(post_dir: Path, username: str, auto_confirm: bool = False):
    """Publica carrossel no Instagram."""
    print(f"\n📁 Post: {post_dir.name}")

    # 1. Coleta PNGs
    pngs = get_png_files(post_dir)
    print(f"🖼️  {len(pngs)} slides encontrados")
    for p in pngs:
        print(f"   → {p.name}")

    # 2. Extrai caption
    caption = extract_caption(post_dir)
    print(f"\n📝 Caption ({len(caption)} chars):")
    print(caption[:200] + ("..." if len(caption) > 200 else ""))

    # 3. Confirmação
    if not auto_confirm:
        resp = input("\n🚀 Publicar agora? (s/n): ").strip().lower()
        if resp not in ("s", "sim", "y", "yes"):
            print("❌ Cancelado.")
            return
    else:
        print("\n🚀 Publicando (--confirm)...")

    # 4. Login
    cl = load_or_login(username)

    # 5. Upload do carrossel
    print("\n⏳ Enviando carrossel...")
    media = cl.album_upload(
        paths=[str(p) for p in pngs],
        caption=caption,
    )

    print(f"\n✅ Publicado com sucesso!")
    print(f"📱 https://www.instagram.com/p/{media.code}/")

    # Salva registro
    log_file = post_dir / "published.json"
    log_file.write_text(json.dumps({
        "media_id": str(media.id),
        "media_code": media.code,
        "url": f"https://www.instagram.com/p/{media.code}/",
        "slides": len(pngs),
        "caption_length": len(caption),
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"📋 Log salvo em {log_file.name}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python publish_carousel.py <pasta-do-post> [username]")
        print("Exemplo: python publish_carousel.py ../output/posts/2026-03-16-ouro-5000")
        sys.exit(1)

    post_dir = Path(sys.argv[1]).resolve()
    if not post_dir.exists():
        print(f"❌ Pasta não encontrada: {post_dir}")
        sys.exit(1)

    args = sys.argv[2:]
    auto_confirm = "--confirm" in args
    username = next((a for a in args if not a.startswith("--")), "rubimfx")

    publish(post_dir, username, auto_confirm)


if __name__ == "__main__":
    main()
