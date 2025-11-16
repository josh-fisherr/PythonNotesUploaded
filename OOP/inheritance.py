# Inheritance is a feature of object-oriented programming (OOP) 
# that enables the transfer of methods and properties of one class to another. 
# Inheritance allows for reusability of code as well as extending the capability of new classes. 
# Two main components of inheritance Parent class & Child class

# Parent Class
class Person:
   def __init__(self, name, age):
       self.name = name 
       self.age = age 
  
   def print_info(self):
       print(f'{self.name} is {self.age} years old')

# Child Class
class Teacher(Person):
  def __init__(self, name, age, subject):
      self.subject = subject
 
      Person.__init__(self, name, age)

# Output
myTeacher = Teacher("Dr. Hirani", 49, "Computer Science")
myTeacher.print_info()
print(myTeacher.subject)