import sys

r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for e in sys.stdin:
    a = 0
    n = [r[c] for c in e.strip()]
    for i in range(len(n)):
        if i + 1 < len(n) and n[i] < n[i + 1]:
            a -= n[i]
        else:
            a += n[i]
    print(a)