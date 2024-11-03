from flask import Flask
import requests
import os

app = Flask(__name__)

# List of replica servers
replica_servers = ['http://localhost:5001', 'http://localhost:5002', 'http://localhost:5003']

# Path to the folder containing video files
video_folder = 'videos'

def push_videos():
    for server in replica_servers:
        for video_file in os.listdir(video_folder):
            file_path = os.path.join(video_folder, video_file)
            if os.path.isfile(file_path):
                # Open the video file and send it to the replica server
                with open(file_path, 'rb') as file:
                    files = {'video': (video_file, file)}
                    requests.post(f"{server}/store_video", files=files)
    print("Videos pushed to replica servers.")

if __name__ == '__main__':
    push_videos()  # Automatically push videos on startup
    app.run(port=5000)
