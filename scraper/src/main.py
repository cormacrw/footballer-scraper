from team_parse import get_team_details
from league_parse import get_league_details
from create_soup import create_soup
from aws_dynamo import update_team
# URL = "https://www.transfermarkt.us/john-stones/leistungsdaten/spieler/203460"
# URL = "https://www.transfermarkt.us/manchester-city/startseite/verein/281"
URL = "https://www.transfermarkt.us/premier-league/startseite/wettbewerb/GB1"

soup = create_soup(URL)

league = get_league_details(soup)

print(league)

for team in league.teams:
    update_team(team)
