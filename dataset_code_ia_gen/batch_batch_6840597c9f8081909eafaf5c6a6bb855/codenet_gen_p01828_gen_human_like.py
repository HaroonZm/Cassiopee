S = input().strip()
T = input().strip()
n = len(S)

def can_form(s_first):
    # s_first: bool, True if s starts first, else t starts first
    i, j = 0, 0  # indices for S and T subsequences
    for idx in range(n):
        expected_char = S[idx]
        if (idx % 2 == 0) == s_first:
            # need character from s subsequence
            while i < n and T[i] != expected_char:
                i += 1
            if i == n:
                return False
            i += 1
        else:
            # need character from t subsequence
            while j < n and S[j] != expected_char:
                j += 1
            if j == n:
                return False
            j += 1
    return True

# Wait, in the problem S is the result name, and we have original companies S and T.
# Actually, we have to check if S can be formed by alternately taking subsequences from original names s and t.
# The input gives S and T (same length), want to check if S can be formed by alternating subsequences of S and T.
# So the first line is the target name S, the second line is the original target company T.
# So the given strings S and T are the original names, and we want to get the target name S by mixing subsequences of S and T? No.
# The problem states:
# Input line 1: S (name of the company you belong to)
# Input line 2: T (name of the target company)
# We want to check if it's possible to form the original company name S (the first line) by mixing subsequences from S and T.

# So the S (line 1) is the target company name
# The mixture is formed by subsequences s from S and t from T, arranged alternately to produce S

# Thus, s is subsequence of S (first string), t is subsequence of T (second string)
# The string formed by mixing s and t in alternating order is equal to the input string S (same as first input line).
# That is, the mixed name is equal to the first input line S.
# Check if possible.

# So the first input is the target name (result), second input is the target company.
# For the two possible interleavings, check if any subsequence s of S and subsequence t of T can be alternated to produce S.

# Implementation plan:
# Since length n is <= 1000, can do DP or greedy approach.
# Let's implement a greedy approach:
# For both patterns (s first or t first), try to greedily find subsequence s from S and t from T that interleaved form S.

def can_form_alternating(s_first):
    s_idx = 0  # index for string S (to take subsequence s)
    t_idx = 0  # index for string T (to take subsequence t)
    for idx in range(n):
        c = S[idx]
        if (idx % 2 == 0) == s_first:
            # character should be from s subsequence of S
            while s_idx < n and S[s_idx] != c:
                s_idx += 1
            if s_idx == n:
                return False
            s_idx += 1
        else:
            # character should be from t subsequence of T
            while t_idx < n and T[t_idx] != c:
                t_idx += 1
            if t_idx == n:
                return False
            t_idx += 1
    return True

if can_form_alternating(True) or can_form_alternating(False):
    print("Yes")
else:
    print("No")