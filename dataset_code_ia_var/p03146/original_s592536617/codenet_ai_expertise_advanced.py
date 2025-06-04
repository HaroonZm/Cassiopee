from itertools import count

def p(a): print(a)

s = int(input())
seen = {s}
x = s

for i in count(2):
    x = x // 2 if x % 2 == 0 else 3 * x + 1
    if x in seen:
        p(i)
        break
    seen.add(x)