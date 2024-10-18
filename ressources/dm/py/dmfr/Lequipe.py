#! /usr/bin/python3

import requests

s = requests.Session()
response = s.get('https://www.dailymotion.com/video/x2lefik')

print(response.text)
