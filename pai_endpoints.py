'''Here's an example of how you might present a detailed explanation of the functions in your code using a style similar to that found in a whitepaper or a technical document.

Overview
This codebase consists of three primary functions, each designed to interact with the Personal AI (P.A.I) API in a unique way. This API allows for data input into the AI system, offering a user interface that the AI can utilize to understand and interact with its user more effectively. These functions are all developed in Python and utilize the requests library for HTTP communications.

upload_memory()
The upload_memory() function enables users to upload text-based memories to their Personal AI's memory stack. Each memory is attached with a source name and can optionally include the time of creation, the device from which the memory was created, and a raw feed text.

The function communicates with the API endpoint by making a POST request with an API key in the header for authentication. A payload in JSON format, carrying all the required and optional memory data, is sent in the request. If the memory block creation is unsuccessful, the function raises an exception.

This function is critical in supplying the AI with past text-based data or experiences that the user wants it to learn from and consider during its interactions with the user.

send_ai_message()
The send_ai_message() function allows users to send messages to their Personal AI and retrieve responses from it. This function communicates with the P.A.I. API via a POST request, including the API key for authentication, and the text and optional context as a payload in JSON format.

If the request is unsuccessful, an exception is raised. The function returns the response from the AI, allowing users to interact with their AI in a conversational manner, using the provided text and context.

upload_url()
The upload_url() function lets users upload a URL to the Personal AI's memory stack. This can be particularly useful when the user wants their AI to consider web content during its interactions. The function communicates with the P.A.I. API using a POST request, including the API key for authentication, and the URL, start time, and source app as a payload in JSON format.

Just like the other functions, this function raises an exception when the request is unsuccessful, ensuring that errors in URL upload operations are promptly flagged.

These functions lay the groundwork for a Python-based application that interacts with the Personal AI system. By combining them in a coherent manner, one can develop an application that provides seamless integration between a user and their AI, thus enhancing the user's experience.
'''


from typing import Optional, Dict
import requests
import json

def upload_memory(api_key: str, text: str, source_name: str, created_time: Optional[str] = None,
                  device_name: Optional[str] = None, raw_feed_text: Optional[str] = None) -> Dict:
    """
    This function uploads a text memory to the user's memory stack.
    """
    url = "https://api.personal.ai/v1/memory"
    
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    
    payload = json.dumps({
        "Text": text,
        "SourceName": source_name,
        "CreatedTime": created_time,
        "DeviceName": device_name,
        "RawFeedText": raw_feed_text
    })
    
    response = requests.post(url, headers=headers, data=payload)
    
    if response.json().get("status") != "Memblock Created":
        raise Exception("Memory block creation failed")
    
    return response.json()

def send_ai_message(api_key: str, text: str, context: Optional[str] = None) -> Dict:
    """
    This function sends a message to the user's AI and returns the response.
    """
    url = "https://api.personal.ai/v1/message"
    
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    
    payload = json.dumps({
        "Text": text,
        "Context": context
    })
    
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code != 200:
        raise Exception("AI message request failed")
    
    return response.json()

def upload_url(api_key: str, url: str, start_time: Optional[str] = None, source_app: Optional[str] = None) -> Dict:
    """
    This function uploads a URL to the user's memory stack.
    """
    api_url = "https://api.personal.ai/v1/upload"
    
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    
    payload = json.dumps({
        "Url": url,
        "StartTime": start_time,
        "SourceApp": source_app
    })
    
    response = requests.post(api_url, headers=headers, data=payload)
    
    if response.status_code != 200:
        raise Exception("URL upload request failed")
    
    return response.json()


