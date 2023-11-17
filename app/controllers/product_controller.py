from models.product_model import Product, db, products_schema, product_schema
from flask import jsonify


def get_product(product_id):
    product = Product.query.filter_by(ProductID=product_id).first()
    if product:
        return product_schema.dump(product)
    return {"error": "product not found"}


def add_product(data):
    new_product = Product(
        ProductID=data["ProductID"],
        ProductName=data["ProductName"],
        SupplierID=data["SupplierID"],
        CategoryID=data["CategoryID"],
        QuantityPerUnit=data["QuantityPerUnit"],
        UnitPrice=data["UnitPrice"],
        UnitsInStock=data["UnitsInStock"],
        UnitsOnOrder=data["UnitsOnOrder"],
        ReorderLevel=data["ReorderLevel"],
        Discontinued=data["Discontinued"],
    )
    db.session.add(new_product)
    db.session.commit()
    return product_schema.dump(new_product)


def update_product(product_id, data):
    product = Product.query.filter_by(ProductID=product_id).first()
    if product:
        product.ProductName = data.get("ProductName", product.ProductName)
        product.SupplierID = data.get("SupplierID", product.SupplierID)
        product.CategoryID = data.get("CategoryID", product.CategoryID)
        product.QuantityPerUnit = data.get("QuantityPerUnit", product.QuantityPerUnit)
        product.UnitPrice = data.get("UnitPrice", product.UnitPrice)
        product.UnitsInStock = data.get("UnitsInStock", product.UnitsInStock)
        product.UnitsOnOrder = data.get("UnitsOnOrder", product.UnitsOnOrder)
        product.ReorderLevel = data.get("ReorderLevel", product.ReorderLevel)
        product.Discontinued = data.get("Discontinued", product.Discontinued)
        db.session.commit()
        return product_schema.dump(product)

    return {"error": "product not found"}
