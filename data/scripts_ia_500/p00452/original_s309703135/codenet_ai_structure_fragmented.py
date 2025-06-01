import bisect
import sys

def set_recursion_limit():
    sys.setrecursionlimit(10**9)

def get_input():
    return sys.stdin.readline()

def read_N_M():
    line = get_input()
    return map(int, line.split())

def read_N():
    N, _ = read_N_M()
    return N

def read_M():
    _, M = read_N_M()
    return M

def read_N_and_M():
    return map(int, get_input().split())

def read_P(N):
    return [0] + [int(get_input()) for _ in range(N)]

def generate_pairs_sums(P, N):
    pairs = []
    for i in range(N):
        for j in range(i, N):
            pairs.append(P[i] + P[j])
    return pairs

def sort_list(lst):
    lst.sort()
    return lst

def find_upper_bound(k, value):
    return bisect.bisect_right(k, value)

def compute_result(k, M):
    ret = 0
    length = len(k)
    for tmp in k:
        if tmp > M:
            break
        r = M - tmp
        l = find_upper_bound(k, r)
        if l >= length:
            current_sum = tmp + k[-1]
        elif l != 0:
            current_sum = tmp + k[l-1]
        else:
            current_sum = tmp
        if current_sum > ret:
            ret = current_sum
    return ret

def is_zero(N, M):
    return N * M == 0

def solve_once():
    N, M = read_N_and_M()
    if is_zero(N, M):
        return False
    P = read_P(N)
    k = generate_pairs_sums(P, N)
    k = sort_list(k)
    result = compute_result(k, M)
    return result

def main_loop():
    ans = []
    while True:
        ret = solve_once()
        if ret:
            ans.append(ret)
        else:
            break
    return ans

def print_answers(ans):
    print("\n".join(map(str, ans)))

def main():
    set_recursion_limit()
    answers = main_loop()
    print_answers(answers)

main()