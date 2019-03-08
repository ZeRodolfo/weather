# -*- coding: utf-8 -*-
from flask import Flask, Response, json
from utils import DateConverter
from database import db_session, init_db

app = Flask(__name__)
init_db()

app.url_map.converters['date'] = DateConverter

@app.route("/weather/local/<int:code>/from/<date:date_from>/to/<date:date_to>", methods=['GET'])
def weather_local(code, date_from, date_to):
    response_data = get_local_forecast(code, date_from, date_to)
    return Response(json.dumps(response_data), status=200, mimetype='application/json')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()