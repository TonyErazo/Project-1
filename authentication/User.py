class User:

    def __init__(self, user_id:int, email: str, password: str, first_name:str, last_name:str, privilege: int):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.privilege = privilege

    def get_user_id(self):
        return self.user_id
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    def get_firstname(self):
        return self.first_name
    
    def get_lastname(self):
        return self.last_name
    
    '''
        Gets the User's priviledge
        1 - Shopper
        2 - Shop Owner
        3 - Administrator
    '''
    def get_privilege(self)-> int:
        return self.privilege