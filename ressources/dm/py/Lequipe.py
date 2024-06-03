#! /usr/bin/python3

import requests

s = requests.Session()
response = s.get('https://pwultrp.alwaysdata.net/equipe.php?m3u8')

print(response.text)
    except Exception as e:
        m3u = na
    finally:
        print(m3u)

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000')
s = requests.Session()
with open('ressources/dm/py/Lequipe_info.txt') as f:
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
