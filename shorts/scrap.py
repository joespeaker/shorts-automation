import requests
from bs4 import BeautifulSoup
import os

def scrape_joebieker():
    """Scrapes joebieker.com for all links on the page
    """

    url = f'https://www.joebieker.com/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    results = []
    for link in soup.find_all('a'):
        results.append({
            'title': link.text,
            'url': link.get('href')
        })

    return results

def main():
    """Scrapes the search results for the query "web scraping" from Google."""

    query = 'web scraping'
    results = scrape_joebieker()

    for result in results:
        print(result['title'])
        print(result['url'])

if __name__ == '__main__':
    main()
