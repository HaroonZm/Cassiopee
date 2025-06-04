import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def merge_sort(arr):
    def sort(lo, hi):
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        inv = sort(lo, mid) + sort(mid, hi)
        i, j = lo, mid
        temp = []
        while i < mid and j < hi:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                inv += mid - i
                j += 1
        temp.extend(arr[i:mid])
        temp.extend(arr[j:hi])
        arr[lo:hi] = temp
        return inv
    return sort(0, len(arr))

n = int(input())
A = list(map(int, input().split()))
print(merge_sort(A))