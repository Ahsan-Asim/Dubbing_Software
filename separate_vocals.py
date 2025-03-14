# import os

# # Input and output paths
# input_audio = "output/original_audio1.mp3"

# # Run Demucs to separate vocals and background
# os.system(f'demucs --two-stems=vocals {input_audio}')

# print("✅ Vocals and background separated!")

import subprocess

def separate_audio(audio_path):
    command = f'demucs --device=cpu "{audio_path}"'  # Changed cuda to cpu
    subprocess.run(command, shell=True)
    print("✅ Vocals and background separated!")

if __name__ == "__main__":
    separate_audio("static/outputs/original_audio.mp3")


