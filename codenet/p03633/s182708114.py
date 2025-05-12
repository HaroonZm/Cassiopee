def gcd(a, b):
  if (b == 0): 
    return a
  return gcd(b, a % b)

arr = [int(input()) for i in range(int(input()))]
ans = 1
for i in arr:
  ans = (ans*i)//gcd(ans, i)
print(ans)