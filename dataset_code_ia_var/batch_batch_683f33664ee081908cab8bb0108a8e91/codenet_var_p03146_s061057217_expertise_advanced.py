from array import array
from sys import stdin

s = int(stdin.readline())
m = array('b', (0,)) * 10**7
m[s] = 1
a = 1

while True:
    a += 1
    s = s // 2 if s % 2 == 0 else 3 * s + 1
    if m[s]:
        print(a)
        break
    m[s] = 1