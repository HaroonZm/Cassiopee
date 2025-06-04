import sys
import itertools
import math
N, M = input().split()
N = int(N)
M = int(M)
i = 0
ID_list = []
ID_sublist = []
gate_possible_list = []
N_dummy = 0
M_dummy = 0
C_dummy = 0
i = 0
k = 0
s = 0
print((1900 * M + 100 * (N - M)) * 2 ** M)