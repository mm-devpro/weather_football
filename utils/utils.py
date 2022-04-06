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

