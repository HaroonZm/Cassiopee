import sys
sys.setrecursionlimit(10**7)
from typing import List, Tuple, Callable, Optional, Iterator

MOD = 10**9 + 7

class Permutation:
    def __init__(self, mapping: List[int]):
        self.n = len(mapping)
        self.mapping = mapping  # 0-based internally
        self._validate_permutation()

    def _validate_permutation(self):
        assert sorted(self.mapping) == list(range(self.n)), "Invalid permutation"

    def compose(self, other: 'Permutation') -> 'Permutation':
        # Compose self after other: f(g(x))
        composed_map = [self.mapping[other.mapping[i]] for i in range(self.n)]
        return Permutation(composed_map)

    def power(self, exponent: int) -> 'Permutation':
        # exponentiation by squaring
        result = Permutation(list(range(self.n)))
        base = self
        exp = exponent
        while exp > 0:
            if exp & 1:
                result = result.compose(base)
            base = base.compose(base)
            exp >>= 1
        return result

    def is_identity_on_range(self, l: int, r: int) -> bool:
        # Check if sub-permutation on [l, r) is identity on that segment
        # l,r are zero-based indices; inclusive l, exclusive r
        for i in range(l, r):
            if self.mapping[i] != i:
                return False
        return True

    def subarray(self, l: int, r: int) -> List[int]:
        # return subarray mapping from l to r-1 as 1-based indices
        return [x + 1 for x in self.mapping[l:r]]

    def sum_range(self, l: int, r: int) -> int:
        # sum of x(l) to x(r), zero-based indexing
        return sum(x + 1 for x in self.mapping[l:r])

    def __repr__(self):
        # for debugging - show as 1-based permutation
        return f"Permutation({[x+1 for x in self.mapping]})"


class PermutationSequence:
    """
    Represents the infinite sequence (x^0, x^1, x^2, ...) where
    x^0 = identity permutation,
    x^{k+1} = p ◦ x^k,
    with fixed p.
    Provides fast random access to x^k via binary lifting.
    """
    def __init__(self, base_perm: Permutation, max_power: int = 40):
        self.n = base_perm.n
        self.max_power = max_power
        self.base_perm = base_perm
        # Precompute powers of p: p^{2^i}
        self.powers = [None] * (self.max_power + 1)
        self.powers[0] = base_perm
        for i in range(1, self.max_power + 1):
            self.powers[i] = self.powers[i-1].compose(self.powers[i-1])

    def at(self, k: int) -> Permutation:
        # Compute p^k efficiently via binary lifting
        result = Permutation(list(range(self.n)))  # identity
        bit_pos = 0
        curr_k = k
        while curr_k > 0:
            if curr_k & 1:
                result = self.powers[bit_pos].compose(result)
            curr_k >>= 1
            bit_pos += 1
        return result


class QueryProcessor:
    """
    Processes queries on the permuted sequence x^t
    according to problem statement, maintaining the state and iterating
    as needed, efficiently.
    """
    def __init__(self, n: int, p_list: List[int], queries: List[Tuple[int,int]]):
        # p_list is 1-based permutation; internally 0-based
        self.n = n
        self.p = Permutation([x-1 for x in p_list])
        self.queries = queries
        self.mod = MOD
        self.seq = PermutationSequence(self.p)
        # As per problem, x^0 = identity and then updated per query

    def process_queries(self) -> Iterator[int]:
        # initial state x^0 = identity
        current_state_index = 0
        for (li, ri) in self.queries:
            l0 = li - 1
            r0 = ri
            ret = 0
            while True:
                # x^{current_state_index} is current state
                current_perm = self.seq.at(current_state_index)
                ret += current_perm.sum_range(l0, r0)
                if current_perm.is_identity_on_range(l0, r0):
                    yield ret % self.mod
                    break
                else:
                    current_state_index += 1


def main():
    input = sys.stdin.readline
    N,Q = map(int,input().split())
    p = [int(input()) for _ in range(N)]
    queries = [tuple(map(int,input().split())) for _ in range(Q)]
    processor = QueryProcessor(N,p,queries)
    outputs = processor.process_queries()
    print('\n'.join(map(str, outputs)))

if __name__ == '__main__':
    main()