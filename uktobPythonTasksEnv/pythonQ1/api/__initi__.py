from flask import Blueprint

# Create a Blueprint object
api_bp = Blueprint('api', __name__)

# Import the routes module to register the routes
from api import routes