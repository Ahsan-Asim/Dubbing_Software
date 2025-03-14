import streamlit as st
import os
import subprocess
from werkzeug.utils import secure_filename

# Configure upload & output folders
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def run_processing_pipeline(video_path, output_video_path):
    """Run your AI dubbing pipeline."""
    subprocess.run(["python", "extract_audio.py", video_path])
    subprocess.run(["python", "separate_vocals.py"])
    subprocess.run(["python", "transcribe_audio.py"])
    subprocess.run(["python", "generate_voice.py"])
    subprocess.run(["python", "generate_captions.py"])
    subprocess.run(["python", "mix_audio.py"])
    subprocess.run(["python", "merge_audio_video.py", video_path, output_video_path])

st.title("🎬 AI Video Dubbing App")

uploaded_file = st.file_uploader("Upload a Video", type=["mp4", "mov", "avi"])

if uploaded_file:
    st.video(uploaded_file)

    if st.button("Process Video 🎙️"):
        new_filename = "Conversation3.mp4"
        video_path = os.path.join(UPLOAD_FOLDER, new_filename)
        
        with open(video_path, "wb") as f:
            f.write(uploaded_file.read())

        output_video_path = os.path.join(OUTPUT_FOLDER, "dubbed_" + secure_filename(uploaded_file.name))
        
        with st.spinner("Processing... ⏳"):
            run_processing_pipeline(video_path, output_video_path)
        
        st.success("✅ Dubbing Completed!")
        st.video(output_video_path)

        with open(output_video_path, "rb") as file:
            st.download_button("Download Dubbed Video 🎬", file, file_name="final_video.mp4", mime="video/mp4")
