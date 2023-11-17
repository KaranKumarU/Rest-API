from flask import Blueprint, request, jsonify
from controllers.product_controller import (
    get_product,
    add_product,
    update_product,
)

product_bp = Blueprint("product", __name__)


@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product_route(product_id):
    return get_product(product_id)


@product_bp.route("/", methods=["POST"])
def add_product_route():
    return add_product(request.json)


@product_bp.route("/<int:product_id>", methods=["PUT"])
def update_product_route(product_id):
    return update_product(product_id, request.json)
