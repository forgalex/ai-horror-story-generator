import subprocess
import datetime
import os
import re

def run_ollama(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'mistral', prompt],
        capture_output=True,
        text=True,
        errors="ignore"  # Ignore encoding issues in the background
    )
    return result.stdout.strip()


def sanitize_filename(text, max_words=4, max_length=100):
    import re
    text = text.replace('\n', ' ').strip()
    text = re.sub(r'[\\/*?:"<>|]', "", text)  # remove forbidden chars
    words = text.split()[:max_words]
    cleaned = "_".join(words)
    return cleaned[:max_length]

def generate_horror_script():
    # Prompt 1: story
    story_prompt = "Write a 10-minute horror story set in an abandoned hotel with a disturbing twist. Don't include the title in the story, i only want the story itself for it."
    story = run_ollama(story_prompt)

    # Prompt 2: title for the story
    title_prompt = f"Give this horror story a short and creepy title, that's only 4 words maximum:\n\n{story}"
    raw_title = run_ollama(title_prompt)

    cleaned_title_line = raw_title.strip().replace("Title:", "").strip()
    clean_title = sanitize_filename(cleaned_title_line)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"stories/{clean_title}_{timestamp}.txt"

    # Make sure folder exists
    os.makedirs("stories", exist_ok=True)

    # Save story
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story)

    print(f"[✓] Story saved as: {filename}")
    return filename, story

if __name__ == "__main__":
    generate_horror_script()
