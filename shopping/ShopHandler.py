
import mysql.connector
import logging

class ShopHandler():

    def add_item(self, item_id:int, user, cnx, cursor):
        while True:
            try:
                amount = int(input("Please enter the quantity you'd like to buy: "))
                # submit this to the user cart
                cart_query = "INSERT INTO carts (userid, itemid, itemamount) VALUES (%s, %s, %s);"
                cursor.execute(cart_query, (user.get_user_id(), item_id, amount))
                cnx.commit()
                print(f"Added {amount} of item {item_id} to your cart.")
                logging.info("Added amount:{amount} item:{item_id} to your cart.")
                break
            except ValueError:
                print("\n" + str(amount) + " is not a valid number, please try again.")
                logging.error("Error adding amount:{amount} item:{item_id} to your cart.")
            except Exception as e:
                print(f"An error occurred: {e}")
                logging.error("Error adding amount:{amount} item:{item_id} to your cart.")
                break

    def remove_item(self, user, cnx, cursor):
        while True:
            try:
                cart_id = int(input("Please enter the index of the item you'd like to remove: "))
                # submit this to the user cart
                cart_query = "DELETE FROM carts WHERE carts.id = %s;"
                result = cursor.execute(cart_query, (cart_id,))
                print(f"Removed {cart_id} to your cart. ")
                cnx.commit()
                logging.info("Removed cart:{cart_id}.")
                break
            except ValueError:
                print("\n" + str(cart_id) + " is not a valid number, please try again.")
                logging.error("Error removing cart: {cart_id} make sure it's a valid number")
            except Exception as e:
                print(f"An error occurred: {e}")
                logging.error("Error removing cart: {cart_id}")
                break

    def get_cart(self, user, cursor):
        show_cart_query = """
            SELECT carts.id, items.name, carts.itemid, carts.itemamount 
                FROM users 
                JOIN carts ON users.id = carts.userid 
                JOIN items ON carts.itemid = items.id 
                WHERE users.id = %s;
        """
        cursor.execute(show_cart_query, (user.get_user_id(),))
        results = cursor.fetchall()
        logging.info("Fetching cart...")
        for row in results:
            print(row)

    def purchase(self, user, cnx, cursor):
        try:
            purchase_query = """
                INSERT INTO orders (`userid`, `itemid`, `amount`, `totalcost`) SELECT users.id, carts.itemid, carts.itemamount, 
                (carts.itemamount * items.price) AS totalcost 
                                FROM users 
                                JOIN carts ON users.id = carts.userid 
                                JOIN items ON carts.itemid = items.id
                                WHERE users.id = %s;
            """
            cursor.execute(purchase_query, (user.get_user_id(),))
            results = cursor.fetchall()

             # Fetch the data to update inventory
            cursor.execute("""
                SELECT carts.itemid, carts.itemamount
                FROM carts
                WHERE carts.userid = %s;
            """, (user.get_user_id(),))

            cart_items = cursor.fetchall()

             # Update the inventory based on the cart contents
            for item_id, item_amount in cart_items:
                update_inventory_query = """
                    UPDATE items
                    SET inventory = inventory - %s
                    WHERE id = %s;
                """
                cursor.execute(update_inventory_query, (item_amount, item_id))
            #for row in results:
            #    print(row)


            remove_item_query = "DELETE FROM carts WHERE userid = %s;"
            remove_item_result = cursor.execute(remove_item_query, (user.get_user_id(),))
            cnx.commit()
            print("Purchase Successful! Cart has been cleared")
            logging.info("Successfully purchased items from cart, the cart items have been moved to orders.")
        except mysql.connector.Error as e:
            print("SQL Error: {0}".format(e))
            logging.error("ShopHandler.py purchase() SQL Error: {0}".format(e))

    def display_orders(self, user, cursor):
        try:
            # Corrected SQL query with proper placeholder
            order_query = """
                SELECT users.email, orders.id AS order_id, orders.amount, items.name AS item_name, orders.totalcost
                FROM orders
                INNER JOIN items ON orders.itemid = items.id
                INNER JOIN users ON orders.userid = users.id;
            """

            # Execute the query with the user ID as the parameter
            cursor.execute(order_query)
            results = cursor.fetchall()
            logging.info("Fetching all orders...")
            # Print the results
            for row in results:
                print(row)
        except mysql.connector.Error as e:
            print("SQL Error: {0}".format(e))
            logging.error("ShopHandler.py display_orders() SQL Error: {0}".format(e))
