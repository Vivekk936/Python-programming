t=input()
while t:
    t-=1
    n=input()
    a=map(int,raw_input().strip().split(' '))
    for i in xrange(len(a)-1):
        if a[i]<a[i+1]:
            break
    for j in xrange(len(a)-1,0,-1):
        if a[j]<a[j-1]:
            break
    if a[i]==a[j] or sorted(a)==a or sorted(a,reverse=True)==a:
        print ("Yes")
    else:
         print ("No")