import json
student ={'student1': {'roll': 101, 'name': 'John' , 'percent': 95.5,'Marks':90}, 'student2': {'roll': 102, 'name': 'Michael' , 'percent': 85.5},'student3': {'roll': 103, 'name': 'Wick' , 'percent': 90.5}}

print(student)


try:
   with open("Student.json", "wt") as f:
    print(json.dump(student,f, indent=4))

except FileNotFoundError :
        print("Student.json not found")

else:
     with open("Student.json", "rt") as f:
       data=json.load(open("Student.json"))
       data.update(student)
       with open("Student.json",'wt') as f:
          json.dump(data,f,indent=4)






