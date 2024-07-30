from command.impl.MenuCommand import MenuCommand
from command.impl.SearchItemCommand import SearchItemCommand
from shopping.ShopHandler import ShopHandler
from shopping.StoreHandler import StoreHandler
from authentication.UserHandler import UserHandler

class CommandHandler:

    def __init__(self, user, cnx, cursor):
        self.user = user
        self.cnx = cnx
        self.cursor = cursor
        self.menu_command = MenuCommand()
        self.search_item_command = SearchItemCommand(user, cnx, cursor)
        self.shop_handler = ShopHandler()
        self.store_handler = StoreHandler()
        self.user_handler = UserHandler()

    def process(self, terminal_input: str):
        match terminal_input.split():
            case ["menu"]:
                self.menu_command.execute(self.user)
            case ["search", *_]:
                item_name = terminal_input.split()[1]
                self.search_item_command.execute(item_name)
            case ["cart", "remove"]:
                self.shop_handler.remove_item(self.user, self.cnx, self.cursor)
            case ["cart"]:
                self.shop_handler.get_cart(self.user, self.cursor)
            case ["purchase"]:
                self.shop_handler.purchase(self.user, self.cnx, self.cursor)
            case ["orders"]:
                self.user_handler.display_orders(self.user, self.cursor)

            case["list", "items"]:
                if self.user.get_privilege() < 2:
                    print("You must be a shop owner or admin to use this command!")
                else:
                    self.store_handler.list_items(self.cursor)
            # change itemname [item_id] [item_name]
            case ["change", *_]:
                if self.user.get_privilege() < 2:
                    print("You must be a shop owner or admin to use this command!")
                else:
                    try:
                        item_id = int(terminal_input.split()[1])
                        self.store_handler.change_item(item_id, self.cnx, self.cursor)
                    except ValueError:
                        print("The item id is not a number!")
            case ["delete", *_]:
                if self.user.get_privilege() < 2:
                    print("You must be a shop owner or admin to use this command!")
                else:
                    try:
                        item_id = int(terminal_input.split()[1])
                        self.store_handler.delete_item(item_id, self.cnx, self.cursor)
                    except ValueError:
                        print("The item id is not a number!")
            case ["add", "item"]:
                if self.user.get_privilege() < 2:
                    print("You must be a shop owner or admin to use this command!")
                else:
                    self.store_handler.add_item(self.cnx, self.cursor)
            case ["list", "users"]:
                if self.user.get_privilege() < 3:
                    print("You must be an admin to use this command!")
                else:
                    self.user_handler.list_users(self.cursor)
            case ["delete", *_]:
                if self.user.get_privilege() < 3:
                    print("You must be an admin to use this command!")
                else:
                    email = terminal_input.split()[1]
                    self.user_handler.delete_user(email, self.cnx, self.cursor)
            case ["ban", *_]:
                if self.user.get_privilege() < 3:
                    print("You must be an admin to use this command!")
                else:
                    email = terminal_input.split()[1]
                    self.user_handler.ban_user(email, self.cnx, self.cursor)
            case ["lock", *_]:
                if self.user.get_privilege() < 3:
                    print("You must be an admin to use this command!")
                else:
                    email = int(terminal_input.split()[1])
                    self.user_handler.lock_user(email, self.cnx, self.cursor)
            case ["create", "user"]:
                if self.user.get_privilege() < 3:
                    print("You must be an admin to use this command!")
                else:
                    self.user_handler.create_user(self.cnx, self.cursor)
            case ["list", "orders"]:
                if self.user.get_privilege() < 2:
                    print("You must be a shop owner or admin to use this command!")
                else:
                    self.shop_handler.display_orders(self.cnx, self.cursor)
            case ["exit"]:
                exit()
            case _: # Default case
                print("Please enter a valid command.")

