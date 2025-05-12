from itertools import accumulate
MAX = 1000000
is_prime = [1] * MAX
is_prime[0] = is_prime[1] = 0
for i in range(2, int(MAX ** (1 / 2)) + 1):
  if is_prime[i]:
    for j in range(i * i, MAX, i):
      is_prime[j] = 0
acc_prime = list(accumulate(is_prime))

while True:
  n = int(input())
  if n == 0:
    break
  ans = 0
  for _ in range(n):
    p, m = map(int, input().split())
    ans += acc_prime[min(p + m, MAX - 1)] - acc_prime[max(0, p - m - 1)] - 1
  print(ans)