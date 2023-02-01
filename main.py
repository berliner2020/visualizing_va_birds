import config
import requests
import pandas
import dash

eBirdAPIkey = config.eBirdAPIkey

headers = {
    "Accept": "application/json",
    "x-ebirdapitoken": eBirdAPIkey,
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0"
           }

r = requests.get(
    "https://api.ebird.org/v2/data/obs/VA/recent",
    headers=headers
)

print(r.json())

