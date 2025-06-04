import sys
from functools import partial

def shell_sort(arr, gaps):
    cnt = 0
    for gap in gaps:
        for i in range(gap, len(arr)):
            v = arr[i]
            j = i
            while j >= gap and arr[j - gap] > v:
                arr[j] = arr[j - gap]
                j -= gap
                cnt += 1
            arr[j] = v
    return cnt

def generate_gaps(n):
    return [int((2.25 ** i - 1) / 1.25) for i in range(17, 0, -1) if (v := int((2.25 ** i - 1) / 1.25)) <= n]

n = int(input())
A = list(map(int, sys.stdin))
G = generate_gaps(n)
cnt = shell_sort(A, G)

print(len(G))
print(*G)
print(cnt)
print(*A, sep='\n')