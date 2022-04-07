from requests import request as r
from utils.football_constants import F_HEADERS, F_URL, TEAMS_IDS, CURR_Y_TEAMS


def get_league_teams(league_id, season):
    """
    GET all the teams from a league/season, filtered with TEAM_IDS constants
    :param league_id: id of the league to retrieve in football-api
    :param season: season year parameter to retrieve in football-api
    :return: DataFrame of teams with names, city and lat/lon
    """
    try:
        f_params = {
            "league": league_id,
            "season": season
        }
        # TODO uncomment this to request from the api, otherwise, it takes infos from the CURR_Y_TEAMS const we created
        # res = r("GET", f'{F_URL}/teams', params=f_params, headers=F_HEADERS)
        # f_teams_ids = [row['team']['id'] for row in res.json()['response']]
        # f_teams = TEAMS_IDS.T.loc[[t in f_teams_ids for t in TEAMS_IDS.columns]]
        f_teams = TEAMS_IDS.T.loc[[t in CURR_Y_TEAMS for t in TEAMS_IDS.columns]]
    except Exception as e:
        return {
            "error": 404,
            "message": f'Erreur de le requete,{e}'
        }
    else:
        return f_teams

