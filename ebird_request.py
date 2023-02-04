import config
import requests
import json

# Setup
eBirdAPIkey = config.eBirdAPIkey

payload = {}
headers = {
            "Accept": "application/json",
            "x-ebirdapitoken": eBirdAPIkey,
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0"
           }
region = "US-VA"


class EBirdRequest:
    def __init__(self):
        self.eBirdAPIkey = eBirdAPIkey
        self.payload = payload
        self.headers = headers
        self.region = region

    def download_json(self):

        # Sent request to eBird API endpoint
        va_response = requests.request(
            "GET",
            url=f"https://api.ebird.org/v2/data/obs/{region}/recent",
            headers=headers
        )

        # Download json data and write to file
        va_json_list = va_response.json()
        va_json_string = json.dumps(va_json_list)

        with open("test.json", "w") as file:
            file.write(va_json_string)

