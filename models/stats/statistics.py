import pandas as pd
import numpy as np
from requests import request as r
from utils.constants import TEAMS_IDS, W_URL
from models.football.team import Team
from models.weather.weather import Weather

class Statistics:

    def __init__(self, team_class):
        """
        Class Statistics to get team games and related weather stats
        :param team_class: must be a team of type Team
        """
        self.team_class = team_class
        self.full_stats = self._set_team_weather_result_stats()

    def _set_team_weather_result_stats(self):
        # 1 Team
        # dates pour le Weather
        # return graph
        t_results = self.team_class.get_results()

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
            res = wt_response.json()['weather']
            df3 = pd.json_normalize(res)
            w = Weather(df3)
            t_results.loc[g, 'wtc_coeff'] = w.wtc_coeff
            t_results.loc[g, 'wtb_coeff'] = w.wtb_coeff
            t_results.loc[g, 'temp_r'] = w.temp_r

        return t_results