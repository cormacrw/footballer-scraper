from bs4 import BeautifulSoup
import requests

def create_soup(url: str) -> BeautifulSoup:
    headers = {
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    page = requests.get(url, headers=headers)

    return BeautifulSoup(page.text, 'html.parser')