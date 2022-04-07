import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from requests import request as r
from utils.football_constants import TEAMS_IDS
from utils.weather_constants import W_URL
from models.football.team import get_team_ended_games
from models.weather.weather import get_weather_coeffs


def get_games_stats_for_a_team(team_id, start, end):
    team_res = get_team_ended_games(team_id, start, end)

    team_res['wtb_coeff'] = np.nan
    team_res['w_icon'] = np.nan
    team_res['wtc_coeff'] = np.nan
    team_res['avg_temp'] = np.nan
    team_res['temp_r'] = np.nan

    for g in team_res.index:
        name, city, lat, lon = TEAMS_IDS.T.loc[team_res.loc[g, 'home_id']]
        params = {
            'lat': lat,
            'lon': lon,
            'date': team_res.loc[g, 'date'].split('T')[0]
        }
        wt_response = r("GET", f'{W_URL}/weather', params=params)
        res = wt_response.json()['weather']
        df = pd.json_normalize(res)
        wtb_coeff, wtc_coeff, avg_temp, w_icon, temp_r = get_weather_coeffs(df)
        team_res.loc[g, 'wtc_coeff'] = wtc_coeff
        team_res.loc[g, 'w_icon'] = w_icon
        team_res.loc[g, 'wtb_coeff'] = wtb_coeff
        team_res.loc[g, 'avg_temp'] = avg_temp
        team_res.loc[g, 'temp_r'] = temp_r

    return team_res


def get_results_graphs(team_id):
    # data
    team_res = get_games_stats_for_a_team(team_id)
    team_res['final_coeff'] = ((team_res['wtc_coeff'] * 4) + (team_res['wtb_coeff'] * 4) + (team_res['temp_r'] * 2)) / 10
    team_home = team_res[team_res.play == 'home']
    team_away = team_res[team_res.play == 'away']
    team_home_win = team_res[(team_res.play == 'home') & (team_res.winner == 'w')]
    team_away_win = team_res[(team_res.play == 'away') & (team_res.winner == 'w')]
    team_d = team_res[team_res.winner == 'd']

    # plot
    fig, axs = plt.subplots(4, 2)
    # check home games only
    df = team_home.groupby('winner')
    for name, group in df:
        axs[0, 0].plot(group.winner, group.wtc_coeff, marker='o', markersize=4, label=name, linestyle='')
        axs[0, 1].plot(group.winner, group.wtb_coeff, marker='o', markersize=4, label=name, linestyle='')
        axs[1, 0].plot(group.winner, group.temp_r, marker='o', markersize=4, label=name, linestyle='')
        axs[1, 1].plot(group.winner, group.final_coeff, marker='o', markersize=4, label=name, linestyle='')

    # check away games only
    df2 = team_away.groupby('winner')
    for name, group in df2:
        axs[2, 0].plot(group.winner, group.wtc_coeff, marker='o', markersize=4, label=name, linestyle='')
        axs[2, 1].plot(group.winner, group.wtb_coeff, marker='o', markersize=4, label=name, linestyle='')
        axs[3, 0].plot(group.winner, group.temp_r, marker='o', markersize=4, label=name, linestyle='')
        axs[3, 1].plot(group.winner, group.final_coeff, marker='o', markersize=4, label=name, linestyle='')

    plt.show()
