#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5897200,CODECS="avc1.640028, mp4a.40.2", RESOLUTION=1920x1080, SUBTITLES="subs", AUDIO="audio_1000017564_128"')
s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-thema.ftven.fr/docs/735e9260-bb63-11ee-a1a7-0200170265fd_0_HLS-francedomtom/manifest.m3u8')

string = response.text
new_string = string.replace("manifest", "video_7201280_p_0")
print(new_string)
new2_string = string.replace("manifest", "A_audio_1000017564_128_fr")
print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_1000017564_128",LANGUAGE="fr",NAME="fr",DEFAULT=YES,AUTOSELECT=YES,URI="{new2_string}"')
