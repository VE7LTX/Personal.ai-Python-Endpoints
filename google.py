"""
Author: Matthew Schafer
Date: April 17, 2023
Description: A script to search Google for "land mobile radio companies" and show number of results and URLS in a list.
Replace: query with your search query
"""

from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json

# Define the search query
query = "land mobile radio companies"  # Replace with your search query

print("Sending search query to Google...")

# Send the query to Google and retrieve the search results
search_results = search(query, num_results=100)  # Change num_results to control the number of results to retrieve

# Create a list to store the URLs
urls = []

print(f"Found {len(search_results)} search results.")

# Iterate over each search result and extract the URL
for idx, result in enumerate(search_results):
    try:
        print(f"Processing search result {idx + 1}/{len(search_results)}: {result}")
        response = requests.get(result)
        soup = BeautifulSoup(response.content, 'html.parser')
        urls.append(result)
    except Exception as e:
        print(f"Error processing search result {idx + 1}: {e}")

print(f"Successfully Found and processed {len(urls)} URLs.")

