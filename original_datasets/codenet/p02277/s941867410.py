#! /usr/local/bin/python3

from sys import stdin
from math import inf

def merge(A, left, mid, right):
    L = A[left:mid]; L.append(("", inf))
    R = A[mid:right]; R.append(("", inf))
    i = iter(L); l = next(i)
    j = iter(R); r = next(j)
    for k in range(left, right):
        if l[1] <= r[1]:
            A[k] = l
            l = next(i)
        else:
            A[k] = r
            r = next(j)

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)
    
def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def main():
    n = int(stdin.readline())
    A = []
    for l in stdin:
        suit, num = l.split()
        A.append((suit, int(num)))
    B = A[:]
    quick_sort(A, 0, n - 1)
    merge_sort(B, 0, n)
    print("Stable" if A == B else "Not stable")
    [print(*a) for a in A]

main()