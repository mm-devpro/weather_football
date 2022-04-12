import os
import json
import pandas as pd


def sanitize_data(data, cols, renamed_cols={}):
    """
    SANITIZE function to return dataframe corresponding to columns and renamed columns wishes
    Works with football-api data
    :param data: data from api (must be json.normalized or pandas df)
    :param cols: col names to be wanted after sanitizing
    :param renamed_cols: columns renamed to fit expectations
    :return: sanitized data
    """
    df = pd.DataFrame(data, columns=cols)
    df.rename(columns=renamed_cols, inplace=True)
    return df


def convert_json_file_to_df(path_to_file):
    with open(os.path.join(path_to_file), 'r') as json_file:
        json_fixtures = json.load(json_file)
        df = pd.json_normalize(json_fixtures[k] for k in json_fixtures)
        return df

