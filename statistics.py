"""
weather :
wtc, wtb, temp_r

football:
local or ext
win, lose, draw
"""
from requests import request as r
import re
import pandas as pd
from weather import Weather
from utils.constants import W_URL, F_URL

json_test = [{'fixture': {'id': 587176, 'referee': 'F. Zwayer', 'timezone': 'UTC', 'date': '2020-09-18T18:30:00+00:00',
                          'timestamp': 1600453800, 'periods': {'first': 1600453800, 'second': 1600457400},
                          'venue': {'id': 700, 'name': 'Allianz Arena', 'city': 'München'}, 'status'
                          : {'long': 'Match Finished', 'short': 'FT', 'elapsed': 90}},
              'league': {'id': 78, 'name': 'Bundesliga 1', 'country': 'Germany',
                         'logo': 'https://media.api-sports.io/football/leagues/78.png',
                         'flag': 'https://media.api-sports.io/flags/de.svg', 'season': 2020,
                         'round': 'Regular Season - 1'}, 'teams': {
        'home': {'id': 157, 'name': 'Bayern Munich', 'logo': 'https://media.api-sports.io/football/teams/157.png',
                 'winner': True},
        'away': {'id': 174, 'name': 'FC Schalke 04', 'logo': 'https://media.api-sports.io/football/teams/174.png',
                 'winner': False}}, 'goals': {'home': 8, 'away': 0},
              'score': {'halftime': {'home': 3, 'away': 0}, 'fulltime': {'home': 8, 'away': 0},
                        'extratime': {'home': None, 'away': None}, 'penalty': {'home': None, 'away': None}}},
             {'fixture': {'id': 587177, 'referee':
                 'F. Brych', 'timezone': 'UTC', 'date': '2020-09-19T16:30:00+00:00', 'timestamp': 1600533000,
                          'periods': {'first': 1600533000, 'second': 1600536600},
                          'venue': {'id': 702, 'name': 'Signal-Iduna-Park', 'city': 'Dortmund'},
                          'status': {'long': 'Match Finished', 'short': 'FT', 'elapsed': 90}},
              'league': {'id': 78, 'name': 'Bundesliga 1', 'country': 'Germany',
                         'logo': 'https://media.api-sports.io/football/leagues/78.png',
                         'flag': 'https://media.api-sports.io/flags/de.svg', 'season': 2020,
                         'round': 'Regular Season - 1'}, 'teams': {'home': {'id': 165, 'name': 'Borussia Dortmund',
                                                                            'logo': 'https://media.api-sports.io/football/teams/165.png',
                                                                            'winner': True}, 'away': {'id': 163,
                                                                                                      'name': 'Borussia Monchengladbach',
                                                                                                      'logo': 'https://media.api-sports.io/football/teams/163.png',
                                                                                                      'winner': False}},
              'goals': {'home': 3, 'away': 0},
              'score': {'halftime': {'home': 1, 'away': 0}, 'fulltime': {'home': 3, 'away': 0},
                        'extratime': {'home': None, 'away': None}, 'penalty': {'home': None, 'away': None}}}]

params = {
    'lat': 48.1371,
    'lon': 11.5753,
    'date': '2020-2-12'
}

payload = {}
headers = {
    'x-rapidapi-key': '6827e339753bf403ef08be29f1c08f14',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

wt_response = r("GET", f'{W_URL}/weather?lat=48.1371&lon=11.5753&date=2021-04-12', params=params)
df = wt_response.json()['weather']

w = Weather(df)

fb = r("GET", f'{F_URL}/fixtures?league=78&season=2020', headers=headers, data=payload)
res = fb.json()['response']

"""
I need to keep :
- fixture: id, date, venue: city
- teams: home: id, winner(false, true, null)
- teams: away: id, winner
- goals: home, away
"""
dt = [{k: v for k, v in x.items() if k in ['fixture', 'goals', 'teams']} for x in json_test]
dt_fixt = [{k: v for k, v in x['fixture'].items() if k in ['date', 'id', 'venue']} for x in dt]
dt_goals = [{k: v for k, v in x['goals'].items()} for x in dt]
dt_teams = [{k: v for k, v in x['teams'].items()} for x in dt]

df2 = pd.json_normalize(json_test).filter(regex=('^teams|fixture.id|fixture.date|fixture.venue.city|goals.home|goals.away'))

print(df2)
