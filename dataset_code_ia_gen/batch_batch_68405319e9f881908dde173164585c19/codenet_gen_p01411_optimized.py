import sys
sys.setrecursionlimit(10**7)
H,N,P,M,K=map(int,sys.stdin.readline().split())
used=[False]*(H+1)
pos=[-1]*(H+1)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    used[a]=True
    pos[a]=b
avail=[]
for h in range(1,H+1):
    if not used[h]:
        avail.append(h)
# dp[k][v]: from stick v at top, probability to land on P after adding k bars
dp=[[0]*(N+2) for _ in range(K+1)]
dp[0][P]=1.0
for k in range(1,K+1):
    ndp=[0]*(N+2)
    ways=len(avail)-k+1
    for v in range(1,N+1):
        val=dp[k-1][v]
        if val==0:
            continue
        # for each possible position to place bar
        p=0
        for i in range(len(avail)):
            if i<k-1:
                continue
            if i==k-1:
                a=avail[i]
                b=pos[a]
                # b may be -1, but we add bar there anyway
                for x in range(1,N+1):
                    ndp[x]+=0
                # Actually here we simulate all placements equally
                # But this is complex
                # Instead, use a reverse approach
        # Since simulating all placements is complex, use expected transition
    # The above approach is complicated, let's model the whole ladder
# Alternative: Precompute next array after each possible horizontal bar added
# So we consider all ways to choose K positions among available positions
# But this is too large
# Instead, use DP: f(k,v): probability that after adding k bars randomly, starting from v at top, ends at P
# The key is that adding bars randomly at randomly chosen positions, the transition matrix is averaged
# Precompute base 'next' array after initial M bars
next_pos=[i for i in range(N+2)]
for h in range(1,H+1):
    if used[h]:
        b=pos[h]
        next_pos[b],next_pos[b+1]=next_pos[b+1],next_pos[b]
# For each free position, possible to add bar connecting some b,b+1
# For each free position, determine which b can be placed (only one b per position)
# Create a list of transitions for each free position
free_trans=[]
for h in avail:
    # at height h, can place bar between b,b+1; b unknown
    # but per problem b is position where to add bar. Here, it can be any in 1..N-1 except forbidden
    # Because no bars at that height, can add any bar between 1 and N-1, with condition no two bars at same height
    # But problem states: horizontal bar connect adjacent sticks; at each height can add exactly one bar at free height
    # So at free height h, the only possible bar to add is between b,b+1; b unknown, but per problem only one bar per height
    # Within the problem, the friend can add a horizontal bar at any free height h, and that's it
    # So the problem reduces to: at that height h, friend can add any bar between b,b+1 with b unknown, but from problem statement it's only one bar per height
    # Actually b is fixed in input, so friend can only add bar as per problem condition: "横棒を追加しても上で指定された条件を満たすような場所のうち1箇所を無作為に選ぶ"
    # So the "places" to add bar correspond exactly to free heights h, places to add a bar at height h connecting two adjacent sticks
    # But which two sticks? The problem statement and sample input suggest only one bar can be added at that height connecting b,b+1 sticks
    # Meaning each free height h corresponds to one possible bar between some b,b+1 adjacent sticks
    # Need to check if input clarifies this
    # Based on problem statement, seems that each horizontal bar connects adjacent sticks; new bars can be placed at free heights
    # So per free height, can add bar connecting any pair of adjacent sticks without creating conflict (no two bars at same height, bars do not cross)
    # But problem statement says we must satisfy conditions and pick one of possible positions uniformly
    # So at each free height, the bar to add is fixed position (height h connects b,b+1 as per problem)
    # Wait, but problem only gives M bars with a_i,b_i, no extra info about which bars can be added at free heights
    # Meaning the new bars can only be added at free heights h, and only connecting sticks b,b+1 with no conflict (must be adjacent sticks)
    # But which b is allowed? Any b in 1 to N-1 with no conflict with existing bars? But no explicit restriction
    # From problem statement: "横棒を追加しても上で指定された条件を満たすような場所のうち 1 箇所を無作為に選ぶ"
    # So the possible places are all possible heights h (from 1 to H) with no bar yet and pair b,b+1 with no conflict
    # But since bars cannot share adjacent sticks at the same height (only one bar per height), so for each free height, possible to add one bar between any b,b+1 provided it does not conflict with bars at adjacent heights at same b or b+1
    # Since problem given only M bars with positions, and user provides no locations for new bars, we assume at free heights, bar can be added with any b satisfying no overlapping horizontal bars (the problem doesn't mention that bars can't cross vertically; only no bar at same height)
    # But likely problem restricts that at height h, only allowed to add bar with index b to be in 1..N-1 and must not conflict adjacent bars at the same height h
    # Problem likely says "横棒を追加しても上で指定された条件を満たすような場所", i.e. locations where bars can be added (height h + b), summing to M+K ≤ H
    # Hence, the M+K bars are fixed at different heights (no two bars at same height)
    # So at free height h, only one possible way to add a bar, at position (h,b) with b unknown
    # But problem states one bar per height
    # Sample input hints that each bar is at a certain height between b,b+1 sticks
    # So we can deduce that at free heights, the only position to add a bar is between two adjacent sticks at that height (and only one such position per height)
    # Since problem doesn't specify which sticks to connect at free heights, we can assume that at each free height h, any bar may be added between any pair b,b+1 provided it does not conflict with existing bars at adjacent heights positions (to prevent crossing)
    # But problem states no crossing bars - only horizontal bars connecting adjacent sticks at same height, and no two bars at same height
    # So adding a bar between b,b+1 at height h is possible if no bar at height h exists, and no bar at height h adjacent to b or b+1 that would cause conflict
    # But as bars only exist at distinct heights, and bars connect only adjacent vertical sticks, no crossing possible if only one bar per height
    # Hence at free heights, bars can be added connecting any b in 1..N-1
    # But problem states "どの場所も等確率で選ばれる", so "場所" means (height, b) pairs possible for new bars
    # So at free heights h, for possible b in 1..N-1 if no bar at height h, bar can be placed; number of such places = number of free heights * (N-1)
    # This complexity suggests a large search space, impossible to brute force
# Conclusion: The problem is about random addition of bars at free height positions that don't violate problem constraints.
# But problem states: "同じ高さには複数の横棒は存在しない": no two horizontal bars at same height
# So only one bar per height
# Given M bars fixed at fixed heights and positions, we have H - M free heights
# The friend adds K bars at distinct heights among free heights (since total M+K ≤ H)
# At each addition, friend uniformly picks one of the free heights and places a bar at that height connecting sticks b,b+1 where b is between 1 and N-1 and no existing bar at that height
# But which b? The problem states "横棒を追加しても上で指定された条件を満たすような場所のうち1箇所を無作為に選ぶ"
# So each free height corresponds to exactly one possible bar: Connecting sticks b,b+1 with b unknown but fixed by problem constraints
# So in problem input, each bar is represented by (a,b)
# So the possible positions where bars can be added equal the free heights, and each free height corresponds to exactly one (a,b)
# Hence, bar position is (height, b)
# So we have to determine all possible (a,b) pairs for new bars that satisfy constraints and aren't already used
# So bars can't be adjacent: bars can't be adjacent in horizontal line meaning can't place bars connecting b,b+1 and b+1,b+2 at same height for example
# But problem states no bars at same height except one
# So per problem, at height h, only one bar can exist connecting b,b+1
# So each free height h can only have one possible b (input allows us to determine)
# So the only possible position to add bar at that height is between some b,b+1, but problem does not say which b for free heights
# The position of new horizontal bars are the free heights, and at that height, bar can be added between the same b,b+1 sticks as the example in sample inputs
# So it suffices to determine for all free heights a in 1..H where no bar exists, which b can be set such that bar can be added at (a,b)
# With the constraint that bars don't cross (no two bars share the same sticks at adjacent heights), but problem does not mention crosses explicitly but by statement "同じ高さには複数の横棒は存在しない"
# So at each height, only one bar (a,b) is possible
# So the number of possible positions to add bars is the number of free heights
# So friend randomly chooses free height, places bar at that height connecting b,b+1 where b is fixed and given (?)
# So in input, this b is not given for free heights
# Hypothesis: at free heights, only one bar can be added, the one connecting the same b as existing pattern in input. Possibly it's always possible to add bar at any free height between any b,b+1 sticks
# But problem statement says "縦棒の上端から a センチメートルの高さにあり，左から b 本目の縦棒と左から b+1 本目の縦棒を結ぶ"
# So all horizontal bars are uniquely defined by (a,b)
# So, friend can add bar only at positions (a,b) that satisfy conditions and are not used yet
# So all positions (a,b) where a is free height, and between sticks b,b+1, no adjacent bars at height a, can be added
# Hence, friend randomly picks one of the possible (a,b) pairs among all free pairs, uniformly
# So we must generate all possible candidates (a,b) for new bars: for all free heights a, for all b in 1..N-1 that do not conflict with existing bars (no bar at height a)
# So in summary:
# - initial M bars fixed
# - friend adds bars at K steps, each time picks randomly one unused (a,b) among possible (free height, b) pairs satisfying conditions
# At each step, number of possible positions reduces by 1 (as bar added)

# Problem boils down to:
# - Compute probability that starting from top stick i, after adding K random bars at random positions (a,b), the final position is P
# - The player will choose i to maximize that probability

# Approach:
# Build a model of the ladder as permutation of sticks
# Each added bar swaps two sticks at that height
# So adding bars corresponds to composing transpositions in permutation group
# Initial permutation is given by existing bars: swaps at fixed heights
# When friend adds K bars at random positions (a,b), the final permutation is initial composed with random transpositions from possible positions chosen uniformly
# So we want expected transition matrix after K random transpositions chosen uniformly among candidates and no repeats
# Using linearity of expectation, but different bars chosen without replacement, so complicated
# Since M+K ≤ H ≤ 500, N ≤ 100, K ≤ 100
# A solution: DP with states as vectors of probability for each stick

# Implementation:
# Represent current probability vector of starting positions at top as size N
# Initial: vector with 1 at chosen i
# At each step:
# For all available candidate bars (a,b) not yet used, each corresponds to swapping sticks b and b+1
# Average over all possible bars (uniform choice) the effect on the probability vector is to swap the probabilities at positions b and b+1 with certain probability 1/(number_of_available_bars)

# So model transition matrix T as average over all possible swaps U_ab:
# T = average over all valid bars of transposition matrix swapping b and b+1
# Apply T to the probability vector K times (since each addition applies a random swap)

# Finally apply initial fixed permutation (existing bars)
# Then for each starting position i in 1..N, compute dp after applying T^K and initial permutation

# Then output max of dp[i] over i

# Steps to implement:

# 1. Build initial permutation from existing bars as a list p:
# p[i] = the stick at bottom that i maps to after traversing ladder

# 2. Build set of candidate bars:
# - For each free height a:
#   For b=1 to N-1:
#     check conditions for bar at (a,b): no conflict with existing bars at that height; none at height a anyway since free
# Since no bars at that height, bar at (a,b) is valid candidate

# So candidate bars = all pairs (a,b) where a is free height, b in 1..N-1

# 3. Number of candidates = c

# 4. Build transition matrix T of size N x N:
# T = sum over all candidate bars of U_ab / c
# U_ab is N x N matrix representing swapping positions b and b+1
# Applying T to vector v:
# For each candidate bar (a,b):
#   Applying U_ab to v swaps v[b-1] and v[b], indices 0-based
# So T*v = sum over candidate bars of U_ab*v / c
# So T*v[i] = sum over all candidate bars of v[i] or v[j] depending on swap

# It's inefficient to build full NxN matrix, better to apply T directly on vector v:

# For v vector of size N:
# T v = average over all bars (swapping b and b+1) applied to v

# So:
# For i in 0..N-1:
#   T v[i] = average over all candidate bars:
#     if i not in {b-1,b}, then T v[i] += v[i]/c
#     else if i == b-1, T v[i] += v[b]/c
#     else if i == b, T v[i] += v[b-1]/c

# Implementation of T*v:

# For given v, initialize Tv=[0]*N

# For each candidate bar (a,b):
#   Tv[b-1]+= v[b]/c
#   Tv[b]+= v[b-1]/c
#   For i not b-1,b:
#     Tv[i]+= v[i]/c

# To optimize, we accumulate counts of how many times each b occurs

# But c = (number_of_free_heights)*(N-1)

# So each position i is swapped with neighbors multiple times

# Aggregate counts per position to apply T efficiently:

# Alternative approach:

# For each position i:
#  - number of bars swapping i with i+1: free_heights count where b = i+1
#  - number of bars swapping i-1 with i: free_heights count where b = i

# But b ranges from 1..N-1

# So for i in 0..N-1:

# Number of bars swapping i and i+1 is number_of_free_heights if i in 0..N-2

# So for each position i, count how many bars swap it with neighbor:

# For each bar (a,b):
# Swaps positions b-1 and b

# So each position i is swapped with:

# i-1 for bars with b = i

# i for bars with b = i+1

# Number of bars is number_of_free_heights per each b

# So, total bars = number_of_free_heights * (N-1)

# So for position i:

# Swapped with i-1 if i>0: number_of_free_heights bars with b=i

# Swapped with i+1 if i<N-1: number_of_free_heights bars with b=i+1

# So for each i:

# The probability to swap with neighbor = 2*number_of_free_heights/(total bars) = 2/(N-1)

# Wait, the bars are all equally likely, each corresponds to a swap of adjacent positions

# So transition matrix T acts as:

# For each index i:

# T v[i] = (1 - 2*number_of_free_heights/(total bars)) * v[i] + sum over swaps affecting i (v[j]/c)

# But complicated

# Instead, we can directly implement matrix power with vector multiply, since K ≤ 100, N ≤ 100

# Steps:

# Build initial permutation vector perm such that perm[i]=position after initial ladder

# Represent vectors as arrays size N

# For each candidate bar, build swap matrix

# Sum all swap matrices to build T

# Then compute T^K using repeated squaring or simple loop since K small

# Finally, for each starting i in 1..N:

# Create initial vector v with 1 at i-1

# Apply perm (initial ladder) to get vector after initial ladder

# Then apply T^K to vector

# The value at position P-1 is probability that starting from i ends at P

# Compute max over i

# Output the max probability

# Implementation