# Public By default, all members within a class are public, and there’s no need to specify
# access modifiers for public members. Being public means that these members 
# can easily be accessed outside of the class, in another part of the program. For example, if we had the following:
class ClassSchedule:
   def __init__(self, course, instructor):
       self.course = course
       self.instructor = instructor
  
   def display_course(self):
       print(f'Course: {self.course}, Instructor: {self.instructor}')

# Protected Protected access modifiers, denoted with the prefix _, 
# prevent members from being accessed outside of the class, unless it’s from a subclass.
# let’s modify the class from the example above and make the members course and instructor protected with the _.
class ClassSchedule:
   def __init__(self, course, instructor):
       self._course = course # protected
       self._instructor = instructor # protected
  
   def display_course(self):
       print(f'Course: {self._course}, Instructor: {self._instructor}')
 
sched = ClassSchedule('Biology', 'Ms. Smith')
sched.display_course()

# Private Private access modifiers, denoted with the prefix __, 
# declare members to be accessible within the class only. Members with this modifier will
#  be marked private and any attempt 
# to access these members outside of the class will cause an Attribute Error message.
class ClassSchedule:
   def __init__(self, course, instructor):
       self.__course = course # private
       self.__instructor = instructor # private
  
   def display_course(self):
       # public
 
       print(f'Course: {self.__course}, Instructor: {self.__instructor}')
 
sched = ClassSchedule('Biology', 'Ms. Smith')
 
sched.__course # this will throw an Attribute Error because we're trying to access a private member
 
sched.display_course() # this won't throw an Attribute Error because this method is public

