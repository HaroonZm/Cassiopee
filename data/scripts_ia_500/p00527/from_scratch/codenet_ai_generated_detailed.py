# IOI Train problem solution in Python
# Goal: Find the maximum length of a valid train composed from two depots S and T according to given rules.

# Approach:
# 1. We have two strings S and T representing depots with cars in order.
# 2. We can, before assembling the train, discard any prefix from either depot (move to waiting track).
# 3. Then, we build a train by alternating cars from S and T starting with 'I' at the front and end, with cars alternating in type (I,O,I,O,...).
# 4. We want the longest possible train, made by some subsequence starting from some positions s_i and t_j in depots S and T.
#
# Key observations:
# - Train must start and end with 'I'.
# - Cars alternate 'I' and 'O'.
# - We can pick cars from either depot at each step, but only the front (current index) of each depot is available.
# - Once assembly starts, no discarding is allowed.
#
# Since picking cars can be from either depot in any order, we want to interleave subsequences from S and T preserving their order.
#
# We use Dynamic Programming:
# Define a DP state:
# dp[i][j][c] = length of longest train formed using suffixes S[i:], T[j:], with the next required car type c ('I' or 'O').
#
# Because the train alternates, if next required car is 'I', after picking it next required will be 'O,' and vice versa.
#
# At each step, we can pick the next car from S[i] if it matches c, or from T[j] if it matches c.
# Also, since the train needs to start and end with 'I', we will consider only trains starting with 'I'.
#
# We'll also handle starting the train from both depots.
#
# Finally, we find the maximum dp value with c='I' starting at some indices.
#
# To optimize memory and speed, we use memoization with recursion.

import sys
sys.setrecursionlimit(10**7)

M, N = map(int, sys.stdin.readline().split())
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

from functools import lru_cache

# Convert characters to booleans for quick alternation check: I=0, O=1
def char_to_bool(c):
    return 0 if c == 'I' else 1

s_arr = [char_to_bool(c) for c in S]
t_arr = [char_to_bool(c) for c in T]

@lru_cache(None)
def dfs(i, j, need):
    # need: 0 for 'I', 1 for 'O'
    # Returns max train length from S[i:], T[j:] needing next car 'I'/'O'
    res = 0
    
    # Try to pick from S if possible
    if i < M and s_arr[i] == need:
        # After picking this car, next need flips (0<->1)
        res = max(res, 1 + dfs(i+1, j, 1 - need))
    # Try to pick from T if possible
    if j < N and t_arr[j] == need:
        res = max(res, 1 + dfs(i, j+1, 1 - need))
    return res

max_len = 0

# According to problem, both ends of train must be 'I'
# So trains length must be odd >= 1 (since odd length sequences alternate starting and ending on 'I')

# Our dp returns length of sequences starting from need car, so let's try all start positions
for i in range(M+1):
    for j in range(N+1):
        # Start assembling train from (i,j) needing 'I' first
        length = dfs(i,j,0)
        # Length must be odd (start and end with 'I')
        # If length is even, discard last car to keep ends 'I'
        if length % 2 == 0:
            length -= 1
        if length > max_len:
            max_len = length

print(max_len)