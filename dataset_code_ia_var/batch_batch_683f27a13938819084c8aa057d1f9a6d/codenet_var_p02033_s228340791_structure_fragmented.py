from bisect import bisect_left

def read_input():
    return list(map(int, input().split()))

def get_inputs():
    N, M = read_input()
    X = read_input()
    Q = int(input())
    L = read_input()
    return N, M, X, Q, L

def append_end_marker(X, N):
    return X + [N+1]

def initial_cost(X):
    return X[0] - 1

def compute_gaps(X, M):
    return [X[i+1] - X[i] - 1 for i in range(M) if X[i+1] - X[i] > 1]

def initialize_C(N):
    C = [0]*(N+1)
    C[0] = -10**9
    return C

def update_costs(costs):
    cost = 0
    costs2 = []
    for c in costs:
        cost += c
        if c > 1:
            costs2.append(c-1)
    return cost, costs2

def fill_C(N, initcost, costs):
    C = initialize_C(N)
    cloned_costs = costs[:]
    for i in range(1, N+1):
        cost, cloned_costs = update_costs(cloned_costs)
        C[i] = -(initcost + cost)
    return C

def process_query(C, l):
    if l < -C[-1]:
        return -1
    return bisect_left(C, -l)

def main():
    N, M, X, Q, L = get_inputs()
    X = append_end_marker(X, N)
    initcost = initial_cost(X)
    costs = compute_gaps(X, M)
    C = fill_C(N, initcost, costs)
    for l in L:
        res = process_query(C, l)
        print(res)

main()