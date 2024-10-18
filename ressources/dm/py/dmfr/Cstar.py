#! /usr/bin/python3

import requests

s = requests.Session()
idvideo = line.split('/')[-1]
        url = f'https://www.dailymotion.com/video/x5gv5v0'
response = requests.get(url).json()
        stream_url = response['qualities']['auto'][0]['url']
        m3u = requests.get(stream_url).text
return m3u

output_directory = 'ressources/dm/py/hls'
os.makedirs(output_directory, exist_ok=True)

continue
        elif line.startswith('#'):
            current_category = line[1:]
        elif line.startswith('https://'):
            if current_category:
                file_name = f"{current_category.strip()}.m3u8"
                file_path = os.path.join(output_directory, file_name)
                m3u_content = snif(line)
                with open(file_path, 'w') as file:
                    file.write(m3u_content)


