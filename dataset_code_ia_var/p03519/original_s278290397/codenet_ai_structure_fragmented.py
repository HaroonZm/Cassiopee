import sys
from heapq import heappop, heappush, heapify

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def compute_initial_ls(A, B):
    return [b - a for a, b in zip(A, B)]

def split_qs(ls):
    q_m = [-v for v in ls[1:-1] if v < 0]
    q_p = [v for v in ls[1:-1] if v >= 0]
    return q_m, q_p

def heapify_qs(q_m, q_p):
    heapify(q_m)
    heapify(q_p)

def get_sum_A(A):
    return sum(A)

def get_sum_q_p(q_p):
    return sum(q_p)

def get_odd(q_p):
    return len(q_p) % 2

def adjust_ans_initial(sum_A, sum_q_p, q_p, q_m, odd):
    if odd:
        if not q_p:
            p_min = float('inf')
        else:
            p_min = q_p[0]
        if not q_m:
            m_min = float('inf')
        else:
            m_min = q_m[0]
        return sum_A + sum_q_p - min(p_min, m_min)
    else:
        return sum_A + sum_q_p

def adjust_sum_A(sum_A, new_x, old_x):
    return sum_A + new_x - old_x

def changed_odd(odd, old_v, new_v):
    return odd ^ ((old_v >= 0) ^ (new_v >= 0))

def update_sum_q_p(sum_q_p, old_v, new_v):
    s = sum_q_p
    if new_v >= 0:
        s += new_v
    if old_v >= 0:
        s -= old_v
    return s

def push_to_heaps(q_p, q_m, v):
    if v >= 0:
        heappush(q_p, v)
    else:
        heappush(q_m, -v)

def clean_heap(q, to_remove, sign=1):
    while q and sign*q[0] in to_remove:
        to_remove.remove(sign*heappop(q))

def post_update_ans(sum_q_p, sum_A, odd, q_p, q_m, to_remove):
    val = sum_A + sum_q_p
    if odd:
        clean_heap(q_p, to_remove, 1)
        clean_heap(q_m, to_remove, -1)
        if q_p and q_m:
            val -= min(q_p[0], q_m[0])
        elif q_p:
            val -= q_p[0]
        elif q_m:
            val -= q_m[0]
    return val

def handle_endpoint(A, p, x, ans, Ans):
    ans += x - A[p]
    Ans.append(ans)
    A[p] = x
    return ans

def handle_query(A, ls, p, x, y, q_p, q_m, to_remove, sum_A, sum_q_p, odd, ans, Ans):
    v = y - x
    sum_A = adjust_sum_A(sum_A, x, A[p])
    if p == 0 or p == len(A) - 1:
        ans = handle_endpoint(A, p, x, ans, Ans)
        return ans, sum_A, sum_q_p, odd
    old_v = ls[p]
    A[p] = x
    new_v = v
    odd = changed_odd(odd, old_v, new_v)
    sum_q_p = update_sum_q_p(sum_q_p, old_v, new_v)
    to_remove.add(old_v)
    ls[p] = new_v
    push_to_heaps(q_p, q_m, new_v)
    ans = post_update_ans(sum_q_p, sum_A, odd, q_p, q_m, to_remove)
    Ans.append(ans)
    return ans, sum_A, sum_q_p, odd

def process_queries(N, Q, A, B):
    ls = compute_initial_ls(A, B)
    q_m, q_p = split_qs(ls)
    heapify_qs(q_m, q_p)
    sum_A = get_sum_A(A)
    sum_q_p = get_sum_q_p(q_p)
    to_remove = set()
    odd = get_odd(q_p)
    Ans = []
    ans = adjust_ans_initial(sum_A, sum_q_p, q_p, q_m, odd)
    for _ in range(Q):
        p, x, y = read_ints()
        p -= 1
        ans, sum_A, sum_q_p, odd = handle_query(
            A, ls, p, x, y, q_p, q_m, to_remove, sum_A, sum_q_p, odd, ans, Ans
        )
    return Ans

def main():
    N, Q = read_ints()
    A = read_ints()
    B = read_ints()
    Ans = process_queries(N, Q, A, B)
    print("\n".join(map(str, Ans)))

main()