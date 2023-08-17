#!/usr/bin/python3
""" script that starts a Flask web application
    defines routes to handle specific urls
    etching data from the storage engine

    cat 7-dump.sql | mysql -uroot -p
"""
from flask import Flask
from flask import render_template
import models
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    d_states = models.storage.all(State)
    return render_template("8-cities_by_states.html", stateslist=d_states.values())


@app.teardown_appcontext
def teardown(self):
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
