def read_input():
    data = list(map(int, open(0).read().split()))
    return data

def parse_input(data):
    N = data[0]
    K = data[1]
    L = data[2]
    A = data[3:]
    return N, K, L, A

def is_valid(a, x):
    return a <= x

def build_R(A, X):
    R = []
    for t, a in enumerate(A):
        if is_valid(a, X):
            R.append(t)
    return R

def count_segments(R, K):
    res = 0
    for idx in range(len(R)):
        if idx+1 >= K:
            res += R[idx-K+1]+1
    return res

def solve_core(A, K, L, X):
    R = []
    res = 0
    for t, a in enumerate(A):
        if is_valid(a, X):
            R.append(t)
        if len(R) >= K:
            res += R[-K]+1
    return res

def solve(A, K, L, X):
    R = []
    res = 0
    for t, a in enumerate(A):
        if is_valid(a, X):
            R.append(t)
        if len(R) >= K:
            res += R[-K]+1
    return res >= L

def get_mid(left, right):
    return (left + right) >> 1

def main():
    data = read_input()
    N, K, L, A = parse_input(data)
    left = 0
    right = N
    while not binary_search_done(left, right):
        mid = get_mid(left, right)
        if test_solve(A, K, L, mid):
            right = mid
        else:
            left = mid
    output_result(right)

def binary_search_done(left, right):
    return left+1 >= right

def test_solve(A, K, L, mid):
    return solve(A, K, L, mid)

def output_result(result):
    print(result)

main()