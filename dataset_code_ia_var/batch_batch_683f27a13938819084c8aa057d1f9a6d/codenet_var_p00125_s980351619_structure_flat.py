import sys
from datetime import date

while True:
    try:
        line = input()
    except EOFError:
        break
    if not line.strip():
        continue
    tokens = line.split()
    if len(tokens) != 6:
        break
    try:
        y1 = int(tokens[0])
        m1 = int(tokens[1])
        d1 = int(tokens[2])
        y2 = int(tokens[3])
        m2 = int(tokens[4])
        d2 = int(tokens[5])
        date1 = date(y1, m1, d1)
        date2 = date(y2, m2, d2)
        delta = date2 - date1
        print(delta.days)
    except Exception:
        break