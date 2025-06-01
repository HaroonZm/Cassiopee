import sys
from sys import stdin
input = stdin.readline

# AOJ 1030 Cubes Without Holes
# Okay, trying to get the count of cubes without holes here, n up to 500

while True:
    n, h = map(int, input().split())
    if n == 0:
        break
    blocked = []
    for _ in range(h):
        c, a_str, b_str = input().split()
        a = int(a_str) - 1  # zero-based index
        b = int(b_str) - 1
        if c == "xy":
            # covering all z at given x=a, y=b
            blocked.extend([a + (b << 9) + (z << 18) for z in range(n)])
        elif c == "xz":
            # covering all y at x=a, z=b
            blocked.extend([a + (y << 9) + (b << 18) for y in range(n)])
        else:
            # covering all x at y=a, z=b
            blocked.extend([x + (a << 9) + (b << 18) for x in range(n)])
    # Convert to set to remove duplicates, then subtract from total cubes
    print(n**3 - len(set(blocked)))