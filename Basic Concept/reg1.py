import re
s=input("Enter the string: ")
k=input("Enter the pattern: ")
r=re.search(k,s)
for r in re.finditer(k,s):
    l=(r.start(),r.end()-1)
else:
    l=(-1,-1)
print(l)
"\n" 