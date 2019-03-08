from sqlalchemy import Column, Integer, DateTime
from database import Base
from datetime import datetime

class Forecast(Base):
    __tablename__ = 'forecast'

    idforecast = Column(Integer, primary_key=True)
    date_at = Column(DateTime, nullable=False, unique=True)
    temperature_min = Column(Integer, nullable=False)
    temperature_max = Column(Integer, nullable=False)
    rain_probability = Column(Integer, nullable=False)
    rain_precipitation = Column(Integer, nullable=False)
    city_id = Column(Integer, nullable=False, unique=True)

    def __init__(self, date_at, temperature_max, temperature_min, rain_probability, rain_precipitation, city_id):
        self.date_at = datetime.strptime(date_at, "%Y-%m-%d")
        self.temperature_max = temperature_max
        self.temperature_min =  temperature_min
        self.rain_probability = rain_probability
        self.rain_precipitation = rain_precipitation
        self.city_id = city_id


    def __repr__(self):
        return '<Forecast %r>' % self.idforecast

    @property
    def serialize(self):
       return {
           'date_at': self.date_at,
           'temperature_min': self.temperature_min,
           'temperature_max': self.temperature_max,
           'rain_probability': self.rain_probability,
           'rain_precipitation': self.rain_precipitation,
           'city_id': self.city_id
       }