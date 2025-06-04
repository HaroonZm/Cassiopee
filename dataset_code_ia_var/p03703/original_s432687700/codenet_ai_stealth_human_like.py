import itertools
import os
import sys

# Setup for local input. Might not always be needed...
if os.environ.get("LOCAL"):
    sys.stdin = open("_in.txt")

# Python's default recursion is way too shallow sometimes.
sys.setrecursionlimit(10**8 + 999)
INF = float('inf')

class BinaryIndexedTree:
    # Somewhat standard BIT, nothing too fancy
    def __init__(self, n):
        self.n = n
        self.bit = [0] * n  # maybe should have used n+1 for easier indexing...

    def add(self, idx, val):
        x = idx + 1
        while x <= self.n:
            self.bit[x-1] += val # -1 offset is annoying but whatever
            x += x & -x

    def sum(self, i):
        # Sums value from 0 to i (inclusive)
        res = 0
        x = i + 1
        while x > 0:
            res += self.bit[x-1]
            x -= x & -x
        return res
    
    def __len__(self):
        return self.n

# Input reading
N_K = sys.stdin.readline().split()
N = int(N_K[0])
K = int(N_K[1])
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
# Off-by-one corrections... kinda annoying!
N += 1

# Build cumulative sums. But the first value should be 0, right?
acc = [0] + [a - K for a in A]
D = list(itertools.accumulate(acc))
# Some explanations: D[l-1] <= D[r] (with l <= r) means avg >= K

def compress(arr):
    # Coordinate compression, seen everywhere in competitive programming
    zipped = [(v, i) for i, v in enumerate(arr)]
    zipped.sort()
    res = [0]*len(arr)
    last = None
    idx = 0
    for val, orig in zipped:
        if val != last:
            idx += 1
        res[orig] = idx
        last = val
    return res

def count(arr):
    # Counts how many pairs (L, r) such that arr[L-1] <= arr[r]
    # Not 100% sure about the variable names here
    ranks = compress(arr)
    bit = BinaryIndexedTree(max(ranks)+1)
    ans = 0
    for i, r in enumerate(ranks):
        ans += bit.sum(r)
        bit.add(r, 1)
    return ans

print(count(D))
# Not the most elegant structure, but does the job for now!