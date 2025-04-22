- NEED PYTHON 3.10
- Then go to https://download.pytorch.org/whl/cpu/torch_stable.html and look up 'torch-2.0.1+cpu-cp310-cp310-win_amd64.whl' and download it locally
- Then go to https://download.pytorch.org/whl/cpu/torchaudio/index.html and look up 'torchaudio‑2.0.2+cpu‑cp310‑cp310‑win_amd64.whl' and download that locally too

Create a virtual environment using python 3.10:


# Create a virtual environment
py -3.10 -m venv bark-venv

# Activate it (Windows)
bark-venv\Scripts\activate

# Then install the dependencies
- pip install "path-to-your-torch-you-downloaded"
- pip install "path-to-your-torchaudio-you-downloaded"
- pip install -r requirements.txt

# Generate a script, adjust prompt to what u want
python generate_script.py

# Generate audio for the latest story saved in stories folder
python generate_voice_bark.py

# That gets saved in narration folder as a .wav file
