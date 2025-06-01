import sys

rec = rhom = 0
for line in sys.stdin:
    a, b, c = map(int, line.split(','))
    rec += c*c == b*b + a*a
    rhom += a == b and a + b > c
print(rec, rhom, sep='\n')