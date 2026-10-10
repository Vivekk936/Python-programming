#__init__() method
#is an instance method
#is used to create  and initialize the attributes during the object creation
class Student:
   """
   This is a class student to manage student info activities
   """
   def __init__(self,name,roll):
       print("Calling the initializer")
       self.name=name
       self.roll=roll

   def study(self,n_hours):   #instance method

           print(f"The student studies for {n_hours} hours")
   def sport(self,sport):
          print(f"The student play {sport}")


#object_name.attribute_name = value
student1 = Student("Shail",3)
student1.grade="B" #one attribute extra
student2 = Student("sohuu",4 )
print(student1.name,student1.roll)
print(student2.name,student2.roll)
print(student1.__dict__)
print(student2.__dict__)
student3= Student("Alice",12)
print(student3.name,student3.roll)
print(student3.__dict__)