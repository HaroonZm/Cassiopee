def invert(p, q):
    def _set_indices(p, q):
        for i, pi in enumerate(p):
            _set_index(pi, i, q)

    def _set_index(pi, i, q):
        q[pi] = i

    _set_indices(p, q)

def swap_if_needed(k, data, first):
    if data[first] - data[first + 1] >= k:
        data[first], data[first + 1] = data[first + 1], data[first]

def handle_too_short(k, data, first, last):
    length = last - first
    if length == 2:
        swap_if_needed(k, data, first)
    return

def insertion_inner(t, v, data, first):
    if data[t] - v < k:
        return t + 1
    if t == first:
        return first
    return insertion_inner(t - 1, v, data, first)

def perform_insertion(t, i, data, v):
    data[t + 1:i + 1] = data[t:i]
    data[t] = v

def do_insertion(k, data, first, last):
    for i in range(first + 1, last):
        v = data[i]
        pos = insertion_inner(i - 1, v, data, first)
        perform_insertion(pos, i, data, v)

def sort_insertion(k, data, first, last):
    length = last - first
    if length <= 2:
        handle_too_short(k, data, first, last)
        return
    do_insertion(k, data, first, last)

def handle_small_merge(k, data, first, last):
    sort_insertion(k, data, first, last)

def get_middle(first, last):
    return (first + last) // 2

def prepare_bounds(data, first, middle):
    bounds = data[first:middle]
    for i in range(len(bounds) - 2, -1, -1):
        bounds[i] = min(bounds[i + 1], bounds[i])
    return bounds

def copy_tmp(data, first, middle):
    return data[first:middle]

def should_use_tmp_array(head1, first_len, head2, last):
    return head1 == first_len or head2 == last

def assign_rest(data, ohead, tmp, head1, first_len):
    data[ohead:ohead + first_len - head1] = tmp[head1:first_len]

def compare_and_assign(data, ohead, bounds, head1, tmp, head2, k):
    if bounds[head1] - data[head2] >= k:
        data[ohead] = data[head2]
        return True
    else:
        data[ohead] = tmp[head1]
        return False

def merge_loop(data, first, last, bounds, tmp, head1, head2, first_len, middle, k):
    ohead = first
    while ohead < last:
        if should_use_tmp_array(head1, first_len, head2, last):
            assign_rest(data, ohead, tmp, head1, first_len)
            return
        if compare_and_assign(data, ohead, bounds, head1, tmp, head2, k):
            head2 += 1
        else:
            head1 += 1
        ohead += 1

def sort_merge(k, data, first, last):
    if last - first < 10:
        handle_small_merge(k, data, first, last)
        return
    middle = get_middle(first, last)
    sort_merge(k, data, first, middle)
    sort_merge(k, data, middle, last)
    bounds = prepare_bounds(data, first, middle)
    tmp = copy_tmp(data, first, middle)
    first_len = middle - first
    head1 = 0
    head2 = middle
    merge_loop(data, first, last, bounds, tmp, head1, head2, first_len, middle, k)

def read_n_and_k():
    parts = input().split(' ')
    n = int(parts[0])
    k = int(parts[1])
    return n, k

def read_p():
    return [int(s) - 1 for s in input().split(' ')]

def make_q(p):
    return list(p)

def process(p, q, k, n):
    invert(p, q)
    sort_merge(k, q, 0, n)
    invert(q, p)

def print_p(p):
    for pi in p:
        print(pi + 1)

def main():
    n, k = read_n_and_k()
    p = read_p()
    q = make_q(p)
    process(p, q, k, n)
    print_p(p)

main()