import datetime as dt

from dateutil import parser
from flask import jsonify

from . import app


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to Timestamp Microservice!', })


@app.route('/<int:timestamp_unix>')
def get_unix_timestamp(timestamp_unix):
    try:
        if timestamp_unix <= 0:
            raise ValueError

        unix = dt.datetime.fromtimestamp(timestamp_unix)
        natural = parser.parse(str(unix)).strftime('%B %d, %Y')

    except (ValueError, OverflowError):
        return jsonify({'natural': None, 'unix': None})

    return jsonify({'natural': natural, 'unix': timestamp_unix, })


@app.route('/<timestamp_natural>')
def get_natural_timestamp(timestamp_natural):
    try:
        unix = int(timestamp_natural)
        return get_unix_timestamp(unix)
    except ValueError:
        try:
            natural = parser.parse(timestamp_natural).strftime('%B %d, %Y')
        except ValueError:
            return jsonify({'natural': None, 'unix': None})

    timestamp_natural_dt = parser.parse(timestamp_natural)
    unix = int(timestamp_natural_dt.strftime('%s'))

    return jsonify({'natural': natural, 'unix': unix, })
