"""
Author: Matthew Schafer
Date: April 17, 2023
Description: A script to create a memory text using the Personal.ai API.
"""

import requests
import json
from datetime import datetime
import pytz

def get_local_time():
    user_tz = datetime.now(pytz.utc).astimezone().tzinfo
    local_time = datetime.now(user_tz).strftime('%a, %d %b %Y %H:%M:%S %Z')
    return local_time

def create_memory(api_key, memory_data):
    base_url = 'https://api.personal.ai/v1/memory'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }

    response = requests.post(base_url, headers=headers, json=memory_data)
    
    if response.status_code == 200:
        creation_status = response.json()['status']
        return creation_status
    else:
        return None

def main():
    api_key = 'sZgZ0RVzIZLey-XKhbaEqUNxDmeYnUtH'
    local_time = get_local_time()
    
    memory_data = {
        "Text": f"This is a test memory created at {local_time}, check your stack and see if it shows up",
        "SourceName": "Python Memory Test Script",
        "CreatedTime": local_time,
        "DeviceName": "Change this Device Name Here",
        "RawFeedText": f"<p>This is a test memory created at {local_time}, <p> with VE7LTX.CC Thanks for Testing Today!"
    }
    
    creation_status = create_memory(api_key, memory_data)
    
    if creation_status is not None:
        print(f"Memory creation status: {creation_status}")
    else:
        print("Error creating memory")

if __name__ == "__main__":
    main()
