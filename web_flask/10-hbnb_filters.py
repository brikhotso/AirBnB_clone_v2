#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def state_cities_list():
    """ Get states sorted by names and render on template """
    states_data = list(storage.all(State).values())
    amenity_data = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html',
                           states=states_data,
                           amenities=amenity_data)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
