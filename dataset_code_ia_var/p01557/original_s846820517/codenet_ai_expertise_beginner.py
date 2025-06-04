import sys

def solve():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(range(1, N+1))

    def get_all_states(start, max_steps):
        from collections import deque
        queue = deque()
        dist = {}
        queue.append((start, 0))
        dist[tuple(start)] = 0

        while queue:
            state, steps = queue.popleft()
            if steps == max_steps:
                continue
            for i in range(N):
                for j in range(i+1, N):
                    new_state = state[:i] + state[i:j+1][::-1] + state[j+1:]
                    t_new = tuple(new_state)
                    if t_new not in dist or dist[t_new] > steps + 1:
                        dist[t_new] = steps + 1
                        queue.append((new_state, steps + 1))
        return dist

    max_half = (N-1)//2
    dist_from_A = get_all_states(A, max_half)
    dist_from_B = get_all_states(B, max_half)
    ans = N - 1
    for key in dist_from_A:
        if key in dist_from_B:
            s = dist_from_A[key] + dist_from_B[key]
            if s < ans:
                ans = s
    print(ans)

solve()