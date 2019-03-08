# -*- coding: utf-8 -*-

from models import Forecast
from database import db_session
from utils import get_diff_days
from api import Weather
from helpers import forecast_exists
from validators import validate_diff_days
import os


def get_local_forecast(code, date_from, date_to):
    validate = validate_diff_days(date_from, date_to)
    if validate['status'] != True:
        return validate

    response_data = {}
    forecasts = search_forecasts(code, date_from, date_to)
    if len(forecasts) > 0:
        response_data['higher_temperature'] = get_higher_temperature(forecasts)
        response_data['lower_temperature'] = get_lower_temperature(forecasts)
        response_data['rain_probabitily'] = get_higher_probability_rain(forecasts)
    else:
        response_data['response'] = "Nao foi encontrada nenhuma informacao para as datas %s a %s" % (date_from.strftime('%d/%m/%Y'), date_to.strftime('%d/%m/%Y'))

    return response_data


def search_forecasts(code, date_from, date_to):
    forecasts = Forecast.query.filter_by(city_id=code).filter(Forecast.date_at >= date_from).filter(Forecast.date_at <= date_to).all()
    diff_days = get_diff_days(date_from, date_to)
    if diff_days != len(forecasts):
        weather = Weather(os.getenv('TOKEN'))
        forecasts_api = weather.load(code, date_from, date_to)

        for forecast_api in forecasts_api:
            if forecast_exists(forecast_api) == False:
                db_session.add(forecast_api)
                db_session.commit()
            
            if forecast_api.date_at.date() >= date_from and forecast_api.date_at.date() <= date_to:
                forecasts.append(forecast_api)
    
    return forecasts


def get_higher_temperature(forecasts):
    higher = {
        'date': None,
        'temperature': -100
    }

    for forecast in forecasts:
        if higher['temperature'] < forecast.temperature_max:
            higher['date'] = forecast.date_at.strftime('%d/%m/%Y')
            higher['temperature'] = forecast.temperature_max

    return higher


def get_lower_temperature(forecasts):
    lower = {
        'date': None,
        'temperature': 200
    }

    for forecast in forecasts:
        if lower['temperature'] > forecast.temperature_min:
            lower['date'] = forecast.date_at.strftime('%d/%m/%Y')
            lower['temperature'] = forecast.temperature_min

    return lower


def get_higher_probability_rain(forecasts):
    rain = {
        'date': None,
        'probability': -100,
        'precipitation': 0
    }

    for forecast in forecasts:
        if rain['probability'] < forecast.rain_probability:
            rain['date'] = forecast.date_at.strftime('%d/%m/%Y')
            rain['probability'] = forecast.rain_probability
            rain['precipitation'] = forecast.rain_precipitation

    return rain