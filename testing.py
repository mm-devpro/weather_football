import json
import os
from requests import request as r
import pandas as pd
import numpy as np
from models.weather.weather import get_weather_coeffs
from models.football.team import get_team_ended_games, get_team_infos
from utils.weather_constants import W_URL
from utils.football_constants import F_URL, TEAMS_IDS, BUNDESLIGA_ID, F_HEADERS

# football test file
with open(os.path.join('./data_files/fb_data.json'), 'r') as json_file:
    json_test = json.load(json_file)


w_params = {
    'lat': 48.1371,
    'lon': 11.5753,
    'date': '2012-08-9'
}
f_params = {
    'league': 78,
    'season': 2020,
    'team': 157
}

payload = {}

wt_response = r("GET", f'{W_URL}/weather', params=w_params)

res1 = wt_response.json()['weather']
df = pd.json_normalize(res1)[12:23]

t_we = df.groupby(df['icon']).size().idxmax()
t_w = df['condition'].value_counts()
# print(f'[-] weather df : \n {t_we}')

wtb_coeff, wtc_coeff, avg_temp, w_icon, temp_r = get_weather_coeffs(df)

# print(f'[-] coeffs: \n {wo.wtc_coeff}, {wo.wtb_coeff}, {wo.temp_r}')

# fb = r("GET", f'{F_URL}/fixtures', params=f_params, headers=F_HEADERS, data=payload)
# res2 = fb.json()['response']
df2 = pd.json_normalize(json_test)

# print(f'[-] fb df : \n {df2}')
# print(f'[-] team : \n {t}')
"""
une equipe => home/away => wtc/wtb/temp => w/l/d
une equipe => home/away => wtc/wtb/temp => num goals
une equipe => home/away => wtc/wtb/temp => ecart goals
"""

# stats = Statistics(t)
# stats_res = stats.full_stats

# print(f'[-] stats : \n {stats_res}')

# rank_params = {
#     'league': BUNDESLIGA_ID,
#     'season': 2020,
#     'team': 164
# }
#
# dp = get_team_infos(164)
# get_average_team_rank(157)
# print(dp)

t_res = get_team_infos(157)

print(t_res)