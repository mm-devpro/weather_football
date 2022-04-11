import pandas as pd
import numpy as np
from datetime import date
from requests import request as r
from utils.football_constants import TEAM_FIXTURE_COLS, TEAM_FIXTURE_RENAMED_COLS, F_HEADERS, F_URL, BUNDESLIGA_ID, TEAMS_IDS
from utils.utils import sanitize_data


def get_all_fixtures():
    curr_date = date.today()
    curr_year = curr_date.year
    games_data = r("GET", f'{F_URL}/fixtures', params={'league': BUNDESLIGA_ID, 'season': 2010}, headers=F_HEADERS)
    games = games_data.json()['response']
    games = sanitize_fixtures(pd.json_normalize(games))
    all_games = games
    for y in range(2011, curr_year):
        fb_params = {
            'league': BUNDESLIGA_ID,
            'season': y,
        }
        try:
            games_data = r("GET", f'{F_URL}/fixtures', params=fb_params, headers=F_HEADERS)
            games = games_data.json()['response']
            games = sanitize_fixtures(pd.json_normalize(games))
        except IndexError as e:
            return {
                "error": 404,
                "message": "problem with retrieving fb fixture data, try again later"
            }
        else:
            all_games = pd.concat([all_games, games])

    all_games.sort_values(by='date', inplace=True, ascending=False, ignore_index=True)
    return all_games


def sanitize_fixtures(f_data):
    games_data = sanitize_data(f_data, cols=TEAM_FIXTURE_COLS, renamed_cols=TEAM_FIXTURE_RENAMED_COLS)
    games_data.rename(columns=TEAM_FIXTURE_RENAMED_COLS, inplace=True)
    games_data['goal_diff'] = abs(games_data.home_goals - games_data.away_goals)
    # renaming winner columns
    games_data = games_data.replace({
        'home_winner': {True: 'w', False: 'l', None: 'd'},
        'away_winner': {True: 'w', False: 'l', None: 'd'}
    })
    # sanitizing venue city column to avoid None
    games_data.city = np.where(games_data.city is None, games_data.city, TEAMS_IDS[games_data.home_id].loc['city'])
    # sanitize date
    games_data['date'] = [x.split('T')[0] for x in games_data['date']]

    return games_data
