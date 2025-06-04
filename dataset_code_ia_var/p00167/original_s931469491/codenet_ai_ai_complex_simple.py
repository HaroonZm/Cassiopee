from functools import reduce
from operator import itemgetter

BubbleSort = lambda L: (
    lambda _: (
        list(
            map(
                lambda i: (L.__setitem__(i, L[i+1]), L.__setitem__(i+1,L[i]), globals().__setitem__('cnt', cnt+1))
                if L[i] > L[i+1] else None,
                range(len(L)-1)
            )
        )
    )
)(None)

exec("""
while True:
    n = eval(input())
    if not n: break
    L, cnt = [], 0
    [L.append(input()) for _ in range(n)]
    list(map(lambda _: BubbleSort(L), [None]*len(L)))
    print(cnt)
""")