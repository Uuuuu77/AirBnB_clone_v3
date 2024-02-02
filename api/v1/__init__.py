# api/v1/__init__.py
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views to register the routes
from api.v1.views.index import *
