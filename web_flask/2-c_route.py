#!/usr/bin/python3
""" script that starts a Flask web application

    python3 -m web_flask.2-c_route
    curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
    curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
    curl 0.0.0.0:5000/c
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
