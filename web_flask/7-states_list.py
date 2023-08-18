#!/usr/bin/python3
""" script that starts a Flask web application
    defines routes to handle specific urls
    fetching data from the storage engine
"""
from flask import Flask
from flask import render_template
import models
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    d_states = models.storage.all(State)
    return render_template("7-states_list.html", stateslist=d_states.values())


@app.teardown_appcontext
def teardown(self):
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
