from heapq import heappush, heappop

def read_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def initialize_dist(N, M, INF):
    return [[INF] * (M + 1) for _ in range(N + 1)]

def initialize_queue():
    return [(0, 0, 1)]

def is_finished(i, N):
    return i == N

def is_better(cost, recorded_cost):
    return recorded_cost + 1e-10 < cost

def extract_element(A, i):
    return A[i]

def range_k(p, M):
    return range(p, M + 1, p)

def calculate_d(cost, k, a):
    return max(cost, abs(k - a) / a)

def need_update(d, old_d):
    return d < old_d

def update_queue(que, d, i, k):
    heappush(que, (d, i + 1, k))

def loop_steps(A, dist, que, N, M):
    while que:
        cost, i, p = heappop(que)
        if is_finished(i, N):
            return
        if is_better(cost, dist[i][p]):
            continue
        a = extract_element(A, i)
        for k in range_k(p, M):
            d = calculate_d(cost, k, a)
            if need_update(d, dist[i + 1][k]):
                dist[i + 1][k] = d
                update_queue(que, d, i, k)

def solve():
    N, A = read_input()
    M = 2 * 10 ** 5
    INF = 10 ** 18
    dist = initialize_dist(N, M, INF)
    que = initialize_queue()
    loop_steps(A, dist, que, N, M)
    return min(dist[N])

def print_result(result):
    print("%.16f" % result)

def main():
    res = solve()
    print_result(res)

main()