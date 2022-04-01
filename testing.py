from requests import request as r
import pandas as pd
import numpy as np
from models.weather.weather import Weather
from models.football.team import Team
from models.stats.statistics import Statistics
from utils.constants import W_URL, F_URL, TEAMS_IDS

json_test = [{'fixture': {'id': 587176, 'referee': 'F. Zwayer', 'timezone': 'UTC', 'date': '2020-12-18T18:30:00+00:00',
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
              'score': {'halftime': {'home': 3, 'away': 0}, 'fulltime': {'home': 0, 'away': 4},
                        'extratime': {'home': None, 'away': None}, 'penalty': {'home': None, 'away': None}}},{'fixture': {'id': 587176, 'referee': 'F. Zwayer', 'timezone': 'UTC', 'date': '2020-09-18T18:30:00+00:00',
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
                 'winner': False}}, 'goals': {'home': 7, 'away': 2},
              'score': {'halftime': {'home': 3, 'away': 0}, 'fulltime': {'home': 0, 'away': 4},
                        'extratime': {'home': None, 'away': None}, 'penalty': {'home': None, 'away': None}}},
             {'fixture': {'id': 587176, 'referee': 'F. Zwayer', 'timezone': 'UTC', 'date': '2020-09-18T18:30:00+00:00',
                          'timestamp': 1600453800, 'periods': {'first': 1600453800, 'second': 1600457400},
                          'venue': {'id': 700, 'name': 'Allianz Arena', 'city': 'München'}, 'status'
                          : {'long': 'Match Finished', 'short': 'FT', 'elapsed': 90}},
              'league': {'id': 78, 'name': 'Bundesliga 1', 'country': 'Germany',
                         'logo': 'https://media.api-sports.io/football/leagues/78.png',
                         'flag': 'https://media.api-sports.io/flags/de.svg', 'season': 2020,
                         'round': 'Regular Season - 1'}, 'teams': {
                 'home': {'id': 157, 'name': 'Bayern Munich',
                          'logo': 'https://media.api-sports.io/football/teams/157.png',
                          'winner': True},
                 'away': {'id': 174, 'name': 'FC Schalke 04',
                          'logo': 'https://media.api-sports.io/football/teams/174.png',
                          'winner': False}}, 'goals': {'home': 8, 'away': 0},
              'score': {'halftime': {'home': 3, 'away': 0}, 'fulltime': {'home': 0, 'away': 4},
                        'extratime': {'home': None, 'away': None}, 'penalty': {'home': None, 'away': None}}},
             {'fixture': {'id': 587176, 'referee': 'F. Zwayer', 'timezone': 'UTC', 'date': '2020-12-18T18:30:00+00:00',
                          'timestamp': 1600453800, 'periods': {'first': 1600453800, 'second': 1600457400},
                          'venue': {'id': 700, 'name': 'Allianz Arena', 'city': 'München'}, 'status'
                          : {'long': 'Match Finished', 'short': 'FT', 'elapsed': 90}},
              'league': {'id': 78, 'name': 'Bundesliga 1', 'country': 'Germany',
                         'logo': 'https://media.api-sports.io/football/leagues/78.png',
                         'flag': 'https://media.api-sports.io/flags/de.svg', 'season': 2020,
                         'round': 'Regular Season - 1'}, 'teams': {
                 'home': {'id': 174, 'name': 'FC Schalke 04',
                          'logo': 'https://media.api-sports.io/football/teams/157.png',
                          'winner': True},
                 'away': {'id': 157, 'name': 'Bayern Munich',
                          'logo': 'https://media.api-sports.io/football/teams/174.png',
                          'winner': False}}, 'goals': {'home': 0, 'away': 4},
              'score': {'halftime': {'home': 3, 'away': 0}, 'fulltime': {'home': 0, 'away': 4},
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

w_params = {
    'lat': 48.1371,
    'lon': 11.5753,
    'date': '2020-8-12'
}
f_params = {
    'league': 78,
    'season': 2020,
    'team': 157
}

payload = {}
headers = {
    'x-rapidapi-key': '6827e339753bf403ef08be29f1c08f14',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

wt_response = r("GET", f'{W_URL}/weather', params=w_params)

res1 = wt_response.json()['weather']
df = pd.json_normalize(res1)

wo = Weather(df)

print(f'[-] coeffs: \n {wo.wtc_coeff}, {wo.wtb_coeff}, {wo.temp_r}')

fb = r("GET", f'{F_URL}/fixtures', params=f_params, headers=headers, data=payload)
res2 = fb.json()['response']
df2 = pd.json_normalize(json_test)
t = Team(df2, 157)

"""
une equipe => home/away => wtc/wtb/temp => w/l/d
une equipe => home/away => wtc/wtb/temp => num goals
une equipe => home/away => wtc/wtb/temp => ecart goals
"""

stats = Statistics(t)
stats_res = stats.full_stats

