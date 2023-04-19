import requests
from bs4 import BeautifulSoup
from player_parse import get_player_details

URL = "https://www.transfermarkt.us/john-stones/leistungsdaten/spieler/203460"

headers = {
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

p = get_player_details(soup)

print(p)