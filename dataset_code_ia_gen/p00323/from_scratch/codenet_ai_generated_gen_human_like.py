import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    N = int(input())
    total_weight = 0
    total_count = 0
    weight_counts = defaultdict(int)

    for _ in range(N):
        a, b = map(int, input().split())
        weight = (1 << a)  # 2^a
        count = (1 << b)   # 2^b
        total_weight += weight * count

    # Now we need to express total_weight as sum of 2^x * 2^y pieces
    # with minimal number of pieces: since unit count is infinite
    # we just represent total_weight in powers of two with count 1 for each power

    # Convert total_weight to binary and output powers of two with count=0
    # because b=0 means only one piece (2^b =1)

    result = []
    pot = 0
    while total_weight > 0:
        if total_weight & 1:
            # output power and 0 as count so count is 2^0=1 piece
            result.append((pot, 0))
        total_weight >>= 1
        pot += 1

    # Output sorted by weight ascending (already ascending)
    for a, b in result:
        print(a, b)

if __name__ == "__main__":
    main()