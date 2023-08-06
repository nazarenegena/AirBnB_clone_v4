#!/usr/bin/python3
""" task 4 """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/4-hbnb', strict_slashes=False)
def hbnb_filters():
    """ Display a HTML page like 2-hbnb.html with all states, cities and
    amenities """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template('3-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

