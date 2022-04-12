import json
import os
from requests import request as r
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from models.stats.statistics import get_team_fixtures_w_weather_from_json_data

# football fixtures json file
# fb_f = get_all_fixtures_from_json_data()
# fb_f_stats = get_team_ended_games_w_stats(157)
# print(f"[-] team ended games: \n {fb_f_stats}")
# print(f"[-] game stats: \n {fb_f_stats}")

# get_results_graphs_for_team(157)
stats = get_team_fixtures_w_weather_from_json_data(157)


print(f"[-] next games by team: \n {stats}")

