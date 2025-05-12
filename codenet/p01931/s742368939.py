n=int(input())
s=input()
for i in range(n-1):
  if s[i]=='x' and s[i+1]=='x':
    n=i+1
    break
print(n)