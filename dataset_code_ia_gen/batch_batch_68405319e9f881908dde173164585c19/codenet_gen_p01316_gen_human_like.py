import sys

def clip(val):
    return max(0, min(255, val))

for line in sys.stdin:
    if not line.strip():
        continue
    N_M = line.strip().split()
    if len(N_M) != 2:
        continue
    N, M = map(int, N_M)
    if N == 0 and M == 0:
        break
    codebook = [int(sys.stdin.readline()) for _ in range(M)]
    x = [int(sys.stdin.readline()) for _ in range(N)]

    # DP: at step i, y_i can be 0..255, store minimal squared error sum
    # and for large N and state space 256, use a dict or list
    # But since states are 0-255, we can use array indexing

    prev_dp = [float('inf')] * 256
    prev_dp[128] = 0  # y_0 = 128

    for i in range(N):
        curr_dp = [float('inf')] * 256
        target = x[i]
        for y_prev in range(256):
            cost_so_far = prev_dp[y_prev]
            if cost_so_far == float('inf'):
                continue
            for c in codebook:
                y_curr = clip(y_prev + c)
                diff = target - y_curr
                new_cost = cost_so_far + diff * diff
                if new_cost < curr_dp[y_curr]:
                    curr_dp[y_curr] = new_cost
        prev_dp = curr_dp

    ans = min(prev_dp)
    print(ans)