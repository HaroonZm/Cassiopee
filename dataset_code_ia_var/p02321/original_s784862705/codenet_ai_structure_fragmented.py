from heapq import heappush, heappop

def read_ints():
    return map(int, input().rstrip().split())

def read_input():
    N, W = read_ints()
    items = [list(read_ints()) for _ in range(N)]
    return N, W, items

def sort_items(items):
    return sorted(items, key=lambda x: x[0] / x[1], reverse=True)

def compute_upper_bounds(S, W, N, w, v, i):
    for j in range(i, N):
        vj, wj = S[j]
        if w + wj > W:
            return upper_bounds_partial(v, vj, wj, W, w)
        w, v = update_weight_value(w, v, wj, vj)
    return upper_bounds_final(v)

def upper_bounds_partial(v, vj, wj, W, w):
    return (-v, -v - vj / wj * (W - w))

def update_weight_value(w, v, wj, vj):
    return w + wj, v + vj

def upper_bounds_final(v):
    return (-v, -v)

def push_initial(q, v1, v2):
    heappush(q, (v2, v1, 0, 0, 0))

def process_queue(q, N, W, S, vm1):
    while not is_queue_empty(q):
        vq1, vq2, wq, vq, i = heappop(q)
        if is_end(i, N):
            continue
        vi, wi = get_item(S, i)
        if can_take_item(wq, wi, W):
            push_with_item(q, vq1, wq, wi, vq, vi, i)
        v1, v2 = compute_upper_bounds(S, W, N, wq, vq, i + 1)
        if v2 < vm1:
            if should_update_vm1(v1, vm1):
                vm1 = v1
            push_without_item(q, v2, v1, wq, vq, i)
    return vm1

def is_queue_empty(q):
    return not q

def is_end(i, N):
    return i == N

def get_item(S, i):
    return S[i]

def can_take_item(wq, wi, W):
    return wq + wi <= W

def push_with_item(q, vq1, wq, wi, vq, vi, i):
    heappush(q, (vq1, vq1, wq + wi, vq + vi, i + 1))

def should_update_vm1(v1, vm1):
    return v1 < vm1

def push_without_item(q, v2, v1, wq, vq, i):
    heappush(q, (v2, v1, wq, vq, i + 1))

def print_result(vm1):
    print(-vm1)

def resolve():
    N, W, items = read_input()
    S = sort_items(items)
    v1, v2 = compute_upper_bounds(S, W, N, 0, 0, 0)
    q = []
    push_initial(q, v1, v2)
    vm1 = v1
    vm1 = process_queue(q, N, W, S, vm1)
    print_result(vm1)

if __name__ == "__main__":
    resolve()