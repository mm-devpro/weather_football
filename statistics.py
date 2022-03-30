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
import numpy as np
from weather import Weather
from football import Team
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
                 'winner': False}}, 'goals': {'home': 8, 'away': 0},
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
                 'away': {'id': 157, 'name': 'FC Schalke 04',
                          'logo': 'https://media.api-sports.io/football/teams/157.png',
                          'winner': True},
                 'home': {'id': 174, 'name': 'Bayern Munich',
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

params = {
    'lat': 48.1371,
    'lon': 11.5753,
    'date': '2020-8-12'
}

payload = {}
headers = {
    'x-rapidapi-key': '6827e339753bf403ef08be29f1c08f14',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

wt_response = r("GET", f'{W_URL}/weather', params=params)
df = wt_response.json()['weather']

wo = Weather(df)
#
# print(f'[-] coeffs: \n {wo.wtc_coeff}, {wo.wtb_coeff}, {wo.temp_r}')

fb = r("GET", f'{F_URL}/fixtures?league=78&season=2020', headers=headers, data=payload)
res = fb.json()['response']

"""
I need to keep :
- fixture: id, date, venue: city
- teams: home: id, winner(false, true, null)
- teams: away: id, winner
- goals: home, away
"""

df2 = pd.DataFrame(pd.json_normalize(json_test),
                   columns=['fixture.id', 'fixture.date', 'fixture.venue.city', 'teams.home.id', 'teams.away.id',
                            'teams.home.name', 'teams.away.name', 'teams.home.winner', 'teams.away.winner',
                            'goals.home', 'goals.away'])
df2.rename(columns={'fixture.id': 'fixture_id', 'fixture.date': 'date', 'fixture.venue.city': 'city',
                    'teams.home.id': 'home_id', 'teams.away.id': 'away_id', 'teams.home.name': 'home_name',
                    'teams.away.name': 'away_name', 'teams.home.winner': 'home_winner',
                    'teams.away.winner': 'away_winner', 'goals.home': 'home_goals', 'goals.away': 'away_goals'},
           inplace=True)

# print(df2)
df2['goal_diff'] = df2.home_goals - df2.away_goals

munich = df2[(df2.home_name == 'Bayern Munich') | (df2.away_name == 'Bayern Munich')]

t = Team(munich, 157)
home, away = t.get_results()
# print(f'[-] teams: \n {away}')

"""
une equipe => home/away => wtc/wtb/temp => w/l/d
une equipe => home/away => wtc/wtb/temp => num goals
une equipe => home/away => wtc/wtb/temp => ecart goals
"""


def get_result_stats():
    # 1 Team
    # dates pour le Weather
    # return graph
    t = Team(munich, 157)
    home, away = t.get_results()

    for g in home.index:
        city, lat, lon = TEAMS_IDS[home['home_id'][g]].values()
        params = {
            'lat': lat,
            'lon': lon,
            'date': home['date'][g].split('T')[0]
        }
        wt_response = r("GET", f'{W_URL}/weather', params=params)
        df = wt_response.json()['weather']
        w = Weather(df)
        home['wtc_coeff'] = w.wtc_coeff
        home['wtb_coeff'] = w.wtb_coeff
        home['temp_r'] = w.temp_r

    for g in away.index:
        city, lat, lon = TEAMS_IDS[away['home_id'][g]].values()
        params = {
            'lat': lat,
            'lon': lon,
            'date': away['date'][g].split('T')[0]
        }
        wt_response = r("GET", f'{W_URL}/weather', params=params)
        df = wt_response.json()['weather']
        w = Weather(df)
        away['wtc_coeff'] = w.wtc_coeff
        away['wtb_coeff'] = w.wtb_coeff
        away['temp_r'] = w.temp_r

    # print(away, home)
    # TODO finish the function
    pass


res_stats = get_result_stats()

print(res_stats)

def get_goal_stats():
    pass


def get_goal_diff_stats():
    pass