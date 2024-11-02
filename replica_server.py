# replica_server.py
from flask import Flask, request

app = Flask(__name__)
videos_store = []  # Store videos here

@app.route('/store_video', methods=['POST'])
def store_video():
    video = request.json.get('video')
    videos_store.append(video)
    return "Video stored successfully."

@app.route('/get_video/<video_name>', methods=['GET'])
def get_video(video_name):
    if video_name in videos_store:
        return f"Streaming video: {video_name}"
    return "Video not found.", 404

if __name__ == '__main__':
    app.run(port=5001)  # Change the port to 5002 and 5003 for other instances
