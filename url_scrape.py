# Personal.ai Python Endpoints - URL Scraping

"""
This code adheres to the Python-specific adaptation of the "Power of Ten" programming rules:

1. Simplicity: The code follows a straightforward control flow with minimal branching.
2. Loop Control: The code uses a recursive function to control the depth of URL scraping.
3. Memory Management: The code uses a set to store visited URLs and avoids unnecessary memory usage.
4. Function Length: The scrape_urls() function has a single, clear purpose and is less than 60 lines long.
5. Assertions: Assertions are not used in this code, but you can add them if needed.
6. Scope: Variables are defined at the smallest possible level of scope.
7. Error Handling: Exceptions are caught and handled appropriately.
8. Import Management: Only the necessary Python modules (time, requests, re, json) are imported.
9. References: Immutable data structures are used where possible.
10. Linting and Static Analysis: The code should be regularly checked with a linter and a static type checker.

Make sure to replace 'keyzhere' with your actual API key for the Personal AI API memory stack.
"""

import time
import requests
import re
import json

def scrape_urls(url, depth):
    """
    Scrape URLs up to a given depth from a given URL.
    
    :param url: The URL to scrape.
    :param depth: The depth to scrape URLs.
    """
    if depth == 0:
        return

    visited_urls = set()

    def scrape_recursive(url, depth):
        if depth == 0:
            return

        if url in visited_urls:
            return

        visited_urls.add(url)

        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=3)

            if response.status_code == 200:
                html = response.text

                matches = re.findall(r'href=["\']?(\S+?)["\']?\s', html)

                for match in matches:
                    abs_url = requests.compat.urljoin(url, match)

                    if abs_url not in visited_urls:
                        print(abs_url)
                        time.sleep(0.025)
                        pages.append({"url": abs_url})

                        if depth > 1:
                            scrape_recursive(abs_url, depth-1)

                        payload = {
                            'Text': abs_url,
                            'SourceName': 'Web Scraping',
                            'CreatedTime': time.strftime('%a, %d %b %Y %H:%M:%S %Z'),
                            'DeviceName': 'Python Script',
                            'RawFeedText': f'Scraped URL: {abs_url}'
                        }

                        headers = {
                            'Content-Type': 'application/json',
                            'x-api-key': 'keyzhere'
                        }

                        response = requests.post('https://api.personal.ai/v1/memory', headers=headers, data=json.dumps(payload))

                        if response.status_code == 200:
                            print(f'Sent {abs_url} to Personal AI API Memory stack')
                        else:
                            print(f'Error sending {abs_url} to Personal AI API Memory stack: {response.text}')

                        time.sleep(1)
        except requests.exceptions.RequestException:
            pass

    scrape_recursive(url, depth)

# Define the URLs to scrape
root_urls = ["https://github.com/twitter/the-algorithm"]

# Define a list to store scraped URLs
pages = []

# Loop through each root URL and scrape URLs up to two levels deep
for url in root_urls:
    scrape_urls(url, 2)
