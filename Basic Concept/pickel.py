import pickle
students ={'student1': {'roll': 101, 'name': 'John' , 'percent': 95.5,'Marks':90}, 'student2': {'roll': 102, 'name': 'Michael' , 'percent': 85.5},'student3': {'roll': 103, 'name': 'Wick' , 'percent': 90.5}}

"""'
with open ('student.txt', 'wt') as f:
  f.write(str(student))
'"""
""""
with open ('student.txt', 'rt') as f:
    content=f.read()

print(type(content))
out=dict(content)
print(out)
"""
#serialisation
with open ('student.bin', 'bw') as f:
    for student in students:
        pickle.dump(students[student],f)

#deserialisation
studentt=[]
with open('student.bin', 'rb') as f:
  while True: 
      try:
          data = pickle.load(f)
          if data['percent']>=90:
              studentt.append(data['name'])
      except EOFError:
         print("done")
         break