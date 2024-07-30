
from authentication.User import User

import mysql.connector
import logging

class LoginHandler:

    '''
        authenticates a login request and validates the input from the database
        @cursor the database cursor
    '''
    def authenticate(self, cursor):
        email = input("Please enter your account e-mail:\n")
        password = input("Please enter your password\n")

        query = "SELECT * from users AS u WHERE u.email='" + email + "' AND u.password='" + password + "';"
        logging.info("Fetching account information...")
        cursor.execute(query)
        results = cursor.fetchone()

        if results:
            print("Valid login")
            user_id = results[0]
            first_name = results[3]
            last_name = results[4]
            privilege = results[5]
            status = results[6]
            logging.info("Account information successfully retrieved.")

            if status == "locked":
                print("Your account has been locked please contact an administrator.")
                logging.info("Account attemped to initiate a session is locked.")
                return False
            elif status == "banned":
                print("Your account has been banned!")
                logging.info("Account attemped to initiate a session is banned.")
                return False

            self.user = User(user_id, email, password, first_name, last_name, privilege)
            return True
        else:
            print("Invalid username or password.")
            logging.info("Invalid account credentials...")
        return False

    '''
        Registers an account into the database
        @cnx database connection
        @cursor the database cursor
    '''
    def register(self, cnx, cursor):
        while True:
            email = input("Please enter an e-mail adddress: ")
            password = input("Please enter a password: ")
            first_name = input("Please enter your first name: ")
            last_name = input("Please enter your last name: ")

            try:
                query = "INSERT INTO users (`email`, `password`, `firstname`, `lastname`) VALUES ('" + email + "', '" + password + "','" + first_name + "', '" + last_name + "');"
                cursor.execute(query)
            except mysql.connector.Error as e:
                print(e)
                print("Registration is not successful, the email entered is currently in use.")
                print("Please enter a different e-mail.")
                logging.error("Account registration failed...")
                continue
            
            print("Account has been registered!")
            logging.info("Account has been registered.")
            #cursor.execute("SELECT * FROM users;")

            cnx.commit()
            logging.info("Updating database...")
            break

    def get_user(self)-> User:
        return self.user