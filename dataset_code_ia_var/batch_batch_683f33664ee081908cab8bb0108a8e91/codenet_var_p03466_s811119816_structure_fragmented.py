import math

def read_int():
    return int(input())

def read_ints():
    return list(map(int, input().split()))

def calc_K(A, B):
    return math.ceil(max(A, B) / (min(A, B) + 1))

def num(x, K):
    return (x, max(0, (x - 1) // K))

def sub(xs, ys):
    return [x - y for (x, y) in zip(xs, ys)]

def binary_search(A, B, K):
    l, r = 0, A + 1
    while r - l > 1:
        m = (l + r) // 2
        rA, rB = get_sub_for_m(A, B, K, m)
        if check_condition(rA, rB, K):
            l = m
        else:
            r = m
    return l

def get_sub_for_m(A, B, K, m):
    na, nb = num(m, K)
    sa, sb = sub((A, B), (na, nb))
    return sa, sb

def check_condition(rA, rB, K):
    return (rA + 1) * K < rB

def create_string(A, B, C, D, K, l):
    s = ''
    for i in range(C - 1, D):
        s += get_char_for_index(A, B, K, l, i)
    return s

def in_first_part(i, na, nb):
    return i < na + nb

def calc_na_nb(K, l):
    return num(l, K)

def calc_nb_na(B, nb, K):
    return num(B - nb, K)

def first_case(i, na, nb, K):
    if i < nb * (K + 1):
        return pick_char(i, K, 'A', 'B')
    else:
        return 'A'

def second_case(j, na, nb, K):
    if j < na * (K + 1):
        return pick_char(j, K, 'B', 'A')
    else:
        return 'B'

def pick_char(i, K, first, second):
    return second if i % (K + 1) == K else first

def get_char_for_index(A, B, K, l, i):
    na, nb = calc_na_nb(K, l)
    if in_first_part(i, na, nb):
        return first_case(i, na, nb, K)
    else:
        nb2, na2 = calc_nb_na(B, nb, K)
        j = A + B - i - 1
        return second_case(j, na2, nb2, K)

def process_query(A, B, C, D):
    K = calc_K(A, B)
    l = binary_search(A, B, K)
    return create_string(A, B, C, D, K, l)

def main():
    Q = read_int()
    for _ in range(Q):
        A, B, C, D = read_ints()
        result = process_query(A, B, C, D)
        print(result)

main()