from datetime import datetime

from models import Product, Category, session_maker

def add_product(name, description, price, amount, category):
    with session_maker() as session:
        product = session.query(Product)
        product = Product(product_name = name, product_description = description, product_price = price, product_amount = amount, category_id = category)
        session.add(product)
        print("Product added successfully!")
        session.commit()



# add_product("Chicken thighs", "Excellent source of iron and zinc ", 50, 600, 4, 1)
# Admin adding product amount
def add_stock(product_id, quantity):
    with session_maker() as session:
        product = session.query(Product).get(product_id)
        product.product_amount += quantity
        print("Product update successfully!")
        session.commit()

# add_stock(1, 2)

# Admin updating product price
def update_price(product_id, price):
    with session_maker() as session:
        product = session.query(Product).get(product_id)
        product.product_price = price
        print("Price updates successfully!")
        session.commit()

# update_price(1, 15)
def view_productsadmin():
    with session_maker() as session:
        products = session.query(Product)
        all_products = []
        # print(all_products)
        for product in products:
            category = session.query(Category).get(product.category_id)
            product_info = {
                "Product ID": product.product_id,
                "Product": product.product_name,
                "Description": product.product_description,
                "Price": product.product_price,
                "Available Units": product.product_amount,
                "Category ID": product.category_id,
                "Category": category.category_name
            }
            all_products.append(product_info)

        for product_info in all_products:
            print(product_info)
        session.commit()
# view_productsadmin()

def delete_product(product_id):
    with session_maker() as session:
        product = session.query(Product).filter(Product.product_id == product_id).first()
        session.delete(product)
        print("Product deleted successfullly!")
        session.commit()
# delete_product(2)
