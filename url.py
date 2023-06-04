"""
Author: Matthew Schafer
Date: April 17, 2023
Description: A script to upload a URL to your Personal.ai using the Upload Url API.
"""

import requests
import json
from datetime import datetime
import pytz

def get_local_time():
    user_tz = datetime.now(pytz.utc).astimezone().tzinfo
    local_time = datetime.now(user_tz).strftime('%a, %d %b %Y %H:%M:%S %Z')
    return local_time

def upload_url(api_key, url_data):
    base_url = 'https://api.personal.ai/v1/upload'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }

    response = requests.post(base_url, headers=headers, json=url_data)
    
    if response.status_code == 200:
        upload_status = response.json()['status']
        return upload_status
    else:
        return None

def main():
    api_key = '{{user-api-key}}'
    local_time = get_local_time()
    url_data = {
        "Url": "https://ve7ltx.cc/",
        "StartTime": local_time,
        "SourceApp": "PY Push Upload_Url"
    }
    
    upload_status = upload_url(api_key, url_data)
    
    if upload_status is not None:
        print(f"Upload status: {upload_status}")
    else:
        print("Error uploading URL")

if __name__ == "__main__":
    main()
