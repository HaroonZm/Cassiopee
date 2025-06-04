def read_input():
    k, q = map(int, input().split())
    d = list(map(int, input().split()))
    return k, q, d

def read_query():
    n, x, m = map(int, input().split())
    return n, x, m

def get_repetition_parts(n, k):
    rep, rest = divmod(n - 1, k)
    return rep, rest

def mods_sequence(d, m):
    return [num % m for num in d]

def get_partial_sum(seq, count):
    from itertools import islice
    return sum(islice(seq, 0, count))

def get_num_zero_elements(mod_seq, rep, rest):
    eq = 0
    for i, gg in enumerate(mod_seq):
        times = rep + (1 if i < rest else 0)
        if gg == 0:
            eq += times
    return eq

def get_last_value(x, total_sum, rep, partial_sum):
    return x + (total_sum * rep) + partial_sum

def get_sum(seq):
    return sum(seq)

def calculate_answer(n, eq, last, m, x):
    return (n - 1) - eq - ((last // m) - (x // m))

def handle_single_query(k, d, n, x, m):
    mod_seq = mods_sequence(d, m)
    rep, rest = get_repetition_parts(n, k)
    total_sum = get_sum(mod_seq)
    partial_sum = get_partial_sum(mod_seq, rest)
    last = get_last_value(x, total_sum, rep, partial_sum)
    eq = get_num_zero_elements(mod_seq, rep, rest)
    ans = calculate_answer(n, eq, last, m, x)
    return ans

def solve():
    k, q, d = read_input()
    results = []
    for _ in range(q):
        n, x, m = read_query()
        ans = handle_single_query(k, d, n, x, m)
        results.append(ans)
    return results

def print_output(results):
    for res in results:
        print(res)

def main():
    results = solve()
    print_output(results)

if __name__ == '__main__':
    main()