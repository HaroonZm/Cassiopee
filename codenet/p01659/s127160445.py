n = input()
a = map(int, raw_input().split())
q = []
ans = 0
for i in a:
  while len(q) and q[-1] > i:
    q.pop()
  if (not len(q)) or q[-1] != i:
    ans += 1
    q.append(i)
print ans