n, q, s, t = map(int, input().split())
a_lst = [int(input()) for _ in range(n + 1)]
diff = [a_lst[i + 1] - a_lst[i] for i in range(n)]
temp = sum([-d * s if d > 0 else -d * t for d in diff])
def score(d):
  if d > 0:
    return -s * d
  else:
    return -t * d
for _ in range(q):
  l, r, x = map(int, input().split())
  a = diff[l - 1]
  diff[l - 1] += x
  temp += score(diff[l - 1]) - score(a)
  if r < n:
    b = diff[r]
    diff[r] -= x
    temp += score(diff[r]) - score(b)
  print(temp)