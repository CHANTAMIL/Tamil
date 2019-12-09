b=[int(x) for x in input().split()]
c=len(b)
e=(len(b))//2
d=b[0:e]
n=b[e:c]
x=d+n
print(sorted(x))
