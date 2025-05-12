# 
import math
import sys
import itertools
import numpy as np

# いっこ入力
n =int(input())

k=0
for i in range(2,1000):
    a = i *(i-1) // 2
    if n == a:
        k = i
        break

if k >= 2:
    print("Yes")
else:
    print("No")
#    sys.exit()
if k >= 1:
    print(k)
    m = [[0]*(k-1) for ii in range(k)]

# print(m)
    t = 1
    for i in range(0,k):
        print(k-1, end=" ")
        for j in range(0,i):
            m[i][j]=m[j][i-1]
            print(m[i][j], end=" ")
        for j in range(i,k-1):
            m[i][j]=t
            t = t + 1
            print(m[i][j], end=" ")
        print("")

#print(m)