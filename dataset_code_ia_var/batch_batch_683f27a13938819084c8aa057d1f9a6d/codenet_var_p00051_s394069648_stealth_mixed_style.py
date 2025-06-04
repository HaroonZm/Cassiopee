import sys
from functools import reduce

input = sys.stdin.readline
output = sys.stdout.write

def handler():
    s = input().strip()
    l = list(s)
    mx = ''.join(sorted(l, key=lambda c: -ord(c)))
    mn = reduce(lambda x, y: x + y, sorted(l))
    print(int(mx) - int(mn), file=sys.stdout)

for _ in range(int(sys.stdin.readline())):
    handler()