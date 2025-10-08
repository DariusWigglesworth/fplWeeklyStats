# From: https://medium.com/@mark_74548/how-to-extract-and-process-data-from-the-fpl-api-e5d95ecd7a84

import requests

def get_fpl_data():
    base_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(base_url)
    data = response.json()
    return data

fpl_data = get_fpl_data()

players_data = fpl_data['elements']
teams_data = fpl_data['teams']

spurs_team_id = None

for team in teams_data:
    if team['name'] == "Spurs":  # Check the FPL website to see how team names are presented.
        spurs_team_id = team['id']
        print(spurs_team_id)
        break

spurs_players = [player for player in players_data if player['team'] == spurs_team_id]

# for player in spurs_players:
#     print(f"{player['first_name']} {player['second_name']} - £{player['now_cost'] / 10}m")

print(spurs_players[0])