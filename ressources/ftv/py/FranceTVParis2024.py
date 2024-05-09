#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5897200,CODECS="avc1.640028, mp4a.40.2", RESOLUTION=1920x1080, SUBTITLES="subs", AUDIO="audio_1000017564_128"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-olympics.ftven.fr/paris2024-francedomtom/master.m3u8')

string = response.text
new_string = string.replace("master", "b0EF_720p", "b0EF_1080p")
print(new_string)
new2_string = string.replace("master", "b0EF_720p", "b0EF_1080p")
print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_1000017564_128",LANGUAGE="fr",NAME="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{new2_string}"')
