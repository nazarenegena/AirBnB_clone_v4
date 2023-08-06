#!/usr/bin/python3
"""
this integrates with AirBnB static HTML Template
"""
import uuid
from flask import Flask, render_template, url_for
from models import storage

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# Begin Flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/100-hbnb/')
def hbnb_filters():
    """
    Handles request to custom template with states, cities, amenities
    """
    states = storage.all("State").values()
    cities = storage.all("City").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template('100-hbnb.html',
                           states=states,
                           cities=cities,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    """
    MAIN Flask App
    """
    app.run(host=host, port=port)
