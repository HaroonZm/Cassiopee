def read_input():
    return int(input())

def get_inf():
    return float("inf")

def init_dp(size, inf):
    return [[inf] * size for _ in range(size)]

def base_case_dp(dp, a, b):
    if b == 0:
        if a == 0:
            return 0
        else:
            return 1
    return None

def assign_dp_dpab_eq(dp, a, b):
    if a == b:
        return 0
    return None

def update_dp_break(dp, a, b, i, dp_val):
    if dp_val <= 50 or a % i == b:
        return i
    return None

def fill_dp_loop(size, dp):
    for b in range(size):
        for a in range(size):
            res = base_case_dp(dp, a, b)
            if res is not None:
                dp[a][b] = res
            elif b > 0:
                for i in range(1, a + 1):
                    if assign_dp_dpab_eq(dp, a, b) == 0:
                        dp[a][b] = 0
                        break
                    dp_val = dp[a % i][b]
                    result = update_dp_break(dp, a, b, i, dp_val)
                    if result is not None:
                        dp[a][b] = result
                        break

def read_list():
    return [int(i) for i in input().split()]

def build_stack(a, N):
    return [[a[i]] for i in range(N)]

def create_visited(size):
    return [False] * size

def process_stack_mod(stack_i, j, x, visited):
    visited[j] = True
    mod_result = j % x
    if not visited[mod_result]:
        stack_i.append(mod_result)
        visited[mod_result] = True

def update_k(N, stack, b, dp):
    k = 0
    for i in range(N):
        values = [dp[j][b[i]] for j in stack[i]]
        if values:
            k = max(k, min(values))
    return k

def get_M(N, a, b, dp):
    max_val = 0
    for i in range(N):
        v = dp[a[i]][b[i]]
        if v > max_val:
            max_val = v
    return max_val

def dfs(x, N, b, dp, stack, ans_ref):
    if x == 0:
        return
    ans_ref[0] += 2 ** x
    for i in range(N):
        visited = create_visited(51)
        for j in stack[i][:]:
            process_stack_mod(stack[i], j, x, visited)
    k = update_k(N, stack, b, dp)
    if k == 0:
        return
    dfs(k, N, b, dp, stack, ans_ref)

def print_or_exit(M):
    if M > 50:
        print(-1)
        exit()

def main():
    N = read_input()
    inf = get_inf()
    dp = init_dp(51, inf)
    fill_dp_loop(51, dp)
    a = read_list()
    b = read_list()
    ans_ref = [0]
    stack = build_stack(a, N)
    M = get_M(N, a, b, dp)
    print_or_exit(M)
    dfs(M, N, b, dp, stack, ans_ref)
    print(ans_ref[0])

main()