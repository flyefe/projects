from flask import Blueprint
from auth import routes
from auth import auth as auth_blueprint


auth = Blueprint('auth', __name__)


