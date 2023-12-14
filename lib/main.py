
from datetime import datetime

from admin import (add_product)
from category import view_categories



def main():

    # Entrypoint of the system
    choice = 0
    while choice != 3:
        print("*** GREEN GROCERY MANAGEMENT SYSTEM ")
        print("1) Enter system as an customer")
        print("2) Enter system as a administrator") 
        

        choice = int(input())

        # enter system as a customer
        if choice == 1:
            validate_customer()

            customer_choice = 0
            while customer_choice != 8:

                print("*** Customer's View")
                print("1) View your details")
                print("2) View products")
                print("3) Make an order")
                print("4) View orders")
                print("5) Update order item")
                print("6) Delete order item")
                print("7) View orders history")
                print("8) Go back to main menu")

                customer_choice = int(input())

                if customer_choice ==  1:
                    customer_id = int(input("Enter your customer ID: "))
                    display_customer(customer_id)
                elif customer_choice == 2:
                    view_productscustomer()
                elif customer_choice == 3:
                    product_id = input("Enter the product ID: ")
                    quantity = int(input("Enter the product quantity: "))
                    customer_id = input("Enter your id: ")
                    make_order(product_id, quantity, customer_id)
                elif customer_choice == 4:
                    customer_id = input("Enter your id: ")
                    date = datetime.now().strftime("%Y-%m-%d")
                    find_orders(customer_id, date)   
                elif customer_choice == 5:
                    order_item_id = int(input("Enter order item ID: "))
                    new_quantity = int(input("Enter new quantity: "))
                    update_order_item(order_item_id, new_quantity)
                elif customer_choice == 6:
                    orderitem_id = input("Enter the order item ID: ")
                    remove_orderitem(orderitem_id)
                elif customer_choice == 7:
                    customer_id = input("Enter your id: ")
                    customer_orderhistory(customer_id)

        # Enter the system as an administrator   
        if choice == 2:

            admin_choice = 0
            while admin_choice != 7:

            
                print("*** Admin's View")
                print("1) View Categories")
                print("2) View products")
                print("3) Add products")
                print("4) Update stock")
                print("5) Update price")
                print("6) Delete product")
                print("7) Go back to main menu")

                admin_choice =int(input())

                if admin_choice == 1:
                    view_categories()
                elif admin_choice == 2:
                    view_productsadmin()

                elif admin_choice == 3:
                    product_name = input("Enter the name of the product: ")
                    product_description = input("Enter the description of the product: ")
                    product_price = input("Enter the price of the product: ")
                    product_amount = input("Enter the amount of the product: ")
                    category_id = input("Enter the category of the product: ")
                    


                    add_product(product_name, product_description, product_price, product_amount, category_id)

                elif admin_choice == 4:
                    product_id = input("Enter the ID of the product: ")
                    quantity = int(input("Enter the quantity: "))
                    add_stock(product_id, quantity)

                elif admin_choice == 5:
                    product_id = input("Enter the ID of the product: ")
                    price = int(input("Enter the price: "))
                    update_price(product_id, price)
                     
                elif admin_choice == 6:
                    product_id = input("Enter id of product you want to delete: ")
                    delete_product(product_id)
                
                







if __name__ == "__main__":
    main()