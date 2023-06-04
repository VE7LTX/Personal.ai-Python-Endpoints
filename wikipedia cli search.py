"""
Author: Matthew Schafer
Date: April 17, 2023
Description: A script to search for a user-specified topic on Wikipedia, upload the page titles to the Personal.ai 
Memory API, and display the matching page titles from the Memory API.
"""

import requests
import time

# Set the base URL for the API requests
base_url = 'https://api.personal.ai/v1'

# Set the API key for authorization
api_key = 'Keys_here'

# Set headers for all requests
headers = {
    'Content-Type': 'application/json',
    'x-api-key': api_key
}

# Prompt the user to enter a search topic
search_topic = input('Enter a search topic: ')

# Get a list of Wikipedia pages on the search topic
wikipedia_url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={search_topic}&format=json'
wikipedia_response = requests.get(wikipedia_url)
wikipedia_data = wikipedia_response.json()

# Iterate over the search results and upload the page titles to the Memory API
memory_objects = []
for result in wikipedia_data['query']['search']:
    page_title = result['title']
    upload_payload = {
        'Url': f'https://en.wikipedia.org/wiki/{page_title}',
        'StartTime': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'SourceApp': 'Wikipedia'
    }
    upload_url = f'{base_url}/upload'
    upload_response = requests.post(upload_url, headers=headers, json=upload_payload)
    if upload_response.status_code == 200:
        print(f'Page "{page_title}" uploaded successfully')
        memory_objects.append({
            'Text': page_title,
            'SourceName': 'Wikipedia',
            'CreatedTime': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'DeviceName': 'Python Script'
        })
    else:
        print(f'Error uploading page "{page_title}"')

# Upload the Memory objects to the Memory API
for memory_object in memory_objects:
    memory_url = f'{base_url}/memory'
    memory_response = requests.post(memory_url, headers=headers, json=memory_object)
    if memory_response.status_code == 200:
        print(f'Memory object "{memory_object["Text"]}" uploaded successfully')
    else:
        print(f'Error uploading memory object "{memory_object["Text"]}"')

# Get a list of all Memory objects from the Memory API
memory_list_url = f'{base_url}/memory/list'
memory_list_response = requests.get(memory_list_url, headers=headers)
memory_list_data = memory_list_response.json()

# Iterate over the Memory objects and print the page titles that match the search
for memory_object in memory_list_data['Memblocks']:
    if memory_object['Text'] == search_topic and memory_object['SourceName'] == 'Wikipedia':
        print(memory_object['Text'])