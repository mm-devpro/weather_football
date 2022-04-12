from os import path, getenv
import json
import sys
import logging
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import pandas as pd
from requests import request as r
from models.football.games import get_all_fixtures
from models.football.team import get_team_infos
from models.stats.statistics import get_game_stats_for_a_team
from utils.football_constants import F_URL, BUNDESLIGA_ID
from utils.weather_constants import W_URL

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

with open(os.path.join('./data_files/fb_data.json'), 'r') as json_file:
    json_test = json.load(json_file)

# load and get .env file variables
load_dotenv()
SECRET_KEY = getenv('SECRET_KEY')
RAPID_API_KEY = getenv('RAPID_API_KEY')
API_URL = getenv('API_URL')


def create_app():
    """
    Function that creates our Flask application.
    This function creates the Flask app
    :return: Initialized Flask app
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("we_api.log"), logging.StreamHandler()],
    )

    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = SECRET_KEY

    # ----------------------------------   start routes
    @app.route(f'{API_URL}/team', methods=['GET'])
    def get_team():
        # json_test must be replaced by game_data
        params = {arg: request.args[arg] for arg in request.args}
        team_id = params['team_id']
        if 'team_id' in params:
            # get team games
            team_games = get_game_stats_for_a_team(json_test, team_id)
            # get team infos
            f_params = {
                'id': team_id
            }
            # data infos
            try:
                f_team_data = r("GET", f'{F_URL}/teams', params=f_params, headers=F_HEADERS)

            except Exception as e:
                return {
                    "error": 404,
                    "message": f'Les parametres {f_params} ne correspondent pas, erreur: {e}'
                }
            else:
                res = f_team_data.json()['response']
            team_infos = get_team_infos(res, team_id)
            return team_games, team_infos
        else:
            return {
                "message": "no team"
            }

    @app.route(f'{API_URL}/league', methods=['GET'])
    def getcity(city_name):
        pass

    @app.route(f'{API_URL}/games', methods=['GET'])
    def get_games():
        game_data = get_all_fixtures(BUNDESLIGA_ID)
        return game_data

    @app.route('/search', methods=['GET'])
    def search():
        params = {arg: request.args[arg] for arg in request.args}
        return json.dumps(params)
    # ----------------------------------------  end routes

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
