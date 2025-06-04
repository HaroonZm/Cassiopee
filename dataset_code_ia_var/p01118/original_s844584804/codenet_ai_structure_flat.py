import sys
import math

pi = 3.14159265358979323846264338

def pnum_eratosthenes(n):
    ptable = [0 for i in range(n+1)]
    plist = []
    for i in range(2, n+1):
        if ptable[i]==0:
            plist.append(i)
            for j in range(i+i, n+1, i):
                ptable[j] = 1
    return plist

def pnum_check(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for x in range(2,n):
            if n % x==0:
                return False
        return True

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return (a*b)//gcd(a,b)

def mat_mul(A, B):
    ans = []
    for a in A:
        c = 0
        for j, row in enumerate(a):
            c += row*B[j]
        ans.append(c)
    return ans

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def dist(A, B):
    d = 0
    for i in range(len(A)):
        d += (A[i]-B[i])**2            
    d = d**(1/2)
    return d

def abs_val(n):
    if n >= 0:
        return n
    else:
        return -n

def printA(A):
    N = len(A)
    for i, n in enumerate(A):
        print(n, end='')
        if i != N-1:
            print(' ', end='')
    print()

# main loop, everything flat below this
while True:
    line = input()
    if not line:
        continue
    H_W = line.split()
    if len(H_W) != 2:
        continue
    H, W = int(H_W[0]), int(H_W[1])
    if H==0 and W==0:
        break
    R = []
    for i in range(H):
        R.append(input())
    S = input()
    count = 0
    x = 0
    y = 0
    for s in S:
        found = False
        for i in range(len(R)):
            if found:
                break
            row = R[i]
            for j in range(len(row)):
                if s == row[j]:
                    count += abs_val(i-x)+abs_val(j-y)+1
                    x = i
                    y = j
                    found = True
                    break
    print(count)