import pandas as pd

def save_urls_to_csv(urls, filename):
    df = pd.DataFrame(urls, columns=['URL'])
    df.to_csv(filename, index=False)

def save_urls_to_json(urls, filename):
    df = pd.DataFrame(urls, columns=['URL'])
    df.to_json(filename, orient='records')
