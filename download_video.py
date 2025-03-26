import requests

url = "static/outputs/final_video.mp4"  # Replace with the actual direct video URL
filename = "video.mp4"

response = requests.get(url, stream=True)

with open(filename, "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        file.write(chunk)

print("✅ Download complete!")
