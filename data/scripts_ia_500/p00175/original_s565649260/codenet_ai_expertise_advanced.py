import sys

sys.setrecursionlimit(10**5)
POW = [4**i for i in range(10)]

while (num := int(input())) != -1:
    if num == 0:
        print(0)
        continue

    digits = []
    for p in reversed(POW):
        q, num = divmod(num, p)
        digits.append(str(q) if digits or q else '')
    print(''.join(filter(None, digits)))