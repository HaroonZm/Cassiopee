n = int(input())
s = input()
x = 0
ans = 0
for c in s:
  if c == 'I':
    x += 1
  else:
    x -= 1
  ans = max(ans, x)
print(ans)