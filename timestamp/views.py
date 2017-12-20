from flask import jsonify
from . import app


@app.route('/')
def index():
    return jsonify({'message': 'hello, world!'})
