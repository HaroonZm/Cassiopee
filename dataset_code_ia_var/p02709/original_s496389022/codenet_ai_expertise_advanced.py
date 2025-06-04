from sys import stdin
from functools import reduce

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
indexed_A = sorted(((a, i) for i, a in enumerate(A)), reverse=True)

dp = [0] * (N + 1)
for i, (a, pos) in enumerate(indexed_A):
    # Utilise list comprehension et zip pour parcourir les états précédents
    new_dp = dp[:]
    for l, dp_val in enumerate(dp[:i+1]):
        # Ajout côté gauche
        left_score = dp_val + (pos - l) * a
        if left_score > new_dp[l+1]:
            new_dp[l+1] = left_score
        # Ajout côté droit
        r = i - l + 1
        right_score = dp_val + (N - r - pos) * a
        if right_score > new_dp[l]:
            new_dp[l] = right_score
    dp = new_dp

print(max(dp))