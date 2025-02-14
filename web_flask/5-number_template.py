#!/usr/bin/python3
""" script that starts a Flask web application

    python3 -m web_flask.5-number_template
    curl 0.0.0.0:5000/number_template/89 ; echo ""
    curl 0.0.0.0:5000/number_template/8.9
    curl 0.0.0.0:5000/number_template/python
"""
from flask import Flask
from flask import render_template


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


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def route_Python_(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def route_number(n):
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def route_HTML(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
