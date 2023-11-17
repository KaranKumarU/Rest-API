from models.customer_model import db, ma


class Product(db.Model):
    __tablename__ = "products"

    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(50), nullable=False)
    SupplierID = db.Column(db.Integer)
    CategoryID = db.Column(db.Integer)
    QuantityPerUnit = db.Column(db.String(50))
    UnitPrice = db.Column(db.Float)
    UnitsInStock = db.Column(db.Integer)
    UnitsOnOrder = db.Column(db.Integer)
    ReorderLevel = db.Column(db.Integer)
    Discontinued = db.Column(db.Boolean)

    def __repr__(self):
        return f"<Product {self.ProductID}>"


class ProductSchema(ma.Schema):
    class Meta:
        fields = (
            "ProductID",
            "ProductName",
            "SupplierID",
            "CategoryID",
            "QuantityPerUnit",
            "UnitPrice",
            "UnitsInStock",
            "UnitsOnOrder",
            "ReorderLevel",
            "Discontinued",
        )


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
