# controller.py
from flask import Flask, request
import requests
import random

app = Flask(__name__)
replica_servers = ['http://localhost:5001', 'http://localhost:5002', 'http://localhost:5003']


@app.route('/request_video/<video_name>', methods=['GET'])
def request_video(video_name):
    # Select a replica server (round-robin or random selection)
    selected_server = random.choice(replica_servers)

    # Redirect the request to the selected replica server
    response = requests.get(f"{selected_server}/get_video/{video_name}")
    if response.status_code == 200:
        return response.text, 200
    return "Video not found on any replica server.", 404


if __name__ == '__main__':
    app.run(port=5004)
