import pandas as pd

"""
FOOTBALL RELATED CONSTANTS
"""
F_URL = "https://v3.football.api-sports.io"
F_HEADERS = {
    'x-rapidapi-key': '6827e339753bf403ef08be29f1c08f14',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}
BUNDESLIGA_ID = 78
TEAMS_IDS = pd.DataFrame({
    157: {
        'name': 'Bayern Munich',
        'city': 'München',
        'lat': 48.1371,
        'lon': 11.5753,
    },
    158: {
        'name': 'Fortuna Dusseldorf',
        'city': 'Dusseldorf',
        'lat': 51.2333,
        'lon': 6.7833,
    },
    159: {
        'name': 'Hertha Berlin',
        'city': 'Berlin',
        'lat': 52.5186,
        'lon': 13.3996,
    },
    160: {
        'name': 'SC Freiburg',
        'city': 'Freiburg im Breisgau',
        'lat': 47.9960,
        'lon': 7.8494,
    },
    161: {
        'name': 'VfL Wolfsburg',
        'city': 'Wolfsburg',
        'lat': 52.4205,
        'lon': 10.7861,
    },
    162: {
        'name': 'Werder Bremen',
        'city': 'Bremen',
        'lat': 53.0736,
        'lon': 8.8064,
    },
    163: {
        'name': 'Borussia Monchengladbach',
        'city': 'Mönchengladbach',
        'lat': 51.2000,
        'lon': 6.4333,
    },
    164: {
        'name': 'FSV Mainz 05',
        'city': 'Mainz',
        'lat': 49.9928,
        'lon': 8.2472,
    },
    165: {
        'name': 'Borussia Dortmund',
        'city': 'Dortmund',
        'lat': 51.5142,
        'lon': 7.4684,
    },
    166: {
        'name': 'Hannover 96',
        'city': 'Hannover',
        'lat': 52.3705,
        'lon': 9.7332,
    },
    167: {
        'name': '1899 Hoffenheim',
        'city': 'Sinsheim',
        'lat': 49.2529,
        'lon': 8.8786,
    },
    168: {
        'name': 'Bayer Leverkusen',
        'city': 'Leverkusen',
        'lat': 51.0303,
        'lon': 6.9843,
    },
    169: {
        'name': 'Eintracht Frankfurt',
        'city': 'Frankfurt am Main',
        'lat': 50.1109,
        'lon': 8.6821,
    },
    170: {
        'name': 'FC Augsburg',
        'city': 'Augsburg',
        'lat': 48.3665,
        'lon': 10.8944,
    },
    171: {
        'name': 'FC Nurnberg',
        'city': 'Nuremberg',
        'lat': 49.4609,
        'lon': 11.0618,
    },
    172: {
        'name': 'VfB Stuttgart',
        'city': 'Stuttgart',
        'lat': 48.7833,
        'lon': 9.1833,
    },
    173: {
        'name': 'RB Leipzig',
        'city': 'Leipzig',
        'lat': 51.3396,
        'lon': 12.3730,
    },
    174: {
        'name': 'FC Schalke 04',
        'city': 'Gelsenkirchen',
        'lat': 51.5075,
        'lon': 7.1228,
    },
    175: {
        'name': 'Hamburger SV',
        'city': 'Hamburg',
        'lat': 53.5510,
        'lon': 9.9936,
    },
    176: {
        'name': 'VfL BOCHUM',
        'city': 'Bochum',
        'lat': 51.4818,
        'lon': 7.2162,
    },
    178: {
        'name': 'SpVgg Greuther Furth',
        'city': 'Fürth',
        'lat': 49.4666,
        'lon': 11.0000,
    },
    180: {
        'name': 'FC Heidenheim',
        'city': 'Heidenheim an der Brenz',
        'lat': 48.6779,
        'lon': 10.1516,
    },
    181: {
        'name': 'SV Darmstadt 98',
        'city': 'Darmstadt',
        'lat': 49.8787,
        'lon': 8.6469,
    },
    182: {
        'name': 'Union Berlin',
        'city': 'Berlin',
        'lat': 52.5200,
        'lon': 13.4049,
    },
    184: {
        'name': 'FC Ingolstadt 04',
        'city': 'Ingolstadt',
        'lat': 48.7666,
        'lon': 11.4333,
    },
    185: {
        'name': 'SC Paderborn 07',
        'city': 'Paderborn',
        'lat': 51.7166,
        'lon': 8.7666,
    },
    186: {
        'name': 'FC St. Pauli',
        'city': 'Hamburg',
        'lat': 53.5510,
        'lon': 9.9936,
    },
    188: {
        'name': 'Arminia Bielefeld',
        'city': 'Bielefeld',
        'lat': 52.0211,
        'lon': 8.5347,
    },
    191: {
        'name': 'Holstein Kiel',
        'city': 'Kiel',
        'lat': 54.3233,
        'lon': 10.1394,
    },
    192: {
        'name': 'FC Koln',
        'city': 'Köln',
        'lat': 50.9351,
        'lon': 6.9531,
    },
    744: {
        'name': 'Eintracht Braunschweig',
        'city': 'Braunschweig',
        'lat': 52.2666,
        'lon': 10.5166,
    },
    745: {
        'name': 'FC Kaiserslautern',
        'city': 'Kaiserslautern',
        'lat': 49.4430,
        'lon': 7.7716,
    },
}, )
TEAM_FIXTURE_COLS = ['fixture.id', 'fixture.date', 'fixture.venue.city', 'teams.home.id', 'teams.away.id',
                     'teams.home.name', 'teams.away.name', 'teams.home.winner', 'teams.away.winner',
                     'goals.home', 'goals.away']
TEAM_FIXTURE_RENAMED_COLS = {'fixture.id': 'fixture_id', 'fixture.date': 'date', 'fixture.venue.city': 'city',
                             'teams.home.id': 'home_id', 'teams.away.id': 'away_id', 'teams.home.name': 'home_name',
                             'teams.away.name': 'away_name', 'teams.home.winner': 'home_winner',
                             'teams.away.winner': 'away_winner', 'goals.home': 'home_goals', 'goals.away': 'away_goals'}
TEAM_INFOS_COLS = ['team.id', 'team.name', 'team.logo', 'venue.city']
TEAM_INFOS_RENAMED_COLS = {'team.id': 'team_id', 'team.name': 'name', 'team.logo': 'logo', 'venue.city': 'city'}

CURR_Y_TEAMS = [157, 159, 160, 161, 163, 164, 165, 167, 168, 169, 170, 172, 173, 176, 178, 182, 188, 192]
