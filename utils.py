import os

def ensure_directories():
    directories = [
        "static/uploads",
        "static/outputs",
        "separated/htdemucs/original_audio/vocals.wav",
        "separated/htdemucs/original_audio/other.wav",
        "separated/htdemucs/vocals",
        "static/outputs/original_audio.mp3",
        "static/outputs/transcription.json",
        "static/outputs/final_synced_audio.mp3",
        "static/uploads/Conversation3.mp4",
        "static/outputs/subtitles.srt",
        "static/outputs/final_video.mp4",
        "static/uploads/speaker_sample.wav"


        # Add more directories as needed
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
