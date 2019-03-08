# -*- coding: utf-8 -*-

from datetime import datetime
from werkzeug.routing import BaseConverter, ValidationError

def get_diff_days(date_from, date_to):
    delta = date_to - date_from
    return delta.days
    
class DateConverter(BaseConverter):
    regex = r'\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        try:
            return datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')