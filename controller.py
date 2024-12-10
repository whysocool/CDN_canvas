from flask import Flask, request, redirect, render_template, url_for
import random
import os

app = Flask(__name__)

replica_servers = [
    'http://localhost:5001',
    'http://localhost:5002',
    'http://localhost:5003'
]

# Path to the local directory containing the original videos
video_folder = 'videos'

def get_available_videos():
    # Dynamically fetch videos by scanning the directory
    if os.path.isdir(video_folder):
        return [f for f in os.listdir(video_folder) if f.lower().endswith('.mp4')]
    return []

@app.route('/')
def index():
    videos = get_available_videos()
    return render_template('index.html', videos=videos)

@app.route('/request_video/<video_name>', methods=['GET'])
def request_video(video_name):
    # Select a replica server randomly
    selected_server = random.choice(replica_servers)
    # Include the controller's IP address in the redirect URL
    controller_url = "http://localhost:5004"
    return redirect(f"{selected_server}/render_video/{video_name}?controller_url={controller_url}")


if __name__ == '__main__':
    app.run(port=5004, debug=True)
