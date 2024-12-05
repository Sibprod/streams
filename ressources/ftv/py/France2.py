#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:5')
print('#EXT-X-STREAM-INF:BANDWIDTH=3032655,AVERAGE-BANDWIDTH=2756959,CODECS="avc1.64001f,mp4a.40.2",RESOLUTION=1280x720,FRAME-RATE=25.000,AUDIO="audio-AACL-96",SUBTITLES="text"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://simulcast-p.ftven.fr/simulcast/France_2/hls_fr2/index.m3u8')

string = response.text
new_string = string.replace("index", "France_2-avc1_2500000=5")
print(new_string)
new2_string = string.replace("index", "France_2-mp4a_96000_fra=1.m3u8")
print(f'#EXT-X-MEDIA:TYPE=AUDIO,URI="https://simulcast-p.ftven.fr/ZXhwPTE3MzM0MTE4OTh+YWNsPSUyZip+aG1hYz1iODZiMmY3Mjg4Mjc5OGZmMzg4Y2JjZTgzNjIxM2ZkZGY5ODE0YzEwMTE1ZTUwMGMwNmQyN2Y1YzdjNzRjMTA4/simulcast/France_2/hls_fr2/France_2-mp4a_96000_fra=1.m3u8",GROUP-ID="audio-AACL-96",LANGUAGE="fr",NAME="Francais",DEFAULT=YES,AUTOSELECT=YES,CHANNELS="2",URI="{new2_string}"')
