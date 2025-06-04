import os
import math

lst = [0,0,0,0,0,0]
n = int(input())
i = 0
while i < n:
    temp = float(input())
    if temp < 165:
        lst[0] += 1
    elif temp < 170:
        lst[1] += 1
    elif temp < 175:
        lst[2] += 1
    elif temp < 180:
        lst[3] += 1
    elif temp < 185:
        lst[4] += 1
    else:
        lst[5] += 1
    i += 1

i = 0
while i < 6:
    print("{}:".format(i+1), end="")
    j = 0
    while j < lst[i]:
        print("*", end = "")
        j += 1
    print()
    i += 1