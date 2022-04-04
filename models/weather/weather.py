import pandas as pd
from utils.weather_constants import W_ICONS, W_CONDITIONS


def set_wtb_coeff(data):
    """
    WEATHER BEAUTY COEFF: between 0 and 1. Get closer to 0 if weather is very nice,
    and get closer to 1 when weather is very bad
    :param data: must be a pandas Dataframe with data from "https://api.brightsky.dev"
    :return: weather beauty coeff
    """
    weather_beauty = data.groupby([data['condition'], data['icon']]).size()
    res = [(W_CONDITIONS[col[0]] + W_ICONS[col[1]]) / 2 for col in weather_beauty.index]

    wtb_coeff = round((weather_beauty * res).sum() / weather_beauty.sum(), 4)
    w_icon = data.groupby(data['icon']).size().idxmax()
    return wtb_coeff, w_icon


def set_wtc_coeff(data):
    """
    WEATHER CONDITIONS COEFF : between 0 and 1, taking into consideration the humidity and cloud cover.
    Closer to 0 means low humidity and no cloud cover, closer to 1 means high humidity and high cloud cover.
    cloud_cover and humidity are in percentage and are changed to frequence
    :param data: must be a pandas Dataframe with data from "https://api.brightsky.dev"
    :return: weather conditions coeff
    """
    cloud_cover = data['cloud_cover'].mean() / 100
    humidity = data['relative_humidity'].mean() / 100
    wtc_coeff = round((cloud_cover + humidity) / 2, 4)
    return wtc_coeff


def set_temp_rate(data):
    """
    TEMPERATURE RATE : between 0 and 1, relative to avg_temp, closer to 0 means low temp, closer to 1 means high temp
    avg_temp in °C
    :param data: must be a pandas Dataframe with data from "https://api.brightsky.dev"
    :return: temperature rate over the day
    """
    avg_temp = data['temperature'].mean()
    temp_r = 0
    match avg_temp:
        case avg_temp if avg_temp <= 0:
            temp_r = 1
        case avg_temp if 0 < avg_temp <= 10:
            temp_r = .85
        case avg_temp if 10 < avg_temp <= 20:
            temp_r = .40
        case avg_temp if 20 < avg_temp <= 30:
            temp_r = .15
        case avg_temp if 30 < avg_temp:
            temp_r = 0

    return avg_temp, temp_r


def get_weather_coeffs(data):
    """
    wtb_coeff = weather beauty
    wtc_coeff = weather conditions
    temp_r = temperature rate
    """
    wtb_coeff, w_icon = set_wtb_coeff(data)
    wtc_coeff = set_wtc_coeff(data)
    avg_temp, temp_r = set_temp_rate(data)

    return wtb_coeff, wtc_coeff, avg_temp, w_icon, temp_r
