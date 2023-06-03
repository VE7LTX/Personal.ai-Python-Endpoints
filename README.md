# Personal.ai Python Endpoints

This repository provides the default setup for all endpoints in the Personal AI Memory Stack V1. It is written in Python and utilizes the `requests` library for HTTP communications.

## Getting Started

### Prerequisites

To get started, you need:

- Python 3.6+

- Python `requests` library. Install it using pip:

  pip install requests

### Installation

Clone this repository to your local machine.

git clone https://github.com/<your-username>/personal-ai-python-endpoints.git

## Usage

This project consists of three main functions:

1. **`upload_memory()`**: This function uploads a text memory to the user's Personal AI memory stack.

   upload_memory(api_key, text, source_name, created_time=None, device_name=None, raw_feed_text=None)

   

2. **`send_ai_message()`**: This function sends a message to the user's Personal AI and returns the response.

   send_ai_message(api_key, text, context=None)

3. **`upload_url()`**: This function uploads a URL to the user's Personal AI memory stack.

   upload_url(api_key, url, start_time=None, source_app=None)

Please refer to the script file for more details on how to use these functions. Note that all the functions require an API key for authenticating with the Personal AI API.

## Testing

You can test these functions by running them in a Python environment and providing the necessary parameters.

Example:

api_key = "your-personal-ai-api-key"

text = "Hello Personal AI"

source_name = "Python Client"

upload_memory(api_key, text, source_name)

