import os, sys
from google import genai
from google.genai import types

# Get API key
api_key = None
for env_path in ['.env', '../.env', '../../.env']:
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith('GOOGLE_API_KEY='):
                    api_key = line.strip().split('=', 1)[1]
                    break
        if api_key: break

if not api_key:
    api_key = os.environ.get('GOOGLE_API_KEY')

if not api_key:
    print("ERROR: GOOGLE_API_KEY not found")
    sys.exit(1)

client = genai.Client(api_key=api_key)

prompts = {
    "foto-mao-deus.png": "Hyper-realistic cinematic photograph of two hands reaching toward each other in dramatic light — one human hand reaching up from darkness below, one divine hand reaching down from golden light above, like Michelangelo's Creation of Adam but photographed in real life. Volumetric god-rays streaming between the hands. Dark moody background with golden warm light from above. Sacred, powerful, intimate moment. Shot on RED cinema camera, 50mm anamorphic lens. 4:5 portrait ratio. No text.",

    "foto-bezerro-ouro.png": "Cinematic dark photograph of a golden calf idol statue sitting on an altar in a desert scene at night, illuminated by firelight from torches around it. The golden surface reflects warm orange light. Dramatic shadows. Biblical Old Testament atmosphere, Exodus scene. Smoke rising from the altar. Ominous and dark mood — the consequence of impatience. Shot on ARRI Alexa, wide angle 24mm. 4:5 portrait. No text, no people.",

    "foto-trono-vazio.png": "Hyper-realistic cinematic photograph of an ancient stone throne sitting empty in a dramatic beam of light inside a dark cave or stone chamber. Golden sunlight streams through a crack in the ceiling illuminating just the throne. Dust particles visible in the light beam. The throne waits — representing a promise not yet fulfilled, a crown not yet claimed. Biblical epic atmosphere, ancient Israel. Shot on RED V-Raptor, 35mm lens. 4:5 portrait. No text, no people.",

    "foto-caverna-luz.png": "Cinematic photograph looking out from inside a dark cave toward a bright opening. A lone silhouette of a man stands at the cave entrance, backlit by golden sunset light streaming in. The cave is dark and rough, the outside is golden and full of promise. Visual metaphor for waiting in darkness and seeing the light ahead. Biblical David in the cave atmosphere. Volumetric light, dust particles. Shot on Canon EOS R5, 24mm wide. 4:5 portrait. No text."
}

output_dir = "output/posts/2026-03-22-ta-demorando/fotos"
os.makedirs(output_dir, exist_ok=True)

for filename, prompt in prompts.items():
    output_path = os.path.join(output_dir, filename)
    print(f"\nGenerating: {filename}")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[types.Content(parts=[types.Part(text=prompt)])],
            config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"])
        )
        saved = False
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                with open(output_path, "wb") as f:
                    f.write(part.inline_data.data)
                size_kb = os.path.getsize(output_path) // 1024
                print(f"  Saved: {output_path} ({size_kb}KB)")
                saved = True
                break
        if not saved:
            print(f"  No image returned. Text response: {response.text[:200] if response.text else 'None'}")
    except Exception as e:
        print(f"  Error: {e}")

print("\nDone!")
