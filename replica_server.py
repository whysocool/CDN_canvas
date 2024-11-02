# replica_server.py
import sys

from flask import Flask, request

app = Flask(__name__)
videos_store = []  # Store videos here


@app.route('/store_video', methods=['POST'])
def store_video():
    video = request.json.get('video')
    videos_store.append(video)
    return "Video stored successfully.", 200


@app.route('/get_video/<video_name>', methods=['GET'])
def get_video(video_name):
    if video_name in videos_store:
        return f"Streaming video: {video_name}", 200
    return "Video not found.", 404


if __name__ == '__main__':
    # Use the port specified as a command-line argument, or default to 5001
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
    app.run(port=port)
