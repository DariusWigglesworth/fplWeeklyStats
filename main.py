import requests
import pandas as pd

# Magic number conversion (Alhpabetical order)
teamIndexes = {
    "Arsenal" : 1,
    "Aston Villa" : 2,
    "Bournemouth" : 3,
    "Brentford" : 4,
    "Brighton" : 5,
    "Burnley" : 6,
    "Chelsea" : 7,
    "Crystal Palace" : 8,
    "Everton" : 9,
    "Fulham" : 10,
    "Leeds" : 11,
    "Liverpool" : 12,
    "Manchester City" : 13,
    "Manchester United" : 14,
    "Newcastle" : 15,
    "Nottingham Forest" : 16,
    "Sunderland" : 17,
    "Tottenham" : 18,
    "Wolves" : 19,
    "West Ham" : 20
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

response = requests.get("https://fantasy.premierleague.com/api/fixtures/?event=" + str(matchweek))

columns = ["Team", "Home/Away", "xG", "xGA", "Opponent"]

df = pd.DataFrame(columns=columns)