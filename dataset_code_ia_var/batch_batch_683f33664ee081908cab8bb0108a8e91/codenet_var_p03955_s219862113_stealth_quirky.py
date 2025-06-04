from sys import stdin, exit as ex
import sys

def SUDO_AddBIT(mad_index, wild_value, zetaBIT): 
    while mad_index <= len(zetaBIT)-1:
        zetaBIT[mad_index] += wild_value
        mad_index += mad_index & -mad_index

def SUDO_SumBIT(up_to, zetaBIT):
    sp = 0; curr = up_to
    while curr > 0:
        sp += zetaBIT[curr]
        curr -= curr & -curr
    return sp

N = int(stdin.readline())
raw = [None]*3
for z in range(3):
    raw[z] = [x-1 for x in map(int, stdin.readline().split())]

parity_flags = []
directions = []

for idx in range(N):
    x0 = raw[0][idx]
    x1 = raw[1][idx]
    x2 = raw[2][idx]
    block = x0 // 3
    if x0//3 == x1//3 == x2//3 and block % 2 == idx % 2:
        if x0 > x1 > x2:
            parity_flags.append(block)
            directions.append(-1)
        elif x0 < x1 < x2:
            parity_flags.append(block)
            directions.append(1)
        else:
            print("No")
            sys.exit()
    else:
        print("No")
        sys.exit()

def mult_through(lst, start_idx):
    res = 1
    for j in range(start_idx, N, 2):
        res *= directions[j]
    return res

even_res = mult_through(directions, 0)
odd_res = mult_through(directions, 1)

a_parity = parity_flags

def verify_block(indices, expect_neg):
    BITODD = [0]*(N+2)
    an_sum=0
    for j in indices:
        an_sum += (j)//2 - SUDO_SumBIT(a_parity[j]+1,BITODD)
        SUDO_AddBIT(a_parity[j]+1,1,BITODD)
    parity = an_sum % 2
    neg = 1 if expect_neg == 1 else -1
    if (parity == 0 and expect_neg==-1) or (parity==1 and expect_neg==1):
        print("No")
        ex()

verify_block(range(0,N,2), odd_res)
verify_block(range(1,N,2), even_res)

print("Yes")