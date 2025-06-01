def read_ints():
    return [int(x) for x in input().split()]

def read_params():
    return read_ints()

def should_stop(n):
    return n == 0

def init_lists(n, m, h):
    A = []
    B = [[] for _ in range(h)]
    C = list(range(n))
    S = [0 for _ in range(n)]
    X = []
    return A, B, C, S, X

def read_A(n):
    A = []
    for _ in range(n):
        A.append(int(input()))
    return A

def read_B(m):
    pairs = []
    for _ in range(m):
        a, b = read_ints()
        pairs.append((a, b))
    return pairs

def fill_B(B, pairs):
    for a, b in pairs:
        B[b].append(a)

def swap_in_C(C, B, X, h):
    for y in range(h):
        for a in B[y]:
            C[a-1:a+1] = [C[a], C[a-1]]
            X.append(sorted(C[a-1:a+1]))

def fill_S(S, C, A):
    for i in range(len(C)):
        S[C[i]] = A[i]

def calculate_ans(S, k):
    return sum(S[:k])

def calculate_tmpdif(X, S, k):
    tmpdif = 0
    for xx in X:
        if xx[0] < k and xx[1] >= k:
            tmpdif = min(tmpdif, S[xx[1]] - S[xx[0]])
    return tmpdif

def process_case():
    n, m, h, k = read_params()
    if should_stop(n):
        return False
    A, B, C, S, X = init_lists(n, m, h)
    A = read_A(n)
    pairs = read_B(m)
    fill_B(B, pairs)
    swap_in_C(C, B, X, h)
    fill_S(S, C, A)
    ans = calculate_ans(S, k)
    tmpdif = calculate_tmpdif(X, S, k)
    print(ans + tmpdif)
    return True

def main():
    while True:
        if not process_case():
            break

main()