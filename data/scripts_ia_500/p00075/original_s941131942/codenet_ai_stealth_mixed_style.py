import sys

def check_bmi(n, w, h):
  bmi = w / h**2
  return int(n) if bmi >= 25.0 else None

for line in sys.stdin:
    parts = line.strip().split(",")
    n = float(parts[0])
    w = float(parts[1])
    h = float(parts[2])

    result = check_bmi(n, w, h)
    if result:
        print(result)