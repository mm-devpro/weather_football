import pandas as pd
from utils.utils import sanitize_fb_team_data


class Team:

    def __init__(self, team_games, team_id):
        self.team_games = sanitize_fb_team_data(team_games, team_id)
        self.team_id = team_id

    def get_results(self):
        # get all games, home or away in the same Dataframe
        home = pd.DataFrame(self.team_games[self.team_games.home_id == self.team_id],
                            columns=['date', 'home_id', 'away_id', 'home_name', 'away_name', 'home_winner', 'home_goals',
                                     'goal_diff'])

        away = pd.DataFrame(self.team_games[self.team_games.away_id == self.team_id],
                            columns=['date', 'home_id', 'away_id', 'home_name', 'away_name', 'away_winner', 'away_goals',
                                     'goal_diff'])
        # renaming the columns, to prepare for concatenation
        home.rename(columns={'home_winner': 'winner', 'home_goals': 'goals'}, inplace=True)
        home['play'] = 'home'
        away.rename(columns={'away_winner': 'winner', 'away_goals': 'goals'}, inplace=True)
        away['play'] = 'away'
        # concatenate home and away
        team_results = pd.concat([home, away])
        # sanitize date
        team_results['date'] = [x.split('T')[0] for x in team_results['date']]
        team_results.sort_values(by='date', inplace=True, ascending=False)

        return team_results
