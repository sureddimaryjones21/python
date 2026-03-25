a=[1,2,3,4,5,6,7,8,9,10]
g=(i for i in a if i%2==0)
for i in g:
  print(i)
s=(i*i for i in a)
for i in s:
  print(i)
n=7
m=(i*n for i in a)
for i in m:
  print(i)  