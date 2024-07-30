from command.CommandHandler import CommandHandler
from command.impl.MenuCommand import MenuCommand
from authentication.LoginHandler import LoginHandler
import mysql.connector
import logging

#Application entry-point
def main():
    logging.basicConfig(filename="application.log", format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO) 
    logging.info("Starting application...")
    login_handler = LoginHandler()
    menu_command = MenuCommand()

    cnx = mysql.connector.connect(host="localhost", user="root", password="0000", database="qcommerce")
    cursor = cnx.cursor()
    logging.info("Successfully connected to database...")
    while True:
        terminal_input = input("Please enter register to create an account or login to sign in\n")

        if terminal_input == "register":
            login_handler.register(cnx, cursor)
        elif terminal_input == "exit":
            exit()

        elif terminal_input == "login":
            authenticated = login_handler.authenticate(cursor)

            while not authenticated:
                authenticated = login_handler.authenticate(cursor)
            
            if authenticated:
                #We've successfully logged in so now we can start processing store commands
                command_handler = CommandHandler(login_handler.get_user(), cnx, cursor)
                command_handler.process("menu")
                while True:
                    terminal_input = input("Please enter a command\n")

                    if(terminal_input == "logout"):
                        authenticated = False
                        break
                    command_handler.process(terminal_input)
        else:
            print("Please enter a valid option")


# Run main function
if __name__ == "__main__":
    main()