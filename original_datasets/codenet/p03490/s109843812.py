import sys

import numpy as np

s = raw_input()
x, y = [int(x) for x in raw_input().split(" ")]

s = s + "T"

a = []
b = []

cum_len = 0
turn = 0
for command in s:
    if command == "F":
        cum_len += 1
    elif command == "T":
        (a if turn == 0 else b).append(cum_len)
        turn ^= 1
        cum_len = 0

a0 = a.pop(0)

alpha = abs(x-a0)
beta = abs(y)

targetX = sum(a) - alpha
targetY = sum(b) - beta

def search(a, target):
    forwardTable = np.zeros((len(a), target+1))
    forwardTable[:,0] = 1
    for i_i in xrange(len(a)):
        new_item = a[i_i]
        if i_i == 0:
            forwardTable[i_i, 2*new_item:2*new_item+1] = 1
        else:
            forwardTable[i_i] += forwardTable[i_i-1]
            if new_item>0:
                forwardTable[i_i,2*new_item:] += forwardTable[i_i-1,:-2*new_item]
        if forwardTable[i_i,-1] > 0:
            forwardTable[-1,-1] = 1
            break

    return (forwardTable[-1,-1]>0)

if (targetX < 0) or (targetY < 0):
    print "No"
    sys.exit()
else:
    if (targetX > 0):
        if not search(a, targetX):
            print "No"
            sys.exit()
    if (targetY > 0):
        if not search(b, targetY):
            print "No"
            sys.exit()
    print "Yes"