S = input().strip()
ans = ''
for c in S:
  if c == 'B':
    if len(ans) > 0:
      ans = ans[:-1]
  else:
    ans += c
print(ans)