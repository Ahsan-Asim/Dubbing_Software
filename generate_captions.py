# import json
# import os

# # File paths
# transcription_file = "output/transcription2.json"
# output_srt_file = "output/subtitles.srt"

# # Check if transcription file exists
# if not os.path.exists(transcription_file):
#     print(f"❌ Error: Transcription file '{transcription_file}' not found!")
#     exit()

# print("📂 Loading transcription file...")
# with open(transcription_file, "r", encoding="utf-8") as f:
#     transcription = json.load(f)

# # Function to format time for SRT
# def format_time(seconds):
#     millisec = int((seconds % 1) * 1000)
#     sec = int(seconds) % 60
#     minutes = (int(seconds) // 60) % 60
#     hours = int(seconds) // 3600
#     return f"{hours:02}:{minutes:02}:{sec:02},{millisec:03}"

# # Generate SRT content
# srt_content = ""
# print("📝 Generating SRT subtitles...")
# for i, segment in enumerate(transcription):
#     if "start" not in segment or "end" not in segment or "text" not in segment:
#         print(f"⚠️ Skipping segment {i+1} due to missing data.")
#         continue
    
#     start_time = format_time(segment["start"])
#     end_time = format_time(segment["end"])
#     text = segment["text"].strip()

#     if text:
#         srt_content += f"{i+1}\n{start_time} --> {end_time}\n{text}\n\n"
#         print(f"✅ Subtitle {i+1}: {start_time} --> {end_time}")

# # Save to SRT file
# with open(output_srt_file, "w", encoding="utf-8") as f:
#     f.write(srt_content)

# print(f"🎬 Subtitles successfully saved to '{output_srt_file}'")


import json

def format_time(seconds):
    millisec = int((seconds % 1) * 1000)
    sec = int(seconds) % 60
    minutes = (int(seconds) // 60) % 60
    hours = int(seconds) // 3600
    return f"{hours:02}:{minutes:02}:{sec:02},{millisec:03}"

def generate_srt(transcription_json, output_srt):
    with open(transcription_json, "r", encoding="utf-8") as f:
        transcription = json.load(f)

    srt_content = ""
    for i, segment in enumerate(transcription):
        start_time = format_time(segment["start"])
        end_time = format_time(segment["end"])
        text = segment["text"].strip()

        if text:
            srt_content += f"{i+1}\n{start_time} --> {end_time}\n{text}\n\n"

    with open(output_srt, "w", encoding="utf-8") as f:
        f.write(srt_content)

    print("✅ Subtitles saved!")

if __name__ == "__main__":
    generate_srt("static/outputs/transcription.json", "static/outputs/subtitles.srt")

