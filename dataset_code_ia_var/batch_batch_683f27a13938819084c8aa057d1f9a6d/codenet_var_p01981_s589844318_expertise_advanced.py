from sys import stdin

from itertools import islice

def parse_lines():
    for line in stdin:
        if not line.strip():
            break
        try:
            g, y, m, d = line.split()
            yield [g, int(y), int(m), int(d)]
        except ValueError:
            break

entries = [list(rec) for rec in parse_lines()]

for entry in entries:
    if entry[1] > 31:
        entry[0] = "?"
        entry[1] -= 30
    elif entry[1] == 31 and entry[2] >= 5:
        entry[0] = "?"
        entry[1] -= 30

for g, y, m, d in entries:
    print(f"{g} {y} {m} {d}")