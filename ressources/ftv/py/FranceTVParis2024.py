#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:BANDWIDTH=2855600,AVERAGE-BANDWIDTH=2479236,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640020,mp4a.40.2"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-olympics.ftven.fr/paris2024-francedomtom/master.m3u8')

string = response.text
new_string = string.replace("playlist", "b0EF_720p")
print(new_string)
new2_string = string.replace("iframe", "b0EF_720p")
print(f'#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=2855600,RESOLUTION=1280x720,CODECS="avc1.640020", URI="{new2_string}"')


