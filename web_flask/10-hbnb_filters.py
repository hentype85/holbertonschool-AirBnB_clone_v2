#!/usr/bin/python3
""" script that starts a Flask web application
    defines routes to handle specific urls
    fetching data from the storage engine
"""
from flask import Flask
from flask import render_template
import models
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    dict_states = models.storage.all(State)
    dict_amenities = models.storage.all(Amenity)
    statelist = []
    amenitylist = []
    for s in dict_states.values():
        statelist.append(s)
    for a in dict_amenities.values():
        amenitylist.append(a)
    return render_template("10-hbnb_filters.html",
                           statelist=statelist,
                           amenitylist=amenitylist)


@app.teardown_appcontext
def teardown(self):
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
