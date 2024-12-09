from flask import Flask
import requests
import os

app = Flask(__name__)

replica_servers = [
    'http://localhost:5001',
    'http://localhost:5002',
    'http://localhost:5003'
]

video_folder = 'videos'

def push_videos():
    for server in replica_servers:
        for video_file in os.listdir(video_folder):
            file_path = os.path.join(video_folder, video_file)
            if os.path.isfile(file_path) and video_file.lower().endswith('.mp4'):
                with open(file_path, 'rb') as file:
                    files = {'video': (video_file, file)}
                    requests.post(f"{server}/store_video", files=files)
    print("Videos pushed to replica servers.")

@app.route('/')
def hello():
    return "Origin Server is Running!"

if __name__ == '__main__':
    push_videos()  # Automatically push videos on startup
    app.run(port=5000)
