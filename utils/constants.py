"""
FOOTBALL RELATED
"""
F_URL = "https://v3.football.api-sports.io"
BUNDESLIGA_ID = 78
TEAMS_IDS = {
    'Bayern Munich': {
        'id': 157,
        'city': 'München',
        'lat': 48.1371,
        'lon': 11.5753,
    },
    'Hertha Berlin': {
        'id': 159,
        'city': 'Berlin',
        'lat': 52.5186,
        'lon': 13.3996,
    },
    'SC Freiburg': {
        'id': 160,
        'city': 'Freiburg im Breisgau',
        'lat': 47.9960,
        'lon': 7.8494,
    },
    'VfL Wolfsburg': {
        'id': 161,
        'city': 'Wolfsburg',
        'lat': 52.4205,
        'lon': 10.7861,
    },
    'Borussia Monchengladbach': {
        'id': 163,
        'city': 'Mönchengladbach',
        'lat': "bla",
        'lon': "bla",
    },
    'FSV Mainz 05': {
        'id': 164,
        'city': 'Mainz',
        'lat': "bla",
        'lon': "bla",
    },
    'Borussia Dortmund': {
        'id': 165,
        'city': 'Dortmund',
        'lat': "bla",
        'lon': "bla",
    },
    '1899 Hoffenheim': {
        'id': 167,
        'city': 'Sinsheim',
        'lat': "bla",
        'lon': "bla",
    },
    'Bayer Leverkusen': {
        'id': 168,
        'city': 'Leverkusen',
        'lat': "bla",
        'lon': "bla",
    },
    'Eintracht Frankfurt': {
        'id': 169,
        'city': 'Frankfurt am Main',
        'lat': "bla",
        'lon': "bla",
    },
    'FC Augsburg': {
        'id': 170,
        'city': 'Augsburg',
        'lat': "bla",
        'lon': "bla",
    },
    'VfB Stuttgart': {
        'id': 172,
        'city': 'Stuttgart',
        'lat': "bla",
        'lon': "bla",
    },
    'RB Leipzig': {
        'id': 173,
        'city': 'Leipzig',
        'lat': "bla",
        'lon': "bla",
    },
    'VfL BOCHUM': {
        'id': 176,
        'city': 'Bochum',
        'lat': "bla",
        'lon': "bla",
    },
    'SpVgg Greuther Furth': {
        'id': 178,
        'city': 'Fürth',
        'lat': "bla",
        'lon': "bla",
    },
    'Union Berlin': {
        'id': 182,
        'city': 'Berlin',
        'lat': "bla",
        'lon': "bla",
    },
    'Arminia Bielefeld': {
        'id': 188,
        'city': 'Bielefeld',
        'lat': "bla",
        'lon': "bla",
    },
    'FC Koln': {
        'id': 192,
        'city': 'Köln',
        'lat': "bla",
        'lon': "bla",
    },
}

"""
WEATHER RELATED
"""
W_URL = "https://api.brightsky.dev"
W_CONDITIONS = {
    'dry': 0,
    'rain': .3,
    'sleet': .6,
    'snow': 1,
}
W_ICONS = {
    'clear-day': 0,
    'clear-night': 0,
    'partly-cloudy-day': .25,
    'partly-cloudy-night': .25,
    'cloudy': .5,
    'wind': .5,
    'rain': .75,
    'sleet': 1,
    'snow': 1,
}
