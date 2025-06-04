from decimal import Decimal

x1, y1 = map(str, input().split())
x2, y2 = map(str, input().split())
x3, y3 = map(str, input().split())

x1, y1 = Decimal(x1), Decimal(y1)
x2, y2 = Decimal(x2), Decimal(y2)
x3, y3 = Decimal(x3), Decimal(y3)

a = ((x1 - x2) ** Decimal('2') + (y1 - y2) ** Decimal('2')) ** Decimal('0.5')
b = ((x3 - x2) ** Decimal('2') + (y3 - y2) ** Decimal('2')) ** Decimal('0.5')
c = ((x1 - x3) ** Decimal('2') + (y1 - y3) ** Decimal('2')) ** Decimal('0.5')
s = (a + b + c) / Decimal('2')

r = a * b * c / (((s * (s - a) * (s - b) * (s - c)) ** Decimal('0.5')) * Decimal('4'))

xa, ya = (x1 + x2) / 2, (y1 + y2) / 2
xb, yb = (x3 + x2) / 2, (y3 + y2) / 2

if (y3 - y2) != 0 and (y2 - y1) != 0:
    a1 = -(x3 - x2) / (y3 - y2)
    b1 = ((x3 - x2) * xb + (y3 - y2) * yb) / (y3 - y2)
    a2 = -(x2 - x1) / (y2 - y1)
    b2 = ((x2 - x1) * xa + (y2 - y1) * ya) / (y2 - y1)
    cx = (b2 - b1) / (a1 - a2)
    cy = a1 * cx + b1

if (y3 - y2) == 0:
    cx = xb
    a2 = -(x2 - x1) / (y2 - y1)
    b2 = ((x2 - x1) * xa + (y2 - y1) * ya) / (y2 - y1)
    cy = a2 * cx + b2

if (y2 - y1) == 0:
    cx = xa
    a1 = -(x3 - x2) / (y3 - y2)
    b1 = ((x3 - x2) * xb + (y3 - y2) * yb) / (y3 - y2)
    cy = a1 * cx + b1

print(cx, cy, r)