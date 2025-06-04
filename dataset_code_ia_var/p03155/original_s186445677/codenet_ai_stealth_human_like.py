# imports... i might not need all of these but whatever, just in case ;)
import math
from collections import Counter, deque, defaultdict #eh, probably overkill but I'll leave it!
from heapq import * # I just like heapq ¯\_(ツ)_/¯
from bisect import * # why not
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement

# let's go!
n = int(input())
h = int(input())
w = int(input())

# hmm, this formula seems right? (n-h+1) * (n-w+1)
ans = (n-h+1)*(n-w+1)
print(ans)
# hope this works...