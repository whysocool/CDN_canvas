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
    # Instead of directly redirecting the user to the replica server,
    # we redirect them to a route that shows them a web page with the video player.
    return redirect(url_for('watch_video', video_name=video_name, server=selected_server))

@app.route('/watch_video/<video_name>')
def watch_video(video_name):
    # The server parameter comes in from the request_video redirect
    server = request.args.get('server')
    if not server:
        # Fallback: If no server chosen, pick one randomly
        server = random.choice(replica_servers)
    # Construct the URL for the video
    video_url = f"{server}/get_video/{video_name}"
    return render_template('video.html', video_name=video_name, video_url=video_url)

if __name__ == '__main__':
    app.run(port=5004, debug=True)
