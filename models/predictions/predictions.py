import pandas as pd
import numpy as np
from models.stats.statistics import get_avg_coeffs_per_venue, get_results_coeffs_for_team
from models.football.team import get_team_ended_games
from utils.football_constants import BUNDESLIGA_ID, F_HEADERS, F_URL


def predict_results_facing_venue(team_id):
    pass


def get_game_prediction(team_id):
    team_results = get_results_coeffs_for_team(team_id)
    games_data = r("GET", f'{F_URL}/fixtures', params={'league': BUNDESLIGA_ID, 'season': 2021, 'team': team_id}, headers=F_HEADERS)

    pass

