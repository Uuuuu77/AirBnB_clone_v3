#!/usr/bin/python3
"""handles several configurations"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown method to close storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handle 404 errors with a JSON response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app.run(host=host, port=port, threaded=True)
