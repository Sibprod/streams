#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:BANDWIDTH=2855600,AVERAGE-BANDWIDTH=2479236,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.640020,mp4a.40.2"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-event.ftven.fr/out/v1/65fb695a25404e08944943d011abca75/index_france-domtom_45.m3u8')

string = response.text
new_string = string.replace("index_france-domtom_45.m3u8", "index_france-domtom_45.m3u8")
print(new_string)
new2_string = string.replace("index_france-domtom_45.m3u8", "index_france-domtom_45.m3u8")
print(f'#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=2855600,RESOLUTION=1280x720,CODECS="avc1.640020", URI="{new2_string}"')
