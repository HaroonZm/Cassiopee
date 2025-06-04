import itertools
import collections

def read_N_M():
    return [int(i) for i in input().split()]

def read_A():
    return [int(i) for i in input().split()]

def compute_prefix_sums(A):
    return [0] + list(itertools.accumulate(A))

def compute_remainders(prefix_sums, M):
    return [x % M for x in prefix_sums]

def count_remainders(remainders):
    d = collections.defaultdict(int)
    for r in remainders:
        d[r] += 1
    return d

def compute_combinations(count):
    if count < 2:
        return 0
    return count * (count - 1) // 2

def sum_combinations_for_remainders(rem_count_dict):
    ans = 0
    for v in rem_count_dict.values():
        ans += compute_combinations(v)
    return ans

def d_candy_distribution(N, M, A):
    prefix_sums = compute_prefix_sums(A)
    remainders = compute_remainders(prefix_sums, M)
    rem_count_dict = count_remainders(remainders)
    ans = sum_combinations_for_remainders(rem_count_dict)
    return ans

def main():
    N, M = read_N_M()
    A = read_A()
    print(d_candy_distribution(N, M, A))

main()