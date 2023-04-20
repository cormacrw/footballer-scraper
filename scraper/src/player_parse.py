from bs4 import BeautifulSoup
from models.player import Player
from create_soup import create_soup
import time

def set_player_number(soup: BeautifulSoup, player: Player):
    try:
        player_number_tag = soup.find_all(class_='data-header__shirt-number')
        
        if len(player_number_tag) == 0:
            print("couldn't find player number element for player id " + player.id)
            return

        player_number_str = player_number_tag[0].string.strip()[1:]
        player.shirt_number = int(player_number_str)
    except:
        print("Error setting player number for player " + player.id)


def set_player_name(soup: BeautifulSoup, player: Player):
    try:
        player_name_text = soup.head.title.string
        dash_i = player_name_text.index('-')
        player.name = player_name_text[:dash_i].strip()
    except:
        print("Error setting player name for player " + player.id)

def set_player_age(soup: BeautifulSoup, player: Player):
    try:
        player_details_tag = soup.find(class_="data-header__details")
        
        if len(player_details_tag) == 0:
            print("couldn't find player details element for player id " + player.id)
            return

        details_children = player_details_tag.contents[1]
        age_tag = details_children.find(attrs={"itemprop": "birthDate"})
        b_index = age_tag.string.index('(')
        cb_index = age_tag.string.index(')')
        player.age = int(age_tag.string[b_index+1:cb_index])
    except:
        print("Error setting player age for player " + player.id)

def set_player_nationality(soup: BeautifulSoup, player: Player):
    try:
        player_details_tag = soup.find(class_="data-header__details")
        
        if len(player_details_tag) == 0:
            print("couldn't find player details element for player id " + player.id)
            return

        details_children = player_details_tag.contents[1]

        nationality_tag = details_children.find(attrs={"itemprop": "nationality"}).find(class_="flaggenrahmen")
        player.nationality = nationality_tag['title']
    except:
        print("Error setting player nationality for player " + player.id)

def set_player_position(soup: BeautifulSoup, player: Player):
    try:
        player_details_tag = soup.find(class_="data-header__details")
        
        if len(player_details_tag) == 0:
            raise Exception("couldn't find player details element")

        position_tag = player_details_tag.contents[3].contents[3].find(class_="data-header__content")
        player.position = position_tag.string.strip()
    except:
        print("Error setting player position for player " + player.id)

def set_player_club(soup: BeautifulSoup, player: Player):
    try:
        club_details_tag = soup.find(class_="data-header__club").find('a')
        player.club = club_details_tag['title']
    except:
        print("Error setting player club for player " + player.id)
    
def get_player_details(playerId: str) -> Player:
    URL = "https://www.transfermarkt.us/hello-world/leistungsdaten/spieler/" + playerId
    soup = create_soup(URL)

    p = Player()
    p.id = playerId
    set_player_number(soup, p)
    set_player_name(soup, p)
    set_player_age(soup, p)
    set_player_nationality(soup, p)
    set_player_club(soup, p)
    set_player_position(soup, p)

    return p