import json
import os
from requests import request as r
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from models.stats.statistics import filter_team_fixtures_w_weather_from_json_data
from models.predictions.predictions import get_fixture_prediction
from utils.create_json_data import save_fixtures_to_json
from utils.football_constants import BUNDESLIGA_ID

# team_games = filter_team_fixtures_w_weather_from_json_data(157)
#
# team_games = pd.DataFrame([get_fixture_prediction(f) for _, f in team_games[:6].T.items()])
# print(team_games.winner, team_games.play)
# print([t for t in team_games.prediction])
save_fixtures_to_json(BUNDESLIGA_ID)
