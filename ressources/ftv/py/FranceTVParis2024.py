#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:BANDWIDTH=5605600,AVERAGE-BANDWIDTH=4918939,RESOLUTION=1920x1080,FRAME-RATE=25.000,CODECS="avc1.640028,mp4a.40.2"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-olympics.ftven.fr/paris2024-francedomtom/master.m3u8')

string = response.text
new_string = string.replace("master", "b0EF_720p", "b0EF_1080p")
print(new_string)

