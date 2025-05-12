import sys
f = sys.stdin

import operator
while True:
    a = sum(map(int, f.readline().split()))
    if a == 0:
        break
    abcde = [a] + [sum(map(int, f.readline().split())) for i in range(4)]
    print(*max(zip('ABCDE', abcde), key=operator.itemgetter(1)))