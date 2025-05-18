N = int(input())
A = list(map(int,input().split()))
ans = 0
print(sum(A)-(N*(N+1))//2)