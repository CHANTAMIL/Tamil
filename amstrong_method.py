def amstrong():
  d=len(n)
  l=0
  for i in range(d):
    j=int(n[i])
    l=l+(j**3)
  l=str(l)
  if(l==n):
    print("yes")
  else:
    print("no")
n=input()
amstrong()
