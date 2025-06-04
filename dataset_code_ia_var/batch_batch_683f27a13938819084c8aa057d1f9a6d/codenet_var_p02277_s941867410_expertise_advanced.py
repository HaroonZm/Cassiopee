#!/usr/local/bin/python3

from sys import stdin
from math import inf

def merge(A, left, mid, right):
    L = [*A[left:mid], ("", inf)]
    R = [*A[mid:right], ("", inf)]
    i = j = 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, left, right):
    if right - left > 1:
        mid = (left + right) >> 1
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

def partition(A, p, r):
    x = A[r][1]
    i = p
    for j in range(p, r):
        if A[j][1] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quick_sort(A, p, r):
    stack = [(p, r)]
    while stack:
        p, r = stack.pop()
        if p < r:
            q = partition(A, p, r)
            stack.append((p, q - 1))
            stack.append((q + 1, r))

def main():
    n = int(stdin.readline())
    A = [tuple((s, int(x))) for s, x in (line.split() for line in stdin)]
    B = A.copy()
    quick_sort(A, 0, n - 1)
    merge_sort(B, 0, n)
    print("Stable" if A == B else "Not stable")
    print('\n'.join(f"{s} {x}" for s, x in A))

if __name__ == "__main__":
    main()