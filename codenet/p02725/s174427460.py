K,N = map(int,input().split())
A = list(map(int,input().split()))
diff = []
for i in range(N-1):
    diff.append(A[i+1]-A[i])
    diff.append(K - A[-1] + A[0])
print(K-max(diff))