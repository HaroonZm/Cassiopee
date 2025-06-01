def read_input():
    N, M = map(int, input().split())
    return N, M

def initialize_D(M, N):
    return [[0] * (N + 1) for _ in range(M)]

def initialize_cnts(M):
    return [0] * M

def read_values_and_update_D_cnts(N, M, D, cnts):
    for i in range(N):
        v = int(input())
        update_cnts(cnts, v)
        update_D(D, v, i)
        
def update_cnts(cnts, v):
    cnts[v - 1] += 1

def update_D(D, v, index):
    D[v - 1][index + 1] = 1

def prefix_sum_D(M, N, D):
    for i in range(M):
        update_prefix_sum(D[i], N)

def update_prefix_sum(d, N):
    for j in range(1, N + 1):
        d[j] += d[j - 1]

def initialize_memo(M):
    size = 2 ** M
    memo = [None] * size
    memo[size - 1] = 0
    return memo

def calculate_need(cnts, D, i, idx):
    length = cnts[i]
    segment = D[i][length + idx] - D[i][idx]
    return length - segment

def dfs(state, idx, N, M, cnts, D, memo):
    if check_memo(memo, state):
        return memo[state]
    res = N
    for i in range(M):
        if check_state_bit(state, i) == False:
            need = calculate_need(cnts, D, i, idx)
            candidate = need + dfs(update_state(state, i), idx + cnts[i], N, M, cnts, D, memo)
            res = min(res, candidate)
    memo[state] = res
    return res

def check_memo(memo, state):
    return memo[state] is not None

def check_state_bit(state, i):
    return (state & (1 << i)) != 0

def update_state(state, i):
    return state | (1 << i)

def main():
    N, M = read_input()
    D = initialize_D(M, N)
    cnts = initialize_cnts(M)
    read_values_and_update_D_cnts(N, M, D, cnts)
    prefix_sum_D(M, N, D)
    memo = initialize_memo(M)
    result = dfs(0, 0, N, M, cnts, D, memo)
    print(result)

main()