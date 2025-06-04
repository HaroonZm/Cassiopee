import itertools

def read_int():
    return int(input())

def read_tuple():
    return tuple(map(int, input().split()))

def get_input():
    N = read_int()
    P = read_tuple()
    Q = read_tuple()
    return N, P, Q

def are_equal(P, Q):
    return P == Q

def construct_pq_list(P, Q):
    return [P, Q]

def sort_pq(PQ):
    return sorted(PQ)

def create_li(N):
    return list(map(lambda x: x + 1, list(range(N))))

def generate_permutations(li, N):
    return itertools.permutations(li, N)

def find_positions(PQ, perms, N):
    i = 0
    j = 0
    a = []
    for v in perms:
        j = increment(j)
        if are_tuples_equal(PQ[i], v):
            a = append_to_list(a, j)
            if is_one(i):
                break_condition = True
                break
            else:
                i = increment(i)
    return a

def increment(x):
    return x + 1

def append_to_list(a, val):
    a.append(val)
    return a

def is_one(i):
    return i == 1

def are_tuples_equal(t1, t2):
    return t1 == t2

def get_difference(a):
    return a[1] - a[0]

def print_result(ans):
    print(ans)

def solve():
    N, P, Q = get_input()
    if are_equal(P, Q):
        ans = 0
    else:
        PQ = construct_pq_list(P, Q)
        PQ = sort_pq(PQ)
        li = create_li(N)
        perms = generate_permutations(li, N)
        a = []
        i = 0
        j = 0
        for v in perms:
            j = increment(j)
            if are_tuples_equal(PQ[i], v):
                a = append_to_list(a, j)
                if is_one(i):
                    break
                else:
                    i = increment(i)
        ans = get_difference(a)
    print_result(ans)

solve()