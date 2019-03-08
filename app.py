# -*- coding: utf-8 -*-
from flask import Flask, Response, json

app = Flask(__name__)

@app.route("/weather/local/<int:code>/from/<string:date_from>/to/<string:date_to>", methods=['GET'])
def weather_local(code, date_from, date_to):
    response_data = []
    return Response(json.dumps(response_data), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run()