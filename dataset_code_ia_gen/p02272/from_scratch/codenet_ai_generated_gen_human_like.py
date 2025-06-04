import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

SENTINEL = 10**10  # Un nombre très grand pour les sentinelles
comparisons = 0

def Merge(A, left, mid, right):
    global comparisons
    n1 = mid - left
    n2 = right - mid
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L[n1] = SENTINEL
    R[n2] = SENTINEL
    i = 0
    j = 0
    for k in range(left, right):
        comparisons += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def Merge_Sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        Merge_Sort(A, left, mid)
        Merge_Sort(A, mid, right)
        Merge(A, left, mid, right)

n = int(input())
A = list(map(int, input().split()))
Merge_Sort(A, 0, n)
print(' '.join(map(str, A)))
print(comparisons)