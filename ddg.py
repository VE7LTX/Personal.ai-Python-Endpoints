"""
Author: Matthew Schafer
Date: April 17, 2023
Description: A script to search DuckDuckGo for "land mobile radio companies" and show number of results and URLS in a list.
Replace: query with your search query
"""
import requests
from requests_html import HTMLSession
import json

# Define the search query
query = "land mobile radio companies"  # Replace with your search query

print("Sending search query to DuckDuckGo...")

# Send the query to DuckDuckGo and retrieve the search results
session = HTMLSession()
response = session.get(f'https://duckduckgo.com/html/?q={query}')
response.html.render()
search_results = response.html.xpath('//a[@class="result__url"]/@href')  # Extract the URLs from the search results

# Create a list to store the URLs
urls = []

print(f"Found {len(search_results)} search results.")

# Iterate over each search result and extract the URL
for idx, result in enumerate(search_results):
    try:
        print(f"Processing search result {idx + 1}/{len(search_results)}: {result}")
        urls.append(result)
    except Exception as e:
        print(f"Error processing search result {idx + 1}: {e}")

print(f"Successfully found and processed {len(urls)} URLs.")
