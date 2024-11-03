from flask import Flask, request, redirect
import random

app = Flask(__name__)
replica_servers = ['http://localhost:5001', 'http://localhost:5002', 'http://localhost:5003']


@app.route('/request_video/<video_name>', methods=['GET'])
def request_video(video_name):
    # Select a replica server (e.g., using random selection)
    selected_server = random.choice(replica_servers)

    # Redirect the client to the selected replica server
    return redirect(f"{selected_server}/get_video/{video_name}")


if __name__ == '__main__':
    app.run(port=5004)
