from datetime import date
import pandas as pd
import numpy as np
from requests import request as r
from utils.utils import sanitize_data
from utils.football_constants import F_HEADERS, F_URL, BUNDESLIGA_ID, TEAM_FIXTURE_COLS, TEAM_FIXTURE_RENAMED_COLS


def get_prev_year_team_rank(team_id):
    """
    Get team rank of the previous year
    :param team_id: Id of the team to retrieve
    :return: Team rank or None if the team was not part of the league during the previous year
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


def get_team_infos(team_id):
    """
        Get team main infos, including name, city, logo, last year position and average rank starting from 2010
        :param team_id: Id of the team to retrieve
        :return: dataframe, Team main infos
    """
    f_params = {
        'id': team_id
    }
    # data infos
    try:
        f_team_data = r("GET", f'{F_URL}/teams', params=f_params, headers=F_HEADERS)

    except Exception as e:
        print(f'Les parametres {f_params} ne correspondent pas')
    else:
        res = f_team_data.json()['response']

    df = pd.DataFrame(pd.json_normalize(res), columns=['team.id', 'team.name', 'team.logo', 'venue.city'])
    df.rename(columns={'team.id': 'team_id', 'team.name': 'name', 'team.logo': 'logo', 'venue.city': 'city'},
              inplace=True)
    # data previous year rank
    df['prev_year_rank'] = get_prev_year_team_rank(team_id)
    df['avg_rank_o_years'] = get_average_team_rank(team_id)
    return df


def get_team_ended_games(team_id):
    """
    Get all ended games of one team with results, goals, and goal difference for each of them
    :param team_id: Id of the team to retrieve
    :return: dataframe, Team game results
    """
    curr_date = date.today()
    curr_season_year = curr_date.year if curr_date.month in range(8, 13) else (curr_date.year - 1)
    f_params = {
        'league': BUNDESLIGA_ID,
        'season': curr_season_year,
        'team': team_id
    }
    f = r("GET", f'{F_URL}/fixtures', params=f_params, headers=F_HEADERS)
    res = f.json()['response']
    df = pd.json_normalize(res)
    print(f'[-] df : \n {df}')
    team_games = sanitize_data(df, cols=TEAM_FIXTURE_COLS, renamed_cols=TEAM_FIXTURE_RENAMED_COLS)
    team_results = sanitize_fixtures_for_team(team_games, team_id)

    return team_results


def get_team_goals(team_id):
    pass


def get_team_next_game(team_id):
    pass


def sanitize_fixtures_for_team(f_data, team_id):
    f_data['goal_diff'] = abs(f_data.home_goals - f_data.away_goals)
    team_data = f_data[(f_data.home_id == team_id) | (f_data.away_id == team_id)]
    # get all games, home or away in the same Dataframe
    home = pd.DataFrame(team_data[team_data.home_id == team_id],
                        columns=['date', 'home_id', 'away_id', 'home_name', 'away_name', 'home_winner',
                                 'home_goals',
                                 'goal_diff'])

    away = pd.DataFrame(team_data[team_data.away_id == team_id],
                        columns=['date', 'home_id', 'away_id', 'home_name', 'away_name', 'away_winner',
                                 'away_goals',
                                 'goal_diff'])
    # renaming the columns, to prepare for concatenation
    home.rename(columns={'home_winner': 'winner', 'home_goals': 'goals'}, inplace=True)
    home['play'] = 'home'
    away.rename(columns={'away_winner': 'winner', 'away_goals': 'goals'}, inplace=True)
    away['play'] = 'away'
    # concatenate home and away
    team_results = pd.concat([home, away])
    # sanitize date
    team_results['date'] = [x.split('T')[0] for x in team_results['date']]
    team_results.sort_values(by='date', inplace=True, ascending=False)

    return team_results
