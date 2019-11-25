import pytest
import requests
import os

url = 'http://localhost:9000/'
video_url = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'

r = requests.get(video_url)
with open("test_video.mp4", 'wb') as f:
    f.write(r.content)

def test_upload_delete():
    with requests.Session() as s:
        payload = {
        'username': 'oneeyedgrape',
        'password': 'password123'
        }
        p = s.post(url+'login', data=payload)  # authenticate
        assert p.url == url+'profile'
        files = {'file': open('test_video.mp4', 'rb')}
        p = s.post(url+'upload', files=files)  # upload video
        # print(p.text)
        assert p.url == url
        p = s.get(url+'watch/1')  # view video
        assert p.url == url+'watch/1'
        p = s.get(url+'delete/1')
        assert p.url == url
