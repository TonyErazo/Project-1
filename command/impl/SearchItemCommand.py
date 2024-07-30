from command.Command import Command
from authentication.User import User
from shopping.ShopHandler import ShopHandler
import logging

class SearchItemCommand(Command):

    def __init__(self, user: User, cnx, cursor):
        self.user = user
        self.cnx = cnx
        self.cursor = cursor
        self.shop_handler = ShopHandler()

    def execute(self, search_item:str):
        print("searching for: " + str(search_item))
        query = "SELECT * FROM items WHERE items.name LIKE '%" + search_item + "%';"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        logging.info("Searching for items... {query}")


        index = 0
        for row in results:
            print(str(index) + " --- " + str(row), "\n")
            index += 1


        if len(results) != 0:
            while True:
                try:
                    item_index = int(input("Please enter which item you'd like to select: "))

                    if(item_index >= len(results)):
                        print("This is out of range please enter a valid value!")
                        logging.error("{item_index} is out of range!")
                        continue
                    break
                except ValueError:
                    print("\n" + str(item_index) + " is not a valid number, please try again.")
                    logging.error("{item_index} is not a valid number!")
                except Exception as e:
                    print(f"An error occurred: {e}")
                    logging.error("Error:{e}")

            item_id = results[item_index][0]
            purchasing = input("Would you like to add this item to your cart? y/n ")

            if purchasing == "y":
                self.shop_handler.add_item(item_id, self.user, self.cnx, self.cursor)
        else:
            print("No results! Perhaps you should search something else")
            logging.info("No results have been found query: {query}")
        
        
