# posrela
from bs4 import BeautifulSoup
from team_parse import get_team_details
from models.league import League
import time

def get_team_ids(soup: BeautifulSoup):
    team_table_container = soup.find(id='yw1')
    team_name_tags = team_table_container.find('tbody').find_all(class_='hauptlink')
    ids = []
    for team_name_tag in team_name_tags:
        url_tag = team_name_tag.find('a')
        ids.append(url_tag['href'].split('/')[4])
    return ids

def get_league_details(soup: BeautifulSoup):
    league = League()
    team_ids = get_team_ids(soup)

    for i, team_id in enumerate(team_ids):
        print(f"Scraping team {i + 1} of {len(team_ids)} with id {team_id}...")
        team = get_team_details(team_id)
        league.teams.append(team)
    
    return league
    
