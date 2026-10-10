"""
Static method-method defined inside a class which is neither bound to the object nor to the class
To create a static method we use a staticmethod decorator
"""
class Student:
   """
   This is a class student to manage student info activities
   """
   college_name = "Doon University"
   department_name = ["Btech", "Management", "BSC"]
   def __init__(self,name,roll):
       print("Calling the initializer")
       self.name=name
       self.roll=roll

   def study(self,n_hours):   #instance method
        print(f"Student {self.name} roll {n_hours} hours")

   def sport(self,sport):
          print(f"The student play {sport} in the {self.college_name}")

   @staticmethod
   def greet(): #works like normal method
       print("Welcome to the Student Class")

   @classmethod

   def greeting(cls):
       print(cls)
       print(f"Welcome to {cls.college_name}")

student1=Student("John",1)
student1.greet()
student1.greeting()
student1.study(5)
student2=Student("Jane",2)
student2.greet()
student2.study(3)