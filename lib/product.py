from datetime import datetime

from models import Product, faker, session_maker
#sample grocery product data
products = [
    Product(product_name = "Spinach", product_description = "This is a vegetable rich in iron, vitamin C and E", product_price = 10, product_amount = 60, category_id = '2'),
    Product(product_name = "Apple", product_description = "This is a fruit that slows down digestion", product_price = 35, product_amount = 100, category_id = '1'),

]


# creating products
def create_product():
    with session_maker() as session:
        for product in products:
            session.add(product)
        session.commit()

# # # create_product()
# reading products
def view_products():
    with session_maker() as session:
        products = session.query(Product)
        for product in products:
            print(product)

# view_products()

# updating products
def update_product():
    with session_maker() as session:
        product = session.query(Product).filter(Product.product_id == 2).first()
        product.product_description = "The apple is suit"
        session.commit()

# update_product()

# deleting products
def delete_product():
    with session_maker() as session:
        product = session.query(Product).filter(Product.product_id == 2).first()
        session.delete(product)
        session.commit()

# delete_product()

