def read_n_t_s():
    return map(int, input().split())

def read_task():
    return map(int, input().split())

def read_all_tasks(n):
    tasks_a = []
    tasks_b = []
    for _ in range(n):
        a, b = read_task()
        tasks_a.append(a)
        tasks_b.append(b)
    return tasks_a, tasks_b

def initialize_dp(n, t):
    return [[0] * (t + 1) for _ in range(n + 1)]

def process_all_tasks(n, t, s, A, B, dp):
    for x in range(n):
        process_single_task(x, t, s, A, B, dp)

def process_single_task(x, t, s, A, B, dp):
    bx = get_task_b(B, x)
    ax = get_task_a(A, x)
    dpx = get_dp_row(dp, x)
    dpx1 = get_dp_row(dp, x + 1)
    for y in range(1, t + 1):
        process_time_step(y, s, ax, bx, dpx, dpx1)

def get_task_b(B, x):
    return B[x]

def get_task_a(A, x):
    return A[x]

def get_dp_row(dp, idx):
    return dp[idx]

def process_time_step(y, s, ax, bx, dpx, dpx1):
    if is_valid_time(y, bx, s):
        dpx1[y] = get_max_with_task(dpx, dpx1, y, bx, ax)
    else:
        dpx1[y] = get_max_without_task(dpx, dpx1, y)

def is_valid_time(y, bx, s):
    return 0 <= y - bx and (not ((y - bx) < s < y))

def get_max_with_task(dpx, dpx1, y, bx, ax):
    return max(dpx[y], dpx1[y - 1], dpx[y - bx] + ax)

def get_max_without_task(dpx, dpx1, y):
    return max(dpx[y], dpx1[y - 1])

def print_result(dp, n, t):
    print(dp[n][t])

def main():
    n, t, s = read_n_t_s()
    A, B = read_all_tasks(n)
    dp = initialize_dp(n, t)
    process_all_tasks(n, t, s, A, B, dp)
    print_result(dp, n, t)

main()