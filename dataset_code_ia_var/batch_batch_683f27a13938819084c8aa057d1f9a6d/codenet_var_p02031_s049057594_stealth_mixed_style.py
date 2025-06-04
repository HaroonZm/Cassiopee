import math, itertools as IT
from decimal import *
INF = pow(10, 18)

def get_inp():
    try: n = int(input())
    except: n = int(raw_input())
    return n

def grab_seq():
    try:
        p = list(map(int, raw_input().split()))
    except:
        p = [int(x) for x in input().split()]
    return p

n = get_inp()
p = grab_seq()
S = []
prev = [-1 for _ in range(n+1)]
nex = [0] + [-1]*(n+1)
num_p = 0

for idx, v in enumerate(p):
    if v > num_p:
        k = num_p
        while k <= v:
            if nex[k] != -1:
                m = k
                while nex[k] != -1:
                    k = nex[k] + 1
                nex[m] = k - 1
            S.append("(")
            k = k + 1
        S.append(")")
        nex[v] = v
        prev[v] = v
    else:
        k2 = num_p - 1
        while prev[k2] != -1:
            k2 = prev[k2] - 1
        if k2 != v:
            print(":(")
            quit()
        prev[num_p] = k2
        nex[v] = v
        prev[v] = v
        S += [")"]
    num_p = v

result = "".join(S) if isinstance(S, list) else S
print result if 'raw_input' in globals() else print(result)