def bubble_sort(A):
    count = 0
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                count += 1
                swapped = True
        if not swapped:
            break
    return count

import sys

for line in sys.stdin:
    N = int(line)
    if N == 0:
        break
    A = [int(next(sys.stdin)) for _ in range(N)]
    print(bubble_sort(A))