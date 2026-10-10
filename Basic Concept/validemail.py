import re
with open("test.txt","rt") as f:
    data=f.read()

pat=r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]+\b"
matches=re.finditer(pat,data)

for match in matches:
    print(match)