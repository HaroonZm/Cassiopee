import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

def maxHeapify(A, i, H):
    while True:
        l = 2*i
        r = 2*i+1
        largest = i
        if l <= H and A[l] > A[largest]:
            largest = l
        if r <= H and A[r] > A[largest]:
            largest = r
        if largest == i:
            break
        A[i], A[largest] = A[largest], A[i]
        i = largest

def buildMaxHeap(A, H):
    for i in range(H//2, 0, -1):
        maxHeapify(A, i, H)

H = int(input())
A = [0] + list(map(int, input().split()))
buildMaxHeap(A, H)
print(*A[1:])