#!/usr/bin/python3
"""Starts a flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def home():
    """"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """"""
    return 'HBNB'


@app.route('/c/<text>')
def c_params(text):
    """"""
    text_new = text.replace('_', ' ')

    return "C {}".format(text_new)


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def p_params(text):
    """"""
    text_new = text.replace('_', ' ')

    return "Python {}".format(text_new)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
