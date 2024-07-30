import mysql.connector
import logging

class UserHandler():

    def list_users(self, cursor):
        list_users_query = "SELECT * FROM users;"
        cursor.execute(list_users_query)
        results = cursor.fetchall()
        for row in results:
            print(row)

    def create_user(self, cnx, cursor):
        while True:
            email = input("Please enter an e-mail adddress: ")
            password = input("Please enter a password: ")
            first_name = input("Please enter your first name: ")
            last_name = input("Please enter your last name: ")
            privilege = input("Please enter a privilege for the account (1-3): ")
            try:
                query = "INSERT INTO users (`email`, `password`, `firstname`, `lastname`, `privilege`) VALUES ('" + email + "', '" + password + "','" + first_name + "', '" + last_name + "', '" + privilege + "');"
                cursor.execute(query)
            except mysql.connector.Error as e:
                print(e)
                print("Registration is not successful, the email entered is currently in use.")
                print("Please enter a different e-mail.")
                logging.error("Error creating user.")
                continue
            
            print("Account has been registered!")
            #cursor.execute("SELECT * FROM users;")

            cnx.commit()
            logging.info("The user has been created.")
            break

    def delete_user(self, email:str, cnx, cursor):
        try:
            # SQL query to delete an item
            delete_user_query = "DELETE FROM users WHERE users.email = %s"

            # Execute the query with item_id as a tuple
            cursor.execute(delete_user_query, (email,))

            # Commit the transaction
            cnx.commit()

            print("User deleted successfully.")
            logging.info("The user has been deleted.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error("Error deleting user.")

    def ban_user(self, email:str, cnx, cursor):
        try:
            # SQL query to update the item
            ban_user_query = """
                UPDATE users
                SET status = %s
                WHERE email = %s
            """
            
            # Execute the query with parameters as a tuple
            cursor.execute(ban_user_query, ("banned", email,))

            # Commit the transaction
            cnx.commit()

            print("User account has been banned successfully.")
            logging.info("The user has been banned.")

        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error("Error banning user.")


    def lock_user(self, email:str, cnx, cursor):
        try:
            # SQL query to update the item
            lock_user_query = """
                UPDATE users
                SET status = %s
                WHERE email = %s
            """
            
            # Execute the query with parameters as a tuple
            cursor.execute(lock_user_query, ("locked", email,))

            # Commit the transaction
            cnx.commit()

            print("User account has been locked successfully.")
            logging.info("The user has been locked.")

        except mysql.connector.Error as e:
            print(f"An error occurred: {e}")
            logging.info("UserHandler.py lock_user() - Error locking user.")

    def display_orders(self, user, cursor):
        try:
            # Corrected SQL query with proper placeholder
            order_query = """
                SELECT orders.id AS order_id, orders.amount, items.name AS item_name
                FROM orders
                INNER JOIN items ON orders.itemid = items.id
                WHERE orders.userid = %s;
            """

            # Execute the query with the user ID as the parameter
            cursor.execute(order_query, (user.get_user_id(),))
            results = cursor.fetchall()
            logging.info("Fetching orders...")
            # Print the results
            for row in results:
                print(row)
        except mysql.connector.Error as e:
            print(f"An error occurred: {e}")
            logging.info("UserHandler.py display_orders() - Error {e}.")