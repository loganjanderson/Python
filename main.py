import requests
import pprint

r = requests.get("https://api.dailysmarty.com/posts")
r.json