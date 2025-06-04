import sys
from collections import Counter

def freq_operation(seq):
    count = Counter(seq)
    return [count[x] for x in seq]

for line in sys.stdin:
    n = line.strip()
    if n == '0':
        break
    n = int(n)
    s = list(map(int, sys.stdin.readline().split()))
    steps = 0
    while True:
        c = freq_operation(s)
        steps += 1
        if c == s:
            print(steps-1)
            print(*s)
            break
        s = c