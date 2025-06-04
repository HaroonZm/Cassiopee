import sys

def get_input():
    return sys.stdin.readline

def parse_first_line(input_func):
    return map(int, input_func().split())

def parse_d_list(input_func):
    return list(map(int, input_func().split()))

def run_query_line(input_func):
    return map(int, input_func().split())

def mod_list(D, m, K):
    return [D[i] % m for i in range(K)]

def compute_smda_mda0(md, K, limit):
    smda = 0
    mda0 = 0
    for i in range(limit):
        if md[i] == 0:
            mda0 += 1
        smda += md[i]
    return smda, mda0

def compute_smd_md0(md, K, start):
    smd = 0
    md0 = 0
    for i in range(start, K):
        if md[i] == 0:
            md0 += 1
        smd += md[i]
    return smd, md0

def sum_md(md):
    return sum(md)

def compute_roop(n, K):
    return (n - 1) // K

def compute_modulo(val, m):
    return val % m

def calc_result(n, x, m, sum_md_val, roop, smda, md0, mda0):
    numerator = x % m + sum_md_val * roop + smda
    term1 = (numerator) // m
    term2 = md0 * roop
    term3 = mda0
    return n - 1 - term1 - term2 - term3

def process_single_query(D, K, n, x, m):
    md = mod_list(D, m, K)
    limit = (n - 1) % K
    smda, mda0 = compute_smda_mda0(md, K, limit)
    smd, md0 = compute_smd_md0(md, K, limit)
    sum_md_val = sum_md(md)
    roop = compute_roop(n, K)
    result = calc_result(n, x, m, sum_md_val, roop, smda, md0, mda0)
    return result

def process_queries(Q, D, K, input_func):
    for _ in range(Q):
        n, x, m = run_query_line(input_func)
        result = process_single_query(D, K, n, x, m)
        print(result)

def main():
    input_func = get_input()
    K, Q = parse_first_line(input_func)
    D = parse_d_list(input_func)
    process_queries(Q, D, K, input_func)

main()