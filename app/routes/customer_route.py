from flask import Blueprint, request, jsonify
from controllers.customer_controller import (
    get_customer,
    add_customer,
    update_customer,
)

customer_bp = Blueprint("customer", __name__)


@customer_bp.route("/<customer_id>", methods=["GET"])
def get_customer_route(customer_id):
    return get_customer(customer_id)


@customer_bp.route("/", methods=["POST"])
def add_customer_route():
    return add_customer(request.json)


@customer_bp.route("/<customer_id>", methods=["PUT"])
def update_customer_route(customer_id):
    return update_customer(customer_id, request.json)
