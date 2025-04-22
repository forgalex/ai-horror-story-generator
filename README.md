# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Then install the dependencies
pip install -r requirements.txt

# Generate a script, adjust prompt to what u want
python generate_script.py

#Generate audio for the latest story saved in stories folder
python generate_voice_bark.py

#That gets saved in narration folder as a .wav file
