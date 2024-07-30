from command.Command import Command
from authentication.User import User

class MenuCommand(Command):

    def execute(self, user: User):
        privilege = user.get_privilege()

        print("Welcome to Q-Commerce: " + user.get_firstname())
        print("The menu is as follows:")
        print("search [item] - Retrieves a list of items that match " +
            "your desired search.")
        print("cart - displays the list of your cart along with the total price")
        print("cart remove - removes item from your cart")
        print("purchase - processes your cart and purchase confirmation")
        print("orders - displays a list of all your past orders")


        match privilege:
            case 2:
                print("list items - list all the items in the story")
                print("change [item_id] - change the name of the item with the specified name")
                print("delete [item_id] - deletes the specified item")
                print("add item - adds an item to the specified store")
            case 3:
                print("list items - list all the items in the story")
                print("change [item_id] - change the name of the item with the specified name")
                print("delete [item_id] - deletes the specified item")
                print("add item - adds an item to the specified store")

                print("list users - list all the users in the database")
                print("ban [user-email] - bans a specified user based on their e-mail")
                print("lock [user-email] - locks a specified user based on their e-mail")
                print("delete [user-email] - deletes a specified user based on their e-mail")
                print("create user")



