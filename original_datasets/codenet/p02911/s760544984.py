N, K, Q = map(int, input().split())
A = [ int(input()) for _ in range(Q) ]

point_list = [0 for _ in range(N)]

for q in range(Q):
    point_list[A[q] - 1] += 1

for n in range(N):
    print('No' if Q - point_list[n] >= K else 'Yes')