from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect

def array2d(d1, d2, init = None):
    return [[init for _ in range(d2)] for _ in range(d1)]

s = input().strip()
c = "CODEFESTIVAL2016"
cnt = 0
for i in range(len(c)):
    if s[i] != c[i]: cnt += 1
print(cnt)