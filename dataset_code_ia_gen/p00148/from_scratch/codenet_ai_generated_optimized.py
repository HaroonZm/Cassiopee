import sys

for line in sys.stdin:
    a = line.strip()
    if not a:
        continue
    a = int(a)
    pos = a % 39
    if pos == 0:
        pos = 39
    print(f"3C{pos:02d}")