from collections import defaultdict
while True:
  n, m = map(int, input().split())
  if n == 0:break
  dic = defaultdict(int)
  for _ in range(n):
    d, v = map(int, input().split())
    dic[d] = max(dic[d], v)
  print(sum(dic.values()))