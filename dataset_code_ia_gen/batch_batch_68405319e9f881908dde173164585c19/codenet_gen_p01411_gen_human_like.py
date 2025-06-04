import sys
sys.setrecursionlimit(10**7)

H, N, P, M, K = map(int, input().split())
rungs = [0]*(H+1)
connections = [0]*(H+1)
occupied = [False]*(H+1)

for _ in range(M):
    A, B = map(int, input().split())
    rungs[A] = B
    occupied[A] = True

# Positions where a rung can be placed (from 1 to H) and not occupied
candidates = []
for h in range(1, H+1):
    if not occupied[h]:
        candidates.append(h)

# Precompute restricted positions to avoid adjacent rungs at the same height
# Actually, the problem states no multiple horizontal lines at the same height, so it's okay

# We'll build a state DP:
# dp[h][i]: probability distribution of the position i after h-th rung

# But we need to model the probability of ending on each stick after K additions of horizontal bars, placed one by one randomly.

# The approach:
# - At each step, we can add a new horizontal rung at one of the free spots uniformly at random.
# - For each possible new rung, it changes the permutation of the sticks accordingly.
# - Since K and candidates are small (<=100), we can model the probability distribution over permutations or better over position probabilities.

# But size of permutations is huge (N up to 100), direct permutation is impossible.

# Alternative modeling:

# The problem can be solved by DP over configurations of rungs added, but too big.

# Key insight (from original contest editorial, similar to problem): 
# The probability can be modeled position-wise.

# Let's define f(k)[pos]: probability that after k additions, the rabbit's stick is pos when starting from initial stick pos0.

# Because the horizontal lines only swap adjacent sticks, and all possible new rungs are chosen uniformly at random each time, we can model the effect of one added rung as an average over transitions induced by these possible rung positions.

# Thus, the transition from f(k) to f(k+1) is:

# f(k+1) = TransitionMatrix * f(k)

# TransitionMatrix is an N x N matrix computed as average over all possible new rungs.

# To construct TransitionMatrix:

# First, build base ladder permutation (initial M rungs).

# Then for each candidate rung (new rung position), build the swap it induces on the permutation.

# TransitionMatrix is identity matrix + sum over all candidate rungs / len(candidates) of the swap at that rung.

# With that, we can compute f = (TransitionMatrix)^K * initial vector (the vector with 1 at chosen position, 0 elsewhere)

# We'll do this for each starting position (1..N), compute probability that the final position is P (winning spot).

# Then output the maximum over starting positions.

# Let's implement steps:

def simulate_ladder(rungs):
    # Simulate ladder to get final position mapping from start to end
    pos = list(range(N+1))
    for h in range(1, H+1):
        b = rungs[h]
        if b != 0:
            # swap pos[b], pos[b+1]
            pos[b], pos[b+1] = pos[b+1], pos[b]
    # pos[i]: index of stick starting at i -> stick at bottom pos[i]
    return pos

# Build initial permutation
initial_perm = simulate_ladder(rungs)

# Build base rungs occupancy
occupied_pos = set(i for i in range(1,H+1) if rungs[i] != 0)
candidate_positions = [i for i in range(1,H+1) if i not in occupied_pos]

# For each candidate position, simulate the swap induced
# The swap is on sticks at positions B_i and B_i+1 for rung at height h, which is rungs[h] = B_i.

# For each candidate h, the swap is at position between sticks b and b+1
# But for candidate positions, we must choose where to put h. The problem states: "a place to add a rung that satisfies the conditions" - only between sticks that don't have a horizontal rung at this height (condition of no two rungs in same height).

# For candidate h, the question is which swap does it correspond to?

# The problem states: "Each horizontal rung connects adjacent sticks, specifying B_i"

# In input, each rung is defined by (A_i, B_i), height and left stick number.

# For candidate h, we must consider all possible B in [1,N-1] to add a rung at height h.

# But "the place" means height h and stick B such that no rung exists at height h.

# Wait, the candidates are heights only; for each candidate h, we can add rungs between which two sticks?

# The problem states: "うさぎはこれらの条件を満たすように M 本の横棒を引いた... 友達がさらに横棒を追加"

# So horizontal lines are at height h joining two adjacent sticks.

# But candidate positions are heights; at each height only one horizontal rung.

# So the available new rungs are at candidate heights, but the candidate heights are those where no rung exist yet.

# So at each candidate height, possible new rung B can be any between 1 and N-1 such that it's not conflicting?

# The problem states "横棒を追加しても上で指定された条件を満たすような場所のうち 1 箇所を無作為に選ぶ"

# So a "place" is a pair (height h, B), but also "no two horizontal lines at the same height"

# Since no horizontal line at height h yet, and B can be any from 1 to N-1, are all possible B allowed?

# The problem constraint suggests given the current rung positions, no two horizontal lines at same height, so adding a rung at height h links stick B and B+1.

# Given that only one horizontal line at each height, the location to add is (h,B), but in input M rungs at (A_i, B_i), so at current heights only one horizontal line.

# So we must consider adding horizontal rung at any height h with any B ?

# The problem statement says "追加する場所は全て等確率", so "場所" means positions where horizontal rung can be added without violating conditions.

# The condition is that no two horizontal lines are at the same height.

# Since at height h, no horizontal rung yet, so can we add at all B in [1, N-1]?

# Probably not: the problem states "横棒は隣り合った2本の縦棒のみを結ぶ", yes.

# So for each height h, possible B is all from 1 to N-1.

# But must check there's no horizontal rung at height h already.

# So for each candidate height h (heights without any rung), place the horizontal rung with B in [1..N-1].

# So that means at candidate height h, there are N-1 possible horizontal rungs to add.

# But the problem says "1 箇所を無作為に選ぶ", so the place is the pair (h, B).

# In the input, we only have M horizontal bars, each is (A_i, B_i)

# So now for candidate heights, all B in [1..N-1] can be used.

# Hence all possible places to add are pairs (h, B) where h not in rung heights, B=1..N-1.

# Wait, the problem statement is ambiguous, but sample has small number of candidates.

# But constraints say M+K <= H, suggesting only one horizontal rung per height.

# So the "places" are heights h where no rung exists.

# However, for each such h, multiple B can be options?

# No, problem says "各横棒は縦棒の上端から a センチメートルの高さにある", so the horizontal rung is located at a height a, connecting sticks numbered B and B+1 (left to right).

# From the input constraints and sample, it looks like for each height a, only one horizontal rung can be placed. So each horizontal rung is uniquely defined by (a,B).

# Because sample input has for height=2, B=1; and height=7, B=3.

# So adding a rung at height h means position (h,B), the "場所" is (height, B).

# Problem states "同じ高さには複数の横棒は存在しない" (No multiple horizontal bars at the same height), which applies.

# So if occupied heights are M, then candidate heights positions are H - M.

# But for candidate heights, which B is possible? The problem states that each horizontal bar connects adjacent two sticks; so potentially multiple B per height could exist? But since a horizontal rung is uniquely defined by height a and B, each height can have at most one horizontal rung.

# So at a given height h, only one B is possible.

# So the only possible (h,B) where h is candidate is to add a horizontal rung at height h connecting B and B+1; B can be from 1 to N-1.

# So is there any restriction on B at height h? The problem statement and samples imply the new rung can be added at height h with any B.

# So to generate all possible addition places, we must consider all pairs (h,B) where h in candidate heights (no rung yet reserved), B in [1..N-1] such that constraints are met.

# Next constraint is: No intersecting horizontal bars, and no adjacent horizontal bars in height?

# The only restriction is no horizontal rung at same height multiple times (guaranteed by candidate heights), so it's okay.

# Therefore, the number of candidate places to add a rung is:

# number_of_candidates = (H - M) * (N - 1)

# Which can be up to 500 * 99 = 49500 ~ 5e4, acceptable.

# Therefore, for transition matrix:

# For each candidate place (h, B):

# Build rung array: set rung at h with B

# Simulate permutation

# Get permutation swap induced by adding the horizontal rung

# Transition matrix is average over all these permutations.

# Also, add identity (no rung added) for 0 additions?

# Not needed, as per problem only additions counted, K times.

# The initial permutation is fixed (with M horizontal bars).

# So the full permutation after additions is initial_perm multiply the product of added permutations.

# Because permutations compose.

# So we can view this as a Markov process on positions:

# The state vector is N elements, probability distribution over stick positions.

# For each addition, the new probability vector is multiplied by the transition matrix.

# Transition matrix T = average over all swap permutations induced by candidate places (h, B)

# The size of T is N x N (~100 x 100), acceptable.

# Let's implement that.

# Steps:

# - Build initial_perm

# - Build identity matrix (size N x N)

# - For each candidate place (h,B):

#   - rungs2 = copy of rungs + set rungs2[h] = B

#   - simulate permutation p

#   - from p, build permutation matrix P

# - sum all P matrices, then divide by total candidate places -> average Transition Matrix

# Then raise Transition Matrix to power K.

# For each starting position s (1..N):

# - initial vector v: v[s] = 1.0, others 0

# - final vector f = T^K * v

# Probability to end on position P (the winning stick) is f[P]

# Take max of f[P] over s

# Output max value

# Let's implement this solution now.

def permutation_to_matrix(perm):
    # perm: list of length N+1, perm[i] = position of stick i after permutation
    # Convert to matrix M where M[i][j] = 1 if i maps to j, else 0
    # i: starting stick index
    # j: ending stick index
    # So for vector v: v_new[j] = sum_i M[i][j]*v[i]
    # Need matrix that when multiplied from left by vector v gives new vector
    # Actually, permutation matrix P satisfies P * v = v_permuted
    # Since perm[i] = destination of i, i.e. i -> perm[i]
    # Then P[i][perm[i]] = 1
    # But for vector multiply v_new = v*P, we usually use v_new[j] = sum_i v[i] * P[i][j]
    # So to get v_new = P * v, we put 1 at [dest][src]?

    # Let's build according to convention v_new = P * v:
    # So P[dest][src] = 1? No, permutation matrix acts as P[i][j] = 1 if i-th position maps to j-th position.

    # Let's define M[i][j] = 1 if element j moves to position i

    # Let's use row vector multiplication: v_new = v * M

    # So v_new[j] = sum_i v[i] * M[i][j]

    # So M[i][j]=1 if from i to j

    # So M[i][j] = 1 if i-th start maps to j-th destination

    # So for i in [1..N], perm[i] is destination of i

    # So M[i][perm[i]] = 1

    M = [[0.0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        M[i][perm[i]] = 1.0
    return M

def mat_mult(A,B):
    size = len(A)
    C = [[0.0]*size for _ in range(size)]
    for i in range(1,size):
        Ai = A[i]
        for j in range(1,size):
            s = 0.0
            for k in range(1,size):
                s += Ai[k]*B[k][j]
            C[i][j] = s
    return C

def mat_vec_mult(v, M):
    size = len(v)
    res = [0.0]*size
    for j in range(1,size):
        s = 0.0
        for i in range(1,size):
            s += v[i]*M[i][j]
        res[j] = s
    return res

def mat_pow(mat, power):
    size = len(mat)
    res = [[0.0]*size for _ in range(size)]
    for i in range(size):
        res[i][i] = 1.0
    base = mat
    while power > 0:
        if power & 1:
            res = mat_mult(res, base)
        base = mat_mult(base, base)
        power >>= 1
    return res

# Prepare transition matrix sum
size = N+1
T_sum = [[0.0]*size for _ in range(size)]

total_candidates = 0
for h in range(1,H+1):
    if not occupied[h]:
        for B in range(1, N):
            # Add rung at (h,B)
            rungs2 = rungs[:]
            rungs2[h] = B
            perm = simulate_ladder(rungs2)
            M = permutation_to_matrix(perm)
            for i in range(1,size):
                Mi = M[i]
                Ti = T_sum[i]
                for j in range(1,size):
                    Ti[j] += Mi[j]
            total_candidates += 1

# Average
for i in range(1,size):
    Ti = T_sum[i]
    for j in range(1,size):
        Ti[j] /= total_candidates

# Transition matrix T_sum is average permutation matrix after adding one rung at random candidate place

# We need to raise T_sum to power K
T_K = mat_pow(T_sum, K)

# Initial position vector is delta vector at start stick s

# After K additions, probability distribution for starting at s is v = delta

# Compute v * T_K for each s, get probability that final position is P

max_prob = 0.0
for s in range(1, N+1):
    v = [0.0]*(N+1)
    v[s] = 1.0
    res = mat_vec_mult(v, T_K)
    # Now res[i]: probability to reach stick i after K additions, starting at s

    # But finally, apply initial permutation to map start pos to end pos? No, initial_perm already included in each step because the rungs2 are with initial rungs + added.

    # But in simulate_ladder(rungs2), we only took the rungs2 (rungs + added rung), so initial_perm represented the ladder with initial bars, the added rung represents addition.

    # But is initial_perm included in each rungs2?

    # Wait, initial_perm is simulation of rungs (M rungs), for each addition we add one extra rung; after K additions, the permutation is initial_perm composed with K added permutations.

    # The constructed T_sum is average permutation of the K-th rung addition (only the added rung applied)

    # So to apply the initial rungs, we must compose initial_perm permutation matrix P_init with T_K

    # So the total transition matrix is: P_init * T_K

# Build initial permutation matrix P_init
P_init = permutation_to_matrix(initial_perm)

# Compose total transition matrix = P_init * T_K
Total_T = mat_mult(P_init, T_K)

for s in range(1, N+1):
    v = [0.0]*(N+1)
    v[s] = 1.0
    res = mat_vec_mult(v, Total_T)
    if res[P] > max_prob:
        max_prob = res[P]

print(max_prob)