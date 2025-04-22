# from TTS.api import TTS
# import os

# def generate_voice(story_file):
#     # Load the story text
#     with open(story_file, "r", encoding="utf-8") as f:
#         text = f.read()

#     # Load the Coqui TTS model (first run downloads it)
#     tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)

#     # Make sure the output folder exists
#     os.makedirs("narration", exist_ok=True)

#     # Generate a filename for the audio
#     base_name = os.path.splitext(os.path.basename(story_file))[0]
#     output_path = f"narration/{base_name}.mp3"

#     # Convert text to speech and save it
#     tts.tts_to_file(text=text, file_path=output_path)
#     print(f"[✓] Narration saved as: {output_path}")

# if __name__ == "__main__":
#     # Automatically find the latest story file
#     story_files = sorted(os.listdir("stories"), reverse=True)
#     latest_story = f"stories/{story_files[0]}"
#     generate_voice(latest_story)
