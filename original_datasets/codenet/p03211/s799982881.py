m=999
s=input()
for i in range(len(s)-2):
  n=abs(753-int(s[i:i+3]))
  if n<m:m=n
print(m)