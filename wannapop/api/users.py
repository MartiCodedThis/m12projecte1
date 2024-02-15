from . import api_bp
from ..models import User, Product
from .helper_json import json_response, json_error_response
from flask import request

url_head = "/api/v1.0/"

@api_bp.route('/users', methods=['GET'])
def list_users():
    search = request.args.get('name')
    if search:
        # Watch SQL at terminal
        User.db_enable_debug()
        # Filter using query param
        my_filter = User.name.like('%' + search + '%')
        users = User.db_query().filter(my_filter)
    else:
        # No filter
        users = User.get_all()
        
    data = User.to_dict_collection(users)
    return json_response(data)
    
@api_bp.route('/users/<int:user_id>', methods=['GET'])
def show_user(user_id):
    user = User.get(user_id)
    if user:
        return json_response(user.to_dict())
    else:
        return json_error_response()
    
@api_bp.route('/users/<int:user_id>/products', methods=['GET'])
def list_user_products(user_id):
    user = User.get(user_id)
    if(user):
        products = Product.get_all_filtered_by(id=user_id)
        data = Product.to_dict_collection(products)
        return json_response(data)
    else:
        return json_error_response()