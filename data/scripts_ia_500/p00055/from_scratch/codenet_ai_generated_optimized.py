import sys

for line in sys.stdin:
    a = float(line.strip())
    s = a
    prev = a
    for i in range(2, 11):
        if i % 2 == 0:
            curr = prev * 2
        else:
            curr = prev / 3
        s += curr
        prev = curr
    print(s)