import boto3
from models.team import Team

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('football-data')

def update_team(team: Team):
    table.put_item(
        Item={
            'fd_pk': f'team#{team.id}',
            'fd_sk': f'team#{team.id}',
            'id': team.id,
            'name': team.name
        }
    )

    for player in team.players:
        table.put_item(
            Item={
                'fd_pk': f'team#{team.id}',
                'fd_sk': f'player#{player.id}',
                'id': player.id,
                'name': player.name,
                'number': player.shirt_number,
                'position': player.position,
                'nationality': player.nationality,
                'club': player.club,
                'age': player.age
            }
        )
    return