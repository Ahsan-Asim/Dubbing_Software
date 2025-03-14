# import os

# # Input and output paths
# input_video = "input/Conversation.mp4"
# output_audio = "output/original_audio1.mp3"

# # Extract audio using ffmpeg
# os.system(f'ffmpeg -i {input_video} -q:a 0 -map a {output_audio}')

# print("✅ Audio extracted successfully!")

import subprocess

def extract_audio(video_path, output_audio_path):
    command = f'ffmpeg -i "{video_path}" -q:a 0 -map a "{output_audio_path}"'
    subprocess.run(command, shell=True)
    print("✅ Audio extracted successfully!")

if __name__ == "__main__":
    extract_audio("static/uploads/Conversation3.mp4", "static/outputs/original_audio.mp3")

