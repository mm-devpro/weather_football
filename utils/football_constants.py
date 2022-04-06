"""
FOOTBALL RELATED CONSTANTS
"""
F_URL = "https://v3.football.api-sports.io"
F_HEADERS = {
    'x-rapidapi-key': '6827e339753bf403ef08be29f1c08f14',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}
BUNDESLIGA_ID = 78
TEAMS_IDS = {
    157: {
        'city': 'München',
        'lat': 48.1371,
        'lon': 11.5753,
    },
    159: {
        'city': 'Berlin',
        'lat': 52.5186,
        'lon': 13.3996,
    },
    160: {
        'city': 'Freiburg im Breisgau',
        'lat': 47.9960,
        'lon': 7.8494,
    },
    161: {
        'city': 'Wolfsburg',
        'lat': 52.4205,
        'lon': 10.7861,
    },
    174: {
        'city': 'Wolfsburg',
        'lat': 52.4205,
        'lon': 10.7861,
    },
    163: {
        'city': 'Mönchengladbach',
        'lat': "bla",
        'lon': "bla",
    },
    164: {
        'city': 'Mainz',
        'lat': "bla",
        'lon': "bla",
    },
    165: {
        'city': 'Dortmund',
        'lat': "bla",
        'lon': "bla",
    },
    167: {
        'city': 'Sinsheim',
        'lat': "bla",
        'lon': "bla",
    },
    168: {
        'city': 'Leverkusen',
        'lat': "bla",
        'lon': "bla",
    },
    169: {
        'city': 'Frankfurt am Main',
        'lat': "bla",
        'lon': "bla",
    },
    170: {
        'city': 'Augsburg',
        'lat': "bla",
        'lon': "bla",
    },
    172: {
        'city': 'Stuttgart',
        'lat': "bla",
        'lon': "bla",
    },
    173: {
        'city': 'Leipzig',
        'lat': "bla",
        'lon': "bla",
    },
    176: {
        'city': 'Bochum',
        'lat': "bla",
        'lon': "bla",
    },
    178: {
        'city': 'Fürth',
        'lat': "bla",
        'lon': "bla",
    },
    182: {
        'city': 'Berlin',
        'lat': "bla",
        'lon': "bla",
    },
    188: {
        'city': 'Bielefeld',
        'lat': "bla",
        'lon': "bla",
    },
    192: {
        'city': 'Köln',
        'lat': "bla",
        'lon': "bla",
    },
}
TEAM_FIXTURE_COLS = ['fixture.id', 'fixture.date', 'fixture.venue.city', 'teams.home.id', 'teams.away.id',
                     'teams.home.name', 'teams.away.name', 'teams.home.winner', 'teams.away.winner',
                     'goals.home', 'goals.away']
TEAM_FIXTURE_RENAMED_COLS = {'fixture.id': 'fixture_id', 'fixture.date': 'date', 'fixture.venue.city': 'city',
                        'teams.home.id': 'home_id', 'teams.away.id': 'away_id', 'teams.home.name': 'home_name',
                        'teams.away.name': 'away_name', 'teams.home.winner': 'home_winner',
                        'teams.away.winner': 'away_winner', 'goals.home': 'home_goals', 'goals.away': 'away_goals'}
TEAM_INFOS_COLS = ['team.id', 'team.name', 'team.logo', 'venue.city']
TEAM_INFOS_RENAMED_COLS = {'team.id': 'team_id', 'team.name': 'name', 'team.logo': 'logo', 'venue.city': 'city'}
