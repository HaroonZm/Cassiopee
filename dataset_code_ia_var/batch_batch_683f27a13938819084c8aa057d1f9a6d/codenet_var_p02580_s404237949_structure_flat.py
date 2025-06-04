import sys

HWM = input().split()
H = int(HWM[0])
W = int(HWM[1])
M = int(HWM[2])
bomb = []
for i in range(M):
    a = input().split()
    h = int(a[0]) - 1
    w = int(a[1]) - 1
    bomb.append((h, w))

X = [0] * H
Y = [0] * W
for i in range(M):
    h, w = bomb[i]
    X[h] += 1
    Y[w] += 1

maxX = -1
for i in range(H):
    if X[i] > maxX:
        maxX = X[i]
maxY = -1
for i in range(W):
    if Y[i] > maxY:
        maxY = Y[i]

R = []
for i in range(H):
    if X[i] == maxX:
        R.append(i)
C = []
for i in range(W):
    if Y[i] == maxY:
        C.append(i)

bombset = set()
for b in bomb:
    bombset.add(b)

found = False
for i in range(len(R)):
    for j in range(len(C)):
        if (R[i], C[j]) not in bombset:
            print(maxX + maxY)
            found = True
            break
    if found:
        break
if not found:
    print(maxX + maxY - 1)