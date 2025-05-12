import math
n,m =map(int,input().split())
 
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(int(n))
  return table
 
a =prime_decomposition(m)

def combination(n,r):
    r = min(r,n-r)
    result = 1
    for i in range(n-r+1,n+1):
        result *= i
    for i in range(1,r+1):
        result //= i
    return result

ans=1
count = 1
if not a:
  print(ans)
  exit()

for i in range(1,len(a)):
  if a[i-1]== a[i]:
    count +=1
  else:
    ans *= combination(count+n-1,count)
    ans %=1000000007
    count = 1
    
ans *= combination(count+n-1,count)
ans %=1000000007
print(ans)