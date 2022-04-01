"""
weather :
wtc, wtb, temp_r

football:
local or ext
win, lose, draw
"""
from requests import request as r
import pandas as pd
import numpy as np
from models.weather.weather import Weather
from models.football.team import Team
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
df = pd.json_normalize(wt_response.json()['weather'])

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
df2 = pd.json_normalize(json_test)
t = Team(df2, 157)
team_results = t.get_results()

"""
une equipe => home/away => wtc/wtb/temp => w/l/d
une equipe => home/away => wtc/wtb/temp => num goals
une equipe => home/away => wtc/wtb/temp => ecart goals
"""


def get_team_weather_result_stats(fb_data, team_id):
    # 1 Team
    # dates pour le Weather
    # return graph
    t = Team(fb_data, team_id)
    t_results = t.get_results()
    print(f'[-] team : {t_results}')
    t_results['wtc_coeff'] = np.nan
    t_results['wtb_coeff'] = np.nan
    t_results['temp_r'] = np.nan

    for g in t_results.index:
        city, lat, lon = TEAMS_IDS[t_results.loc[g, 'home_id']].values()
        params = {
            'lat': lat,
            'lon': lon,
            'date': t_results.loc[g, 'date'].split('T')[0]
        }
        wt_response = r("GET", f'{W_URL}/weather', params=params)
        df3 = pd.json_normalize(wt_response.json()['weather'])
        w = Weather(df3)
        t_results.loc[g, 'wtc_coeff'] = w.wtc_coeff
        t_results.loc[g, 'wtb_coeff'] = w.wtb_coeff
        t_results.loc[g, 'temp_r'] = w.temp_r

    return t_results


def get_result_stats(fb_data, team_id):
    t_results = get_team_weather_result_stats(fb_data, team_id)
    # print(f'[-] teams: \n {t_results}')
    return pd.DataFrame(t_results, columns=['date', 'home_id', 'play', 'winner', 'wtc_coeff', 'wtb_coeff', 'temp_r'])


res_stats = get_result_stats(df2, 157)

# print(f"[-] results : \n {res_stats}")


def get_goal_stats(fb_data, team_id):
    t_goals = get_team_weather_result_stats(fb_data, team_id)
    return pd.DataFrame(t_goals, columns=['date', 'home_id', 'play', 'goals', 'wtc_coeff', 'wtb_coeff', 'temp_r'])


def get_goal_diff_stats(fb_data, team_id):
    t_goal_diff = get_team_weather_result_stats(fb_data, team_id)
    return pd.DataFrame(t_goal_diff, columns=['date', 'home_id', 'play', 'goal_diff', 'wtc_coeff', 'wtb_coeff', 'temp_r'])