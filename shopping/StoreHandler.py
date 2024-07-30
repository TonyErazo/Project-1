import logging

class StoreHandler():

    def list_items(self, cursor):
        list_item_query = "SELECT * FROM items;"
        cursor.execute(list_item_query)
        results = cursor.fetchall()
        logging.info("fetching list items...")
        for row in results:
            print(row)

    def change_item(self, item_id: int, cnx, cursor):
        while True:
            try:
                # Collect user input
                item_name = input("Please enter the name for the item: ")
                item_price = float(input("Please enter the price for the item (decimal format ex: 1.32): "))
                item_description = input("Please enter the description for the item: ")
                item_inventory = int(input("Please enter the current inventory for the item: "))

                # SQL query to update the item
                change_item_query = """
                    UPDATE items
                    SET name = %s, price = %s, description = %s, inventory = %s
                    WHERE id = %s
                """
                
                # Execute the query with parameters as a tuple
                cursor.execute(change_item_query, (item_name, item_price, item_description, item_inventory, item_id))

                # Commit the transaction
                cnx.commit()

                print("Item updated successfully.")
                logging.info("The item has been updated.")
                break  # Exit loop after successful update

            except ValueError:
                print("\nMake sure price is a decimal and inventory is a number, please try again.")
                logging.error("Error changing item, value error make sure price {price} is a decimal and inventory{decimal} is a number .")
            except Exception as e:
                print(f"An error occurred: {e}")
                logging.error("Error changing item.")
                break

    def delete_item(self, item_id: int, cnx, cursor):
        try:
            # SQL query to delete an item
            delete_item_query = "DELETE FROM items WHERE id = %s"

            # Execute the query with item_id as a tuple
            cursor.execute(delete_item_query, (item_id,))

            # Commit the transaction
            cnx.commit()

            print("Item deleted successfully.")
            logging.info("The item has been deleted.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error("Error deleting item.")

    def add_item(self, cnx, cursor):
         while True:
            try:
                # Collect user input
                item_name = input("Please enter the name for the item: ")
                item_price = float(input("Please enter the price for the item (decimal format ex: 1.32): "))
                item_description = input("Please enter the description for the item: ")
                item_inventory = int(input("Please enter the current inventory for the item: "))

                # SQL query to update the item
                add_item_query = """
                    INSERT INTO items (`name`, `price`, `description`, `inventory`)
                    VALUES (%s, %s, %s, %s);
                """
                
                # Execute the query with parameters as a tuple
                cursor.execute(add_item_query, (item_name, item_price, item_description, item_inventory))

                # Commit the transaction
                cnx.commit()

                print("Item added successfully.")
                logging.info("Item has been added.")
                break  # Exit loop after successful update

            except ValueError:
                print("\nMake sure price is a decimal and inventory is a number, please try again.")
                logging.error("Error adding item, value error make sure price {price} is a decimal and inventory{decimal} is a number .")
            except Exception as e:
                print(f"An error occurred: {e}")
                logging.error("Error adding item. {e}")
                break       

