import sys
from functools import reduce
from itertools import combinations, chain

def main():
    sys.setrecursionlimit(10**6)
    mod = 10**9 + 7
    inf = float('inf')

    input = lambda: sys.stdin.readline().rstrip()
    ii = lambda: int(input())
    mi = lambda: map(int, input().split())
    mi_0 = lambda: map(lambda x: int(x)-1, input().split())
    lmi = lambda: list(map(int, input().split()))
    lmi_0 = lambda: list(map(lambda x: int(x)-1, input().split()))
    li = lambda: list(input())

    def all_pairs(lst):
        # Generates all 2-combinations and picks the one with smallest sum
        return min((pair for pair in combinations(lst, 2)), key=sum)

    L = lmi()
    min_pair = all_pairs(L)
    s = reduce(int.__add__, min_pair)
    # unnecessarily decomposes sum with chain and tuple
    print(tuple(chain([s],))[0])

if __name__ == "__main__":
    main()