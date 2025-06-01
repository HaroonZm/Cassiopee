import sys, math, os, fractions

PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

def water_bill(n):
    if n <= 10:
        return 4280 - 1150
    elif n <= 20:
        return 4280 - (1150 + (n - 10) * 125)
    elif n <= 30:
        return 4280 - (1150 + 1250 + (n - 20) * 140)
    else:
        return 4280 - (1150 + 1250 + 1400 + (n - 30) * 160)

while True:
    n = int(input())
    if n == -1:
        break
    print(water_bill(n))