# -*- coding: utf-8 -*-

from models import Forecast

def forecast_exists(forecast):
	forecast_exist = Forecast.query.filter_by(city_id=forecast.city_id).filter_by(date_at=forecast.date_at).first()

	if forecast_exist != None:
		return True
	else: 
		return False