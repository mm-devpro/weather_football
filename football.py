import pandas as pd


class Team:

    def __init__(self, fb_data):
        self.fb_data = pd.json_normalize(fb_data)

    def _get_results(self, loc="local", res="win"):
        pass

    def _get_goals(self):
        pass

    def _get_goal_diff(self):
        pass
