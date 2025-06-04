import array
import bisect
import collections
import fractions
import heapq
import itertools
import math
import re
import string

n_k = input().strip().split()
n = int(n_k[0])
k = int(n_k[1])
if (n + 1) / 2 >= k:
    print('YES')
else:
    print('NO')