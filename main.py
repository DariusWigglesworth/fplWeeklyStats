import requests
import json
from pathlib import Path
import pandas as pd

# Magic number conversion (Alhpabetical order)
teamIndexes = {
    1 : "Arsenal",
    2 : "Aston Villa",
    3 : "Bournemouth",
    4 : "Brentford",
    5 : "Brighton",
    6 : "Burnley",
    7 : "Chelsea",
    8 : "Crystal Palace",
    9 : "Everton",
    10 : "Fulham",
    11 : "Leeds",
    12 : "Liverpool",
    13 : "Manchester City",
    14 : "Manchester United",
    15 : "Newcastle",
    16 : "Nottingham Forest",
    17 : "Sunderland",
    18 : "Tottenham",
    19 : "Wolves",
    20 : "West Ham"
}

# expected goals (Home), expected goals against (Home), expected goals (Away), expected goals against (Away)
teamStats = [
    {"Games (H)" : 4, "xG (H)" : 8.1, "xGA (H)" : 1.7, "Games (A)" : 3, "xG (A)" : 3.8, "xGA (A)" : 2.6},
    {"Games (H)" : 4, "xG (H)" : 3.5, "xGA (H)" : 5.5, "Games (A)" : 3, "xG (A)" : 4.4, "xGA (A)" : 6.2},
    {"Games (H)" : 3, "xG (H)" : 4.4, "xGA (H)" : 2.2, "Games (A)" : 3, "xG (A)" : 4.0, "xGA (A)" : 4.2},
    {"Games (H)" : 4, "xG (H)" : 5.2, "xGA (H)" : 5.3, "Games (A)" : 3, "xG (A)" : 4.2, "xGA (A)" : 4.3},
    {"Games (H)" : 3, "xG (H)" : 5.0, "xGA (H)" : 3.7, "Games (A)" : 4, "xG (A)" : 6.2, "xGA (A)" : 8.9},
    {"Games (H)" : 3, "xG (H)" : 2.0, "xGA (H)" : 4.5, "Games (A)" : 4, "xG (A)" : 2.9, "xGA (A)" : 8.9},
    {"Games (H)" : 4, "xG (H)" : 6.5, "xGA (H)" : 5.8, "Games (A)" : 3, "xG (A)" : 4.9, "xGA (A)" : 3.9},
    {"Games (H)" : 3, "xG (H)" : 5.8, "xGA (H)" : 3.4, "Games (A)" : 4, "xG (A)" : 5.9, "xGA (A)" : 5.3},
    {"Games (H)" : 2, "xG (H)" : 6.3, "xGA (H)" : 5.5, "Games (A)" : 3, "xG (A)" : 3.0, "xGA (A)" : 4.0},
    {"Games (H)" : 3, "xG (H)" : 6.5, "xGA (H)" : 3.3, "Games (A)" : 3, "xG (A)" : 5.4, "xGA (A)" : 5.3},
    {"Games (H)" : 4, "xG (H)" : 6.1, "xGA (H)" : 2.5, "Games (A)" : 3, "xG (A)" : 5.5, "xGA (A)" : 5.3},
    {"Games (H)" : 3, "xG (H)" : 6.2, "xGA (H)" : 2.7, "Games (A)" : 4, "xG (A)" : 5.0, "xGA (A)" : 2.3},
    {"Games (H)" : 3, "xG (H)" : 6.2, "xGA (H)" : 2.7, "Games (A)" : 4, "xG (A)" : 5.9, "xGA (A)" : 4.4},
    {"Games (H)" : 4, "xG (H)" : 8.7, "xGA (H)" : 3.6, "Games (A)" : 3, "xG (A)" : 6.3, "xGA (A)" : 6.4},
    {"Games (H)" : 4, "xG (H)" : 6.4, "xGA (H)" : 3.3, "Games (A)" : 3, "xG (A)" : 7.0, "xGA (A)" : 3.5},
    {"Games (H)" : 4, "xG (H)" : 4.1, "xGA (H)" : 4.5, "Games (A)" : 4, "xG (A)" : 4.5, "xGA (A)" : 7.4},
    {"Games (H)" : 3, "xG (H)" : 3.3, "xGA (H)" : 3.5, "Games (A)" : 3, "xG (A)" : 2.7, "xGA (A)" : 2.7},
    {"Games (H)" : 3, "xG (H)" : 7.0, "xGA (H)" : 3.3, "Games (A)" : 4, "xG (A)" : 5.4, "xGA (A)" : 5.0},
    {"Games (H)" : 4, "xG (H)" : 3.0, "xGA (H)" : 4.8, "Games (A)" : 3, "xG (A)" : 5.4, "xGA (A)" : 5.0},
    {"Games (H)" : 4, "xG (H)" : 4.0, "xGA (H)" : 5.8, "Games (A)" : 3, "xG (A)" : 3.1, "xGA (A)" : 3.6}
]

matchweek = 8 # Set to current week

# See following URL for info on FPL API:
# https://medium.com/@mark_74548/how-to-extract-and-process-data-from-the-fpl-api-e5d95ecd7a84
matchweekURL = "https://fantasy.premierleague.com/api/fixtures/?event=" + str(matchweek)

# Check if data.json exists and is up to date
path = Path("data.json")
if not path.is_file():
    response = requests.get(matchweekURL)
    data = response.json()
    path.write_text(json.dumps(data), encoding="utf-8")
else:
    with open(path, 'r') as file:
        data = json.load(file)
        if data[0]["event"] != matchweek:
            response = requests.get(matchweekURL)
            data = response.json()
            path.write_text(json.dumps(data), encoding="utf-8")


columns = ["Team", "Home/Away", "xG/90", "xGA/90", "Opponent"]
df = pd.DataFrame(columns=columns)

with open("data.json", 'r') as file:
    data = json.load(file)
    for match in data:
        homeTeam = teamIndexes[match["team_h"]]
        awayTeam = teamIndexes[match["team_a"]]
        homeTeamStats = teamStats[match["team_h"] - 1]
        awayTeamStats = teamStats[match["team_a"] - 1]

        homePer90xG = round(homeTeamStats["xG (H)"] / homeTeamStats["Games (H)"], 2)
        homePer90xGA = round(homeTeamStats["xGA (H)"] / homeTeamStats["Games (H)"], 2)
        awayPer90xG = round(awayTeamStats["xG (A)"] / awayTeamStats["Games (A)"], 2)
        awayPer90xGA = round(awayTeamStats["xGA (A)"] / awayTeamStats["Games (A)"], 2)

        df = pd.concat([df, pd.DataFrame([[homeTeam, "Home", homePer90xG, homePer90xGA, awayTeam]], columns=columns)], ignore_index=True)
        df = pd.concat([df, pd.DataFrame([[awayTeam, "Away", awayPer90xG, awayPer90xGA, homeTeam]], columns=columns)], ignore_index=True)


print(df)