import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

def longest_alt(arr):
    max_len = 1
    length = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            length += 1
            if length > max_len:
                max_len = length
        else:
            length = 1
    return max_len

# If no operation is done
res = longest_alt(S)

# We want to consider flipping a subarray once
# Strategy:
# For each position i, define B[i] = 1 if S[i] == i%2 else 0 (matches alt pattern 1)
# and C[i] = 1 if S[i] == (i+1)%2 else 0 (matches alt pattern 2)
#
# Flipping a subarray [l, r] means flipping bits in S[l:r], so the final matching changes accordingly.
#
# We want to find the subarray [l, r] to flip that maximizes the maximum length of alternating sequence.

# Create arrays for the two alternating patterns
alt1 = [i % 2 for i in range(N)]
alt2 = [(i + 1) % 2 for i in range(N)]

# For each pattern, create an array matches: 1 if S[i] == pattern[i], else 0
matches1 = [1 if S[i] == alt1[i] else 0 for i in range(N)]
matches2 = [1 if S[i] == alt2[i] else 0 for i in range(N)]

# For flipping a subarray, the match changes:
# positions inside flipped subarray are flipped: match[i] := 1 - match[i]
# we want to find a subarray [l,r] where replacing matches[i] by 1 - matches[i] increases the maximum length of alternating sequence.

# To find the subarray that maximizes increase in longest alt sequence, we consider difference arrays:
# For each position i:
# diff[i] = (1 - matches[i]) - matches[i] = 1 - 2*matches[i]
# This is the gain in matches from flipping at position i

# We want to find the subarray [l, r] that maximizes sum of diff[l:r+1]

# But simply maximizing sum of diff does not guarantee longer alt sequence, we need to find the max length of alt sequence IF flipped this subarray.

# Instead, we use a standard approach:
# The length of longest alternating sequence can be obtained by the length of the longest run of consecutive 1's in matches.

# Flipping a subarray means toggling matches inside that interval (1->0,0->1)

# To maximize the length of consecutive 1's, we try flipping subarray that converts 0's to 1's and maybe break some 1's, but overall increase max run of 1's.

# We find maximal length of subarray of diff (which represents gain) and use that to update result:

def max_subarray_sum(arr):
    max_ending = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x)
        if max_ending > max_so_far:
            max_so_far = max_ending
    return max_so_far

# We try both alt1 and alt2 patterns, calculate max subarray gain and update result
# But max subarray gain gives max increase in matches sum, not directly max run length.
# So another approach:

# We use a method inspired by editorial of similar problem:
# We create for matches array a binary array, longest runs of 1s, we consider that flipping a subarray reverses bits there.
# For each position, compute longest consecutive 1s prefix and suffix.

def max_alt_with_flip(matches):
    # base longest consecutive ones max
    base_max = 0
    length = 0
    for v in matches:
        if v == 1:
            length +=1
            base_max = max(base_max, length)
        else:
            length = 0
    # compute prefix sums of matches and difference array:
    diff = []
    for v in matches:
        diff.append(1 - 2*v)  # flipping gives gain = 1-2*v
    max_gain = float('-inf')
    current = 0
    min_pre = 0
    max_gain = 0
    pre_sum = 0
    for d in diff:
        pre_sum += d
        max_gain = max(max_gain, pre_sum - min_pre)
        min_pre = min(min_pre, pre_sum)

    return base_max + max_gain

# Compute result for both patterns and take max (also consider no operation)
ans = max(res, max_alt_with_flip(matches1), max_alt_with_flip(matches2))
print(ans)