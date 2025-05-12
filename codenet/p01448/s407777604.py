from itertools import accumulate
n = int(input())
lst = [0] * 100002
for _ in range(n):
  a, b = map(int, input().split())
  lst[a - 1] += 1
  lst[b] -= 1
lst = list(accumulate(lst))
for i in range(n, -1, -1):
  if i <= lst[i]:
    print(i)
    break