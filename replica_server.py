from flask import Flask, request, send_from_directory
import os
import sys

app = Flask(__name__)

port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
video_store_folder = f'stored_videos_{port}'
os.makedirs(video_store_folder, exist_ok=True)


@app.route('/store_video', methods=['POST'])
def store_video():
    if 'video' not in request.files:
        return "No video file found in request.", 400

    video = request.files['video']  # video is a FileStorage object
    video.save(os.path.join(video_store_folder, video.filename))
    return f"Video {video.filename} stored successfully in {video_store_folder}.", 200


@app.route('/get_video/<video_name>', methods=['GET'])
def get_video(video_name):
    return send_from_directory(video_store_folder, video_name)


if __name__ == '__main__':
    app.run(port=port)
