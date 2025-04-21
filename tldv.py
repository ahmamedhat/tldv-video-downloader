from datetime import datetime
from os import system
import requests
import json

## Please install ffmpeg before running this script and make sure it's in your PATH
## brew install ffmpeg

## Please install requests before running this script
## pip3 install requests

## download video from tldv.io
##
## 1. Go to https://tldv.io/
## 2. Login
## 3. Go to the meeting you want to download
## 4. Copy the URL of the meeting
## 5. Open the developer tools (F12)
## 6. Go to the network tab
## 7. Refresh the page
## 8. Find the request to https://gw.tldv.io/v1/meetings/64145828ced74b0013d496ce/watch-page?noTranscript=true
## 9. Copy the auth token from the request headers
## 10. Run this script and paste the URL and auth token
## 11. python3 tldv.py

url = input("Please paste the URL of the meeting you want to download: ")

meeting_id = url.split("/")[-1]

print("\rFound meeting ID: ", meeting_id)

auth_token = input("Auth token: ")

data = requests.get(
    f"https://gw.tldv.io/v1/meetings/{meeting_id}/watch-page?noTranscript=true",
    headers={
        "Authorization": f"Bearer {auth_token}",
    },
)

try:
    response = json.loads(data.text)

    meeting = response.get("meeting", {})
    name = meeting.get("name", "No name")
    createdAt = meeting.get("createdAt", datetime.now())
    source = response.get("video", {}).get("source", None)

    date = datetime.strptime((createdAt), "%Y-%m-%dT%H:%M:%S.%fZ")
    normalised_date = date.strftime("%Y-%m-%d-%H-%M-%S")

    filename = f"{normalised_date}_{name}"
    filename_ext = ".mp4"

    command = f'ffmpeg -i {source} -c copy "{filename}.{filename_ext}"'

    json_filename = f'{filename}.json'

    with open(json_filename, "w") as f:
        f.write(data.text)

    print(command)

    print("Downloading video...")

    system(command)

except:
    print("Error encountered")
    print(data.text) 