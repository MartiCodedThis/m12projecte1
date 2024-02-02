from . import api_bp
from .errors import not_found, bad_request
from ..models import Category
from .helper_json import json_request, json_response
from flask import current_app, request

@api_bp.route('/categories', methods=['GET'])
def api_get_cats():
    result = Category.get_all()
    data = Category.to_dict_collection(result)
    return json_response(data)