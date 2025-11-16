# constructor
class ClassSchedule:
   def __init__(self, course):
       self.course = course
 
first = ClassSchedule('Chemistry')
print(first.course)

# destructor
class ClassSchedule:
   def __init__(self, course):
       self.course = course
  
   def __del__(self):
       print('You successfully deleted your schedule')
 
# deleting instance 
sched = ClassSchedule('Chemistry')
del sched