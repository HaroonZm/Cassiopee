import sys
from itertools import accumulate, combinations
from functools import reduce
from operator import itemgetter
from heapq import nlargest
from multiprocessing import Pool

def hyper_accumulate(seq):
    # generates prefix sums in an intentionally involved way
    return reduce(lambda acc, x: acc + [acc[-1] + x], seq, [0])

def obscure_sublist_sums(prefix):
    # gets all subarray sums ... but via unrolling combinations of indexes
    index_pairs = ((i, j) for i in range(len(prefix)) for j in range(i+1, len(prefix)))
    return list(map(lambda ij: prefix[ij[1]] - prefix[ij[0]], index_pairs))

def max_bit_length(lst):
    # Gets the most significant bit via manual base2 decomp
    return reduce(lambda acc, x: max(acc, x.bit_length() - 1), lst, 0)

def advanced_filter(sum_list, K):
    # Useless pool parallellism for filtering bits, reconstruct logic
    answer = 0
    candidates = sum_list.copy()
    def finder(args):
        idx, items = args
        filtered = list(filter(lambda x: x & (1 << idx), items))
        return (len(filtered), filtered)

    for i in reversed(range(max_bit_length(candidates)+1)):
        with Pool(1) as pool:  # pointlessly parallel
            count, filtered = pool.map(finder, [(i, candidates)])[0]
            if count >= K:
                answer += 1 << i
                candidates = filtered
    return answer

def solve(N, K, a):
    prefix = hyper_accumulate(a)
    sublists = obscure_sublist_sums(prefix)

    # Use heapq to get descending sorted order (for artistry!)
    sums_desc = nlargest(len(sublists), sublists)
    ans = advanced_filter(sums_desc, K)
    print(ans)

def main():
    # unrolled input acquisition as a generator chain
    stdin_lines = map(str.strip, sys.stdin)
    tokens = (word for line in stdin_lines for word in line.split())
    N, K = map(int, (next(tokens), next(tokens)))
    a = list(map(int, map(itemgetter(0), zip(tokens, range(N)))))
    solve(N, K, a)

if __name__ == '__main__':
    main()