import subprocess

def merge_audio_video(video_path, dubbed_audio_path, subtitles_path, output_video_path):
    command = f'ffmpeg -i "{video_path}" -i "{dubbed_audio_path}" -map 0:v -map 1:a -c:v libx264 -c:a aac -strict experimental -vf "subtitles={subtitles_path}" "{output_video_path}"'
    subprocess.run(command, shell=True)
    print("✅ Dubbed video created successfully!")

if __name__ == "__main__":
    merge_audio_video(
        "static/uploads/Conversation3.mp4",
        "static/outputs/final_synced_audio.mp3",
        "static/outputs/subtitles.srt",
        "static/outputs/final_video.mp4"
    )
