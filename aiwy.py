import os
import json
import subprocess
from TTS.api import TTS
from pydub import AudioSegment

# ✅ Define paths
# speaker_audio_path = "static/outputs/original_audio.mp3"
# transcription_path = "static/outputs/transcription.json"
# background_music_path = "separated/htdemucs/original_audio/other.wav"
# output_audio_path = "static/outputs/final_synced_audio.mp3"
# video_path = "static/uploads/Conversation3.mp4"
# subtitles_path = "static/outputs/subtitles.srt"
# output_video_path = "static/outputs/final_video.mp4"
# extracted_sample_path = "static/uploads/speaker_sample.wav"
from utils import ensure_directories

ensure_directories()


# ✅ Ensure required files exist
for file_path in [speaker_audio_path, transcription_path, video_path, subtitles_path, background_music_path]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File '{file_path}' not found! Please upload it.")

# ✅ Load full speaker audio
full_audio = AudioSegment.from_mp3(speaker_audio_path)

# ✅ Extract a 15-second sample from the first 30 seconds
sample_duration = 15000  # 15 seconds in milliseconds
extracted_sample = full_audio[:sample_duration]
extracted_sample.export(extracted_sample_path, format="wav")
print("✅ Extracted 15-second speaker sample!")

# ✅ Load Coqui TTS with voice cloning (CPU mode)
try:
    import torch
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    torch.set_default_tensor_type(torch.FloatTensor)  # Ensure CPU compatibility
    print("✅ TTS model loaded successfully on CPU!")
except Exception as e:
    raise RuntimeError(f"❌ Failed to load TTS model: {e}")

# ✅ Read transcription JSON
try:
    with open(transcription_path, "r", encoding="utf-8") as f:
        transcript_data = json.load(f)
        print(f"✅ Loaded transcription with {len(transcript_data)} segments.")
except Exception as e:
    raise RuntimeError(f"❌ Error reading transcription JSON: {e}")

# ✅ Generate AI voice with timestamps
speech_segments = []
total_duration = 0

def generate_speech(text, file_path):
    """Generate speech using Coqui TTS and save to file."""
    try:
        tts.tts_to_file(
            text=text,
            file_path=file_path,
            speaker_wav=extracted_sample_path,
            language="en"
        )
        return AudioSegment.from_wav(file_path)
    except Exception as e:
        print(f"❌ Error generating speech for '{text}': {e}")
        return None

for segment in transcript_data:
    text = segment.get("text", "").strip()
    start_time = segment.get("start", 0)
    end_time = segment.get("end", start_time)
    duration = (end_time - start_time) * 1000

    if not text:
        print(f"⚠️ Skipping empty text segment at {start_time}s")
        continue

    temp_speech_file = f"temp_segment_{segment['id']}.wav"
    generated_speech = generate_speech(text, temp_speech_file)

    if generated_speech:
        generated_speech = generated_speech.set_frame_rate(22050).set_channels(1)

        if len(generated_speech) > duration:
            generated_speech = generated_speech[:int(duration)]
        else:
            silence_padding = AudioSegment.silent(duration=int(duration - len(generated_speech)))
            generated_speech += silence_padding

        silence_before = AudioSegment.silent(duration=int((start_time - total_duration) * 1000))
        speech_segments.append(silence_before + generated_speech)
        total_duration = end_time
    else:
        print(f"⚠️ Skipping failed segment at {start_time}s")

print("✅ AI-generated speech cloned and synchronized successfully!")

# ✅ Combine all speech segments
final_speech = sum(speech_segments)

# ✅ Load and adjust background music
try:
    background_music = AudioSegment.from_wav(background_music_path)
    background_music = background_music[:len(final_speech)] - 20
    print("✅ Background music loaded and adjusted!")
except Exception as e:
    raise RuntimeError(f"❌ Error loading background music: {e}")

# ✅ Merge speech with background music
final_audio = final_speech.overlay(background_music)

# ✅ Save final merged audio
try:
    final_audio.export(output_audio_path, format="mp3")
    print("✅ Background music merged with cloned voice!")
except Exception as e:
    raise RuntimeError(f"❌ Failed to export final audio: {e}")

# ✅ Merge final audio with video and subtitles
try:
    command = f'ffmpeg -i "{video_path}" -i "{output_audio_path}" -map 0:v -map 1:a -c:v libx264 -c:a aac -strict experimental -vf "subtitles={subtitles_path}" "{output_video_path}"'
    subprocess.run(command, shell=True, check=True)
    print("✅ Final dubbed video created successfully!")
except subprocess.CalledProcessError as e:
    raise RuntimeError(f"❌ FFmpeg error: {e}")
