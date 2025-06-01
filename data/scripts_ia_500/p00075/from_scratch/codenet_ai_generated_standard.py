import sys

for line in sys.stdin:
    if not line.strip():
        continue
    s, w, h = line.strip().split(',')
    bmi = float(w) / (float(h) ** 2)
    if bmi >= 25:
        print(s)