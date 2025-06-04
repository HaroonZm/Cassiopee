import sys
import itertools
from functools import lru_cache

sys.setrecursionlimit(10**7)
INF = float('inf')
EPS = 1e-13
MOD = 10**9+7

# Directions for 4 and 8 neighbors (mostly unused here, but kept for possible generality)
DIR4 = [(-1,0),(0,1),(1,0),(0,-1)]
DIR8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

input = sys.stdin.readline

def ints(): return list(map(int, input().split()))
def ints0(): return [int(x)-1 for x in input().split()]
def floats(): return list(map(float, input().split()))
def strs(): return input().split()
def read_int(): return int(input())
def read_float(): return float(input())
def read_line(): return input()
def pf(s): print(s, flush=True)

def main():
    results = []

    while True:
        n = int(input())
        if n == 0:
            break
        group = [strs() for _ in range(n)]
        name_to_idx = {name: idx for idx, (name, *rest) in enumerate(group)}
        tips = []
        bs = {}
        bb = {}
        base_score = int(group[0][1])
        key_name = group[0][0]

        for i in range(1, n):
            info = group[i]
            name = info[0]
            val = int(info[1])
            if key_name in info[3:]:
                continue
            if info[2] == '0':
                base_score += val
                continue
            mask = 2 ** name_to_idx[name]
            restriction = sum(2**name_to_idx[restricted] for restricted in info[3:])
            tips.append((mask, val, restriction))
            bs[mask] = restriction
            bb[mask] = val

        full_mask = sum(mask for mask, _, _ in tips)
        size = len(tips)
        half = size // 2
        half_masks = [tips[i][0] for i in range(half)]

        @lru_cache(maxsize=None)
        def dp(rem_mask):
            # Fast DP with memoization
            if rem_mask == 0:
                return 0
            best = 0
            selected = 0
            score_acc = 0
            excl_mask = 0
            mask = rem_mask
            while mask:
                sub = mask & -mask
                if (bs[sub] & rem_mask) == 0:
                    excl_mask |= sub
                    score_acc += bb[sub]
                mask ^= sub
            residual_mask = rem_mask ^ excl_mask
            mask = residual_mask
            while mask:
                sub = mask & -mask
                partial = bb[sub]
                partial += dp(residual_mask ^ sub ^ (rem_mask & bs[sub]))
                best = max(best, partial)
                mask ^= sub
            return best + score_acc

        answer = 0
        from operator import or_, ior
        # Meet-in-the-middle: enumerate subsets in the first half and solve with DP for the second half
        for k in range(half+1):
            for comb in itertools.combinations(half_masks, k):
                cur_mask = 0; cur_score = 0; ban_mask = 0
                valid = True
                for mk in comb:
                    if bs[mk] & cur_mask:
                        valid = False
                        break
                    cur_score += bb[mk]
                    ban_mask |= bs[mk]
                    cur_mask |= mk
                if not valid:
                    continue
                # what's left for the other half
                second_half_mask = full_mask ^ cur_mask
                second_half_mask ^= (second_half_mask & ban_mask)
                cur_score += dp(second_half_mask)
                answer = max(answer, cur_score)

        results.append(str(answer + base_score))

    print('\n'.join(results))

main()