from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Customer(db.Model):
    __tablename__ = "customers"

    CustomerID = db.Column(db.String(50), primary_key=True)
    CompanyName = db.Column(db.String(50), nullable=False)
    ContactName = db.Column(db.String(50))
    ContactTitle = db.Column(db.String(50))
    Address = db.Column(db.String(255))
    City = db.Column(db.String(50))
    Region = db.Column(db.String(50))
    PostalCode = db.Column(db.String(20))
    Country = db.Column(db.String(50))
    Phone = db.Column(db.String(20))
    Fax = db.Column(db.String(20))

    def __repr__(self):
        return f"<Customer {self.CustomerID}>"


class CustomerSchema(ma.Schema):
    class Meta:
        fields = (
            "CustomerID",
            "CompanyName",
            "ContactName",
            "ContactTitle",
            "Address",
            "City",
            "Region",
            "PostalCode",
            "Country",
            "Phone",
            "Fax",
        )


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
