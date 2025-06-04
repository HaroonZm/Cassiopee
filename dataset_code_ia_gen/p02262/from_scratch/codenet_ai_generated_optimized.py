import sys
input = sys.stdin.readline

def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v

def shellSort(A, n):
    global cnt
    cnt = 0
    G = []
    h = 1
    while h <= n:
        G.append(h)
        h = 3*h +1
    G.reverse()
    for g in G:
        insertionSort(A, n, g)
    return G

n = int(input())
A = [int(input()) for _ in range(n)]
cnt = 0
G = shellSort(A, n)
print(len(G))
print(*G)
print(cnt)
print(*A, sep='\n')