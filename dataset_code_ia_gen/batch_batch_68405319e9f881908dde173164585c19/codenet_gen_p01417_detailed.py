import sys
import math
from itertools import combinations

def main():
    # Read the first line containing N (total colors) and M (friends to assign colors)
    input_line = sys.stdin.readline().strip()
    while input_line == '':
        input_line = sys.stdin.readline().strip()
    N, M = map(int, input_line.split())

    colors = []
    # Read the next N lines, each containing L, a, b values for a color in Lab color space
    for _ in range(N):
        line = sys.stdin.readline().strip()
        while line == '':
            line = sys.stdin.readline().strip()
        L, a, b = map(float, line.split())
        colors.append((L, a, b))

    # If M is 1, the maximum total distance among chosen colors is zero since there's only one member/color
    if M == 1:
        print(f"{0.0:.20f}")
        return

    # Precompute distance matrix to avoid recalculating distances multiple times
    # Distance is defined as squared sum of differences of each component
    dist = [[0.0]*N for _ in range(N)]
    for i in range(N):
        L1, a1, b1 = colors[i]
        for j in range(i+1, N):
            L2, a2, b2 = colors[j]
            d = (L1 - L2)**2 + (a1 - a2)**2 + (b1 - b2)**2
            dist[i][j] = d
            dist[j][i] = d  # symmetric

    max_sum_distance = 0.0

    # We need to select M colors out of N such that the sum of all pairwise distances among these M colors is maximized
    # The sum of distances for a combination can be computed by summing dist[i][j] for all pairs i<j in the combination

    # Since N can be up to 20, iterating over all combinations of M from N is feasible:
    # maximum C(20, M) combinations ~ several hundred thousands which is acceptable for a problem of this scale

    # Iterate over all combinations of M colors
    for comb in combinations(range(N), M):
        total = 0.0
        # Sum distances between all pairs inside the combination
        for i in range(M):
            for j in range(i+1, M):
                total += dist[comb[i]][comb[j]]

        # Update maximum sum if this combination is better
        if total > max_sum_distance:
            max_sum_distance = total

    # Output the maximum sum with precision within 10^{-5}
    print(f"{max_sum_distance:.20f}")

if __name__ == "__main__":
    main()