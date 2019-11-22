n=int(input())
m=1
for i in range(0,n):
  for j in range(0,m+n):
    print(end=" ")
  m=m-1
  for j in range(0,i,1):
    if  i%2!=0:
      print("*",end=" ")
  print(" ")
for k in range(n,0,-1):
  for l in range(0,m+n):
    print(end=" ")
  m=m+1
  for l in range(0,k):
    if  k%2!=0:
      print("*",end=" ")
  print(" ")
