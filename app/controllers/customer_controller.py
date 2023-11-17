from models.customer_model import Customer, db, customers_schema, customer_schema
from flask import jsonify


def get_customer(customer_id):
    customer = Customer.query.filter_by(CustomerID=customer_id).first()
    if customer:
        return customer_schema.dump(customer)
    return {"error": "customer not found"}


def add_customer(data):
    new_customer = Customer(
        CustomerID=data["CustomerID"],
        CompanyName=data["CompanyName"],
        ContactName=data["ContactName"],
        Address=data["Address"],
        City=data["City"],
        Region=data["Region"],
        PostalCode=data["PostalCode"],
        Country=data["Country"],
        Phone=data["Phone"],
        Fax=data["Fax"],
    )
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.dump(new_customer)


def update_customer(customer_id, data):
    customer = Customer.query.filter_by(CustomerID=customer_id).first()
    if customer:
        customer.CompanyName = data.get("CompanyName", customer.CompanyName)
        customer.ContactName = data.get("ContactName", customer.ContactName)
        customer.Address = data.get("Address", customer.Address)
        customer.City = data.get("City", customer.City)
        customer.Region = data.get("Region", customer.Region)
        customer.PostalCode = data.get("PostalCode", customer.PostalCode)
        customer.Country = data.get("Country", customer.Country)
        customer.Phone = data.get("Phone", customer.Phone)
        customer.Fax = data.get("Fax", customer.Fax)
        db.session.commit()
        return customer_schema.dump(customer)

    return {"error": "customer not found"}
