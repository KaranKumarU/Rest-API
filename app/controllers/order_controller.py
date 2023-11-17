from models.order_model import Order, db, orders_schema, order_schema
from flask import jsonify
from tabulate import tabulate as tabulate_func


def get_order(order_id):
    order = Order.query.filter_by(OrderID=order_id).first()
    if order:
        return order_schema.dump(order)
    return {"error": "order not found"}


def select_order_history(customer_id):
    cust_orders = Order.query.filter_by(CustomerID=customer_id).all()

    if cust_orders:
        serialized_orders = orders_schema.dump(cust_orders)
        headers = serialized_orders[0].keys()
        rows = [list(item.values()) for item in serialized_orders]
        table = tabulate_func(rows, headers, tablefmt="grid")
        return f"<pre>{table}</pre>"
    else:
        return {"error": "customer's order not found"}


def add_order(data):
    new_order = Order(
        OrderID=data["OrderID"],
        CustomerID=data["CustomerID"],
        EmployeeID=data["EmployeeID"],
        OrderDate=data["OrderDate"],
        RequiredDate=data["RequiredDate"],
        ShippedDate=data["ShippedDate"],
        ShipVia=data["ShipVia"],
        Freight=data["Freight"],
        ShipName=data["ShipName"],
        ShipAddress=data["ShipAddress"],
        ShipCity=data["ShipCity"],
        ShipRegion=data["ShipRegion"],
        ShipPostalCode=data["ShipPostalCode"],
        ShipCountry=data["ShipCountry"],
    )
    db.session.add(new_order)
    db.session.commit()
    return order_schema.dump(new_order)


def update_order(order_id, data):
    order = Order.query.filter_by(OrderID=order_id).first()
    if order:
        order.CustomerID = data.get("CustomerID", order.CustomerID)
        order.EmployeeID = data.get("EmployeeID", order.EmployeeID)
        order.OrderDate = data.get("OrderDate", order.OrderDate)
        order.RequiredDate = data.get("RequiredDate", order.RequiredDate)
        order.ShippedDate = data.get("ShippedDate", order.ShippedDate)
        order.ShipVia = data.get("ShipVia", order.ShipVia)
        order.Freight = data.get("Freight", order.Freight)
        order.ShipName = data.get("ShipName", order.ShipName)
        order.ShipAddress = data.get("ShipAddress", order.ShipAddress)
        order.ShipCity = data.get("ShipCity", order.ShipCity)
        order.ShipRegion = data.get("ShipRegion", order.ShipRegion)
        order.ShipPostalCode = data.get("ShipPostalCode", order.ShipPostalCode)
        order.ShipCountry = data.get("ShipCountry", order.ShipCountry)
        db.session.commit()
        return order_schema.dump(order)

    return {"error": "order not found"}
