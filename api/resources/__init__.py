from flask import Blueprint
from flask_restful import Api

from resources.users_resource import UsersResource
from resources.user_resource import UserResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/user/<userid>')
