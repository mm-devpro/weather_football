from datetime import date
import os
import json
import pandas as pd
import numpy as np
from requests import request as r
from models.football.games import get_all_fixtures
from utils.utils import sanitize_data
from utils.football_constants import F_HEADERS, F_URL, BUNDESLIGA_ID, TEAM_FIXTURE_COLS, TEAM_FIXTURE_RENAMED_COLS, \
    TEAM_INFOS_COLS, TEAM_INFOS_RENAMED_COLS, TEAMS_IDS

with open(os.path.join('./data_files/fb_data.json'), 'r') as json_file:
    json_test = json.load(json_file)


def get_prev_year_team_rank(team_id):
    """
    Get team rank of the previous year
    :param team_id: Id of the team to retrieve
    :return: Team rank or None if the team was not part of the league during the previous year
    """
    """
    curr_date = date.today()
    # get current season year which can be the previous one, as season starts in september
    curr_season_year = curr_date.year if curr_date.month in range(8, 13) else (curr_date.year - 1)
    rank_params = {
        'league': BUNDESLIGA_ID,
        'season': int(curr_season_year) - 1,
        'team': team_id
    }

    try:
        prev_rank_data = r("GET", f'{F_URL}/standings', params=rank_params, headers=F_HEADERS)
        if prev_rank_data.json()['results'] != 0:
            prev_rank = prev_rank_data.json()['response'][0]['league']['standings'][0][0]['rank']
        else:
            prev_rank = None
    except IndexError as e:
        prev_rank = None
    """
    prev_rank = TEAM_IDS['team_id']['prev_y_rank']

    return prev_rank


def get_average_team_rank(team_id):
    """
    Get team avg rank starting from 2010
    :param team_id: Id of the team to retrieve
    :return: int, Team avg rank
    """
    ranks = []
    curr_year = date.today().year
    for y in range(2010, curr_year):
        rank_params = {
            'league': BUNDESLIGA_ID,
            'season': y,
            'team': team_id
        }
        try:
            rank_data = r("GET", f'{F_URL}/standings', params=rank_params, headers=F_HEADERS)
            if rank_data.json()['results'] != 0:
                rank = rank_data.json()['response'][0]['league']['standings'][0][0]['rank']
                ranks.append(rank)
            else:
                continue
        except IndexError as e:
            continue
    avg = np.around(np.mean(ranks), 2)
    return avg


def get_team_infos(fb_data, team_id):
    """
    Get team main infos, including name, city, logo, last year position and average rank starting from 2010
    :param fb_data: team data from football api
    :param team_id: Id of the team to retrieve
    :return: dataframe, Team main infos
    """
    """
    f_params = {
        'id': team_id
    }
    # data infos
    try:
        f_team_data = r("GET", f'{F_URL}/teams', params=f_params, headers=F_HEADERS)

    except Exception as e:
        return {
            "error": 404,
            "message": f'Les parametres {f_params} ne correspondent pas, erreur: {e}'
        }
    else:
        res = f_team_data.json()['response']
    """
    df = sanitize_data(pd.json_normalize(fb_data), cols=TEAM_INFOS_COLS, renamed_cols=TEAM_INFOS_RENAMED_COLS)
    # data previous year rank
    df['prev_year_rank'] = get_prev_year_team_rank(team_id)
    df['avg_rank_o_years'] = get_average_team_rank(team_id)
    return df


def get_team_ended_games(fb_data, team_id):
    """
    Get all ended games of one team with results, goals, and goal difference for each of them
    :param fb_data: fixture data from football api
    :param team_id: Id of the team to retrieve
    :return: dataframe, Team game results
    """
    team_games = get_team_games(fb_data, team_id)
    curr_d = str(date.today())
    team_games = team_games[str(team_games.date) < curr_d]
    return team_games


def get_team_games_for_years(fb_data, team_id, start, end):
    """
    Get all games of one team between start and end dates
    :param fb_data: fixture data from football api
    :param team_id: Id of the team to retrieve
    :param start: start date
    :param end: end date
    :return: dataframe, Team game results
    """
    team_games = get_team_games(fb_data, team_id)
    team_games = team_games[(start <= team_games.date) & (team_games.date < end)]
    return team_games


def get_team_games(fb_data, team_id):
    """
    Get all games of one team with results, goals, and goal difference
    :param fb_data: fixture data from football api
    :param team_id: Id of the team to retrieve
    :return: dataframe, Team game results
    """
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


def get_team_next_games(fb_data, team_id):
    """
    Get next non-started games of one team (for the current season) with results, goals, and goal difference for each of them
    :param fb_data: fixture data from football api
    :param team_id: Id of the team to retrieve
    :return: dataframe, Team game results
    """
    team_games = get_team_games(fb_data, team_id)
    curr_d = str(date.today())
    team_games = team_games[team_games.date >= curr_d]
    return team_games


