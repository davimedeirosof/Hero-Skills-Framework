#!/usr/bin/env python3
"""
Clone de imagem PRO — recria pessoa de referência em novos cenários com realismo profissional.

Técnicas aplicadas:
  - Identity Header (bloco de identidade fixa em todo prompt)
  - Multi-reference support (até 3 fotos de ângulos diferentes)
  - Prompts narrativos (não keyword lists)
  - Camera/lens anchors reais
  - Anti-AI keywords (pores, texture, imperfections)
  - Negative prompt embedding
  - Film stock emulation

Uso:
  python clone_image.py <foto-ref> <cenario-ou-preset> [output.png]
  python clone_image.py <foto-ref> --batch [output-dir]
  python clone_image.py <foto-ref> --multi <foto2> <foto3> <cenario> [output.png]
  python clone_image.py --list  (lista presets disponíveis)

Exemplos:
  python clone_image.py foto.jpg trading-desk output.png
  python clone_image.py foto.jpg "CEO in modern office" output.png
  python clone_image.py foto.jpg --multi foto2.jpg foto3.jpg podcast-studio output.png
  python clone_image.py foto.jpg --batch clones/
"""

import os
import sys
from pathlib import Path


# ══════════════════════════════════════════════════════════════
# IDENTITY HEADER — Cola de identidade para consistência facial
# Ajuste os detalhes após ver as fotos reais do Gabriel
# ══════════════════════════════════════════════════════════════

GABRIEL_IDENTITY = """[IDENTITY — GABRIEL RUBIM]
Subject: Gabriel Rubim, Brazilian male, early 30s
Face: light olive/fair Brazilian skin with warm undertones, hazel-brown eyes,
      strong defined jawline, short well-trimmed dark beard and goatee,
      thick dark eyebrows, straight nose, natural slight asymmetry
Hair: dark brown/black, short modern fade cut on sides, slightly longer on top
      with natural texture swept to the side
Build: muscular athletic build, broad shoulders, strong arms with sleeve tattoo
      on left arm (lion and geometric/religious motifs), confident posture
Style: professional-casual, prefers dark fitted clothing (black polos, dark shirts),
      clean and minimal aesthetic
Distinctive: trading educator, financial expert, tattoo sleeve left arm,
      strong masculine presence, authoritative energy
[END IDENTITY]"""


# ══════════════════════════════════════════════════════════════
# ANTI-AI REALISM BLOCK — Sempre incluído no final do prompt
# ══════════════════════════════════════════════════════════════

REALISM_BLOCK = (
    "CRITICAL REALISM REQUIREMENTS: "
    "Natural skin texture with visible pores and subtle imperfections. "
    "Slight natural facial asymmetry preserved. "
    "Realistic subsurface scattering on skin. "
    "No airbrushing, no beauty filter, no digital smoothing. "
    "Natural stubble texture visible. "
    "Authentic micro-expression, not posed or forced. "
    "Documentary-quality skin rendering with real human imperfections. "
    "DO NOT generate: plastic/waxy/porcelain skin, dead/doll eyes, "
    "uncanny valley features, perfect symmetry, cartoon/CGI/3D render style, "
    "extra fingers or malformed hands, overexposed or oversaturated colors."
)


# ══════════════════════════════════════════════════════════════
# CLONE INSTRUCTION TEMPLATE — Estrutura profissional de clonagem
# ══════════════════════════════════════════════════════════════

CLONE_TEMPLATE = """The attached reference photo(s) show Gabriel Rubim. This is the identity anchor.

{identity}

CLONE DIRECTIVE: Reproduce this EXACT person in the new scene described below.
Strictly maintain: facial geometry, skin tone, eye color and shape, jaw structure,
nose shape, hair style and color, beard/stubble pattern. The face must be identical
to the reference — do not idealize or alter facial features.

SCENE: {scenario}

{camera_lighting}

COMPOSITION: {composition}

COLOR GRADE: {color_grade}

{realism}

Generate a single photorealistic photograph. 4:5 portrait aspect ratio optimized for Instagram.
The result should be indistinguishable from a real professional photograph."""


# ══════════════════════════════════════════════════════════════
# CAMERA + LIGHTING PRESETS
# ══════════════════════════════════════════════════════════════

CAMERA_PRESETS = {
    "editorial": "Shot on Canon EOS R5, 85mm f/1.4 lens, ISO 200, shallow depth of field, natural bokeh. Soft Rembrandt lighting from the left with subtle fill light.",
    "cinematic": "Shot on Sony FX3, 50mm f/1.4 lens, ISO 400, cinematic depth of field. Dramatic one-light setup with strong directional key light, deep shadows.",
    "candid": "Shot on Fujifilm X100V, 35mm equivalent, f/2.0, ISO 400. Natural available light, candid documentary feel, slight film grain.",
    "luxury": "Shot on Leica SL2-S, 75mm f/2.0 lens, ISO 200, ultra-shallow depth of field. Premium studio lighting with soft key light and warm rim light.",
    "dramatic": "Shot on Canon EOS R1, 50mm f/1.2 lens, ISO 800. High contrast single-source lighting, deep crushed blacks, volumetric light beams.",
    "street": "Shot on Ricoh GR III, 28mm equivalent, f/2.8, ISO 800. Natural street lighting, slight chromatic aberration, authentic imperfections.",
    "stage": "Shot from audience level with 70-200mm f/2.8 telephoto, ISO 1600. Stage spotlight from above, blue fill from background screens, press photography compression.",
    "warm": "Shot on Fujifilm GFX 50S II, 63mm f/2.0 lens, ISO 200. Natural warm window light from the left, golden hour tones, Kodak Portra 400 film emulation.",
}

COLOR_PRESETS = {
    "portra": "Kodak Portra 400 film emulation — warm skin-flattering tones, soft shadows, natural warmth, subtle grain.",
    "cinestill": "Cinestill 800T film aesthetic — cool blue shadows, warm highlights, neon halation, heavy cinematic grain, night photography feel.",
    "chrome": "Fujifilm Classic Chrome — subdued muted tones, brown shadows, slightly desaturated, editorial magazine quality.",
    "bw": "Ilford HP5 Plus black and white — high contrast, deep dramatic blacks, visible grain, journalistic gravitas.",
    "gold": "Kodak Gold 200 — warm golden tones, rich but natural saturation, summer outdoor feel, lifted shadows.",
    "natural": "Natural color grading as-shot — realistic contrast, honest colors, no heavy processing, authentic.",
    "teal-orange": "Cinematic teal and orange color grade — cool blue shadows, warm orange highlights, Hollywood blockbuster feel.",
}


# ══════════════════════════════════════════════════════════════
# CENÁRIOS PRÉ-DEFINIDOS (PRO — prompts narrativos completos)
# ══════════════════════════════════════════════════════════════

SCENARIOS = {
    "trading-desk": {
        "scenario": (
            "Gabriel is seated at a professional trading desk in a dark room. "
            "Three 27-inch monitors behind him show candlestick charts and financial data (slightly out of focus). "
            "Cool blue ambient light from monitors illuminates his face, with warm secondary light from the left. "
            "He leans forward slightly with a focused, determined expression, one hand on keyboard. "
            "Authentic financial professional workspace — sticky notes on monitor edges, coffee mug nearby. "
            "Real workspace, not staged studio."
        ),
        "camera": "cinematic",
        "color": "teal-orange",
        "composition": "Environmental portrait, three-quarter body, subject at left third, monitors filling right side. Eye-level camera height.",
    },
    "office-ceo": {
        "scenario": (
            "Gabriel stands in a modern luxury corner office with floor-to-ceiling windows "
            "overlooking a city skyline at golden hour sunset. He wears a tailored dark navy blazer "
            "over a white collar shirt, no tie. He looks directly at camera with calm, confident expression. "
            "Minimalist executive desk with a single laptop behind him. "
            "Warm golden light streaming through windows creating natural rim lighting on his silhouette."
        ),
        "camera": "luxury",
        "color": "portra",
        "composition": "Three-quarter body shot, subject centered, city skyline bokeh background. Slight low angle for authority.",
    },
    "podcast-studio": {
        "scenario": (
            "Gabriel is seated at a professional podcast recording setup. Large condenser microphone "
            "visible in foreground (slightly blurred). He leans slightly forward toward the mic, "
            "engaged expression, mid-sentence, animated hand gesture. Dark studio background with "
            "soft neon blue rim light from behind and warm key light from left. "
            "Acoustic foam panels soft in background. He wears a casual fitted black shirt. "
            "Authentic broadcast energy."
        ),
        "camera": "cinematic",
        "color": "cinestill",
        "composition": "Bust shot with microphone in foreground bokeh. Subject at right third, slight off-center framing.",
    },
    "stage-speaker": {
        "scenario": (
            "Gabriel on a large conference stage, standing at center stage with a professional "
            "lavalier microphone. One hand raised mid-gesture while addressing a packed audience. "
            "Strong overhead spotlight creating dramatic top-light on his face. Large screen behind "
            "showing financial charts (blurred). Audience silhouettes visible in lower foreground. "
            "He wears an all-black fitted outfit. TED-talk scale stage. "
            "Powerful, authoritative presence, caught mid-speech in natural movement."
        ),
        "camera": "stage",
        "color": "natural",
        "composition": "Full body shot from audience level (press pit angle). Telephoto compression, wide stage framing with subject as focal point.",
    },
    "casual-street": {
        "scenario": (
            "Gabriel walking confidently through a modern urban financial district street. "
            "He wears dark fitted jeans, a premium black bomber jacket over a white t-shirt. "
            "Slightly looking ahead with confident natural stride, unaware of camera feel. "
            "Modern glass office buildings in blurred background. "
            "Caught mid-stride, authentic candid movement."
        ),
        "camera": "street",
        "color": "gold",
        "composition": "Full body, subject at left third walking toward right. Slight motion feel on lower body, face in sharp focus. Golden hour warm side lighting.",
    },
    "teaching-whiteboard": {
        "scenario": (
            "Gabriel teaching in a modern seminar room, standing at the front next to a large "
            "whiteboard covered in hand-drawn trading concepts — candlestick patterns, order blocks, "
            "support/resistance levels. He points at a key concept with his right hand, "
            "slight turn toward camera with engaged expression. He wears a fitted black polo shirt. "
            "Natural fluorescent office light with soft fill from windows on the right. "
            "Unposed, candid teaching moment."
        ),
        "camera": "candid",
        "color": "chrome",
        "composition": "Three-quarter body, subject at right third, whiteboard filling left side. Eye-level, slight Dutch angle for energy.",
    },
    "results-celebration": {
        "scenario": (
            "Gabriel reacting positively at his trading desk — genuine broad smile, "
            "slight fist pump with right hand. Monitors behind showing green chart movements and profit numbers. "
            "He wears a casual fitted dark shirt. Natural energy, authentic emotion, not posed. "
            "Monitor glow provides ambient cool light, warm desk lamp from left."
        ),
        "camera": "candid",
        "color": "natural",
        "composition": "Bust shot, centered, monitors blurred behind. Caught in authentic moment of celebration.",
    },
    "rooftop-night": {
        "scenario": (
            "Gabriel standing on a high rooftop terrace at night, city lights creating beautiful "
            "bokeh behind him. He wears a dark fitted turtleneck. He looks slightly to the side "
            "with a reflective, contemplative expression. City glow creates warm ambient rim "
            "lighting from behind, face lit by subtle portable fill light. "
            "Premium luxury brand aesthetic, aspirational but authentic."
        ),
        "camera": "luxury",
        "color": "cinestill",
        "composition": "Head and shoulders, subject centered, city bokeh background. Tight crop, intimate.",
    },
    "home-content": {
        "scenario": (
            "Gabriel at a minimalist home studio desk, recording content. Ring light softbox "
            "visible at edge of frame, professional microphone, dual monitors with trading charts. "
            "He looks at camera with natural engaged expression, mid-explanation. "
            "Modern minimalist workspace with bookshelves and houseplants soft in background. "
            "Authentic creator vibe, behind-the-scenes feel."
        ),
        "camera": "warm",
        "color": "portra",
        "composition": "Three-quarter body at desk, environmental portrait showing the workspace. Warm lived-in atmosphere.",
    },
    "thinking-window": {
        "scenario": (
            "Gabriel at a large window, looking outside at an urban city view. Profile/three-quarter angle. "
            "He holds a coffee cup in both hands, thoughtful introspective expression. "
            "Morning light from window creates beautiful sidelight on face, casting gentle shadows. "
            "Muted, contemplative atmosphere. He wears a clean dark t-shirt. "
            "Quiet power and reflection."
        ),
        "camera": "warm",
        "color": "chrome",
        "composition": "Profile to three-quarter angle, subject at right third, window light source at left. Intimate editorial crop.",
    },
    "market-stress": {
        "scenario": (
            "Gabriel standing in front of large trading floor screens displaying market charts with "
            "red numbers and downward arrows. Cool blue-white light from screens illuminates his face "
            "from behind, creating a strong silhouette effect with face still visible. "
            "He looks directly at camera with intense, determined expression. "
            "High-stakes atmosphere, market crisis energy."
        ),
        "camera": "dramatic",
        "color": "teal-orange",
        "composition": "Bust shot, centered, screens filling entire background. High contrast, dramatic framing.",
    },
    "walking-office": {
        "scenario": (
            "Gabriel walking through the glass entrance of a modern financial district building. "
            "He carries a leather portfolio. Dark fitted blazer, confident purposeful stride, "
            "slight toward-camera gaze. Morning light from behind creating rim light effect, "
            "slight lens flare. Dynamic, authoritative, arriving for business."
        ),
        "camera": "editorial",
        "color": "gold",
        "composition": "Full body, slight low angle, subject walking toward camera. Dynamic movement feel with face in sharp focus.",
    },
}


def load_image_bytes(path):
    """Carrega imagem como bytes."""
    with open(path, "rb") as f:
        return f.read()


def get_mime_type(path):
    """Retorna MIME type baseado na extensão."""
    ext = Path(path).suffix.lower()
    mime_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
    }
    return mime_map.get(ext, "image/jpeg")


def get_api_key():
    """Busca GOOGLE_API_KEY do env ou .env file."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        for env_path in [
            os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"),
            os.path.join(os.path.dirname(__file__), "..", ".env"),
        ]:
            if os.path.exists(env_path):
                with open(env_path) as f:
                    for line in f:
                        if line.startswith("GOOGLE_API_KEY="):
                            api_key = line.strip().split("=", 1)[1]
                            break
                if api_key:
                    break
    return api_key


def build_prompt(scenario_text, camera_key="editorial", color_key="portra", composition="Rule of thirds, eye-level, shallow depth of field."):
    """Monta o prompt profissional completo."""
    camera = CAMERA_PRESETS.get(camera_key, CAMERA_PRESETS["editorial"])
    color = COLOR_PRESETS.get(color_key, COLOR_PRESETS["portra"])

    return CLONE_TEMPLATE.format(
        identity=GABRIEL_IDENTITY,
        scenario=scenario_text,
        camera_lighting=camera,
        composition=composition,
        color_grade=color,
        realism=REALISM_BLOCK,
    )


def clone(reference_paths, scenario_prompt, output_path, model="gemini-2.5-flash-image"):
    """
    Gera imagem clonada com técnicas profissionais.

    Args:
        reference_paths: str ou list[str] — uma ou mais fotos de referência
        scenario_prompt: str — prompt completo já montado ou texto livre
        output_path: str — caminho do arquivo de saída
        model: str — modelo Gemini a usar
    """
    from google import genai
    from google.genai import types

    api_key = get_api_key()
    if not api_key:
        print("GOOGLE_API_KEY not found")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # Suporte a uma ou múltiplas referências
    if isinstance(reference_paths, str):
        reference_paths = [reference_paths]

    # Montar parts com todas as referências
    parts = []
    for i, ref_path in enumerate(reference_paths):
        ref_bytes = load_image_bytes(ref_path)
        ref_mime = get_mime_type(ref_path)
        ref_size = len(ref_bytes) // 1024
        print(f"Reference {i+1}: {ref_path} ({ref_size}KB, {ref_mime})")
        parts.append(
            types.Part(
                inline_data=types.Blob(
                    mime_type=ref_mime,
                    data=ref_bytes
                )
            )
        )

    # Adicionar prompt de texto
    parts.append(types.Part(text=scenario_prompt))

    print(f"Model: {model}")
    print(f"Generating clone...")

    response = client.models.generate_content(
        model=model,
        contents=[types.Content(parts=parts)],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"]
        )
    )

    # Salvar resultado
    image_saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data:
            with open(output_path, "wb") as f:
                f.write(part.inline_data.data)
            size_kb = os.path.getsize(output_path) // 1024
            print(f"Clone saved: {output_path} ({size_kb}KB)")
            image_saved = True
            break

    if not image_saved:
        print("No image generated. Response text:")
        for part in response.candidates[0].content.parts:
            if part.text:
                print(part.text[:500])
        return False

    return True


def clone_preset(reference_paths, preset_name, output_path, model="gemini-2.5-flash-image"):
    """Gera clone usando preset pré-definido."""
    if preset_name not in SCENARIOS:
        print(f"Preset '{preset_name}' not found. Available: {', '.join(SCENARIOS.keys())}")
        return False

    preset = SCENARIOS[preset_name]
    prompt = build_prompt(
        scenario_text=preset["scenario"],
        camera_key=preset.get("camera", "editorial"),
        color_key=preset.get("color", "portra"),
        composition=preset.get("composition", "Rule of thirds, eye-level."),
    )
    return clone(reference_paths, prompt, output_path, model)


def clone_custom(reference_paths, custom_scenario, output_path,
                 camera="editorial", color="portra", model="gemini-2.5-flash-image"):
    """Gera clone com cenário customizado + técnicas profissionais."""
    prompt = build_prompt(
        scenario_text=custom_scenario,
        camera_key=camera,
        color_key=color,
    )
    return clone(reference_paths, prompt, output_path, model)


def batch_clone(reference_paths, output_dir, scenarios=None):
    """Gera múltiplos clones de uma mesma referência em diferentes cenários."""
    os.makedirs(output_dir, exist_ok=True)
    scenarios = scenarios or SCENARIOS
    results = []

    for i, (name, preset) in enumerate(scenarios.items(), 1):
        output_path = os.path.join(output_dir, f"clone-{name}.png")
        print(f"\n{'='*50}")
        print(f"[{i}/{len(scenarios)}] Generating: {name}")
        print(f"{'='*50}")
        success = clone_preset(reference_paths, name, output_path)
        results.append((name, success, output_path))

    print(f"\n{'='*60}")
    print(f"BATCH RESULTS ({sum(1 for _, s, _ in results if s)}/{len(results)} success)")
    print(f"{'='*60}")
    for name, success, path in results:
        status = "OK" if success else "FAIL"
        print(f"  [{status}] {name}: {path}")

    return results


def list_presets():
    """Lista todos os presets disponíveis."""
    print(f"\n{'='*60}")
    print(f"  CLONE PRESETS ({len(SCENARIOS)} scenarios)")
    print(f"{'='*60}")
    for name, preset in SCENARIOS.items():
        scenario_preview = preset["scenario"][:80]
        camera = preset.get("camera", "editorial")
        color = preset.get("color", "portra")
        print(f"\n  {name}")
        print(f"    Camera: {camera} | Color: {color}")
        print(f"    Scene: {scenario_preview}...")

    print(f"\n{'='*60}")
    print(f"  CAMERA PRESETS: {', '.join(CAMERA_PRESETS.keys())}")
    print(f"  COLOR PRESETS:  {', '.join(COLOR_PRESETS.keys())}")
    print(f"{'='*60}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        print("Clone Image PRO — Photorealistic character cloning")
        print()
        print("Usage:")
        print("  Single preset:  python clone_image.py <ref.jpg> <preset-name> [output.png]")
        print("  Custom scene:   python clone_image.py <ref.jpg> \"scene description\" [output.png]")
        print("  Multi-ref:      python clone_image.py <ref1.jpg> --multi <ref2.jpg> [ref3.jpg] <preset-or-scene> [output.png]")
        print("  Batch all:      python clone_image.py <ref.jpg> --batch [output-dir]")
        print("  List presets:   python clone_image.py --list")
        print()
        print("Options:")
        print("  --camera <preset>  Camera/lighting preset (default: editorial)")
        print("  --color <preset>   Color grade preset (default: portra)")
        print("  --model <name>     Gemini model (default: gemini-2.5-flash-image)")
        sys.exit(0)

    if sys.argv[1] == "--list":
        list_presets()
        sys.exit(0)

    reference = sys.argv[1]
    if not os.path.exists(reference):
        print(f"Reference file not found: {reference}")
        sys.exit(1)

    # Parse optional flags
    camera = "editorial"
    color = "portra"
    model = "gemini-2.5-flash-image"

    args = sys.argv[2:]
    if "--camera" in args:
        idx = args.index("--camera")
        camera = args.pop(idx + 1)
        args.pop(idx)
    if "--color" in args:
        idx = args.index("--color")
        color = args.pop(idx + 1)
        args.pop(idx)
    if "--model" in args:
        idx = args.index("--model")
        model = args.pop(idx + 1)
        args.pop(idx)

    if not args:
        print("Missing scenario or command. Use --help for usage.")
        sys.exit(1)

    # Multi-reference mode
    if args[0] == "--multi":
        refs = [reference]
        args = args[1:]
        while args and os.path.exists(args[0]):
            refs.append(args.pop(0))
        if not args:
            print("Missing scenario after reference images.")
            sys.exit(1)
        scenario_or_preset = args[0]
        output = args[1] if len(args) > 1 else "clone-output.png"

        if scenario_or_preset in SCENARIOS:
            clone_preset(refs, scenario_or_preset, output, model)
        else:
            clone_custom(refs, scenario_or_preset, output, camera, color, model)

    # Batch mode
    elif args[0] == "--batch":
        output_dir = args[1] if len(args) > 1 else "clones"
        batch_clone([reference], output_dir)

    # Single mode (preset or custom)
    else:
        scenario_or_preset = args[0]
        output = args[1] if len(args) > 1 else "clone-output.png"

        if scenario_or_preset in SCENARIOS:
            clone_preset([reference], scenario_or_preset, output, model)
        else:
            clone_custom([reference], scenario_or_preset, output, camera, color, model)
