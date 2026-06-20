class InvalidUsername(Exception):
    pass
class UserNotFoundError(Exception):
    pass
class ShorterUsernameError(Exception):
    pass
class LoginSystem:
    def __init__(self,user_name):
        if len(user_name) < 4:
            raise ShorterUsernameError("user name is tto short")
        if not user_name.isalpha():
            raise InvalidUsername("invalid username")
        valid_iusers = ["rahul","anjali","kiran","rah@l"]
        if user_name not in valid_iusers:
            raise UserNotFoundError("user not found")
n = int(input())
user_name = [] 

Login =LoginSystem(user_name)
try:
    Login.LoginSystem(user_name)
except ShorterUsernameError as e:
    print(e)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
except InvalidUsername as e:
    print(e)
except UserNotFoundError as e:
    print(e)   
print("login successful")