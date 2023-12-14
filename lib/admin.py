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

