import sys

rect_count = 0
rhomb_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a, b, c = map(int, line.split(','))
    if a == b and c == a * 2:
        rhomb_count += 1
    elif c * c == a * a + b * b:
        rect_count += 1
    elif a == b:
        rhomb_count += 1

print(rect_count)
print(rhomb_count)