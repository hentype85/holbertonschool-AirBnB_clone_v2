#!/usr/bin/python3
""" script that starts a Flask web application
    python3 -m web_flask.1-hbnb_route
    curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """home"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index():
    """route /hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
