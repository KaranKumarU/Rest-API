from flask import Flask
from routes.customer_route import customer_bp
from routes.product_route import product_bp
from routes.order_route import order_bp
from models.customer_model import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")
    db.init_app(app)

    return app


app = create_app()
app.register_blueprint(customer_bp, url_prefix="/customers")
app.register_blueprint(product_bp, url_prefix="/products")
app.register_blueprint(order_bp, url_prefix="/orders")

if __name__ == "__main__":
    app.run(debug=True)
