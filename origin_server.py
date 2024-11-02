# origin_server.py
from flask import Flask
import requests

app = Flask(__name__)

# List of replica servers
replica_servers = ['http://localhost:5001', 'http://localhost:5002', 'http://localhost:5003']

def push_videos():
    # Example video data
    videos = ["video1.mp4", "video2.mp4"]
    for server in replica_servers:
        for video in videos:
            # Simulating sending video data to replica servers
            requests.post(f"{server}/store_video", json={"video": video})
    print("Videos pushed to replica servers.")

if __name__ == '__main__':
    push_videos()  # Automatically push videos on startup
    app.run(port=5000)
