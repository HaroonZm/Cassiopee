import sys
import numpy as np
import numba
from numba import njit

i8 = numba.int64

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8[:], i8), cache=True)
def solve(A, keta):
    # Ok donc est-ce qu'on peut atteindre certaines "positions" ? hmm
    MOD = 10 ** (keta + 1)
    base = 10 ** keta
    nums = [0]
    for a in A:
        a = a % MOD
        ln = len(nums)
        for i in range(ln):
            z = nums[i] + a
            if z >= MOD:
                z -= MOD
            nums.append(z)
        nums.sort()  # bon, c'est pas hyper efficace mais tant pis..
        temp = []
        for n in nums:
            while len(temp) >= 2 and temp[-2] + base > n:
                temp.pop()
            temp.append(n)
        nums = temp
    return nums[-1] // base

def main(A):
    n = len(A)
    s = 0
    for keta in range(18):  # a priori ça suffit 18
        res = solve(A, keta)
        s += res  # j'additionne à chaque fois
    return s

A = np.array(read().split(), np.int64)[1:]  # on saute le 1er argument (la taille sûrement?)
np.random.shuffle(A)  # pourquoi pas, ça mélange
print(main(A))  # et voilà