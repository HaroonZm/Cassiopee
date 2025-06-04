import sys

rectangles = 0
rhombuses = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a, b, c = map(int, line.split(','))
    a2 = a * a
    b2 = b * b
    c2 = c * c
    # For a parallelogram with sides a, b and diagonal c:
    # c^2 = a^2 + b^2 - 2ab*cos(theta)
    # Rectangle => theta = 90° => c^2 = a^2 + b^2
    if c2 == a2 + b2:
        rectangles += 1
    # Rhombus => a == b and diagonal length corresponds to a rhombus diagonal length
    # diagonals in rhombus: d1^2 + d2^2 = 4a^2
    # given only one diagonal c, and sides a,b, with a == b
    # so c < 2a, and c > 0, also given a+b>c always, so check if a == b and c < 2a
    # The problem sample input suggests counting cases where a==b but c2 != a2+b2 as rhombus.
    elif a == b:
        rhombuses += 1

print(rectangles)
print(rhombuses)