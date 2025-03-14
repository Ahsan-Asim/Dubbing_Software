# import whisper
# import json

# print("🚀 Loading Whisper model...")  # Show loading message
# model = whisper.load_model("small")
# print("✅ Model loaded successfully!")

# # Path to audio file
# audio_path = "separated/htdemucs/original_audio1/vocals.wav"
# print(f"🎤 Processing audio: {audio_path}")

# # Transcribe speech
# print("⏳ Transcription in progress... (This may take some time)")
# result = model.transcribe(
#     audio_path,
#     language="en",
#     word_timestamps=True,
#     temperature=0.5,
#     best_of=5,
#     beam_size=5,
#     fp16=False  # ✅ Force FP32 to avoid warning
# )

# print("✅ Transcription completed!")

# # Save as JSON
# output_path = "output/transcription2.json"
# print(f"💾 Saving transcription to {output_path}...")
# with open(output_path, "w") as f:
#     json.dump(result["segments"], f, indent=4)

# print("🎉✅ Transcription saved successfully!")

import whisper
import json

def transcribe_audio(audio_path, output_json):
    print("⏳ Transcribing audio... This may take a while.")
    model = whisper.load_model("small")
    result = model.transcribe(audio_path, language="en", word_timestamps=True)

    with open(output_json, "w") as f:
        json.dump(result["segments"], f, indent=4)

    print("✅ Transcription saved!")

if __name__ == "__main__":
    transcribe_audio("separated/htdemucs/original_audio/vocals.wav", "static/outputs/transcription.json")

