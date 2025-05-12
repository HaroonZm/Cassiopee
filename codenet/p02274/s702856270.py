import sys

sintinel = 1000000001

def merge_sort(A, l, r):
    if l + 1 < r:
        mid = (l + r) // 2
        cnt1 = merge_sort(A, l, mid)
        cnt2 = merge_sort(A, mid, r)
        cnt3 = merge(A, l, mid, r)
        return (cnt1 + cnt2 + cnt3)
    else:
        return 0

def merge(A, l, mid, r):
    n1 = len(A[l:mid])
    L = A[l:mid] + [sintinel]
    R = A[mid:r] + [sintinel]
    i = j = 0
    cnt = 0
    for k in range(l, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            cnt += n1 - i
            A[k] = R[j]
            j += 1
    return cnt

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

c = merge_sort(A, 0, n)
print(c)