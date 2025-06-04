import itertools as ite
from decimal import *
import math

INF = 10 ** 18

n = input()
p = map(int, raw_input().split())
S = ""
prev = [-1] * (n + 1)
nex = [0] + [-1] * (n + 1)
num_p = 0

for num in p:
    if num > num_p:
        num_next = num_p
        while num_next <= num:
            if nex[num_next] != -1:
                id = num_next
                while nex[num_next] != -1:
                    num_next = nex[num_next] + 1
                nex[id] = num_next - 1
            S += "("
            num_next += 1
        S += ")"
        nex[num] = num
        prev[num] = num
    else:
        num_prev = num_p - 1
        while prev[num_prev] != -1:
            num_prev = prev[num_prev] - 1
        if num_prev != num:
            print ":("
            exit()
        prev[num_p] = num_prev
        nex[num] = num
        prev[num] = num
        S += ")"
    num_p = num

print S