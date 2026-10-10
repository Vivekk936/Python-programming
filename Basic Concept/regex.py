import re
s=input("Enter a string: ")
k=re.search("the",s)
r=re.search("[0-9][0-9]",s)
d=re.search("[0-9][.][0-9]",s)
print(k)
print(r)
print(d)
k1=re.search("[0-9].[0-9]","House number : 251/A") # . matches any character except new line
print(k1)

import re
#[A-z] [a-z]
s1=input("Enter a string: ")
pat=r"old\new" # r is used to tell python take \n as normal string

p1=r"[A-Z][a-z][a-z]"
s9=re.search(p1,s1)
print(s9)

pat1=r"[a-z][a-z]\d"#\d matches 1 digit character.It  is similar to [0-9]
mat=re.search(pat1,s1)
print(mat)
pat11=r"[a-z][a-z]\D"#\D matches 1 non digit character.
mat1=re.search(pat11,s1)
print(mat1)

pat2=r"[a-z]\s"#\s matches space character,tab and \n character.
mat2=re.search(pat2,s1)
print(mat2)
pat3=r"[a-z]\S"#\S noT matches space character.
mat3=re.search(pat3,s1)
print(mat3)


pat4=r"[a-z]\w"#\w matches [0-9],[a-z],[A-Z] and _
mat4=re.search(pat4,s1)
print(mat4)


import re
s1="I want to buy ps5 which is of Version 2026 series.Email me at abc123@gmail.com"
m=r"[a-z]{4}"
ree=re.search(m,s1)
print(ree)
m1=r"[A-Z][a-z]{4}"
re1=re.search (m1,s1)
print(re1)
pat2=r"[a-z]{2,5}"#{2,5} means either it can match 2 to 5.
mat2=re.search(pat2,s1)
print(mat2)
pat3=r"[a-z]+" # means matches 1 or more
mat3=re.search(pat3,s1)
print(mat3)
pat4=r"[a-z][a-z]?"# 0 or 1 repetitions of previous pattern
mat4=re.search(pat4,s1)
print(mat4)

pat5=r"[a-z][a-z ]*"# * 0 or more repetitions of previous pattern
mat5=re.search(pat5,s1)
print(mat5)

pat6=r"^[A-Z]" #^ looks beginning of string
mat6=re.search(pat6,s1)
print(mat6)

pat7=r"[a-z ]$"
mat7=re.search(pat7,s1)
print(mat7)

pat8=r"(com)"#() this means group [] bracket takes only one of them
mat8=re.search(pat8,s1)
print(mat8)