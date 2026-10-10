class Student:
   """
   This is a class student to manage student info activities
   """
   def study(self,n_hours):   #instance method

           print(f"The student studies for {n_hours} hours")
   def sport(self,sport):
          print(f"The student play {sport}")

student1=Student()
student2=Student()
"""print(student1)
print(Student.__doc__)
"""
print(student1)
student1.study(3)
student1.sport("Football")
print(student2)
student2.study(2)
student2.sport("Tennis")
"""
When we call an instance method using the object/instance of the class Python 
passes the object itself as the first argument to that method. 
That first argument is by standard is self 
"""
