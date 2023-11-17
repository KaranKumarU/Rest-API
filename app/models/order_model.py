from models.customer_model import db, ma


class Order(db.Model):
    __tablename__ = "orders"

    OrderID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.String(50))
    EmployeeID = db.Column(db.Integer)
    OrderDate = db.Column(db.DateTime)
    RequiredDate = db.Column(db.DateTime)
    ShippedDate = db.Column(db.DateTime)
    ShipVia = db.Column(db.Integer)
    Freight = db.Column(db.Float)
    ShipName = db.Column(db.String(50))
    ShipAddress = db.Column(db.String(255))
    ShipCity = db.Column(db.String(50))
    ShipRegion = db.Column(db.String(50))
    ShipPostalCode = db.Column(db.String(20))
    ShipCountry = db.Column(db.String(50))

    def __repr__(self):
        return f"<Order {self.OrderID}>"


class OrderSchema(ma.Schema):
    class Meta:
        fields = (
            "OrderID",
            "CustomerID",
            "EmployeeID",
            "OrderDate",
            "RequiredDate",
            "ShippedDate",
            "ShipVia",
            "Freight",
            "ShipName",
            "ShipAddress",
            "ShipCity",
            "ShipRegion",
            "ShipPostalCode",
            "ShipCountry",
        )


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
