#!/usr/bin/python3
""" script that starts a Flask web application
    python3 -m web_flask.0-hello_route
    curl 0.0.0.0:5000 ; echo "" | cat -e
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """return message"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """web application listening"""
    app.run(host='0.0.0.0', port=5000)
