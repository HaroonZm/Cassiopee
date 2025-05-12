N = int(input())
A = sorted(list(map(int, input().split())))
print(sum([A[i]-i-1 for i in range(N)]))