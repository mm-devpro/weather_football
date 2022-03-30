import pandas as pd


class Team:

    def __init__(self, team_games, team_id):
        self.team_games = team_games
        self.team_id = team_id

    def get_results(self):
        home = pd.DataFrame(self.team_games[self.team_games.home_id == self.team_id],
                                         columns=['date', 'home_id', 'home_winner', 'home_goals', 'goal_diff'])

        away = pd.DataFrame(self.team_games[self.team_games.away_id == self.team_id],
                     columns=['date', 'home_id', 'away_winner', 'away_goals', 'goal_diff'])
        return home, away


"""
-> chaque match :
    si team est home/away, si elle a gagné/perdu/nul, nbre de buts et ecart de buts, date
"""
