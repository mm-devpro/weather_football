import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from requests import request as r
from utils.football_constants import TEAMS_IDS, HOME_TEAM_FIXTURES_W_WEATHER, AWAY_TEAM_FIXTURES_W_WEATHER
from utils.weather_constants import W_URL
from utils.utils import convert_json_file_to_df
from models.football.team_fixtures import filter_team_fixtures, get_ended_fixtures
from models.weather.weather import get_weather_coeffs


def get_fixture_stats(fb_data):
    """
    Get all the fixtures then add weather coeffs to get all stats
    :param fb_data: football data as pandas DataFrame
    :return: pandas DataFrame with all the weather corresponding datas
    """
    game_stats = fb_data
    game_stats['wtb_coeff'] = np.nan
    game_stats['w_icon'] = np.nan
    game_stats['wtc_coeff'] = np.nan
    game_stats['avg_temp'] = np.nan
    game_stats['temp_r'] = np.nan

    for g in game_stats.index:
        prev_y_rank, name, city, lat, lon = TEAMS_IDS.T.loc[game_stats.loc[g, 'home_id']]
        params = {
            'lat': lat,
            'lon': lon,
            'date': game_stats.loc[g, 'date'].split('T')[0]
        }
        wt_response = r("GET", f'{W_URL}/weather', params=params)
        res = wt_response.json()['weather']
        df = pd.json_normalize(res)
        wtb_coeff, wtc_coeff, avg_temp, w_icon, temp_r = get_weather_coeffs(df)
        game_stats.loc[g, 'wtc_coeff'] = wtc_coeff
        game_stats.loc[g, 'w_icon'] = w_icon
        game_stats.loc[g, 'wtb_coeff'] = wtb_coeff
        game_stats.loc[g, 'avg_temp'] = avg_temp
        game_stats.loc[g, 'temp_r'] = temp_r

    return game_stats


def filter_team_fixtures_w_weather(fb_data, team_id):
    """
    Get all the fixtures of one team then add weather coeffs to get all stats
    :param fb_data: football data as pandas DataFrame
    :param team_id: Id of the football team to retrieve
    :return: pandas DataFrame with all the weather corresponding datas for one team
    """
    team_games = filter_team_fixtures(fb_data, team_id, HOME_TEAM_FIXTURES_W_WEATHER, AWAY_TEAM_FIXTURES_W_WEATHER)
    return team_games


def get_avg_coeffs_per_venue():
    games = get_fixtures_stats_from_json_data()
    curr_d = str(date.today())
    games = games[games.date < curr_d]
    df = pd.DataFrame(games, columns=['home_id', 'city', 'wtb_coeff', 'wtc_coeff', 'w_icon', 'avg_temp', 'temp_r'])
    df2 = df.groupby('city').mean()
    return df2


"""
------------------------- SAME FUNCTIONS BUT WITHOUT FOOTBALL/WEATHER API CALLS -------------------------------------
"""


def get_fixtures_stats_from_json_data():
    fb_data = convert_json_file_to_df('./data_files/fb_fixtures_w_weather.json')
    return fb_data


def filter_team_fixtures_w_weather_from_json_data(team_id):
    fb_data = get_fixtures_stats_from_json_data()
    team_fixtures_w_weather = filter_team_fixtures_w_weather(fb_data, team_id)
    return team_fixtures_w_weather


def get_team_ended_games_w_stats(team_id):
    """
    Get all ended games of one team with results, goals, and goal difference for each of them
    :param team_id: ID of the team to retrieve
    :return: dataframe, Team game results
    """
    team_games = get_team_fixtures_stats_from_json_data(team_id)
    curr_d = str(date.today())
    team_games = team_games[team_games.date < curr_d]
    return team_games


def get_team_next_games_w_weather(team_id):
    """
    Get all games to come of one team
    :param team_id: ID of the team to retrieve
    :return: dataframe, Team game results
    """
    team_games = get_team_game_stats_from_json_data(team_id)
    curr_d = str(date.today())
    team_games = team_games[team_games.date >= curr_d]
    return team_games


def get_results_coeffs_for_team(team_id):
    # data
    team = get_team_ended_fi_w_stats(team_id)
    team_res = pd.DataFrame(team.groupby(['play', 'winner']).median(), columns=['goals', 'goal_diff', 'wtb_coeff', 'wtc_coeff', 'avg_temp', 'temp_r'])

    return team_res

    # plot
    # fig, axs = plt.subplots(2, 2)
    # fig = plt.figure()
    # # check home games only
    # df = team_home.groupby('winner').mean()
    # print(df)
    # # for name, group in df:
    # #     # axs[0, 0].plot(group.winner, group.wtc_coeff, marker='o', markersize=4, label=name, linestyle='')
    # #     # axs[0, 0].plot(group.winner, group.wtb_coeff, marker='o', markersize=4, label=name, linestyle='')
    # #     # axs[1, 0].plot(group.winner, group.temp_r, marker='o', markersize=4, label=name, linestyle='')
    # #     plt.plot(group.winner, group.final_coeff, marker='o', markersize=4, label=name, linestyle='')
    # #
    # # # check away games only
    # df2 = team_away.groupby('winner').mean()
    # print(df2)
    # # for name, group in df2:
    # #     # axs[2, 0].plot(group.winner, group.wtc_coeff, marker='o', markersize=4, label=name, linestyle='')
    # #     # axs[2, 1].plot(group.winner, group.wtb_coeff, marker='o', markersize=4, label=name, linestyle='')
    # #     # axs[3, 0].plot(group.winner, group.temp_r, marker='o', markersize=4, label=name, linestyle='')
    # #     axs[1, 0].plot(group.winner, group.final_coeff, marker='o', markersize=4, label=name, linestyle='')
    #
    # plt.show()