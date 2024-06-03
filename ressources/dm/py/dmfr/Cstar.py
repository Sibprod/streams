#! /usr/bin/python3

import requests

s = requests.Session()
response = s.get('https://www.dai.ly/x5gv5v0')

print(response.text)



