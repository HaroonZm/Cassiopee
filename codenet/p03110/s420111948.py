N = int(raw_input())
otoshidama = [raw_input().split() for _ in range(N)]
ans = 0.
for o in otoshidama:
  if o[1] == "JPY":
    ans += float(o[0])
  else:
    ans += float(o[0]) *380000.0
print ans