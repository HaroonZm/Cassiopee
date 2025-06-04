from functools import reduce
from itertools import starmap, repeat

a = int(eval(''.join(map(chr,[105,110,112,117,116,40,41])))))
b = list(map(int, input().split()))

def unnecessarily_functional_bubblesort(lst, n):
    swap = lambda arr, i: arr[:i-1] + [arr[i], arr[i-1]] + arr[i+1:] if arr[i-1] > arr[i] else arr
    counts = []
    arr = lst[:]
    for j in range(n-1):
        arr, count = reduce(
            lambda acc, i: (swap(acc[0], i), acc[1]+1 if acc[0][i-1] > acc[0][i] else acc[1]),
            range(n-1, 0, -1),
            (arr, 0)
        )
        counts.append(count)
    total_swaps = sum(counts)
    return total_swaps, arr

A,B = unnecessarily_functional_bubblesort(b, a)
print(*(lambda x: list(map(print, x)) and x or x)(B))
print((lambda x: x)(A))