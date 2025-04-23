import os
from dotenv import load_dotenv
import ollama

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
reference_story_path = os.path.join(base_dir, "scary_story_reference.txt")
output_folder = os.path.join(base_dir, "output")
output_file_path = os.path.join(output_folder, "scary_story.txt")

def read_reference_story():
    with open(reference_story_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_story(prompt, model_name=MODEL_NAME):
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def save_story_to_file(story_content, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(story_content)
    print(f"Story saved to: {file_path}")

reference_story = read_reference_story()
topic_of_scary_story = "Camping trips"

prompt = f"""
You are a person sharing a terrifying experience as if you're telling it around a campfire late at night. The tone should feel **real**, like you're reliving the moment while you talk. Think pauses, quiet tension, and unease. Use **ellipses** (...) and **commas** to mimic the rhythm of natural speech. For important or shocking moments, emphasize a word in **ALL CAPS followed by !** — like: "and then... it SCREAMED!"

Stay grounded — the story should feel **completely realistic**, like it actually happened. No ghosts shooting lasers or obvious fantasy. Think: unexplained figures, eerie feelings, late-night drives, creepy coincidences — stuff that makes your skin crawl because it *could be real*.

Your story should last about **3 minutes when read aloud at a natural pace**. So include enough detail and storytelling to fill that time.

Here's an example of the type of story this should resemble:
\"\"\" 
{reference_story}
\"\"\"

Now, write a new scary story on the topic of: **{topic_of_scary_story}**

Begin the story:
"""

# Generate and save
story = generate_story(prompt)
save_story_to_file(story, output_file_path)
