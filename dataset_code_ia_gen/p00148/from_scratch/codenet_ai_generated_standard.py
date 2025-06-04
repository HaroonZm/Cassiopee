import sys

for line in sys.stdin:
    if not line.strip():
        continue
    a = int(line.strip())
    n = (a - 1) % 39 + 1
    print(f"3C{n:02d}")