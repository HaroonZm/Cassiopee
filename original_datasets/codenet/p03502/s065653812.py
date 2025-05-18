ss=input().strip()

n=int(ss)
nn=0

for s in ss:
  nn+=int(s)

print("Yes" if n%nn==0 else "No")