import sys
from sys import stdin
from dataclasses import dataclass
from typing import List

input = stdin.readline

@dataclass(frozen=True, slots=True)
class Item:
    name: str
    w: int
    s: int

def optimal_stack_sequence(items: List[Item]) -> List[str]:
    # Sort items: Heaviest first, then by strength descending for tie-breaks
    items.sort(key=lambda x: (-x.w, -x.s))
    ans = []
    remaining = items
    while remaining:
        # Precompute total remaining weight for fast subtraction below (sum is O(N))
        total_weight = sum(x.w for x in remaining)
        # Find the topmost item (capacity not exceeded when bottom)
        idx = next(
            i for i, x in enumerate(remaining)
            if x.s >= total_weight - x.w
        )
        ans.append(remaining[idx].name)
        remaining = [x for j, x in enumerate(remaining) if j != idx]
    return ans

def main(args):
    while True:
        try:
            n = int(input())
        except:
            break
        if n == 0:
            break
        items = [
            Item(*[temp if i == 0 else int(temp) for i, temp in enumerate(input().split())])
            for _ in range(n)
        ]
        sequence = optimal_stack_sequence(items)
        print('\n'.join(sequence))

if __name__ == '__main__':
    main(sys.argv[1:])