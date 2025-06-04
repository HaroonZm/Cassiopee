import sys

value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    total = 0
    prev = 0
    for c in reversed(s):
        curr = value[c]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    print(total)