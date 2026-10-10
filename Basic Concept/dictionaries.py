
#student1={'marks':[90,90,90,90],'name':'John'}
#print(student1)
user_dict = {}
value=[]
for i in range(1,2):
   key = input("Enter a key to access: ")

   for j in range(7):
       a = int(input("Enter marks:"))
       value.append(a)
   user_dict[key] = value
# Direct access; raises KeyError if key is missing
print(user_dict)

