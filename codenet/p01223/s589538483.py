t = int(input())
for _ in range(t):
  n = int(input())
  lst = list(map(int, input().split()))
  M = m = 0
  for i in range(n - 1):
    M = max(lst[i + 1] - lst[i], M)
    m = min(lst[i + 1] - lst[i], m)
  print(M, -m)