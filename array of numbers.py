b=[7,3,4]
for i in range(len(b)):
  for j in range(i+1,len(b)):
    if b[i]>b[j]:
      b[i],b[j]=b[j],b[i]
print(b)
