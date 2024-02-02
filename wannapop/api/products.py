from . import api_bp
from .errors import not_found, bad_request
from ..models import Product
from .helper_json import json_request, json_response
from flask import current_app, request

@api_bp.route('/products', methods=['GET'])
def api_product_get():
    search = request.args.get('title')
    if search:
        Product.db_enable_debug()
        my_filter = Product.title.like('%' + search + '%')
        result = Product.db_query().filter(my_filter)
    else:
        result = Product.get_all()
    data = Product.to_dict_collection(result)
    return json_response(data)