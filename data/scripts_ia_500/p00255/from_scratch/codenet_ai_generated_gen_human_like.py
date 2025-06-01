import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n, pipe_lengths):
        self.parent = list(range(n))
        self.size = [1]*n
        self.length_sum = pipe_lengths[:]
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y, joint_len):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        # When two sets are joined, add joint length and sum lengths
        self.length_sum[x] += self.length_sum[y] + joint_len
        self.size[x] += self.size[y]
        return True
    def pay(self, x):
        x = self.find(x)
        return self.size[x]*self.length_sum[x]

while True:
    n = int(input())
    if n == 0:
        break
    pipes = list(map(int, input().split()))
    joints = list(map(int, input().split()))
    uf = UnionFind(n, pipes)
    # Initially, salary if no pipes are joined: sum of pi * 1 = sum pipes
    # We want to maximize total pay = sum over all groups of (number_of_pipes_in_group * sum_of_lengths_in_group)
    # Joining pipes decreases number_of_groups but increases lengths by joints
    # Idea: greedily join pairs that maximize increase in total pay
    # Since pipes are in a line and joint i connects i and i+1 only,
    # we will consider joining unions sequentially.
    # We can greedily choose joints to join in any order?
    # Actually, joining is sequential and only adjacent pipes.
    # We try to join all pipes in order from left to right with all joints and see what max is.

    # But full union all: one group, pay = 1 * total length (pipes sum + joints sum)
    # No union: pay = n * sum pipes

    # To maximize pay, union joins that increase pay more than separate pipes pay
    # Each union merges two groups into one:
    # Before union: pay = sizeA*sumA + sizeB*sumB
    # After union: pay = (sizeA+sizeB)*(sumA+sumB+joint)
    # delta = after - before = (sizeA+sizeB)*(sumA+sumB+joint) - (sizeA*sumA + sizeB*sumB)
    # Compute delta to decide if union is beneficial.
    # Since pipes are initially singletons (size=1, sum=p_i), we can process unions in order.

    # Simpler approach: joining all pipes in order, we keep track of pay.

    # Because union of two single pipes always changes pay to 2*(p_i + p_{i+1} + joint_i) - (p_i + p_{i+1}) = 
    # 2*p_i + 2*p_{i+1} + 2*joint_i - p_i - p_{i+1} = p_i + p_{i+1} + 2*joint_i
    # But initial pay is p_i + p_{i+1}

    # So joining two pipes is beneficial if this > initial pay? Always positive.

    # But when merging bigger groups, delta depends on sum and size.

    # Because joints are only between adjacent pipes, and order is fixed, 
    # the number of groups after merging is m, 1 ≤ m ≤ n, and each group is contiguous pipes.

    # So problem reduces to segmenting pipes into contiguous groups,
    # Each group's pay = number_of_pipes * (sum_of_pipes + sum_of_joints_inside_that_group)

    # Because joints are only between consecutive pipes, and define group boundaries.

    # So the problem is to partition pipes into segments.

    # To solve maximal total pay over segments, we can use DP:

    # dp[i]: max total pay for first i pipes
    # dp[0] = 0
    # For i in 1 to n:
    #   for k in 0 to i-1:
    #       segment_length = i - k
    #       pipes_sum = sum of p[k+1..i]
    #       joints_sum = sum of j[k+1..i-1], if segment_length >= 2 else 0 (if segment_length == 1)
    #       segment_pay = segment_length * (pipes_sum + joints_sum)
    #       dp[i] = max(dp[i], dp[k] + segment_pay)

    # But n up to 65000, O(n^2) impossible.

    # With n large, we need O(n) or O(n log n).

    # Note:
    # dp[i] = max over k < i of dp[k] + (i-k)*(sum_pipes(k+1,i) + sum_joints(k+1,i-1))

    # Let's precompute prefix sums:
    # S_p[i]: sum of pipes from 1 to i
    # S_j[i]: sum of joints from 1 to i
    # Then pipes sum in [k+1, i] = S_p[i] - S_p[k]
    # Joints sum in [k+1, i-1] = S_j[i-1] - S_j[k], if k+1 <= i-1 else 0

    # dp[i] = max_{k<i} dp[k] + (i-k)*( (S_p[i] - S_p[k]) + (S_j[i-1] - S_j[k]) )
    #        = max_{k<i} dp[k] + (i-k)*(S_p[i] + S_j[i-1]) - (i-k)*(S_p[k] + S_j[k])

    # Fix i terms:
    # dp[i] = (i)*(S_p[i] + S_j[i-1]) + max_{k<i} { dp[k] - k*(S_p[i] + S_j[i-1]) - (i-k)*(S_p[k] + S_j[k]) }

    # This is still complicated.

    # Rewrite it:
    # dp[i] = max_{k<i} [ dp[k] - (i-k)*(S_p[k] + S_j[k]) ] + (i - k)*(S_p[i] + S_j[i-1])

    # Alternative:

    # Instead, rewrite the formula carefully:

    # dp[i] = max_{k<i} [ dp[k] + (i-k)*( (S_p[i] - S_p[k]) + (S_j[i-1] - S_j[k]) ) ]
    #       = max_{k<i} { dp[k] + (i-k)*(S_p[i] + S_j[i-1]) - (i-k)*(S_p[k] + S_j[k]) }

    # So dp[i] = (S_p[i] + S_j[i-1]) * i + max_{k < i} { dp[k] - (S_p[i] + S_j[i-1]) * k - (i-k)*(S_p[k] + S_j[k]) }

    # But (i-k)*(S_p[k] + S_j[k]) depends on i,k and is complex.

    # Try to find a way to reduce it to a convex hull trick problem.

    # Let's define A_i = S_p[i] + S_j[i-1]

    # Then dp[i] = max_{k < i} [ dp[k] + (i-k)*A_i - (i-k)*A_k ]
    #             = max_{k < i} [ dp[k] + (i-k)(A_i - A_k) ]

    # So dp[i] = max_{k < i} [ dp[k] + (i-k)*(A_i - A_k) ]

    # A_i and A_k known.

    # Rearrange:
    # dp[i] = max_{k < i} [ dp[k] + (i-k)*A_i - (i-k)*A_k ]
    #       = max_{k < i} [ dp[k] - i*A_k + k*A_k + i*A_i - k*A_i ]
    #       = i*A_i + max_{k < i} [ dp[k] + k*A_k - i*A_k - k*A_i ]

    # Simplify inside max:
    # dp[k] + k*A_k - i*A_k - k*A_i = (dp[k] + k*A_k) - i*A_k - k*A_i

    # Fix i, variable k in max:

    # max_{k < i} [ (dp[k] + k*A_k) - i*A_k - k*A_i ] = max_{k < i} [ (dp[k] + k*A_k) - i*A_k - k*A_i ]

    # Because i and A_i fixed for dp[i], the expensive part is max over k of [dp[k] + k*A_k - i*A_k - k*A_i]

    # Let's write:

    # max_{k < i} [ (dp[k] + k*A_k) - i*A_k - k*A_i ] = max_{k < i} [ (dp[k] + k*A_k) - k*A_i - i*A_k ]

    # Rearrange:

    # = max_{k < i} [ (dp[k] + k*A_k - k*A_i) - i*A_k ] = max_{k < i} [ (dp[k] + k*(A_k - A_i)) - i*A_k ]

    # But since A_i is fixed, also note that i is variable in outer loop.

    # So for fixed k, the function in i becomes:

    # f_k(i) = (dp[k] + k*(A_k - A_i)) - i*A_k

    # But A_i depends on i, so A_i changes with i. This makes it harder.

    # Alternatively, test values or use offline approach.

    # Since A_i = S_p[i] + S_j[i-1], and both arrays are monotonic nondecreasing (sum array), A_i increases.

    # Use convex hull trick.

    # Each line corresponds to a segment at k:

    # dp[i] = i*A_i + max_{k < i} [ (dp[k] + k*A_k) - i*A_k - k*A_i ]

    # = i*A_i + max_{k < i} [ (dp[k] + k*A_k) - k*A_i - i*A_k ]

    # Take variable i on x-axis and let:

    # For each k, line:

    # y = m*x + b

    # Here:

    # m = -A_k

    # x = i

    # b = dp[k] + k*A_k - k*A_i

    # But k*A_i depends on i (x), so can't be part of const b.

    # Wait, we can rearrange to separate terms that depend on i (x):

    # But b contains k*A_i, which depends on i.

    # So direct convex hull is not straightforward.

    # But instead, re-express original dp formula as:

    # dp[i] = max_{k < i} dp[k] + (i - k)(S_p[i] - S_p[k] + S_j[i -1] - S_j[k])

    # dp[i] = max_{k < i} dp[k] + (i-k)*S_p[i] - (i-k)*S_p[k] + (i-k)*S_j[i-1] - (i-k)*S_j[k]

    # = max_{k < i} dp[k] - (i-k)*S_p[k] - (i-k)*S_j[k] + (i-k)*S_p[i] + (i-k)*S_j[i-1]

    # As S_p[i] and S_j[i-1] constants for given i:

    # dp[i] = max_{k < i} [ dp[k] - (i-k)* (S_p[k] + S_j[k]) ] + (i-k)* (S_p[i] + S_j[i-1])

    # Wait, that matches before; let's put:

    # Let B_i = S_p[i] + S_j[i-1]

    # Then: dp[i] = max_{k<i} [dp[k] - (i-k)*B_k] + (i-k)*B_i

    # Now (i-k)*B_i varies with i and k.

    # But since B_i is fixed for i, for inner max over k:

    # max_{k<i} [dp[k] - (i-k)*B_k] => for fixed i, variable k from 0 to i-1.

    # Let's define function:

    # For dp[i]:

    # dp[i] = max_{k<i} [ dp[k] - (i-k)*B_k ] + (i-k)*B_i

    # Then:

    # dp[i] - B_i*i = max_{k < i} [ dp[k] - B_k*k ] - max_{k < i} [ B_k * i ]

    # Seems complicated, but better to implement as:

    # For i = 1 to n:

    # We try to find k (0 <= k < i) maximizing dp[k] - (i - k)*B_k

    # This is same as dp[k] - i*B_k + k*B_k

    # dp[k] + k*B_k - i*B_k

    # For fixed i, linear function in B_k with slope -i.

    # So for all k, the value at i is dp[k] + k*B_k - i*B_k

    # For fixed i, max over k.

    # So if we define line for each k: y = m*i + c with m = -B_k, c = dp[k] + k*B_k

    # Then for each i, dp[i] = max over k of (m*i + c) + (i-k)*B_i

    # Hold on, complex.

    # But maybe better to just solve the problem using segment grouping greedily.

    # Because the problem restricts joints to connect pipe i and i+1, groups are contiguous segments.

    # We want to partition the pipe series into segments to maximize sum over segments of |segment| * sum_lengths(segment)

    # For segments:

    # Length of each segment = number of pipes in it

    # Sum of lengths = sum pipes lengths + sum joints lengths inside segment

    # Because joints only connect consecutive pipes, the total sum of joints inside the segment is sum of corresponding j.

    # So the problem becomes to partition the array into contiguous segments to maximize:

    # sum over segments s: |s| * (sum of pipes + sum of joints in s)

    # Let's think about the cost function for a segment [l, r], 1-based:

    # cost = (r - l + 1) * (S_p[r] - S_p[l-1] + S_j[r-1] - S_j[l-1])

    # Where S_p and S_j are prefix sums and S_j[0] = 0.

    # We want to find partition points that maximize total cost.

    # This is a classical segmentation optimization solvable by convex hull trick with dp:

    # dp[i] = max_{0 <= k < i} dp[k] + (i - k) * (S_p[i] - S_p[k] + S_j[i-1] - S_j[k])

    # We can rewrite:

    # dp[i] = max_{0 <= k < i} [ dp[k] - k*(S_p[i] + S_j[i-1]) + i*(S_p[i] + S_j[i-1]) - (S_p[i]*k + S_j[i-1]*k) + ... ]

    # Wait, too complicated.

    # It's better to write:

    # Define A[i] = S_p[i] + S_j[i-1]

    # So dp[i] = max_{k < i} dp[k] + (i-k)*(A[i] - A[k])

    # = max_{k < i} [ dp[k] + i*A[i] - k*A[i] - i*A[k] + k*A[k] ]

    # = i*A[i] + max_{k < i} [ dp[k] + k*A[k] - k*A[i] - i*A[k] ]

    # = i*A[i] + max_{k < i} [ (dp[k] + k*A[k]) - k*A[i] - i*A[k] ]

    # Let's denote:

    # For each k, f_k(i) = (dp[k] + k*A[k]) - k*A[i] - i*A[k] = (dp[k] + k*A[k]) - k*A[i] - i*A[k]

    # For fixed i, to find max over k, treat i as x variable:

    # Then f_k(i) = (-A_k)*i + (dp[k] + k*A[k] - k*A[i])

    # But A[i] depends on i, so k*A[i] depends on i, varying inside the constant term.

    # So the convex hull trick is tricky.

    # Alternatively, because we cannot remove the k*A[i], we use a trick:

    # Let's define dp[i] - i*A[i] = max_{k < i} [ dp[k] + k*A[k] - k*A[i] - i*A[k] - i*A[i] ]

    # Not clarifying.

    # Let's try a different approach.

    # Observation: For two adjacent pipes i and i+1,

    # The difference in pay by merging is joint length * segment size factor.

    # Another observation: greedily merging all joints with small joint length is good.

    # Actually, since the problem is about grouping contiguous segments,

    # The problem is segmented dp:

    # Define dp[i] as above, and implement convex hull trick:

    # dp[i] = max_{k < i} dp[k] + (i-k)*(A[i] - A[k]) = max_{k < i} [dp[k] - k*A[k]] + i*A[i] - i*A[k] + k*A[k]

    # Wait actually:

    # dp[i] = max_{k < i} [ dp[k] + (i-k)*A[i] - (i-k)*A[k] ]

    # = max_{k < i} [ dp[k] - i*A[k] + k*A[k] + i*A[i] - k*A[i] ]

    # = i*A[i] + max_{k < i} [ dp[k] + k*A[k] - k*A[i] - i*A[k] ]

    # = i*A[i] + max_{k < i} [ (dp[k]