def read_N():
    return int(input())

def read_S(N):
    return [input() for _ in range(N)]

def compute_indices(i, j, k, N):
    return (j + k) % N, (i + k) % N

def compare_elements(S, i, j, k, N):
    idx1, idx2 = compute_indices(i, j, k, N)
    return S[i][idx1] == S[j][idx2]

def check_single_k(S, N, k):
    flag = True
    for i in range(N):
        if not check_inner_loop(S, N, k, i):
            flag = False
            break
    return flag

def check_inner_loop(S, N, k, i):
    for j in range(i + 1, N):
        if not compare_elements(S, i, j, k, N):
            return False
    return True

def process_k(S, N):
    total = 0
    for k in range(N):
        if check_single_k(S, N, k):
            total += N
    return total

def main():
    N = read_N()
    S = read_S(N)
    ans = process_k(S, N)
    print(ans)

main()