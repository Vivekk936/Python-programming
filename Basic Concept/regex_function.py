import re
s1="We are learning regex in Python"
pat=(r"[a-z][a-z][a-z]")
mat=re.match(pat,s1)
print(mat)

#findall()
s2="lacy=4352353536362622525, Jack=3493939453, Carol=9080088900"
pat2=r"[0-9]{10}"
mat2=re.findall(pat2,s2)
print(mat2)

#\b boundary
pat3=r"\b[0-9]{7,15}\b" #\b it will not print the number exceeding 15
mat3=re.findall(pat3,s2)
print(mat3)
#finditer()
pat4=r"[0-9]{7,15}"
mat4=re.finditer(pat4,s2)
for match in mat4:
    print(match)
print(mat4)