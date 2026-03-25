#!/usr/bin/env python3
"""
Gerador de slides HTML para carrosséis @rubimfx
Gera HTML 1080x1440 pronto para screenshot via Playwright
Suporta: capa com foto, dados, contexto, bridge, CTA
"""
import os
import sys
import json
import base64

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "output", "slides")
IMAGES_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "output", "images")
ASSETS_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# CSS Base compartilhado por todos os slides
CSS_BASE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    width: 1080px;
    height: 1440px;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #FFFFFF;
    overflow: hidden;
    position: relative;
}

/* Header Bar */
.header {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 48px;
    z-index: 10;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.header-left {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 15px;
    font-weight: 600;
    color: rgba(255,255,255,0.7);
    letter-spacing: 0.5px;
}
.header-left img {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    object-fit: cover;
}
.header-right {
    font-size: 13px;
    color: rgba(255,255,255,0.4);
    font-weight: 500;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Badge */
.badge {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.badge-macro { background: #E94560; }
.badge-trading { background: #3B82F6; }
.badge-dados { background: #F59E0B; }
.badge-brasil { background: #22C55E; }

/* Watermark */
.watermark {
    position: absolute;
    bottom: 36px;
    right: 48px;
    font-size: 13px;
    color: rgba(255,255,255,0.2);
    font-weight: 500;
}

/* Page number */
.page-num {
    position: absolute;
    bottom: 36px;
    left: 48px;
    font-size: 13px;
    color: rgba(255,255,255,0.25);
    font-weight: 500;
}

/* Swipe indicator */
.swipe {
    position: absolute;
    bottom: 36px;
    right: 48px;
    font-size: 13px;
    color: rgba(255,255,255,0.35);
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 6px;
}
"""

def generate_cover(title, subtitle="", badge="MACRO", image_path=None, date="MAR 2026", profile_img=None):
    """Gera slide de capa com foto + overlay"""
    
    bg_style = "background: linear-gradient(135deg, #0D1117 0%, #1A1B2E 50%, #0A0E1A 100%);"
    overlay = ""
    
    if image_path and os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            img_data = base64.b64encode(f.read()).decode()
        ext = image_path.split('.')[-1]
        mime = f"image/{'jpeg' if ext in ('jpg','jpeg') else ext}"
        bg_style = f"background: url('data:{mime};base64,{img_data}') center/cover no-repeat;"
        overlay = """
        <div style="position:absolute;top:0;left:0;right:0;bottom:0;
            background:linear-gradient(180deg, rgba(10,14,26,0.85) 0%, rgba(10,14,26,0.6) 40%, rgba(10,14,26,0.9) 100%);
            z-index:1;"></div>
        """
    
    # Destacar última palavra em accent color
    words = title.split()
    if len(words) > 1:
        title_html = " ".join(words[:-1]) + f' <span style="color:#F59E0B">{words[-1]}</span>'
    else:
        title_html = title

    badge_class = f"badge-{'macro' if 'MACRO' in badge.upper() else 'trading' if 'TRAD' in badge.upper() else 'dados' if 'DADO' in badge.upper() else 'brasil'}"
    
    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>
{CSS_BASE}
body {{ {bg_style} }}
.content {{
    position: relative; z-index: 5;
    display: flex; flex-direction: column;
    justify-content: center; align-items: flex-start;
    height: 100%; padding: 120px 64px 100px;
}}
.cover-badge {{ margin-bottom: 32px; }}
.cover-title {{
    font-family: 'Inter', sans-serif;
    font-weight: 900; font-size: 56px;
    line-height: 1.15; max-width: 920px;
    margin-bottom: 24px;
    text-shadow: 0 2px 20px rgba(0,0,0,0.5);
}}
.cover-subtitle {{
    font-size: 20px; font-weight: 400;
    color: rgba(255,255,255,0.7);
    max-width: 700px; line-height: 1.6;
    border-left: 3px solid #F59E0B;
    padding-left: 16px;
}}
</style></head><body>
{overlay}
<div class="header" style="z-index:10">
    <div class="header-left">@rubimfx · Economia & Trading</div>
    <div class="header-right">{date}</div>
</div>
<div class="content">
    <div class="cover-badge"><span class="badge {badge_class}">{badge}</span></div>
    <div class="cover-title">{title_html}</div>
    {"<div class='cover-subtitle'>" + subtitle + "</div>" if subtitle else ""}
</div>
<div class="swipe" style="z-index:10">DESLIZE ▸</div>
</body></html>"""


def generate_context(title, body, highlight="", page="2/10", date="MAR 2026", bg="#0D1117"):
    """Gera slide de contexto/explicação"""
    highlight_html = ""
    if highlight:
        highlight_html = f"""<div style="
            font-family:'JetBrains Mono',monospace;font-weight:700;
            font-size:48px;color:#F59E0B;margin:32px 0;
            padding:20px 0;border-top:1px solid rgba(255,255,255,0.08);
            border-bottom:1px solid rgba(255,255,255,0.08);
        ">{highlight}</div>"""

    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>
{CSS_BASE}
body {{ background: {bg}; }}
</style></head><body>
<div class="header">
    <div class="header-left">@rubimfx · Economia & Trading</div>
    <div class="header-right">{date}</div>
</div>
<div style="padding:120px 64px 100px;display:flex;flex-direction:column;justify-content:center;height:100%">
    <div style="font-weight:800;font-size:36px;line-height:1.3;margin-bottom:24px;max-width:900px">{title}</div>
    <div style="width:60px;height:4px;background:#F59E0B;margin-bottom:32px;border-radius:2px"></div>
    {highlight_html}
    <div style="font-size:22px;line-height:1.7;color:rgba(255,255,255,0.75);max-width:880px">{body}</div>
</div>
<div class="watermark">@rubimfx</div>
<div class="page-num">{page}</div>
</body></html>"""


def generate_data(number, label, description, change="", change_positive=True, page="3/10", date="MAR 2026", bg="#1A1B2E"):
    """Gera slide de dados com número grande"""
    change_html = ""
    if change:
        color = "#22C55E" if change_positive else "#EF4444"
        arrow = "▲" if change_positive else "▼"
        change_html = f'<div style="font-size:24px;color:{color};margin-top:12px;font-weight:600">{arrow} {change}</div>'

    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>
{CSS_BASE}
body {{ background: {bg}; }}
</style></head><body>
<div class="header">
    <div class="header-left">@rubimfx · Economia & Trading</div>
    <div class="header-right">{date}</div>
</div>
<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;padding:120px 64px 100px;text-align:center">
    <div style="font-size:16px;color:rgba(255,255,255,0.5);font-weight:600;letter-spacing:2px;text-transform:uppercase;margin-bottom:24px">{label}</div>
    <div style="font-family:'JetBrains Mono',monospace;font-weight:700;font-size:96px;color:#F59E0B;line-height:1">{number}</div>
    {change_html}
    <div style="margin-top:40px;padding:24px 32px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:12px;max-width:700px">
        <div style="font-size:20px;line-height:1.7;color:rgba(255,255,255,0.7)">{description}</div>
    </div>
</div>
<div class="watermark">@rubimfx</div>
<div class="page-num">{page}</div>
</body></html>"""


def generate_comparison(title, left_label, left_items, right_label, right_items, page="5/10", date="MAR 2026", bg="#0D1117"):
    """Gera slide comparativo (antes/depois, bull/bear)"""
    left_html = "".join([f'<div style="padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.06);font-size:18px;color:rgba(255,255,255,0.8)">{item}</div>' for item in left_items])
    right_html = "".join([f'<div style="padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.06);font-size:18px;color:rgba(255,255,255,0.8)">{item}</div>' for item in right_items])

    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>
{CSS_BASE}
body {{ background: {bg}; }}
</style></head><body>
<div class="header">
    <div class="header-left">@rubimfx · Economia & Trading</div>
    <div class="header-right">{date}</div>
</div>
<div style="padding:120px 64px 100px;height:100%;display:flex;flex-direction:column;justify-content:center">
    <div style="font-weight:800;font-size:32px;margin-bottom:40px;text-align:center">{title}</div>
    <div style="display:flex;gap:24px">
        <div style="flex:1;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.2);border-radius:12px;padding:28px">
            <div style="font-weight:700;font-size:18px;color:#EF4444;margin-bottom:20px;text-transform:uppercase;letter-spacing:1px">{left_label}</div>
            {left_html}
        </div>
        <div style="flex:1;background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);border-radius:12px;padding:28px">
            <div style="font-weight:700;font-size:18px;color:#22C55E;margin-bottom:20px;text-transform:uppercase;letter-spacing:1px">{right_label}</div>
            {right_html}
        </div>
    </div>
</div>
<div class="watermark">@rubimfx</div>
<div class="page-num">{page}</div>
</body></html>"""


def generate_bridge(title, items, warning="", page="7/10", date="MAR 2026", bg="#0A0E1A"):
    """Gera slide bridge macro→trading com setup"""
    items_html = ""
    for item in items:
        asset = item.get("asset", "")
        direction = item.get("direction", "")
        detail = item.get("detail", "")
        color = "#22C55E" if "alta" in direction.lower() or "↑" in direction else "#EF4444" if "baixa" in direction.lower() or "↓" in direction else "#F59E0B"
        items_html += f"""
        <div style="display:flex;align-items:center;gap:16px;padding:20px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:8px;margin-bottom:12px">
            <div style="font-weight:700;font-size:20px;min-width:120px">{asset}</div>
            <div style="color:{color};font-weight:700;font-size:18px;min-width:60px">{direction}</div>
            <div style="font-size:17px;color:rgba(255,255,255,0.6)">{detail}</div>
        </div>"""
    
    warning_html = ""
    if warning:
        warning_html = f"""<div style="margin-top:24px;padding:16px 20px;background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);border-radius:8px;font-size:16px;color:#EF4444;font-weight:500">⚠️ {warning}</div>"""

    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>
{CSS_BASE}
body {{ background: {bg}; }}
</style></head><body>
<div class="header">
    <div class="header-left">@rubimfx · Economia & Trading</div>
    <div class="header-right">{date}</div>
</div>
<div style="padding:120px 64px 100px;height:100%;display:flex;flex-direction:column;justify-content:center">
    <div style="font-weight:800;font-size:36px;margin-bottom:8px">{title}</div>
    <div style="font-size:14px;color:rgba(255,255,255,0.4);margin-bottom:32px;font-weight:600;letter-spacing:1px;text-transform:uppercase">Setup operacional</div>
    <div style="border-left:3px solid #F59E0B;padding-left:24px">
        {items_html}
    </div>
    {warning_html}
    <div style="margin-top:24px;font-size:13px;color:rgba(255,255,255,0.3)">Conteúdo educacional. Não é recomendação de investimento.</div>
</div>
<div class="watermark">@rubimfx</div>
<div class="page-num">{page}</div>
</body></html>"""


def generate_cta(question, cta_text, handle="@rubimfx", bg="#0D1117"):
    """Gera slide final CTA"""
    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>
{CSS_BASE}
body {{ background: linear-gradient(135deg, #0D1117 0%, #1A1B2E 100%); }}
</style></head><body>
<div class="header">
    <div class="header-left">@rubimfx · Economia & Trading</div>
    <div class="header-right"></div>
</div>
<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;text-align:center;padding:120px 80px 100px">
    <div style="font-weight:800;font-size:44px;margin-bottom:40px;line-height:1.3">{question}</div>
    <div style="width:60px;height:4px;background:#F59E0B;margin-bottom:40px;border-radius:2px"></div>
    <div style="font-size:22px;color:rgba(255,255,255,0.6);line-height:1.7;margin-bottom:48px;max-width:700px">{cta_text}</div>
    <div style="font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:28px;color:#F59E0B">{handle}</div>
    <div style="margin-top:24px;display:flex;gap:24px">
        <div style="padding:12px 24px;border:1px solid rgba(255,255,255,0.15);border-radius:8px;font-size:15px;color:rgba(255,255,255,0.5)">💾 Salvar</div>
        <div style="padding:12px 24px;border:1px solid rgba(255,255,255,0.15);border-radius:8px;font-size:15px;color:rgba(255,255,255,0.5)">↗️ Compartilhar</div>
    </div>
</div>
</body></html>"""


def save_slide(html, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ {filename}")
    return filepath


# Exemplo de uso / teste
if __name__ == "__main__":
    print("🎨 Gerando slides de teste...\n")
    
    # Slide 1 - Capa
    html = generate_cover(
        title="A economia cresceu. O seu bolso sabe disso?",
        subtitle="Enquanto o PIB sobe, 78,9% dos brasileiros dizem que a vida ficou mais cara.",
        badge="ECONOMIA",
    )
    save_slide(html, "test-01-cover.html")
    
    # Slide 2 - Contexto  
    html = generate_context(
        title="O paradoxo econômico da década",
        body="O PIB cresceu 3,4% em 2025. Mas o brasileiro médio não sentiu. Enquanto números macro mostram expansão, o bolso aperta. A explicação está nos detalhes.",
        highlight="PIB +3,4%",
        page="2/8"
    )
    save_slide(html, "test-02-context.html")
    
    # Slide 3 - Dados
    html = generate_data(
        number="78,9%",
        label="Dos brasileiros afirmam que",
        description="O custo de vida está acima do suportável. Pesquisa Febraban/RADAR 2026 com amostra nacional.",
        change="+12,3 p.p. vs 2024",
        change_positive=False,
        page="3/8"
    )
    save_slide(html, "test-03-data.html")
    
    # Slide 4 - Comparação
    html = generate_comparison(
        title="Macro vs. Realidade",
        left_label="📊 Macro (oficial)",
        left_items=["PIB +3,4%", "Desemprego 6,1%", "Inflação 4,8%", "Bolsa +22%"],
        right_label="🏠 Realidade (rua)",
        right_items=["Aluguel +18%", "Cesta básica +23%", "Gasolina R$7,20", "Crédito 45% a.a."],
        page="4/8"
    )
    save_slide(html, "test-04-comparison.html")
    
    # Slide 5 - Bridge
    html = generate_bridge(
        title="E na prática?",
        items=[
            {"asset": "IBOV", "direction": "↑ Alta", "detail": "Suporte 138k, alvo 145k"},
            {"asset": "USD/BRL", "direction": "↓ Baixa", "detail": "Abaixo de 5.00, viés vendedor"},
            {"asset": "Selic", "direction": "→ Lateral", "detail": "Manter 13.25% até junho"},
        ],
        warning="IPCA de abril pode mudar cenário. Acompanhe.",
        page="7/8"
    )
    save_slide(html, "test-05-bridge.html")
    
    # Slide 6 - CTA
    html = generate_cta(
        question="E você? Sentiu a economia crescer?",
        cta_text="Comenta aqui embaixo. Salva esse post pra acompanhar os próximos dados.",
    )
    save_slide(html, "test-06-cta.html")
    
    print(f"\n✅ 6 slides gerados em: {OUTPUT_DIR}")
    print("Para visualizar: abra os arquivos .html no navegador")
