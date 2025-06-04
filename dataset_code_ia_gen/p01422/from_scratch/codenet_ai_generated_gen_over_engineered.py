import sys
import math
from typing import List, Tuple, Optional, Callable

class BeautifulCurrencyProblem:
    def __init__(self, coin_values: List[int]):
        self.N = len(coin_values)
        self.original_values = coin_values
        self.sorted_indices = sorted(range(self.N), key=lambda i: coin_values[i])
        self.sorted_values = [coin_values[i] for i in self.sorted_indices]
        
    # Abstracted interface to get coin values in sorted order
    def get_original_sorted_values(self) -> List[int]:
        return self.sorted_values[:]  # Return a copy
    
    # Validate if a candidate solution is beautiful
    @staticmethod
    def is_beautiful(candidate: List[int]) -> bool:
        # candidate is sorted
        for i in range(len(candidate)-1):
            if candidate[i] == 0:
                # zero value coin invalid (must be positive integer)
                return False
            if candidate[i+1] % candidate[i] != 0:
                return False
        return True
    
    # Compute max confusion ratio given final changed values (sorted)
    def max_confusion_ratio(self, modified_sorted: List[int]) -> float:
        max_ratio = 0.0
        for orig_idx, val in zip(self.sorted_indices, modified_sorted):
            orig_val = self.original_values[orig_idx]
            ratio = abs(orig_val - val) / orig_val
            if ratio > max_ratio:
                max_ratio = ratio
        return max_ratio
    
    # Abstract generator of possible candidates with pruning and caching
    # We implement a bounded search trying to find better candidates
    def minimal_max_confusion_ratio(self) -> float:
        # Search strategy:
        # We'll binary search on max confusion ratio (low=0, high=1)
        # For each mid, test if there exists a beautiful sequence within max confusion ratio constraint
        
        # For quick pruning: for each a_i and candidate b_i, abs(b_i - a_i) <= max_ratio * a_i
        # So b_i in [floor(a_i*(1 - max_ratio)), ceil(a_i*(1 + max_ratio))]
        # We search values in these intervals only
        
        def can_build_beautiful(max_ratio: float) -> bool:
            # We want to assign values b_i to sorted coins s.t. max confusion ratio <= max_ratio
            # and beautiful property satisfied
            
            intervals = [
                (math.ceil(val * (1 - max_ratio)), math.floor(val * (1 + max_ratio)))
                for val in self.sorted_values
            ]
            
            # Because values must be positive integers
            for i, (l, r) in enumerate(intervals):
                if r < l or r < 1:
                    return False # no possible value
            
            # Recursive DFS with memoization for efficiency
            memo = {}
            
            def dfs(pos: int, prev_val: Optional[int]) -> bool:
                if pos == self.N:
                    return True
                key = (pos, prev_val)
                if key in memo:
                    return memo[key]
                l, r = intervals[pos]
                l = max(l, 1) # must be positive integer
                # To reduce search space, we generate candidate values b_pos
                # in [l, r] that satisfy divisibility rule with prev_val
                
                # If pos == 0, any value in interval allowed
                candidates = []
                if pos == 0:
                    # We try all possibilities in [l, r], but large interval could be costly
                    # Optimization: only try values close to original to minimize ratios,
                    # but here all in range so we try all (small N problem, at most 20)
                    # But can be large. To optimize, try both floor and ceil of original value
                    orig_v = self.sorted_values[0]
                    options = set()
                    # try values from l to r near orig_v with absolute difference <= max_ratio * orig_v
                    lowbound = max(l, orig_v)
                    highbound = min(r, orig_v)
                    # To limit, generate candidates around orig_v +- some margin
                    # But since interval guaranteed tight by max_ratio, use entire [l,r]
                    # But might be large, so limit candidates
                    if r - l < 100:
                        candidates = list(range(l, r+1))
                    else:
                        # try closest integers to orig_v within range
                        candidates = [orig_v]
                        # also try extremes
                        candidates.append(l)
                        candidates.append(r)
                else:
                    # must satisfy divisibility: b_pos % prev_val == 0
                    start = (l + prev_val - 1)//prev_val * prev_val
                    candidates = []
                    if start <= r:
                        # if candidate range big, limit search to small neighborhood to optimize
                        if (r - start) // prev_val > 100:
                            # try fewer candidates near original
                            orig_v = self.sorted_values[pos]
                            # candidate multiples near orig_v
                            multiples = []
                            base = orig_v // prev_val * prev_val
                            for m in range(base - 5*prev_val, base + 6*prev_val, prev_val):
                                if l <= m <= r and m >= 1:
                                    multiples.append(m)
                            # remove duplicates
                            candidates = list(set(multiples))
                        else:
                            candidates = list(range(start, r+1, prev_val))
                candidates = [c for c in candidates if c >= 1 and l <= c <= r]
                # Sort candidates by absolute difference from original to achieve pruning
                orig_val = self.sorted_values[pos]
                candidates.sort(key=lambda x: abs(x - orig_val))
                
                for c in candidates:
                    if dfs(pos+1, c):
                        memo[key] = True
                        return True
                memo[key] = False
                return False
            
            return dfs(0, None)
        
        low = 0.0
        high = 1.0
        # Because ratio can be up to almost 1 (change from a_i to anything from 0 to 2*a_i)
        # Binary search with precision 1e-10 (sufficient for 1e-8 absolute error final)
        for _ in range(80):
            mid = (low + high) / 2
            if can_build_beautiful(mid):
                high = mid
            else:
                low = mid
        return high


class InputReader:
    def __init__(self, source=sys.stdin):
        self.source = source
    def read_int(self) -> int:
        line = self.source.readline()
        while line.strip() == '':
            line = self.source.readline()
        return int(line.strip())
    def read_int_list(self) -> List[int]:
        line = self.source.readline()
        while line.strip() == '':
            line = self.source.readline()
        return list(map(int, line.strip().split()))

class OutputWriter:
    @staticmethod
    def print_float(value: float):
        # print with sufficient precision for constraints
        print("%.12f" % value)

def main():
    reader = InputReader()
    N = reader.read_int()
    currencies = reader.read_int_list()
    problem = BeautifulCurrencyProblem(currencies)
    result = problem.minimal_max_confusion_ratio()
    OutputWriter.print_float(result)

if __name__ == "__main__":
    main()