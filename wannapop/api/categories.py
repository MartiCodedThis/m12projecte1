from . import api_bp
from ..models import Category
from .helper_json import json_response

@api_bp.route('/categories', methods=['GET'])
def api_get_cats():
    result = Category.get_all()
    data = Category.to_dict_collection(result)
    return json_response(data)