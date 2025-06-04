import sys

rec = 0
rhom = 0

for s in sys.stdin:
    a, b, c = [int(x) for x in s.split(',')]
    if c ** 2 == b ** 2 + a ** 2:
        rec += 1
    elif a == b and a + b > c:
        rhom += 1

print(rec)
print(rhom)