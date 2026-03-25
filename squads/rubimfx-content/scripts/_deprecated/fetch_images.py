#!/usr/bin/env python3
"""
Busca imagens para carrosséis @rubimfx
Fontes: Unsplash (grátis), Pexels (grátis), download direto
"""
import urllib.request
import urllib.parse
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "output", "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY", "")
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY", "")

def search_unsplash(query, count=3):
    if not UNSPLASH_ACCESS_KEY:
        print("⚠️  UNSPLASH_ACCESS_KEY não configurada")
        return []
    url = f"https://api.unsplash.com/search/photos?query={urllib.parse.quote(query)}&per_page={count}&orientation=portrait"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}",
        "Accept-Version": "v1"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
            results = []
            for photo in data.get("results", []):
                results.append({
                    "id": photo["id"],
                    "url": f"{photo['urls']['regular']}&w=1080&h=1440&fit=crop",
                    "author": photo["user"]["name"],
                    "desc": photo.get("description", "")
                })
            return results
    except Exception as e:
        print(f"Erro Unsplash: {e}")
        return []

def search_pexels(query, count=3):
    if not PEXELS_API_KEY:
        print("⚠️  PEXELS_API_KEY não configurada")
        return []
    url = f"https://api.pexels.com/v1/search?query={urllib.parse.quote(query)}&per_page={count}&orientation=portrait"
    req = urllib.request.Request(url, headers={"Authorization": PEXELS_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
            results = []
            for photo in data.get("photos", []):
                results.append({
                    "id": str(photo["id"]),
                    "url": photo["src"]["large2x"],
                    "author": photo["photographer"],
                    "desc": photo.get("alt", "")
                })
            return results
    except Exception as e:
        print(f"Erro Pexels: {e}")
        return []

def download_image(url, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            with open(filepath, 'wb') as f:
                f.write(resp.read())
        size = os.path.getsize(filepath) // 1024
        print(f"✅ {filename} ({size}KB)")
        return filepath
    except Exception as e:
        print(f"❌ {filename}: {e}")
        return None

def search_all(query, count=3):
    results = search_unsplash(query, count)
    if not results:
        results = search_pexels(query, count)
    if not results:
        print(f"Nenhuma fonte disponível. Configure UNSPLASH_ACCESS_KEY ou PEXELS_API_KEY")
    return results

# Mapeamento de temas para buscas otimizadas
TOPIC_MAP = {
    "economia": ["economy finance dark", "stock market graph", "money inflation"],
    "fed": ["federal reserve", "interest rates finance", "central bank"],
    "dolar": ["us dollar currency", "forex trading screen", "money exchange"],
    "ouro": ["gold bars vault", "gold market trading", "precious metals"],
    "brasil": ["brazil congress brasilia", "sao paulo skyline night", "brazil economy"],
    "mercado": ["stock market screen", "wall street trading", "financial data"],
    "petroleo": ["oil barrel industry", "oil rig ocean", "energy market"],
    "crypto": ["bitcoin digital", "cryptocurrency trading", "blockchain"],
    "eleicoes": ["brazil politics voting", "election democracy", "congress brasilia"],
    "inflacao": ["inflation grocery", "price increase", "cost living"],
    "guerra": ["geopolitics world map", "military strategy", "conflict tension"],
    "china": ["china economy shanghai", "trade war", "asian market"],
    "tecnologia": ["artificial intelligence", "tech innovation", "digital"],
    "trump": ["white house politics", "trade tariffs", "us politics"],
    "juros": ["interest rates bank", "central bank policy", "monetary policy"],
}

def get_queries(topic):
    topic_lower = topic.lower()
    for key, queries in TOPIC_MAP.items():
        if key in topic_lower:
            return queries
    return [topic]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""
Uso: python3 fetch_images.py <comando> [args]

Comandos:
  search <tema>        Busca e baixa imagens para o tema
  download <url> <nome> Baixa imagem de URL direta
  list                  Lista imagens já baixadas
  topics                Mostra temas mapeados

Exemplo:
  python3 fetch_images.py search "federal reserve juros"
  python3 fetch_images.py download "https://..." "capa.jpg"
""")
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "search":
        topic = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "economy"
        queries = get_queries(topic)
        print(f"🔍 Buscando: {topic}")
        print(f"   Queries: {queries}")
        for q in queries:
            results = search_all(q, 2)
            for i, r in enumerate(results):
                ext = "jpg"
                fname = f"{q.replace(' ', '_')}_{i+1}_{r['id']}.{ext}"
                download_image(r["url"], fname)

    elif cmd == "download":
        url = sys.argv[2]
        name = sys.argv[3] if len(sys.argv) > 3 else "image.jpg"
        download_image(url, name)

    elif cmd == "list":
        files = [f for f in os.listdir(OUTPUT_DIR) if not f.startswith('.')]
        print(f"📁 {len(files)} imagens:")
        for f in sorted(files):
            size = os.path.getsize(os.path.join(OUTPUT_DIR, f)) // 1024
            print(f"  {f} ({size}KB)")

    elif cmd == "topics":
        for k, v in TOPIC_MAP.items():
            print(f"  {k}: {v}")
