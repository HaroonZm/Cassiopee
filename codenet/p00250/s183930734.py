from bisect import bisect_left as bl

while True:
  n, m = map(int, input().split())
  if n == 0:
    break
  klst = list(map(int, input().split()))
  cum = []
  acc = 0
  for k in klst:
    acc += k
    acc %= m
    cum.append(acc)
  
  use = [0]
  use_len = 1
  ans = 0
  for k in cum:
    ind = bl(use, k + 1)
    if ind < use_len:
      ans = max(ans, (k - use[ind]) % m)
    ans = max(ans, k)
    use.insert(bl(use, k), k)
    use_len += 1
  print(ans)