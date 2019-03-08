# -*- coding: utf-8 -*-
 
import json, requests
from models import Forecast

class Weather():
    def __init__(self, token):
        self.token = token
        self.base_url = "http://apiadvisor.climatempo.com.br/api/v1"

    def load(self, city_code, date_from, date_to):
        url = "%s/forecast/locale/%s/days/15?token=%s" % (self.base_url, city_code, self.token)
        data = requests.get(url).json()
        return self.get_forecast(data, date_from, date_to)

    def get_forecast(self, data, date_from, date_to):
        forecasts = []
        for data_forecast in data['data']:  
            forecast = Forecast(data_forecast['date'], data_forecast['temperature']['max'], data_forecast['temperature']['min'], data_forecast['rain']['probability'], data_forecast['rain']['precipitation'], data['id'])
            forecasts.append(forecast)

        return forecasts