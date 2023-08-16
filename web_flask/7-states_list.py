#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models.state import State
import models


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    models.storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    dict_states = models.storage.all(State)
    stateslist = []
    for k, v in dict_states.items():
        stateslist.append(v)
    return render_template("7-states_list.html", stateslist=stateslist)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
