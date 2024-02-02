#!/usr/bin/python3
"""handles configurations"""

from flask import jsonify, request
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """returns status of the api"""
    if request.method == 'GET':
        return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieves the number of each object type"""
    if request.method == 'GET':
        response = {}
        stats = {
                "Amenity": "amenities",
                "City": "cities",
                "Place": "places",
                "Review": "reviews",
                "State": "states",
                "User": "users"
        }
        for key, value in stats.items():
            response[value] = storage.count()
        return jsonify(response)
