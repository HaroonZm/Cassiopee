def read_input():
    return list(map(int, open(0).read().split()))

def parse_input(data):
    N, K, L, *A = data
    return N, K, L, A

def get_positions(X, A):
    R = []
    for t, a in enumerate(A):
        if a <= X:
            R.append(t)
    return R

def increment_res(R, K):
    if len(R) >= K:
        return R[-K]+1
    return 0

def can_be_solved(X, K, L, A):
    R = []
    res = 0
    for t, a in enumerate(A):
        if a <= X:
            R.append(t)
        res += increment_res(R, K)
    return res >= L

def binary_search(N, K, L, A):
    left = 0
    right = N
    while left + 1 < right:
        mid = (left + right) >> 1
        if can_be_solved(mid, K, L, A):
            right = mid
        else:
            left = mid
    return right

def main():
    data = read_input()
    N, K, L, A = parse_input(data)
    result = binary_search(N, K, L, A)
    print(result)

main()