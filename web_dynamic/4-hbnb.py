#!/usr/bin/python3
<<<<<<< HEAD
"""
integrates with AirBnB static html
"""
import uuid
from flask import Flask, render_template, url_for, request, jsonify
from models import storage

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/4-hbnb/')
def hbnb_filters(the_id=None):
    """
    handles request to custom template with states, cities & amentities
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('4-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)


@app.route('/api/v1/places_search', methods=['POST'])
def places_search():
    """
    handles POST request to /api/v1/places_search
    """
    amenities = request.get_json().get('amenities')
    if amenities is None:
        amenities = []
    places = storage.all('Place').values()
    filtered_places = []
    for place in places:
        if all(amenity.id in place.amenity_ids for amenity in amenities):
            filtered_places.append(place.to_dict())
    return jsonify(filtered_places)


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
=======
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
>>>>>>> 28b8064c8a1df4f7fa641630b90667ae6fd1ef88

