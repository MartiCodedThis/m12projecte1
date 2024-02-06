from . import api_bp
from .errors import not_found, bad_request
from ..models import Product, Order
from .helper_json import json_request, json_response
from flask import current_app, request

@api_bp.route('/products', methods=['GET'])
def api_products_get():
    search = request.args.get('title')
    if search:
        Product.db_enable_debug()
        my_filter = Product.title.like('%' + search + '%')
        result = Product.db_query().filter(my_filter)
    else:
        result = Product.get_all()
    data = Product.to_dict_collection(result)
    return json_response(data)

@api_bp.route('/products/<int:product_id>', methods=['GET'])
def api_product_details(product_id):
    prod = Product.get(product_id)
    if prod:
        return json_response(prod.to_dict())
    else:
        current_app.logger.debug("Product {} not found".format(product_id))
        return not_found("Product not found")
    

@api_bp.route('/products/<int:product_id>', methods=['PUT'])
def api_product_edit(product_id):
    prod = Product.get(product_id)
    if prod:
        try:
            data = json_request(['title', 'description', 'photo', 'price', 'category_id'], False)
        except Exception as e:
            current_app.logger.debug(e)
            return bad_request(str(e))
        else:
            prod.update(**data)
            current_app.logger.debug("UPDATED product: {}".format(prod.to_dict()))
            return json_response(prod.to_dict())
    else:
        current_app.logger.debug("Product {} not found".format(product_id))
        return not_found("Product not found")

@api_bp.route('/products/<int:product_id>/orders', methods=['GET'])
def api_product_get_orders(product_id):
    prod = Product.get(product_id)
    if prod:
        orders = Order.get_all_filtered_by(id=product_id)
        data = Order.to_dict_collection(orders)
        return json_response(data)
    else:
        current_app.logger.debug("Product {} not found".format(product_id))
        return not_found("Product not found")
