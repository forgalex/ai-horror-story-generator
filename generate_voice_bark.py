from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import numpy as np
import os
import glob
import torch
import re
import datetime

# Use GPU if available
if torch.cuda.is_available():
    torch_device = "cuda"
    print("Using GPU (CUDA)")
else:
    torch_device = "cpu"
    print("No GPU found, falling back to CPU")

def split_text_to_chunks(text, max_chars=220):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chars:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def generate_voice_bark(story_file):
    with open(story_file, "r", encoding="utf-8") as f:
        text = f.read()

    print("[Bark] Preloading models...")
    preload_models()

    print("[Bark] Loading Emmett's voice...")
    voice_data = np.load("voices/Emmett.npz", allow_pickle=True)
    voice_embedding = {
        "semantic_prompt": voice_data["semantic_prompt"],
        "coarse_prompt": voice_data["coarse_prompt"],
        "fine_prompt": voice_data["fine_prompt"],
    }

    print("[Bark] Generating voice from text...")

    # Split into clean sentence-based chunks
    chunks = split_text_to_chunks(text)
    all_audio = []

    for i, chunk in enumerate(chunks):
        print(f" → Generating chunk {i + 1}/{len(chunks)}...")
        try:
            audio_array = generate_audio(chunk, history_prompt=voice_embedding)
            all_audio.append(audio_array)
        except Exception as e:
            print(f" [!] Error on chunk {i + 1}: {e}")

    if not all_audio:
        print("⚠️ No audio was generated.")
        return

    full_audio = np.concatenate(all_audio)

    os.makedirs("narration", exist_ok=True)
    base_name = os.path.splitext(os.path.basename(story_file))[0]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"narration/{base_name}_{timestamp}_bark.wav"

    write_wav(output_path, SAMPLE_RATE, full_audio)
    print(f"[✓] Narration saved as: {output_path}")

if __name__ == "__main__":
    story_files = glob.glob("output/*.txt")
    latest_story = max(story_files, key=os.path.getmtime)
    generate_voice_bark(latest_story)
