# Your code here!

def gcd(x, y):
   if x < y:
      x, y = y, x
   if x % y == 0:
      return y
   else:
      return gcd(y, x % y)

n = int(input())
A = list(map(int, input().split()))

l = A[0]
for i in range(1, n):
   l = l * A[i] / gcd(l, A[i])
print(int(l))