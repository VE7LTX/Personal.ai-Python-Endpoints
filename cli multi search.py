"""
Author: Matthew Schafer
Date: April 17, 2023
Description: A script to search various sources (Project Gutenberg, Reddit, YouTube, academic journals, and news websites)
for a user-specified keyword and display the URLs of the search results.
"""

import json
import re
import urllib
from urllib.parse import urlparse, urljoin

import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Define input for user
keyword = input("Enter a keyword to search for: ")  # Replace with your search query

def send_request(url):
    # Send an HTTP GET request to the URL and read the response
    response = requests.get(url)

    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    return soup

def search_gutenberg(keyword):
    # Build the URL for the Project Gutenberg search query
    query = urllib.parse.quote(keyword)
    url = f'https://www.gutenberg.org/ebooks/search/?query={query}'

    # Send an HTTP GET request to the URL and read the response
    soup = send_request(url)

    # Extract the book URLs from the search results
    urls = []
    for a in soup.find_all('a', href=True):
        if '/ebooks/' in a['href']:
            urls.append(urljoin(url, a['href']))
    
    return urls

def search_reddit(keyword):
    # Build the URL for the Reddit search query
    query = urllib.parse.quote(keyword)
    url = f'https://www.reddit.com/search?q={query}&sort=relevance&t=all'

    # Send an HTTP GET request to the URL and read the response
    soup = send_request(url)

    # Extract the post URLs from the search results
    urls = []
    for a in soup.find_all('a', {'class': 'SQnoC3ObvgnGjWt90zD9Z'}):
        urls.append(urljoin(url, a['href']))
    
    return urls

def search_youtube(keyword):
    # Build the URL for the YouTube search query
    query = urllib.parse.quote(keyword)
    url = f"https://www.youtube.com/results?search_query={query}"

    # Send an HTTP GET request to the URL and read the response
    soup = send_request(url)

    # Extract the video URLs from the search results
    urls = []
    for a in soup.findAll('a', href=True):
        if '/watch?v=' in a['href']:
            urls.append(urljoin('https://www.youtube.com/', a['href']))
    
    return urls

def search_academic_journals(keyword):
    # Build the URL for the NCBI PubMed search query
    keyword = keyword.replace(' ', '+')
    url = f"https://www.ncbi.nlm.nih.gov/pubmed/?term={keyword}"

    # Send an HTTP GET request to the URL and read the response
    response = requests.get(url)

    # Parse the response content using ElementTree
    root = ET.fromstring(response.content)

    # Extract the article URLs from the search results
    urls = []
    for article in root.iter('PubmedArticle'):
        titles = article.findall('.//ArticleTitle')
        url = article.findall('.//ArticleId[@IdType="pubmed"]')
        if len(titles) > 0:
            urls.append(urljoin('https://www.ncbi.nlm.nih.gov/pubmed/', url[0].text))
    
    return urls

def search_news(keyword):
    # Build the URLs for various news websites search queries
    cbc_url = f'https://www.cbc.ca/search?q={keyword}'
    ctv_url = f'https://www.ctvnews.ca/search-results/search-ctv-news-7.137#p={keyword}'
    global_url = f'https://globalnews.ca/search/{keyword}/'
    globe_url = f'https://www.theglobeandmail.com/search/?q={keyword}'
    post_url = f'https://nationalpost.com/?s={keyword}'
    star_url = f'https://www.thestar.com/search.html?q={keyword}&sortorder=desc&pagesize=10'
    sun_url = f'https://vancouversun.com/?s={keyword}'

    # Send HTTP requests to the news websites and parse the response content
    cbc_soup = send_request(cbc_url)
    ctv_soup = send_request(ctv_url)
    global_soup = send_request(global_url)
    globe_soup = send_request(globe_url)
    post_soup = send_request(post_url)
    star_soup = send_request(star_url)
    sun_soup = send_request(sun_url)

    # Extract the article URLs from the search results
    cbc_links = [a['href'] for a in cbc_soup.find_all('a', {'class': 'headline'})]
    ctv_links = [a['href'] for a in ctv_soup.find_all('a', {'class': 'card_link__1-Mi_ first_link__2zDcK '})]
    global_links = [a['href'] for a in global_soup.find_all('a', {'class': 'global-card__title-link'})]
    globe_links = [a['href'] for a in globe_soup.find_all('a', {'class': 'c-card__link'})]
    post_links = [a['href'] for a in post_soup.find_all('a', {'class': 'entry-title-link'})]
    star_links = [a['href'] for a in star_soup.find_all('a', {'class': 'article-title'})]
    sun_links = [a['href'] for a in sun_soup.find_all('a', {'class': 'entry-title-link'})]

    urls = cbc_links + ctv_links + global_links + globe_links + post_links + star_links + sun_links
    urls = list(set(urls))

    return urls

if __name__ == "__main__":
    keyword = input("Enter a keyword to search for: ")

    gutenberg_results = search_gutenberg(keyword)
    reddit_results = search_reddit(keyword)
    youtube_results = search_youtube(keyword)
    academic_journal_results = search_academic_journals(keyword)
    news_results = search_news(keyword)

    print("\nProject Gutenberg search results:")
    for url in gutenberg_results:
        print(url)

    print("\nReddit search results:")
    for url in reddit_results:
        print(url)

    print("\nYouTube search results:")
    for url in youtube_results:
        print(url)

    print("\nAcademic journal search results:")
    for url in academic_journal_results:
        print(url)

    print("\nNews search results:")
    for url in news_results:
        print(url)
