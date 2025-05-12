#!/usr/bin/env python
import numpy as np
X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = []
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
for i in range(min(K,X)):
    for j in range(min((K//(i+1),Y))):
        for k in range(min(((K//(i+1)+1)//(j+1)),Z)):
            D.append(A[i]+B[j]+C[k])
D.sort(reverse=True)
for i in range(K):
    print(int(D[i]))