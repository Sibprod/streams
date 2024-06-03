#! /usr/bin/python3

import requests

s = requests.Session()
response = s.get('https://pwultrp.alwaysdata.net/lcp.php?m3u8')

print(response.text)
