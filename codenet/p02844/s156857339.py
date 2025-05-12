input()
a, b, c = set(), set(), set()
for x in input():
  c.update(y + x for y in b)
  b.update(y + x for y in a)
  a.add(x)
print(len(c))