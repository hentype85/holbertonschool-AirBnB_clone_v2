#!/usr/bin/python3
""" script that starts a Flask web application

    python3 -m web_flask.6-number_odd_or_even
    curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
    curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
    curl 0.0.0.0:5000/number_odd_or_even/python
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


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def route_HTML(n):
    if n % 2 == 0:
        txt = "even"
    else:
        txt = "odd"
    return render_template("6-number_odd_or_even.html", n=n, txt=txt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
