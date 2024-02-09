from . import api_bp
from .errors import not_found, bad_request
from ..models import Order, ConfirmedOrder
from .helper_json import json_response, json_request
from flask import current_app


@api_bp.route('/orders', methods = ['POST'])
def api_order_add():
    
    data = json_request(['id','product_id', 'buyer_id', 'offer', 'created'], False)
    order = Order.create()
    order.update(**data)
    return json_response(order.to_dict())

@api_bp.route('/orders/<int:order_id>', methods = ['PUT'])
def api_order_edit(order_id):
    order = Order.get(order_id)
    if order:
        try:
            data = json_request(['id', 'product_id', 'buyer_id', 'offer', 'created'], False)
        except Exception as e:
            current_app.logger.debug(e)
            return bad_request(str(e))
        else:
            order.update(**data)
            current_app.logger.debug("UPDATED order: {}".format(order.to_dict()))
            return json_response(order.to_dict())
    else:
        current_app.logger.debug("Order {} not found".format(order_id))
        return not_found("Order not found")

@api_bp.route('/orders/<int:order_id>', methods = ['DELETE'])
def api_order_delete(order_id):
    order = Order.get(order_id)
    if order:
        order.delete()
        current_app.logger.debug("CANCELLED order {}".format(order_id))
        return json_response(order.to_dict())
    
@api_bp.route('/orders/<int:order_id>/confirmed', methods=['POST'])
def api_order_confirm(order_id):
    order = Order.get(order_id)
    if order:
        ConfirmedOrder.create(order_id=order_id)
        current_app.logger.debug("CONFIRMED order {}".format(order_id))
        return json_response(order.to_dict())
    else:
        current_app.logger.debug("Order {} not found".format(order_id))
        return not_found("Order not found")


@api_bp.route('/orders/<int:order_id>/confirmed', methods=['DELETE'])
def api_order_cancel(order_id):
    order = ConfirmedOrder.get(order_id)
    if order:
        order.delete()
        current_app.logger.debug("CANCELLED confirmed order {}".format(order_id))
        return json_response("Order cancelled!")
    else:
        current_app.logger.debug("Confirmed order {} not found".format(order_id))
        return not_found("Order not found")