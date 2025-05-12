import sys
sys.setrecursionlimit(1000000)
memo = {0:1}
def fact(num):
  if num in memo:return memo[num]
  memo[num] = num * fact(num - 1)
  return memo[num]
n = int(input())
print(fact(n + 1) + 2)
for i in range(n):
  print(i + 2)