#! /usr/bin/python3

import requests

print('#EXTM3U')
print('#EXT-X-VERSION:7')
print('#EXT-X-STREAM-INF:BANDWIDTH=2444000,AVERAGE-BANDWIDTH=2222000,CODECS="mp4a.40.5,avc1.4D401F",RESOLUTION=1280x720,AUDIO="audio-aach-96",CLOSED-CAPTIONS=NONE
')
s = requests.Session()
response = s.get(f'https://mdw-cji.akamaized.net/abxplore/hls/manifest.m3u8')

string = response.text
new_string = string.replace("manifest", "mwabxplore-audio_96545_fra=96000-video=2000000.m3u8")
print(new_string)
print(f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-aach-96",LANGUAGE="fr",NAME="French",DEFAULT=YES,AUTOSELECT=YES,CHANNELS="2"')

