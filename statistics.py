"""
weather :
wtc, wtb, temp_r

football:
local or ext
win, lose, draw
"""
from requests import request as r
import pandas as pd
from weather import Weather
from utils.constants import W_URL, F_URL

params = {
    'lat': 48.1371,
    'lon': 11.5753,
    'date': '2020-2-12'
}

payload = {}
headers = {
    'x-rapidapi-key': '6827e339753bf403ef08be29f1c08f14',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

wt_response = r("GET", f'{W_URL}/weather?lat=48.1371&lon=11.5753&date=2021-04-12', params=params)
df = wt_response.json()['weather']

w = Weather(df)

fb = r("GET", f'{F_URL}/fixtures?league=78&season=2020', headers=headers, data=payload)
res = fb.json()['response']

"""
I need to keep :
- fixture: id, date
- venue: city
- teams: home: id, winner(false, true, null)
- teams: away: id, winner
- goals: home, away
"""
dt = [{k: v for k, v in x.items() if k in ['fixture', 'goals', 'teams']} for x in res]
dt_fixt = [{k: v for k, v in x['fixture'].items() if k in ['date', 'id']} for x in dt]
dt_goals = [{k: v for k, v in x['fixture'].items() if k in ['date', 'id']} for x in dt]
df2 = pd.DataFrame(dt[:2])
# dt2 = [e['fixture'] for e in df2]

