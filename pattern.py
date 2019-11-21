N=int(input())
for i in range(0,N,1):
  for k in range(0,i+1):
    print("*",end=" ")
  print("\r")
for i in range(N,0,-1):
  s=i-1
  for k in range(0,i):
    print("*",end=" ")
  print()
  for j in range(0,N-s):
    print(" ",end=" ")
  

  
