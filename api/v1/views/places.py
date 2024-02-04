#!/usr/bin/python3
""" Handles place api configuration """

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.city import City
from models.user import User
from models.place import Place


@app_views.route('/cities/<city_id>/places', strict_slashes=False,
                 methods=['GET'])
def get_places(city_id):
    """ Gets all place objects per city """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify([place.to_dict() for place in city.places])


@app_views.route('/places/<place_id>', strict_slashes=False, methods=['GET'])
def get_place(place_id):
    """ Gets place object per id """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', strict_slashes=False,
                 methods=['DELETE'])
def del_place(place_id):
    """ Deletes a place object """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return (jsonify({})), 200


@app_views.route('/cities/<city_id>/places', strict_slashes=False,
                 methods=['POST'])
def add_place(city_id):
    """ Adds new place """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    js_data = request.get_json()
    if not js_data:
        abort(400, 'Not a JSON')
    if 'user_id' not in js_data:
        # abort(400, 'Missing user_id')
        return jsonify({"error": "Missing user_id"}), 400
    user_id = js_data['user_id']
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if 'name' not in js_data:
        return jsonify({"error": "Missing name"}), 400
    js_data['city_id'] = city_id
    place = Place(**js_data)
    place.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', strict_slashes=False, methods=['PUT'])
def update_place(place_id):
    """ Updates a place """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    js_data = request.get_json()
    if not js_data:
        abort(400, 'Not a JSON')
    for key, val in js_data.items():
        if key not in ["id", "user_id", "city_id", "created_at", "updated_at"]:
            setattr(place, key, val)
    place.save()
    return jsonify(place.to_dict()), 200
