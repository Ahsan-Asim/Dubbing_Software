# Dubbing Software

This project uses AI tools to perform the following tasks:
1. Extracts vocals and background music from audio.
2. Transcribes the audio using Whisper.
3. Generates subtitles.
4. Syncs the AI-generated speech with background music.
5. Merges the synced audio with the video and adds subtitles to create the final dubbed video.

## Requirements

- Python 3.10 or higher
- ffmpeg (for video processing)
- Coqui TTS (Text-to-Speech for voice synthesis)
- Whisper (for transcription)
- Demucs (for separating vocals and background music)
- Pydub (for audio manipulation)

## Installation

### Set up Python environment

Create and activate a virtual environment:

python -m venv coqui_env
# Windows
.\coqui_env\Scripts\activate
# macOS/Linux
source coqui_env/bin/activate

# Now
Install the required dependencies:
pip install -r requirements.txt


# Required Dependencies:
TTS (Text to Speech by Coqui)
whisper (for transcription)
pydub (for audio manipulation)
ffmpeg (required for video processing)


# Install ffmpeg
You need to have ffmpeg installed for video processing. You can download it from FFmpeg's official website or install it via a package manager.

# Download Coqui TTS Models
Download the appropriate TTS model from Coqui's repository or the model used in this project (xtts_v2). Ensure it's placed in the correct directory:
TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)


# Usage

Prepare input files:

Audio file (e.g., original_audio.mp3)

Video file (e.g., video.mp4)

Transcription file (e.g., transcription.json)

Background music (e.g., other.wav)

Take speaker vocal sample

clone voice and generate complete transcritpion with that voice

sync the dubbed audio with original video by maintaing proper lipsyncing


# Run the project:
Execute the script:
python app.py

# The program will:

Extract vocals and background music from the provided audio.

Transcribe the audio.

Generate AI speech using the transcription.

Merge the generated speech with background music and the video.

Add subtitles to the final video.

# Final Output

The final video will be saved in the static/outputs/ folder as final_video.mp4.



# Troubleshooting

If you encounter issues with missing modules or dependencies:

Ensure you're working within the correct Python environment.

Reinstall dependencies using pip install -r requirements.txt.

Verify ffmpeg is properly installed and accessible from your command line.



# Limitations 

work finely from urdu to english dubbing

work efficiently for single speaker

