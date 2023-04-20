# posrela
from bs4 import BeautifulSoup
from player_parse import get_player_details
from models.team import Team
from create_soup import create_soup
import time

def set_team_id(soup: BeautifulSoup, team: Team):
    try:
        sub_nav_tag = soup.find(id='subnavi')
        
        team.id = sub_nav_tag.attrs['data-id']
    except:
        print("Error setting team id for team " + team.id)


def set_team_name(soup: BeautifulSoup, team: Team):
    try:
        team_name_tag = soup.find(class_='data-header__headline-wrapper')

        team.name = team_name_tag.string.strip()
    except:
        print("Error setting team name for team " + team.id)

def get_player_ids(soup: BeautifulSoup):
    player_name_tags = soup.find_all(class_='posrela')
    ids = []
    for player_name_tag in player_name_tags:
        url_tag = player_name_tag.find('table').find(class_='hide-for-small').find('a')
        ids.append(url_tag['href'].split('/').pop())
    return ids

def get_team_details(teamId: str):
    URL = "https://www.transfermarkt.us/manchester-city/startseite/verein/" + teamId +"/saison_id/2022"
    soup = create_soup(URL)

    team = Team()
    set_team_id(soup, team)
    set_team_name(soup, team)

    player_ids = get_player_ids(soup)
    for i, player_id in enumerate(player_ids):
        print(f"Scraping player {i + 1} of {len(player_ids)} with id {player_id}...")
        player = get_player_details(player_id)
        team.players.append(player)
    
    return team
    
