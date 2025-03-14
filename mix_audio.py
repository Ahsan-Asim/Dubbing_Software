from pydub import AudioSegment
import os

# File paths
speech_file = "static/outputs/dubbed_audio.mp3"
bg_music_file = "separated/htdemucs/original_audio/other.wav"
output_file = "static/outputs/final_synced_audio.mp3"

# Check if required files exist
if not os.path.exists(speech_file):
    print(f"❌ Error: Speech audio file '{speech_file}' not found!")
    exit()

if not os.path.exists(bg_music_file):
    print(f"❌ Error: Background music file '{bg_music_file}' not found!")
    exit()

print("📂 Loading AI-generated voice...")
speech_audio = AudioSegment.from_mp3(speech_file)

print("🎵 Loading background music...")
bg_music = AudioSegment.from_wav(bg_music_file)

# Lower background music volume
bg_music = bg_music - 10
print("🔉 Lowered background music volume by 10dB.")

# Match lengths of speech and background music
if len(bg_music) > len(speech_audio):
    print(f"✂️ Trimming background music to match speech length: {len(speech_audio) / 1000:.2f}s")
    bg_music = bg_music[:len(speech_audio)]
else:
    print(f"✂️ Trimming speech to match background music length: {len(bg_music) / 1000:.2f}s")
    speech_audio = speech_audio[:len(bg_music)]

# Overlay speech onto background music
print("🎶 Mixing AI voice with background music...")
final_audio = bg_music.overlay(speech_audio)

# Export final audio
final_audio.export(output_file, format="mp3")
print(f"✅ Mixed final audio saved as '{output_file}'")
