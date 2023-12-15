from datetime import datetime

from models import Customer, OrderItem, Product, faker, session_maker

# Customer functions on orders
#  View customer order

def customer_orderhistory(customer_id):
    with session_maker() as session:

        orderitems = session.query(OrderItem).filter(OrderItem.customer_id == customer_id).all()
        # print(orderitem)
        if len(orderitems) == 0 :
            print("Customer has no orders")
        else:
            order_details = []
            for orderitem in orderitems:
                product = session.query(Product).get(orderitem.product_id)
                order_info = {
                    "Order Id": orderitem.orderitem_id,
                    "Order Date": orderitem.order_date,
                    "Product": product.product_name,
                    "Quantity": orderitem.quantity,
                    "Total Price": orderitem.totalprice
                }
                order_details.append(order_info)

            for order_info in order_details:
                print(order_info)
# customer_orderhistory(2)


# View orders made on the current day by the current customer
def find_orders(customer_id, date):
    with session_maker() as session:
        orders = session.query(OrderItem).filter(OrderItem.customer_id == customer_id, OrderItem.order_date.like(f'{date}%')).all()
        if len(orders) == 0:
            print("No orders found for the customer on the specified day")
        else:
            for order in orders:
                product = session.query(Product).get(order.product_id)
                print(f"Order ID: {order.orderitem_id}, Order Date: {order.order_date} Product: {product.product_name}, Quantity: {order.quantity}, Total Price: {order.totalprice}")


# find_orders(customer_id, date)


# Customer updating order item
def update_order_item(order_item_id, new_quantity):
    with session_maker() as session:
        orderitem = session.query(OrderItem).filter_by(orderitem_id=order_item_id).first()
        if orderitem is not None:
            # Calculate quantity difference 
            quantity_diff = new_quantity - orderitem.quantity

            product = session.query(Product).filter_by(product_id=orderitem.product_id).first()
            # Update the order item quantity and total price
            orderitem.quantity = new_quantity
            orderitem.totalprice = product.product_price * new_quantity

            # Update product amount
            if product is not None:
                product.product_amount -= quantity_diff

            session.commit()
            print("Order item updated successfully.")
        else:
            print("Order item not found.")


# update_order_item(order_item_id, new_quantity)



# Customer deleting an order item
def remove_orderitem(order_item_id):
    with session_maker() as session:
        orderitem = session.query(OrderItem).filter_by(orderitem_id=order_item_id).first()
        if orderitem is not None:
            product = session.query(Product).filter_by(product_id=orderitem.product_id).first()
            if product is not None:
                product.product_amount += orderitem.quantity
                session.delete(orderitem)
                session.commit()
                print("Order item deleted successfully.")
            else:
                print("Product is not available.")
        else:
            print("Order item not found.")

# remove_orderitem(order_item_id)

# Order invoice
def get_total_price(customer_id):
    current_date = datetime.now().strftime("%Y-%m-%d")
    with session_maker() as session:
        orders = session.query(OrderItem).filter_by(customer_id=customer_id, order_date=current_date).all()
        if len(orders) > 0:
            total_price = 0
            for order in orders:
                total_price += order.totalprice
            print(f"Total price for customer ID {customer_id} on {current_date}: {total_price}")
        else:
            print("No orders found.")


# customer_id = int(input("Enter customer ID: "))
# get_total_price(customer_id)