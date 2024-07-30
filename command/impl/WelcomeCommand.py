from command.Command import Command

class MenuCommand(Command):

    def execute(self):
        print("Welcome to the Q-Commerce!")
        print("Type signup to register an account")
        print("Type login to sign in")
