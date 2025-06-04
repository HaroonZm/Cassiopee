import sys

d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

for line in sys.stdin:
    l = [d[i] for i in line.rstrip()]
    if len(l) == 1:
        print(l[0])
    else:
        s = sum(l)
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                s -= 2 * l[i]
        print(s)