import re

s2="lacy=4352353536362622525, Jack=3493939453, Carol=9080088900"
pat=r"\d{10}"
matches=re.compile(pat)#compile function saves lot of time
mat=re.findall(matches,s2)
print(mat)