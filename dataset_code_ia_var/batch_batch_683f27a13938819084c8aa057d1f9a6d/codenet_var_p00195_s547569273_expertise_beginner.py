import sys

for line in sys.stdin:
    am, pm = map(int, line.strip().split())
    if am == 0 and pm == 0:
        break
    totals = []
    totals.append(am + pm)
    for i in range(4):
        am, pm = map(int, sys.stdin.readline().strip().split())
        totals.append(am + pm)
    highest = max(totals)
    shop_index = totals.index(highest)
    print(chr(ord('A') + shop_index), highest)