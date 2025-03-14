from pydub import AudioSegment
from gtts import gTTS
import json
import os

def generate_voice(transcription_json, output_audio):
    with open(transcription_json, "r", encoding="utf-8") as f:
        transcription = json.load(f)

    base_audio = AudioSegment.silent(duration=5 * 60 * 1000)

    for i, segment in enumerate(transcription):
        start_time = int(segment["start"] * 1000)  
        text = segment.get("text", "").strip()

        if not text:
            continue  

        tts = gTTS(text=text, lang="en", slow=False)
        temp_filename = f"temp_{i}.mp3"
        tts.save(temp_filename)

        speech = AudioSegment.from_mp3(temp_filename)
        base_audio = base_audio.overlay(speech, position=start_time)

        os.remove(temp_filename)

    base_audio.export(output_audio, format="mp3")
    print("✅ Voice generation completed!")

if __name__ == "__main__":
    generate_voice("static/outputs/transcription.json", "static/outputs/dubbed_audio.mp3")


