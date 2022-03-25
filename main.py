from os import path, getenv
import sys
import logging
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
from requests import request as r
import pandas as pd

from weather import Weather
from utils.constants import W_URL, F_URL

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# load and get .env file variables
load_dotenv()
SECRET_KEY = getenv('SECRET_KEY')
RAPID_API_KEY = getenv('RAPID_API_KEY')


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

    # ###### weather api ######
    params = {
        'lat': 48.1371,
        'lon': 11.5753,
        'date': '2020-2-12'
    }

    # ##### football api #####
    payload = {}
    headers = {
        'x-rapidapi-key': RAPID_API_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    # routes
    @app.route('/<endpoint>', methods=['GET', 'POST'])
    def index(endpoint):
        fb_response = r("GET", f'{F_URL}/teams?league=78&season=2021', headers=headers, data=payload)
        JSON_resp = fb_response.json()
        print([[teams for teams in re['team'].values()] for re in JSON_resp['response']])
        return JSON_resp

    @app.route('/city/<city_name>', methods=['GET'])
    def getcity(city_name):
        wt_response = r("GET", f'{W_URL}/weather?lat=48.1371&lon=11.5753&date=2021-04-12', params=params)
        wt_json = wt_response.json()
        df = wt_response.json()['weather']
        w = Weather(df)

        print(w.wtc_coeff, w.wtb_coeff, w.temp_r)
        return wt_json

    @app.route('/search', methods=['GET'])
    def search():
        args = request.args
        print(args)
        return args
    # end routes

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
