from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

N = input()

m = {}

for loop in range(N):
    s, p1, p2 = raw_input().split()
    m[s] = (int(p1), int(p2))

N = input()
lst = raw_input().replace('/', '//').split()
sta = []

for s in lst:
    hoge = [0 for i in range(256)]
    if s in m:
        p = m[s]
        for i in range(p[0], p[1] + 1):
            hoge[i] = 1
        sta.append(hoge)
    elif s in ['+', '-', '*', '//']:
        n2 = sta.pop()
        n1 = sta.pop()
        for i in xrange(256):
            for j in xrange(256):
                if n1[i] and n2[j]:
                    try:
                        index = eval(str(i) + s + str(j))
                        hoge[index % 256] = 1
                    except:
                        print "error"
                        exit()
        sta.append(hoge)
    else:
        hoge[int(s)] = 1
        sta.append(hoge)

print "correct"