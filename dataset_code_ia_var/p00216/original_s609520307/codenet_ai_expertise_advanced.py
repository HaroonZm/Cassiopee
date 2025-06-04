import sys
import os

if os.environ.get('PYDEV') == "True":
    sys.stdin = open("sample-input.txt")

def water_bill(n):
    brackets = [
        (10, 1150, 125),
        (20, 1250, 140),
        (30, 1400, 160)
    ]
    base = 4280
    if n <= 10:
        return base - brackets[0][1]
    elif n <= 20:
        return base - (brackets[0][1] + (n - 10) * brackets[0][2])
    elif n <= 30:
        return base - (brackets[0][1] + brackets[1][1] + (n - 20) * brackets[1][2])
    else:
        return base - (brackets[0][1] + brackets[1][1] + brackets[2][1] + (n - 30) * brackets[2][2])

for line in sys.stdin:
    n = int(line)
    if n == -1:
        break
    print(water_bill(n))