import pandas as pd


def sanitize_fb_team_data(fb_data, team_id):
    """
    SANITIZE function to return data of a specific team.
    Works with football-api data
    :param fb_data: football data from football-api (must be json.normalized or pandas df)
    :param team_id: team ID to retrieve
    :return: the team and its results
    """
    df = pd.DataFrame(fb_data,
                       columns=['fixture.id', 'fixture.date', 'fixture.venue.city', 'teams.home.id', 'teams.away.id',
                                'teams.home.name', 'teams.away.name', 'teams.home.winner', 'teams.away.winner',
                                'goals.home', 'goals.away'])
    df.rename(columns={'fixture.id': 'fixture_id', 'fixture.date': 'date', 'fixture.venue.city': 'city',
                        'teams.home.id': 'home_id', 'teams.away.id': 'away_id', 'teams.home.name': 'home_name',
                        'teams.away.name': 'away_name', 'teams.home.winner': 'home_winner',
                        'teams.away.winner': 'away_winner', 'goals.home': 'home_goals', 'goals.away': 'away_goals'},
               inplace=True)

    df['goal_diff'] = abs(df.home_goals - df.away_goals)

    team = df[(df.home_id == team_id) | (df.away_id == team_id)]

    return team

