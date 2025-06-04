import sys

for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    parts = line.split(",")
    s = int(parts[0])
    w = float(parts[1])
    h = float(parts[2])
    bmi = w / (h * h)
    if bmi >= 25:
        print(s)