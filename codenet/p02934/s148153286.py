n=int(input())
a=[int(x) for x in input().split()]
c=0
for i in range(n):
  c+=a[i]**(-1)
print(c**(-1))