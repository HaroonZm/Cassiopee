import sys
from math import isclose

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    colors = [tuple(map(float, input().split())) for _ in range(N)]
    
    # Precompute distances squared between all pairs
    dist = [[0.0]*N for _ in range(N)]
    for i in range(N):
        L1, a1, b1 = colors[i]
        for j in range(i+1, N):
            L2, a2, b2 = colors[j]
            d = (L1 - L2)**2 + (a1 - a2)**2 + (b1 - b2)**2
            dist[i][j] = d
            dist[j][i] = d
    
    # If M == 1, no pairs, distance is zero
    if M == 1 or M == 0:
        print("0.00000000000000000000")
        return
    
    max_sum = 0.0
    
    # Choose M colors out of N to maximize sum of distances between all pairs
    # Since N <= 20 and M <= N, we can generate all combinations
    
    from itertools import combinations
    
    for comb in combinations(range(N), M):
        s = 0.0
        # sum distances between all pairs in comb
        for i in range(M):
            for j in range(i+1, M):
                s += dist[comb[i]][comb[j]]
        if s > max_sum:
            max_sum = s
    
    print(f"{max_sum:.20f}")

if __name__ == "__main__":
    main()