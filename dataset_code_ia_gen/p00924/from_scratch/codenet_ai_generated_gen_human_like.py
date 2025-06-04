from sys import stdin
from itertools import accumulate

def min_swaps(initial, target):
    # initial and target are lists of positions of bits '1'
    # compute minimum adjacent swaps to transform initial into target
    # Since only adjacent swaps allowed, the minimal number of swaps is sum of absolute displacement
    return sum(abs(i - j) for i, j in zip(sorted(initial), sorted(target)))

def solve():
    input = stdin.readline
    N, M = map(int, input().split())
    bits = list(map(int, input().split()))
    runs = list(map(int, input().split()))
    
    # We have two possible target bitstrings according to runs:
    # One starting with 0, another starting with 1
    # First, sum of runs is N
    # So build two possible bitstrings that fit runs (lengths in runs)
    # First possible start bit:
    start0 = 0
    start1 = 1
    
    # build target bitstrings
    def build_target(start_bit):
        res = []
        cur = start_bit
        for length in runs:
            res.extend([cur]*length)
            cur = 1 - cur
        return res

    target0 = build_target(start0)
    target1 = build_target(start1)
    
    # We want to reorder bits (initial) to one of these targets
    # They have the same run-length code but different start bit
    # The problem states that initial can become either target0 or target1,
    # possibly only one is valid (but problem states can become one of these two)
    
    # The minimal number of swaps is minimized when the ordered positions of ones in initial and target match best
    
    # Get positions of ones in initial and in targets
    ones_init = [i for i, b in enumerate(bits) if b == 1]
    
    ones_target0 = [i for i,b in enumerate(target0) if b ==1]
    ones_target1 = [i for i,b in enumerate(target1) if b ==1]
    
    # Compute minimal swaps for both targets
    swaps0 = min_swaps(ones_init, ones_target0)
    swaps1 = min_swaps(ones_init, ones_target1)
    
    # Output minimum
    print(min(swaps0, swaps1))

if __name__ == "__main__":
    solve()