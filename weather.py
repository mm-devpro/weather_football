import pandas as pd
from utils.constants import W_ICONS, W_CONDITIONS


class Weather:
    """
    Class Weather, to get daily infos and coeff
    """

    def __init__(self, wt_data):
        """
        Weather class to handle weather data from weather api
        :param wt_data: Dataframe of the weather data
        """
        self.wt_data = wt_data[12:23]
        self._set_coeff()

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        pass

    def get_stats(self):
        return self.wt_data['condition'].value_counts()

    def _set_coeff(self):
        """
        wtb_coeff = weather beauty
        wtc_coeff = weather conditions
        temp_r = temperature rate

        WEATHER BEAUTY COEFF: between 0 and 1. Get closer to 0 if weather is very nice, 
        and get closer to 1 when weather is very bad
        """
        weather_beauty = self.wt_data.groupby([self.wt_data['condition'], self.wt_data['icon']]).size()
        res = [(W_CONDITIONS[col[0]] + W_ICONS[col[1]]) / 2 for col in weather_beauty.index]

        self.wtb_coeff = round((weather_beauty * res).sum() / weather_beauty.sum(), 4)

        """
        WEATHER CONDITIONS COEFF : between 0 and 1, taking into consideration the humidity and cloud cover. 
        Closer to 0 means low humidity and no cloud cover, closer to 1 means high humidity and high cloud cover.
        >>>>> cloud_cover and humidity are in percentage and are changed to frequence
        """
        cloud_cover = self.wt_data['cloud_cover'].mean() / 100
        humidity = self.wt_data['relative_humidity'].mean() / 100

        self.wtc_coeff = round((cloud_cover + humidity) / 2, 4)

        """
        TEMPERATURE RATE : between 0 and 1, relative to avg_temp, closer to 0 means low temp, closer to 1 means high temp
        >>>>> avg_temp in °C
        """
        avg_temp = self.wt_data['temperature'].mean()

        match avg_temp:
            case avg_temp if avg_temp <= 0:
                self.temp_r = 1
            case avg_temp if 0 < avg_temp <= 10:
                self.temp_r = .85
            case avg_temp if 10 < avg_temp <= 20:
                self.temp_r = .40
            case avg_temp if 20 < avg_temp <= 30:
                self.temp_r = .15
            case avg_temp if 30 < avg_temp:
                self.temp_r = 0


