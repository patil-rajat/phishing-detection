from scraper import scrape_urls
from utils import save_urls_to_csv

def main():
    page_url = "https://en.wikipedia.org/wiki/Peace_negotiations_in_the_Russian_invasion_of_Ukraine"
    urls = scrape_urls(page_url)
    
    if urls:
        save_urls_to_csv(urls, 'scraped_urls.csv')
        print(f"Saved {len(urls)} URLs to scraped_urls.csv")

if __name__ == "__main__":
    main()
