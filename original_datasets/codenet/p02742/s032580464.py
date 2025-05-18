import sys
h, w = map(int, input().split())
if h == 1 or w == 1:
  print(1)
  sys.exit()
ans = h//2*w
if h%2 != 0:
  if w%2 != 0:
    ans += w//2+1
  else:
    ans += w/2
print(int(ans))