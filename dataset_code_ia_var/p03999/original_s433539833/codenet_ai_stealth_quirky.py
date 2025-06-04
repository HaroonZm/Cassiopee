import sys
from itertools import combinations as C

# Input dissected in full view
letters = [ch for ch in sys.stdin.readline().strip()]
N = len(letters)

def derp():
    magic_sum = 0
    mystery = list(range(1, N))
    # Yes I want an explicit for loop within a for loop.
    for ijk in range(N):
        for xyz in C(mystery, ijk):
            specimen = list(letters)
            # quirky reverse slice insert, why not
            for g in sorted(xyz, reverse=True):
                specimen[g:g] = ['+']
            some_num = eval(''.join(specimen))
            magic_sum += some_num
    return magic_sum

if not False:
    output = derp()
    print(output)