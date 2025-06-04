from numpy import zeros, roll

def get_inputs():
    n, M = map(int, input().split())
    return n, M

def compute_l(n):
    return n * 3 + 1

def initialize_d(l, n):
    d = zeros((l, n * 5), dtype='int64')
    d[0][0] = 1
    return d

def get_indices(i):
    j = i - 1
    k = i - 2
    return j, k

def compute_term1(d, i, k, j):
    if i < 3:
        return zeros_like_row(d)
    return d[i-3] * k * j

def compute_term2(d, k, j):
    if k < 0:
        return zeros_like_row(d)
    return roll(d[k], -1) * j

def compute_term3(d, j):
    if j < 0:
        return zeros_like_row(d)
    return roll(d[j], 1)

def zeros_like_row(d):
    return zeros(d.shape[1], dtype='int64')

def update_row(d, i, M):
    j, k = get_indices(i)
    term1 = compute_term1(d, i, k, j)
    term2 = compute_term2(d, k, j)
    term3 = compute_term3(d, j)
    d[i] = (term1 + term2 + term3) % M

def process(d, l, M):
    for i in range(1, l):
        update_row(d, i, M)

def final_sum(d, l, M):
    return int(sum(d[-1][:l]) % M)

def main():
    n, M = get_inputs()
    l = compute_l(n)
    d = initialize_d(l, n)
    process(d, l, M)
    result = final_sum(d, l, M)
    print(result)

main()