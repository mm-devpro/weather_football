import pandas as pd
import numpy as np
from models.stats.statistics import get_avg_coeffs_per_venue, get_result_coeffs_for_team
from models.football.team_fixtures import get_all_fixtures_from_json_data
from models.stats.statistics import filter_team_fixtures_w_weather_from_json_data
from utils.football_constants import BUNDESLIGA_ID, F_HEADERS, F_URL


def get_fixture_prediction(fixture):
    """
    GET game prediction and return the game with draw/lose/win ratios
    :param fixture: pandas Serie with fixture infos from football api
    :return: fixture with added column "prediction" with draw/lose/win ratios
    """
    game = fixture
    home_team_coeffs = get_result_coeffs_for_team(fixture.home_id).loc['home']
    away_team_coeffs = get_result_coeffs_for_team(fixture.away_id).loc['away']
    h_mask = pd.DataFrame(home_team_coeffs, columns=['wtb_coeff', 'wtc_coeff', 'avg_temp'])
    a_mask = pd.DataFrame(away_team_coeffs, columns=['wtb_coeff', 'wtc_coeff', 'avg_temp'])
    game_coeffs = pd.Series(game, index=['wtb_coeff', 'wtc_coeff', 'avg_temp'])
    # print(f"[-] home team 1: \n {home_team_coeffs}")

    # difference between game coeffs and home or away avg coeffs (absolute values)
    home_team_coeffs.loc[:, [col not in ['temp_r', 'goals', 'goal_diff'] for col in home_team_coeffs.columns]] = \
        h_mask.subtract(game_coeffs, axis=1).abs()
    away_team_coeffs.loc[:, [col not in ['temp_r', 'goals', 'goal_diff'] for col in away_team_coeffs.columns]] = \
        a_mask.subtract(game_coeffs, axis=1).abs()
    # print(f"[-] home team 2: \n {home_team_coeffs}")
    # update variables, and divide coeffs by coeff_sum and return (1 - result) / 2 to get freq
    h_mask = pd.DataFrame(home_team_coeffs, columns=['wtb_coeff', 'wtc_coeff', 'avg_temp'])
    a_mask = pd.DataFrame(away_team_coeffs, columns=['wtb_coeff', 'wtc_coeff', 'avg_temp'])
    sum_h_coeffs = h_mask.sum(axis=0)
    sum_a_coeffs = a_mask.sum(axis=0)

    home_team_coeffs.loc[:, [col not in ['temp_r', 'goals', 'goal_diff'] for col in home_team_coeffs.columns]] = \
        (1 - (h_mask.div(sum_h_coeffs))) / 2
    away_team_coeffs.loc[:, [col not in ['temp_r', 'goals', 'goal_diff'] for col in away_team_coeffs.columns]] = \
        (1 - (a_mask.div(sum_a_coeffs))) / 2

    # get freq of all coeffs added
    home_team_coeffs.loc[:, 'result_ratio'] = (home_team_coeffs['wtb_coeff'] + home_team_coeffs['wtc_coeff'] + home_team_coeffs['avg_temp']) / 3
    away_team_coeffs.loc[:, 'result_ratio'] = (away_team_coeffs['wtb_coeff'] + away_team_coeffs['wtc_coeff'] + away_team_coeffs['avg_temp']) / 3

    if game.play == 'away':
        game_pred_ratio = (away_team_coeffs.reindex(index=['d', 'w', 'l']).loc[:, 'result_ratio'] + home_team_coeffs.reindex(index=['d', 'l', 'w']).loc[:, 'result_ratio']) / 2
        goal_pred = home_team_coeffs.loc[:, 'goals']
        goal_diff_pred = home_team_coeffs.loc[:, 'goal_diff']
        pred = pd.DataFrame([game_pred_ratio, goal_pred, goal_diff_pred]).T
        fixture.loc['prediction'] = pred.loc[pred.result_ratio.abs().idxmax()]
        is_pred_true(fixture)
        return fixture
    elif game.play == 'home':
        game_pred_ratio = (home_team_coeffs.reindex(index=['d', 'w', 'l']).loc[:, 'result_ratio'] + away_team_coeffs.reindex(index=['d', 'l', 'w']).loc[:, 'result_ratio']) / 2
        goal_pred = home_team_coeffs.loc[:, 'goals']
        goal_diff_pred = home_team_coeffs.loc[:, 'goal_diff']
        pred = pd.DataFrame([game_pred_ratio, goal_pred, goal_diff_pred]).T
        fixture.loc['prediction'] = pred.loc[pred.result_ratio.abs().idxmax()]
        is_pred_true(fixture)
        return fixture
    else:
        return


def is_pred_true(f_data):
    result = pd.Series({}, index=['result', 'goals', 'goal_diff'], dtype='float64')
    result['result'] = True if f_data.winner == f_data.prediction.name else False
    result['goals'] = True if f_data.goals == f_data.prediction.goals else False
    result['goal_diff'] = True if f_data.goal_diff == f_data.prediction.goal_diff else False
    f_data['pred_result'] = result
    return f_data
