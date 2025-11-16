# A popular example of encapsulation is a class, as it “encapsulates” 
# members such as variables and methods in one single unit. In this article, we’ll explore different members of a class.

class UserInfo:
   def __init__(self, username, email_address):
      self.username = username
      self.email_address = email_address
 
   def check_username(self, username_to_check):
       if username_to_check == self.username:
           return True
       else:
           return False

# This is using the constructor to create a new instance of username and email address
user = UserInfo('user123', 'abc@edf.ghi')
 
# This will return the data that is stored
user.username
user.email_address

# We can call the method check_username on our object to run the method:
user = UserInfo('user123', 'abc@edf.ghi')
 
user.check_username('user123') # returns True
user.check_username('user456') # returns False

