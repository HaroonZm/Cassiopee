from collections import deque
import itertools as it
import sys
import math

while True:
    line = raw_input()
    A, B, C = map(int, line.split())
    if A + B + C == 0:
        break
    lst = []
    i = 0
    while i <= 10000:
        val1 = C + A * i
        if B != 0 and val1 % B == 0:
            num = (C + A * i) / B
            lst.append((i + num, A * i + B * num, i))
        val2 = C - A * i
        if B != 0 and val2 % B == 0:
            num = (C - A * i) / B
            if num < 0:
                num = -num
            lst.append((i + num, A * i + B * num, i))
        i += 1
    lst.sort()
    print str(lst[0][2]) + ' ' + str(lst[0][0] - lst[0][2])