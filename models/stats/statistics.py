import pandas as pd
import numpy as np
from requests import request as r
from utils.football_constants import TEAMS_IDS
from utils.weather_constants import W_URL
from models.football.team import get_team_ended_games
from models.weather.weather import get_weather_coeffs


def get_games_stats_for_a_team(team_id):
    team_res = get_team_ended_games(team_id)

    team_res['wtb_coeff'] = np.nan
    team_res['w_icon'] = np.nan
    team_res['wtc_coeff'] = np.nan
    team_res['avg_temp'] = np.nan
    team_res['temp_r'] = np.nan

    for g in team_res.index:
        city, lat, lon = TEAMS_IDS[team_res.loc[g, 'home_id']].values()
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

