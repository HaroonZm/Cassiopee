a,b,c=map(int, input().split())
if c < a+b+2:
  ans = b+c
else:
  ans = b+a+b+1
print(ans)