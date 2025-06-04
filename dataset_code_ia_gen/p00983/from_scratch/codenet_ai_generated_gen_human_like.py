import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

n, m = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# dp[i][j] = number of ways to assign first i documents with j in pile1 (and i-j in pile2)
# piles must be decreasing sequences from top to bottom, so we keep track of last inserted element in each pile
# but we cannot keep last element exactly because too large state
# Instead, we use the following approach:

# We proceed from top of the pile to bottom:
# when adding document s[i], we must put it on pile1 or pile2
# The stacks must be strictly decreasing from top to bottom so pushed order must be in decreasing order
# Because s_i are unique numbers 1 to n, we can keep the order constraints.

# We do DP with two pointers:
# But since we are only checking constraints, we can keep track of max elements put so far in each pile
# Actually, we can only track the minimal element on each pile (because the next element to be placed must be smaller than the top)
# But top elements are always the last placed

# To handle large constraints, we do the following:

# Since all documents 1..n appear once
# The piles must form decreasing stacks, so if we consider the order of appearance in s:
# The piles are sequences with decreasing numbers, preserving order assigned.

# We do DP over i, j = number of documents placed on pile1
# For dp[i][j], we know documents assigned to pile1 are s[..] with count j, pile2 count i-j
# We keep for pile1 and pile2 last inserted element values.

# To avoid high complexity, we use a DP with two arrays:
# For each length assigned to pile1 (j), we store the minimal last element of pile1 (top of pile1)
# and minimal last element of pile2

# To reduce complexity, we adopt this approach:

# We process documents from top to bottom (i=0 to n-1)
# At step i, we have a map from (last_pile1, last_pile2, count_pile1) -> ways

# Instead of storing last elements exactly, we store last elements for piles as the last inserted document serial number
# Because the stacks must be decreasing, adding a new document s[i]:
# We can put s[i] on pile1 if s[i] < last_pile1 (or last_pile1 is None if empty)
# Or on pile2 if s[i] < last_pile2 (or last_pile2 is None if empty)

# To implement efficiently, we can store dp as a dictionary keyed by (pile1_top, pile2_top, pile1_size)
# For each i, process dp from previous step, try put s[i] in pile1 or pile2 if possible and if pile sizes <= m

# However n=5000 is too large for this.

# Therefore, we note that since serial numbers are 1..n uniquely,
# We can transform problem:
# Assign each position either to pile1 or pile2 so that sequences on pile1 and pile2 are strictly decreasing (in the order assigned),
# and pile sizes <= m

# Because they must be strictly decreasing, the assigned subsequences are strictly decreasing subsequences of s in order.

# So we must count number of ways to split s into two strictly decreasing subsequences each of length <= m, covering all elements.

# This is known to be equivalent to counting the number of 2-colorings of s where both color classes are strictly decreasing sequences of length <= m.

# Counting the number of ways is complicated.

# We can instead transform the problem via the following method:

# In the operation after forming two piles, the order of extracted documents (comparing tops) must be sorted increasing from last to first because the two piles are decreasing sequences, with max on top.

# The condition for feasibility is that the document order can be split into two decreasing sequences each length not exceeding m.

# Because length of each pile <= m, and total length n.

# Now we can try a recursive backtracking with memo to count number of ways.

# Implement memoized recursive solution:

from functools import lru_cache

@lru_cache(None)
def dfs(i, top1, size1, top2, size2):
    # i: current index in s
    # top1: serial number of top doc in pile1 (or 0 if empty)
    # size1: size of pile1
    # top2: top doc in pile2 (or 0 if empty)
    # size2: size of pile2
    if i == n:
        return 1
    res = 0
    curr = s[i]
    # try put on pile1 if it maintains decreasing order and size limits
    if size1 < m and (top1 == 0 or curr < top1):
        res += dfs(i+1, curr, size1+1, top2, size2)
    # try put on pile2 if it maintains decreasing order and size limits
    if size2 < m and (top2 == 0 or curr < top2):
        res += dfs(i+1, top1, size1, curr, size2+1)
    return res % MOD

answer = dfs(0,0,0,0,0)
print(answer)