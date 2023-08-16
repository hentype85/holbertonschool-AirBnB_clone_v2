#!/usr/bin/python3
""" script that starts a Flask web application

    defines routes to handle specific urls
    etching data from the storage engine

    cat 7-dump.sql | mysql -uroot -p
    curl 0.0.0.0:5000/states_list ; echo ""
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    import models
    models.storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    import models
    from models.state import State
    dict_states = models.storage.all(State)
    stateslist = []
    for k, v in dict_states.items():
        stateslist.append(v)
    return render_template("7-states_list.html", stateslist=stateslist)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
