"""
class variable are defined at the class level
Same copy of the class variables are shared among the objects
"""
class Student:
   """
   This is a class student to manage student info activities
   """
   college_name="Doon University"
   department_name=["Btech","Management","BSC"]
   def __init__(self,name,roll):
       print("Calling the initializer")
       self.name=name
       self.roll=roll

   def study(self,n_hours):   #instance method

           print(f"The student studies for {n_hours} hours")
   def sport(self,sport):
          print(f"The student play {sport}")

help(Student)
student1=Student("Wick",1)
print(student1.name,student1.roll)
print(student1.__dict__)
print(student1.department_name)
print(student1.college_name)

student2=Student("luck",3)
print(student2.department_name)
print(student2.college_name)