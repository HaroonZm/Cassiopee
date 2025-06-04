from typing import List, Callable, Any
from functools import partial

def partition(A: List[Any], p: int, r: int, key: Callable = lambda x: x) -> int:
    pivot = key(A[r])
    i = p - 1
    for j in range(p, r):
        if key(A[j]) <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort(A: List[Any], p: int, r: int, key: Callable = lambda x: x) -> None:
    stack = [(p, r)]
    while stack:
        p, r = stack.pop()
        if p < r:
            q = partition(A, p, r, key)
            stack.append((p, q - 1))
            stack.append((q + 1, r))

def main():
    import sys
    input_iter = iter(sys.stdin.read().splitlines())
    n = int(next(input_iter))
    A = [tuple((s := line.split())[0], int(s[1])) for line in input_iter]
    key = lambda x: x[1]
    stable_sorted = sorted(A, key=key)
    quick_sort(A, 0, n - 1, key=key)
    print('Stable' if stable_sorted == A else 'Not stable')
    print('\n'.join(f"{egara} {number}" for egara, number in A))

if __name__ == '__main__':
    main()