#!/usr/bin/python3
""" script that starts a Flask web application

    python3 -m web_flask.4-number_route
    curl 0.0.0.0:5000/number/8.9
    curl 0.0.0.0:5000/number/python
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route_index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def route_HBNB():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def route_C_(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def route_Python_(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def route_number(n):
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
