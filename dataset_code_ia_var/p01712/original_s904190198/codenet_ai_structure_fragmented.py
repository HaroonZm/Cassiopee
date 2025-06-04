def read_input():
    return [int(i) for i in input().split()]

def read_single_input_set(n):
    return [[int(i) for i in input().split()] for _ in range(n)]

def init_imos(N):
    return [0] * (N + 2)

def get_max_zero(val):
    return max(0, val)

def get_min_high(val, high):
    return min(high + 1, val)

def update_imos_h(imos_h, y, w, H):
    idx_start = get_max_zero(y - w)
    idx_end = get_min_high(y + w, H)
    imos_h[idx_start] += 1
    imos_h[idx_end] -= 1

def update_imos_w(imos_w, x, w, W):
    idx_start = get_max_zero(x - w)
    idx_end = get_min_high(x + w, W)
    imos_w[idx_start] += 1
    imos_w[idx_end] -= 1

def apply_updates(X, imos_h, imos_w, H, W):
    for x, y, w in X:
        update_imos_h(imos_h, y, w, H)
        update_imos_w(imos_w, x, w, W)

def compute_prefix(arr, N):
    for i in range(N):
        arr[i + 1] += arr[i]

def check_all_covered(arr, N):
    return all(arr[i] >= 1 for i in range(N))

def print_result(is_h, is_w):
    if is_h or is_w:
        print('Yes')
    else:
        print('No')

def main():
    nwh = read_input()
    n, W, H = nwh
    X = read_single_input_set(n)
    imos_h = init_imos(H)
    imos_w = init_imos(W)
    apply_updates(X, imos_h, imos_w, H, W)
    compute_prefix(imos_h, H)
    compute_prefix(imos_w, W)
    is_w = check_all_covered(imos_w, W)
    is_h = check_all_covered(imos_h, H)
    print_result(is_h, is_w)

main()