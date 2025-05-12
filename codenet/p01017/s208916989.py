H, W = map(int, input().split())
a_mp = [list(map(int, input().split())) for _ in range(H)]
b_mp = [list(map(int, input().split())) for _ in range(H)]
h, w = map(int, input().split())
c_mp = [list(map(int, input().split())) for _ in range(h)]
INF = 10 ** 20

def check(x, y):
  ret = 0
  for dy in range(h):
    for dx in range(w):
      if b_mp[y + dy][x + dx] != c_mp[dy][dx]:
        return -INF
      ret += a_mp[y + dy][x + dx]
  return ret

ans = -INF
for y in range(H - h + 1):
  for x in range(W - w + 1):
    ans = max(ans, check(x, y))
if ans == -INF:
  print("NA")
else:
  print(ans)