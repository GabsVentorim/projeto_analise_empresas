import requests
from bs4 import BeautifulSoup
from typing import List, Dict

# Limit to top 3 unique recent news (not sure if more will be helpfull -> ask for luquinhas)
NEWS_NUM = 3 

class WebScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def fetch_page(self, url: str) -> str:
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return ""

    def get_company_news(self, ticker: str) -> List[Dict]:
        """Scrapes recent news for a given company ticker."""
        # test
        url = f"https://finance.yahoo.com/quote/{ticker}/news"
        html = self.fetch_page(url)
        
        if not html:
            return []

        soup = BeautifulSoup(html, 'html.parser')
        news_data = []
        
        links = [a['href'] for a in soup.find_all('a', href=True) if '/news/' in a['href']]
        
        for link in set(links[:NEWS_NUM]): 
            full_url = link if link.startswith('http') else f"https://finance.yahoo.com{link}"
            article_html = self.fetch_page(full_url)
            
            if article_html:
                article_soup = BeautifulSoup(article_html, 'html.parser')
                paragraphs = article_soup.find_all('p')
                content = " ".join([p.get_text() for p in paragraphs])
                
                if len(content) > 100: # Filter out empty or broken pages
                    news_data.append({
                        "source_url": full_url,
                        "raw_content": content
                    })
                    
        return news_data