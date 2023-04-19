from bs4 import BeautifulSoup
from player import Player

def set_player_number(soup: BeautifulSoup, player: Player):
    player_number_tag = soup.find_all(class_='data-header__shirt-number')
    
    if len(player_number_tag) == 0:
        raise Exception("couldn't find player number element")

    player_number_str = player_number_tag[0].string.strip()[1:]
    player.shirt_number = int(player_number_str)


def set_player_name(soup: BeautifulSoup, player: Player):
    player_name_text = soup.head.title.string
    dash_i = player_name_text.index('-')
    player.name = player_name_text[:dash_i].strip()

def set_player_age(soup: BeautifulSoup, player: Player):
    player_details_tag = soup.find(class_="data-header__details")
    
    if len(player_details_tag) == 0:
        raise Exception("couldn't find player details element")

    details_children = player_details_tag.contents[1]
    age_tag = details_children.find(attrs={"itemprop": "birthDate"})
    b_index = age_tag.string.index('(')
    cb_index = age_tag.string.index(')')
    player.age = int(age_tag.string[b_index+1:cb_index])

def set_player_nationality(soup: BeautifulSoup, player: Player):
    player_details_tag = soup.find(class_="data-header__details")
    
    if len(player_details_tag) == 0:
        raise Exception("couldn't find player details element")

    details_children = player_details_tag.contents[1]

    nationality_tag = details_children.find(attrs={"itemprop": "nationality"}).find(class_="flaggenrahmen")
    player.nationality = nationality_tag['title']

def set_player_position(soup: BeautifulSoup, player: Player):
    player_details_tag = soup.find(class_="data-header__details")
    
    if len(player_details_tag) == 0:
        raise Exception("couldn't find player details element")

    position_tag = player_details_tag.contents[3].contents[3].find(class_="data-header__content")
    player.position = position_tag.string.strip()

def set_player_club(soup: BeautifulSoup, player: Player):
    club_details_tag = soup.find(class_="data-header__club").find('a')
    player.club = club_details_tag['title']

    
def get_player_details(soup: BeautifulSoup) -> Player:
    p = Player()

    set_player_number(soup, p)
    set_player_name(soup, p)
    set_player_age(soup, p)
    set_player_nationality(soup, p)
    set_player_club(soup, p)
    set_player_position(soup, p)

    return p