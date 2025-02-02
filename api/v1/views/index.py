#!/usr/bin/python3
"""handles configurations"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """ Return json string """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def obj_count():
    """ Return the number of each object type per class """
    obj_dict = {
                "amenities": storage.count("Amenity"),
                "cities": storage.count("City"),
                "places": storage.count("Place"),
                "reviews": storage.count("Review"),
                "states": storage.count("State"),
                "users": storage.count("User")
                }
    return jsonify(obj_dict)
