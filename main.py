from scraper import scrape_urls
from utils import save_urls_to_csv

def main():
    page_url = "Enter link here"
    urls = scrape_urls(page_url)
    
    if urls:
        save_urls_to_csv(urls, 'scraped_urls.csv')
        print(f"Saved {len(urls)} URLs to scraped_urls.csv")

if __name__ == "__main__":
    main()
