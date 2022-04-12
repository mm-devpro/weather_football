import json
import os
from requests import request as r
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from models.stats.statistics import filter_team_fixtures_w_weather_from_json_data, get_results_coeffs_for_team

# football fixtures json file
# fb_f = get_all_fixtures_from_json_data()
# fb_f_stats = get_team_ended_games_w_stats(157)
# print(f"[-] team ended games: \n {fb_f_stats}")
# print(f"[-] game stats: \n {fb_f_stats}")

# get_results_graphs_for_team(157)
team_games = filter_team_fixtures_w_weather_from_json_data(157)
t_med_bremen = get_results_coeffs_for_team(162)
t_med_munich = get_results_coeffs_for_team(157)
team_game = team_games.iloc[220]


print(f"[-] team: \n {team_game}")
print(f"[-] coeffs: \n {t_med_bremen} \n {t_med_munich}")

# {
#     predictions: {
#         d : 0.26,
#         w: 0.34,
#         l: 0.44,
#         goals: 2.0,
#         goal_diff: 1.0,
#     },
#     result: {
#         game: True,
#         goals: True,
#         goal_diff: False,
#     }
# }

"""
MUNICH
0.196
    d: 0.235, => 0.039 => 0.039/0.076 = 1 - 0.5131 = 0.49/2 0.25
    l: 0.199, => 0.003 => 0.003/0.076 = 1 - 0.0394 = 0.97/2 0.49
    w: 0.230, => 0.034 => 0.034/0.076 = 1 - 0.4473 = 0.56/2 0.28
    total        0.076
0.7240
    d: 0.8072 => 0.0832 => 0.2853
    l: 0.7668 => 0.0428 => 0.3895
    w: 0.7918 => 0.0678 => 0.3250 
    total        0.1938
    
wtb + wtc / 2  
    d : 26.76%
    l : 43.97%              Munich va perdre (43%) en mettant 1 but et en perdant 1-3
    w : 30.25%
18.152

1.8 => munich perd 1-3
1.7 => 
                                                            d: 1.35     
BREMEN                                                      l: 3.02      
0.196                                                       w: -3.36 
    d: 0.249, => 0.053 => 0.2827
    l: 0.232, => 0.036 => 0.3524
    w: 0.229, => 0.033 => 0.3647
    total        0.122
0.7240
    d: 0.8066 => 0.0826 => 0.2255
    l: 0.7782 => 0.0542 => 0.3199
    w: 0.7377 => 0.0137 => 0.4544
    total        0.1505
    
wtb + wtc / 2  
d : 25.41%
l : 40.95%
w : 33.61%              Bremen va gagner (40.95%) en mettant 2 buts et en gagnant 2-0 
"""