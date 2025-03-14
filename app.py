from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename
import subprocess
import torch
torch.set_default_device("cpu")  # Force PyTorch to run on CPU

app = Flask(__name__)

# Configure upload and output folders
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

def run_processing_pipeline(video_path, output_video_path):
    """Run your dubbing pipeline here."""
    # Step 1: Extract Audio
    subprocess.run(["python", "extract_audio.py", video_path])

    # Step 2: Separate Vocals
    subprocess.run(["python", "separate_vocals.py"])

    # Step 3: Transcribe Audio
    subprocess.run(["python", "transcribe_audio.py"])

    # Step 4: Generate Voice
    subprocess.run(["python", "generate_voice.py"])

    # # Step 5: Generate Captions
    subprocess.run(["python", "generate_captions.py"])

    # # Step 6: Mix Audio
    subprocess.run(["python", "mix_audio.py"])

    # # Step 7: Merge Dubbing Output
    subprocess.run(["python", "merge_audio_video.py", video_path, output_video_path])
    # subprocess.run(["python", "aiwy.py"])

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Get uploaded video file
        uploaded_file = request.files["file"]
        if uploaded_file.filename == "":
            return "No file selected!"

        # Save uploaded file as "Conversation3.mp4"
        new_filename = "Conversation3.mp4"
        video_path = os.path.join(app.config["UPLOAD_FOLDER"], new_filename)
        uploaded_file.save(video_path)

        # Define output path with original filename
        original_filename = secure_filename(uploaded_file.filename)
        output_video_path = os.path.join(app.config["OUTPUT_FOLDER"], "dubbed_" + original_filename)

        # Run processing
        run_processing_pipeline(video_path, output_video_path)

        return f"""
        <h3>✅ Dubbing Completed!</h3>
        <a href='/download/{'dubbed_' + original_filename}'>Download Dubbed Video</a>
        """

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    filename= "final_video.mp4"
    output_video_path = os.path.join(app.config["OUTPUT_FOLDER"], filename)
    return send_file(output_video_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

