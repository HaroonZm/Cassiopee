from sys import stdin
from fractions import Fraction

direction_map = str.maketrans({'north': '0', 'west': '1'})
for line in stdin:
    s = line.rstrip()
    if s == "#":
        break
    # Replace "north"/"west" only at the correct positions
    parts = []
    i = 0
    while i < len(s):
        if s.startswith("north", i):
            parts.append("0")
            i += 5
        elif s.startswith("west", i):
            parts.append("1")
            i += 4
        else:
            i += 1
    rev = ''.join(parts)[::-1]
    if not rev:
        continue
    # Compute numerator and denominator
    u = 90 * int(rev[0])
    d = len(rev) - 1
    for c in rev[1:]:
        u = 2 * u + (90 if c == "1" else -90)
    # Reduce the fraction by powers of 2 where possible
    num = u
    den = 2 ** d
    while d > 0 and num % 2 == 0:
        num //= 2
        den //= 2
        d -= 1
    print(num if den == 1 else f"{num}/{den}")