from sqlalchemy import func

from models import Category, Customer, Product, faker, session_maker


# View customer details
# Tuple implemented
def get_all_customers():
    with session_maker() as session:
        customers = session.query(Customer).all()
        customer_tuples = [(customer.customer_id, customer.customer_fname, customer.customer_lname, customer.customer_mobile) for customer in customers]
        return customer_tuples


# all_customers = get_all_customers()
# for customer in all_customers:
#     print(customer)


# Validate customer, if not present, allow signup
def validate_customer():
    customer_id = int(input("Enter customer ID: "))
    with session_maker() as session:
        customer = session.query(Customer).filter_by(customer_id=customer_id).first()
        if customer is None:
            print("Customer is not registered, please sign up to be registered.")
            signup_customer()
        else:
            print("Customer is registered.")

# Signing up a new customer
def signup_customer():
    # Prompt for customer details
    customer_fname = input("Enter your first name: ")
    customer_lname = input("Enter your last name: ")
    customer_mobile = input("Enter your mobile number: ")

    with session_maker() as session:
        new_customer = Customer(customer_fname=customer_fname, customer_lname=customer_lname, customer_mobile=customer_mobile)
        session.add(new_customer)
        session.commit()
        print("Signup Successful!")

# validate_customer()



# Displaying individual customer details
# Dictionary implemeted
def display_customer(customer_id):
    with session_maker() as session:
        customer = session.query(Customer).filter_by(customer_id=customer_id).first()
        if customer is not None:
            print("These are your customer details:")
            print(f"Customer ID: {customer.customer_id}")
            print(f"First Name: {customer.customer_fname}")
            print(f"Last Name: {customer.customer_lname}")
            print(f"Mobile: {customer.customer_mobile}")
        else:
            print("Customer not found.")

# Viewing the available products for sale
# List of dictionary implemented
def view_productscustomer():
    with session_maker() as session:
        products = session.query(Product)
        all_products = []
        # print(all_products)
        for product in products:
            category = session.query(Category).get(product.category_id)
            product_info = {
                "Product ID": product.product_id,
                "Product": product.product_name,
                "Category": category.category_name,
                "Description": product.product_description,
                "Price": product.product_price,
                "Available Units": product.product_amount
            }
            all_products.append(product_info)
        for product_info in all_products:
            print(product_info)
# view_productscustomer()