import pandas as pd
import numpy as np
from datetime import date
from requests import request as r
from utils.football_constants import TEAM_FIXTURE_COLS, TEAM_FIXTURE_RENAMED_COLS, F_HEADERS, F_URL, BUNDESLIGA_ID, TEAMS_IDS
from utils.utils import sanitize_data, convert_json_file_to_df

"""
------------------------------------------------------------------------------------------------------------------
------------------------------ FUNCTIONS RETURNING GAMES, OF A LEAGUE OR SPECIFIC TEAM ---------------------------
------------------------------------------------------------------------------------------------------------------
"""


def get_all_fixtures(league_id):
    """
    Method to query all fixtures of one league
    :param league_id: ID of the league to retrieve
    :return: all the fixtures/games of one league from 2010 to today
    """
    curr_date = date.today()
    curr_year = curr_date.year
    games_data = r("GET", f'{F_URL}/fixtures', params={'league': league_id, 'season': 2010}, headers=F_HEADERS)
    games = games_data.json()['response']
    games = sanitize_fixtures(pd.json_normalize(games))
    all_games = games
    for y in range(2011, curr_year):
        print(f"[-] season years: \n {y}")
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


def get_ended_fixtures(fb_data, team_id=None):
    """
    Get all ended games of one league or a specific team
    :param fb_data: fixture data from football api
    :param team_id: Id of team to retrieve, not mandatory
    :return: dataframe, all ended game results of a league/team
    """
    curr_d = str(date.today())
    games = fb_data
    if team_id is not None:
        games = filter_team_fixtures(fb_data, team_id)
    return games[games.date < curr_d]


def get_next_fixtures(fb_data, team_id=None):
    """
    Get games to come of one league or a specific team
    :param fb_data: fixture data from football api
    :param team_id: Id of team to retrieve, not mandatory
    :return: dataframe, all games to come of a league/team
    """
    curr_d = str(date.today())
    games = fb_data
    if team_id is not None:
        games = filter_team_fixtures(fb_data, team_id)
    return games[games.date >= curr_d]


def get_fixtures_for_spec_years(fb_data, start_date, end_date, team_id=None):
    """
    Get all games of one league or a specific team between start and end dates
    :param fb_data: fixture data from football api
    :param team_id: Id of the team to retrieve
    :param start_date: start date
    :param end_date: end date
    :return: dataframe, Team game results
    """
    games = fb_data
    if team_id is not None:
        games = filter_team_fixtures(fb_data, team_id)
    return games[(start_date <= games.date) & (games.date < end_date)]


def filter_team_fixtures(fb_data, team_id):
    """
    Filter all games of one team out of the dataset
    :param fb_data: fixture data from football api
    :param team_id: Id of the team to retrieve
    :return: dataframe, Team game results
    """
    # mask over the full dataset of games
    team_games = fb_data[(fb_data.home_id == team_id) | (fb_data.away_id == team_id)]
    # get all games, home or away in the same Dataframe
    home = pd.DataFrame(team_games[team_games.home_id == team_id],
                        columns=['date', 'city', 'home_id', 'away_id', 'home_name', 'away_name', 'home_winner',
                                 'home_goals',
                                 'goal_diff'])

    away = pd.DataFrame(team_games[team_games.away_id == team_id],
                        columns=['date', 'city', 'home_id', 'away_id', 'home_name', 'away_name', 'away_winner',
                                 'away_goals',
                                 'goal_diff'])
    # renaming the columns, to prepare for concatenation
    home.rename(columns={'home_winner': 'winner', 'home_goals': 'goals'}, inplace=True)
    home['play'] = 'home'
    away.rename(columns={'away_winner': 'winner', 'away_goals': 'goals'}, inplace=True)
    away['play'] = 'away'
    # concatenate home and away
    team_results = pd.concat([home, away])
    return team_results


def sanitize_fixtures(f_data):
    """
    Sanitize football games to return a DataFrame
    :param f_data: football games JSON format from football api
    :return: sanitized DataFrame for football fixtures
    """
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


"""
------------------------------------------------------------------------------------------------------------
--------------------------------- FUNCTIONS TO AVOID FOOTBALL API CALLS ------------------------------------------------------------------------------------------------------------------------------------------------
"""


def get_all_fixtures_from_json_data():
    """
    Get all fixtures from json data file
    :return: Pandas DataFrame with all games
    """
    fb_games = convert_json_file_to_df('./data_files/fb_fixtures.json')
    return fb_games


def save_fixtures_to_json(league_id):
    """
    Create json data files from football api and weather api, for specific league.
    :param league_id: ID of league to retrieve
    """
    df = get_all_fixtures(league_id)
    df2 = get_game_stats(df)
    df.to_json(r'./data_files/fb_fixtures.json', orient='index')
    df2.to_json(r'./data_files/fb_fixtures_w_weather.json', orient='index')