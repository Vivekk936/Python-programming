import re
s=input()
pat=r"(?<=[^AEIOUaeiou])[AEIOUaeiou]{2,}(?=[^AEIOUaeiou])"
mat=re.findall(pat,s)
if mat:
    print("\n".join(mat))
else:
    print(-1)