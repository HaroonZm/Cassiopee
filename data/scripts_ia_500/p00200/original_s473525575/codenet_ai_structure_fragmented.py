inf = 0x10101010

def initialize_cost(m):
    return [inf]*m

def initialize_visited(m):
    return [False]*m

def find_next_node(visited, cost, A, strt, m):
    min_cost = inf
    next_node = -1
    for i in range(m):
        if visited[i]:
            continue
        if A[strt][i]:
            d = cost[strt] + A[strt][i]
            if d < cost[i]:
                cost[i] = d
        if cost[i] < min_cost:
            min_cost = cost[i]
            next_node = i
    return next_node

def update_visited(visited, node):
    visited[node] = True

def solve(A, strt, m):
    cost = initialize_cost(m)
    visited = initialize_visited(m)
    cost[strt] = 0
    while True:
        update_visited(visited, strt)
        next_node = find_next_node(visited, cost, A, strt, m)
        strt = next_node
        if next_node == -1:
            break
    return cost

def read_ints():
    return map(int, raw_input().split())

def create_matrix(m):
    matrix = []
    for _ in range(m):
        matrix.append([0]*m)
    return matrix

def fill_matrices(n, m, T, C):
    for _ in range(n):
        a,b,c,t = read_ints()
        a -= 1
        b -= 1
        T[a][b] = t
        T[b][a] = t
        C[a][b] = c
        C[b][a] = c

def compute_all_solutions(matrix, m):
    solutions = []
    for i in range(m):
        solutions.append(solve(matrix, i, m))
    return solutions

def process_queries(q, TS, CS):
    for _ in range(q):
        a,b,q_val = read_ints()
        a -= 1
        b -= 1
        if q_val == 0:
            print CS[a][b]
        else:
            print TS[a][b]

def main():
    while True:
        n,m = read_ints()
        if n == 0:
            break
        T = create_matrix(m)
        C = create_matrix(m)
        fill_matrices(n, m, T, C)
        TS = compute_all_solutions(T, m)
        CS = compute_all_solutions(C, m)
        q = int(raw_input())
        process_queries(q, TS, CS)

main()