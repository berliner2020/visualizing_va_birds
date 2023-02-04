import config
import requests
import json
import pandas as pd
import dash

# Setup
eBirdAPIkey = config.eBirdAPIkey

payload = {}
headers = {
            "Accept": "application/json",
            "x-ebirdapitoken": eBirdAPIkey,
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0"
           }

# Models
# Get subregion information for US-VA
# subregion = "US-VA"
# va_subregions = requests.request(
#     "GET",
#     url=f"https://api.ebird.org/v2/ref/region/list/subnational2/{subregion}",
#     headers=headers
# )
#
# print(va_subregions.json())







# r = requests.get(
#     "https://api.ebird.org/v2/data/obs/VA/recent",
#     headers=headers
# )

# region = requests.get(
#     "https://api.ebird.org/v2/ref/region/info/US",
#     headers=headers
# )


