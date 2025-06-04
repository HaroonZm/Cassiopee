import sys

def read_input():
    return map(int, input().split())

def adjust_R(N, R):
    if 2 * R > N:
        R = N - R
    return R

def read_P(N):
    return [0] + list(map(int, input().split()))

def find_cycle_lengths(P, N):
    used = [False] * (N + 1)
    cycle_lengths = []
    for i in range(1, N + 1):
        cnt = count_cycle(i, P, used)
        if cnt:
            cycle_lengths.append(cnt)
    return cycle_lengths

def count_cycle(start, P, used):
    cnt = 0
    i = start
    while not used[i]:
        used[i] = True
        cnt += 1
        i = P[i]
    return cnt

def build_length_table(L, N):
    table = [0] * (N + 1)
    for l in L:
        table[l] += 1
    return table

def decompose_cycles(table, N):
    decomposed = []
    for i in range(N // 2, 0, -1):
        x = table[i]
        if not x:
            continue
        process_cycle_count(i, x, decomposed)
    return decomposed

def process_cycle_count(length, count, decomposed):
    if count == 1:
        decomposed.append(length)
    else:
        p = 1
        while p + p <= count:
            decomposed.append(p * length)
            p = p + p
        if count - p + 1:
            decomposed.append(length * (count - p + 1))

def filter_and_sort(L, R):
    return sorted([l for l in L if l <= R])

def subset_sum_possible(L, R):
    H = 1
    for l in L:
        H = H | (H << l)
    return bool(H & (1 << R))

def solve():
    N, R = read_input()
    R = adjust_R(N, R)
    P = read_P(N)
    L = find_cycle_lengths(P, N)
    table = build_length_table(L, N)
    decomposed = decompose_cycles(table, N)
    relevant = filter_and_sort(decomposed, R)
    if subset_sum_possible(relevant, R):
        print('Yes')
    else:
        print('No')

solve()