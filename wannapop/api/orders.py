from . import api_bp
from .errors import not_found, bad_request
from ..models import Order, ConfirmedOrder
from .helper_auth import token_auth
from .helper_json import json_response, json_request, json_error_response
from .helper_auth import token_auth
from flask import current_app


@api_bp.route('/orders', methods = ['POST'])
@token_auth.login_required
def api_order_add():
    user_id = token_auth.current_user().id
    data = json_request(['product_id', 'buyer_id', 'offer', 'created'], False)
    order = Order.create(**data, buyer_id=user_id)
    return json_response(order.to_dict())

@api_bp.route('/orders/<int:order_id>', methods = ['PUT'])
@token_auth.login_required
def api_order_edit(order_id):
    order = Order.get(order_id)
    if order:
        
        try:
            user_id = token_auth.current_user().id
            data = json_request(['product_id', 'offer', 'created'], False)
        except Exception as e:
            current_app.logger.debug(e)
            return bad_request(str(e))
        else:
            order.update(**data, buyer_id=user_id)
            current_app.logger.debug("UPDATED order: {}".format(order.to_dict()))
            return json_response(order.to_dict())
    else:
        current_app.logger.debug("Order {} not found".format(order_id))
        return not_found("Order not found")

@api_bp.route('/orders/<int:order_id>', methods = ['DELETE'])
@token_auth.login_required
def api_order_delete(order_id):
    order = Order.get(order_id)
    if order:
        order.delete()
        current_app.logger.debug("CANCELLED order {}".format(order_id))
        return json_response(order.to_dict())
    
@api_bp.route('/orders/<int:order_id>/confirmed', methods=['POST'])
@token_auth.login_required
def api_order_confirm(order_id):
    order = Order.get(order_id)
    is_confirmed = ConfirmedOrder.get(order_id)
    user=token_auth.current_user()
    if order:
        if user.id != order.seller_id :
            return json_error_response("403", "User not authorized to accept this order")
        else:
            if is_confirmed:
                return json_error_response("404", "Order already confirmed")
            else:
                ConfirmedOrder.create(order_id=order_id)
                current_app.logger.debug("CONFIRMED order {}".format(order_id))
                return json_response(order.to_dict())
    else:
        current_app.logger.debug("Order {} not found".format(order_id))
        return not_found("Order not found")

@api_bp.route('/orders/<int:order_id>/confirmed', methods=['DELETE'])
@token_auth.login_required
@token_auth.login_required
def api_order_cancel(order_id):
    user_id = token_auth.current_user().id
    order = ConfirmedOrder.get(order_id)
    user=token_auth.current_user()
    if order:
        if user.id != order.seller_id :
            return json_error_response("403", "User not authorized to remove this order")
        else:
            order.delete()
            current_app.logger.debug("CANCELLED confirmed order {}".format(order_id))
            return json_response("Order cancelled!")
    else:
        current_app.logger.debug("Confirmed order {} not found".format(order_id))
        return not_found("Order not found")