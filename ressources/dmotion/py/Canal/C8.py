#!/usr/bin/python3

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Referer": "http://www.callofliberty.fr/"
}

print('#EXTM3U')
print('#EXT-X-STREAM-INF:BANDWIDTH=7680000')

master_url = "http://s2.callofliberty.fr/direct/C8/master.m3u8"
s = requests.Session()

def get_specific_line_online(url, line_number):
    response = s.get(url, headers=headers)
    if response.status_code == 200:
        lines = response.text.split('\n')
        if 1 <= line_number <= len(lines):
            return lines[line_number - 1]
        else:
            return None
    else:
        return None

chunks = get_specific_line_online(master_url, 3)

prefix = "http://s2.callofliberty.fr/HLS-AES/"
index = chunks.find(prefix)

if index != -1:
    shortchunks = chunks[index + len(prefix):]
else:
    shortchunks = chunks
    
modified_url = shortchunks.replace("live-2", "live-3")

print(modified_url)
        #print(m3u)
        m3u = d[max(d, key=int)]    
    except Exception as e:
        m3u = na
    finally:
        print(m3u)

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000')
s = requests.Session()
with open('ressources/dmotion/py/Canal/C8_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
