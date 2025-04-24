from TTS.tts.configs.bark_config import BarkConfig
from TTS.tts.models.bark import Bark
import scipy

# Load Bark configuration
config = BarkConfig()

# Initialize model from config
model = Bark.init_from_config(config)

# Load pretrained checkpoint
model.load_checkpoint(config, checkpoint_dir="bark/", eval=True)

# Define the text you want to synthesize
text = "Hope you found this video useful. Subscribe to my channel for more content!"

# Use your custom voice directory and speaker ID
output_dict = model.synthesize(
    text,
    config,
    speaker_id="speaker",  # name of the folder under bark_voices/
    voice_dirs="bark_voices/"  # path to the directory containing custom speaker folders
)

# Set sample rate (Bark defaults to 24kHz)
sample_rate = 24000

# Save audio to disk
scipy.io.wavfile.write("generated_audio.wav", rate=sample_rate, data=output_dict["wav"])