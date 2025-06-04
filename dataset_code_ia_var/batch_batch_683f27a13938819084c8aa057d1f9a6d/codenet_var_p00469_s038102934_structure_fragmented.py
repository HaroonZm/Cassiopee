def get_input():
    return input()

def is_end_signal(e):
    return e == '0'

def parse_int(e):
    return int(e)

def get_n_and_k():
    e = get_input()
    if is_end_signal(e):
        return None, None, True
    n = parse_int(e)
    k = parse_int(get_input())
    return n, k, False

def create_list(n):
    result = []
    for _ in [0] * n:
        result.append(get_input())
    return result

def generate_permutations(lst, k):
    from itertools import permutations as perm
    return perm(lst, k)

def join_permutation(p):
    return ''.join(p)

def get_unique_joined_permutations(perms):
    unique = set()
    for p in perms:
        joined = join_permutation(p)
        unique.add(joined)
    return unique

def process_case(n, k):
    C = create_list(n)
    perms = generate_permutations(C, k)
    unique = get_unique_joined_permutations(perms)
    return len(unique)

def process_inputs():
    while True:
        n, k, end = get_n_and_k()
        if end:
            break
        res = process_case(n, k)
        print(res)

if __name__ == '__main__':
    process_inputs()