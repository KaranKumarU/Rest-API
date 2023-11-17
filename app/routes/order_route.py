from flask import Blueprint, request, jsonify
from controllers.order_controller import (
    get_order,
    select_order_history,
    add_order,
    update_order,
)

order_bp = Blueprint("order", __name__)


@order_bp.route("/<int:order_id>", methods=["GET"])
def get_order_route(order_id):
    return get_order(order_id)


@order_bp.route("/order_history/<customer_id>", methods=["GET"])
def select_order_history_route(customer_id):
    return select_order_history(customer_id)


@order_bp.route("/", methods=["POST"])
def add_order_route():
    return add_order(request.json)


@order_bp.route("/<int:order_id>", methods=["PUT"])
def update_order_route(order_id):
    return update_order(order_id, request.json)
