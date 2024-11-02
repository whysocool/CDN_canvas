# client.py
import requests

def request_video(video_name):
    controller_url = 'http://localhost:5004'
    response = requests.get(f"{controller_url}/request_video/{video_name}")
    print(response.text)

if __name__ == '__main__':
    video_name = input("Enter the video name you want to request: ")
    request_video(video_name)
