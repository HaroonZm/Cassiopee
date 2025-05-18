import math
# N, M, K = [int(_) for _ in input().split()]
N = int(input())

def num_divisors_table(n):
  table = [0] * (n + 1)

  for i in range(1, n + 1):
    for j in range(i, n + 1, i):
      table[j] += 1

  return table

cd_table = num_divisors_table(N)
ans = 0
for i in range(1, N+1):
  ans += i * cd_table[i]
print(ans)