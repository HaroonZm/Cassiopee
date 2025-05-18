n = int(input())
A = list(map(int, input().split()))
q = int(input())
for i in range(q):
    a, b, c = map(int, input().split())
    print(A[a:b].count(c))