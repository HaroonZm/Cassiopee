l = list(map(int, input().split()))
s = set()
for x in l:
    s.add(x)
c = 0
for _ in s:
    c += 1
print(c)