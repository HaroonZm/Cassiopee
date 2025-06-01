import sys

rectangle_count = 0
rhombus_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a_str, b_str, c_str = line.split(',')
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)

    if a == b and c == a * 2:
        # This would imply an equilateral triangle, which is impossible here.
        # Ignore such case (not specified)
        pass 

    # Check if rhombus: all sides equal
    if a == b:
        rhombus_count += 1

    # Check if rectangle: sides not equal but right angles (diagonal satisfies Pythagoras)
    # For parallelogram with sides a,b and diagonal c: if c^2 == a^2 + b^2 => rectangle
    if (c * c) == (a * a + b * b) and a != b:
        rectangle_count += 1

print(rectangle_count)
print(rhombus_count)