s = raw_input()
ans = 0
for i in range(len(s)):
  if s[i] == "0" and i != len(s) - 1:
    continue

  left  = int(s[:i]) if i else 0
  right = int(s[i:])

  if left <= right and left % 2 == right % 2:
    ans += 1
print ans