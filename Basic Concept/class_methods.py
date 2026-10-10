"""
Class methods are methods defined inside the lcass that are bound to the class
To create a class method we use a decorator -> classmethod
"""
"""class Welcome:

    @classmethod
    def greeting(cls):
        print(cls)
        print("Welcome to my class")

g1=Welcome()
g1.greeting()
print(Welcome)"""
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

           print(f"The student studies for {n_hours} hours")
   def sport(self,sport):
          print(f"The student play {sport} in the {self.college_name}")

   @classmethod
   def greeting(cls):
       print(cls)
       print(f"Welcome to {cls.college_name}")

student1=Student("luck",3)
student1.study(4)
student1.sport("Football")
student1.greeting()


