N,T = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N-1):
  # print(i, A[i+1]-A[i], 10)
  cnt += min(T, A[i+1]-A[i])
print(cnt+T)