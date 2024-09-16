import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_urls(page_url):
    response = requests.get(page_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        urls = [urljoin(page_url, link['href']) for link in links]
        return urls
    else:
        print(f"Failed to retrieve page: {page_url}")
        return []
