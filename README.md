NEED PYTHON 3.10
Then go to https://download.pytorch.org/whl/cpu/torch_stable.html and look up () and download it locally

Create a virtual environment using python 3.10:


# Create a virtual environment
py -3.10 -m venv bark-venv

# Activate it (Windows)
bark-venv\Scripts\activate

# Then install the dependencies
pip install "path-to-your-torch-you-downloaded"
pip install -r requirements.txt

# Generate a script, adjust prompt to what u want
python generate_script.py

# Generate audio for the latest story saved in stories folder
python generate_voice_bark.py

# That gets saved in narration folder as a .wav file
