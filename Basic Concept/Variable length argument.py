def sum(*args):
    sum=0
    for num in args:
        sum+=num
    return sum

n=int(input("Enter a limit: "))

sii=0
for i in range(1,n+1):
        s=int(input("Enter a number: "))
        sii+=sum(s)

print(sii)