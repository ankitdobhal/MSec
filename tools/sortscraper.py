#!/usr/bin/python3
import requests
import sys
import webbrowser
if len(sys.argv) != 2 :
	print("Usage : python Sortscraper.py http://google.com")
	exit(1)

headers = {}
headers['User-Agent'] = "Googlebot"

req = requests.get(sys.argv[1],headers=headers)

res = webbrowser.open(sys.argv[1])

print(req.text)