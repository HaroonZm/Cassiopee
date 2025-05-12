n = int(input())
A = list(map(int, input().split()))
q = int(input())

for i in range(q):
    b, e, k = list(map(int, input().split()))

    print(A[b:e].count(k))