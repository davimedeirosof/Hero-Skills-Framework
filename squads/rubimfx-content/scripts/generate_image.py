#!/usr/bin/env python3
"""
Gera imagens via Nano Banana (Google Gemini API).
Uso:
  python generate_image.py "prompt da imagem" output.png
  python generate_image.py "prompt" output.png --model gemini-2.5-flash-image
"""

import os
import sys
import base64

def generate(prompt, output_path, model="gemini-2.5-flash-image"):
    from google import genai
    from google.genai import types

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        env_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env")
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.startswith("GOOGLE_API_KEY="):
                        api_key = line.strip().split("=", 1)[1]
                        break
    if not api_key:
        print("GOOGLE_API_KEY not found in env or .env file")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print(f"Generating image with {model}...")
    print(f"Prompt: {prompt[:100]}...")

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"]
        )
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data:
            with open(output_path, "wb") as f:
                f.write(part.inline_data.data)
            size_kb = os.path.getsize(output_path) // 1024
            print(f"Image saved: {output_path} ({size_kb}KB)")
            return True

    print("No image in response. Text response:")
    for part in response.candidates[0].content.parts:
        if part.text:
            print(part.text)
    return False


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_image.py 'prompt' output.png [--model model-name]")
        sys.exit(1)

    prompt = sys.argv[1]
    output = sys.argv[2]
    model = "gemini-2.5-flash-image"

    if "--model" in sys.argv:
        idx = sys.argv.index("--model")
        model = sys.argv[idx + 1]

    generate(prompt, output, model)
