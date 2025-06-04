from sys import exit
from collections import deque

As = input()
As1 = []
for A in As: As1.append(ord(A)-ord('a'))
length = len(As1)
pos = [length]*26
PosNext = list(map(list, [[length]*26]*(length+1)))
z = range(length-1, -1, -1)
for i in z:
    PosNext[i+1] = pos[:]
    pos[As1[i]] = i
PosNext[0] = pos[:]
Prev = [None for _ in ('_'*length)]
queue = deque()
queue.append((0, -1))
while len(queue):
    t = queue.popleft()
    sz, idx = t
    for c in range(26):
        npos = PosNext[idx+1][c]
        if npos == length:
            aa = []
            aa.append(chr(ord('a')+c))
            while idx != -1:
                aa.append(chr(ord('a')+As1[idx]))
                idx = Prev[idx]
            print("".join(aa[::-1]))
            exit()
        if Prev[npos] is None:
            Prev[npos] = idx
            queue.append((sz+1, npos))