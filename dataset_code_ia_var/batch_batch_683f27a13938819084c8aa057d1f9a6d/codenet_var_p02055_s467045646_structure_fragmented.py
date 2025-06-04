def read_N_and_R():
    N, R = map(int, input().split())
    return N, R

def adjust_R(N, R):
    if 2 * R > N:
        R = N - R
    return R

def read_P(N):
    nums = list(map(int, input().split()))
    return [0] + nums

def cycle_lengths(N, P):
    used = [False] * (N + 1)
    lengths = []
    for i in range(1, N + 1):
        cnt = 0
        j = i
        while not used[j]:
            used[j] = True
            cnt += 1
            j = P[j]
        if cnt:
            lengths.append(cnt)
    return lengths

def build_table(N, lengths):
    table = [0] * (N + 1)
    for l in lengths:
        table[l] += 1
    return table

def try_append_single(L, x, i):
    if x == 1:
        L.append(i)
    else:
        L.append(i)

def process_groups(N, R, table):
    L = []
    for i in range(1, min(R, N // 2) + 1):
        x = table[i]
        if not x:
            continue
        try_append_single(L, x, i)
        if x > 1:
            p = 2
            while 2 * p <= x:
                table[p * i] += 1
                p *= 2
            if x == p:
                L.append(i)
            table[i * (x - p + 1)] += 1
    return L

def compute_H(L):
    H = 1
    for l in L:
        H = H | (H << l)
    return H

def has_subset_sum(H, R):
    return (H & (1 << R)) != 0

def output_result(result):
    if result:
        print('Yes')
    else:
        print('No')

def main():
    N, R = read_N_and_R()
    R = adjust_R(N, R)
    P = read_P(N)
    lengths = cycle_lengths(N, P)
    table = build_table(N, lengths)
    L = process_groups(N, R, table)
    H = compute_H(L)
    result = has_subset_sum(H, R)
    output_result(result)

main()