import pandas as pd
from models.stats.statistics import get_fixture_stats
from models.football.team_fixtures import get_all_fixtures


def save_fixtures_to_json(league_id):
    """
    Create json data files from football api and weather api, for specific league.
    :param league_id: ID of league to retrieve
    """
    df = get_all_fixtures(league_id)
    df2 = get_fixture_stats(df)
    df.to_json(r'./data_files/fb_fixtures.json', orient='index')
    df2.to_json(r'./data_files/fb_fixtures_w_weather.json', orient='index')

