A,B,K=map(int,input().split())
ans = set(range(A,min(A+K,B+1))).union(set(range(B,max(A-1,B-K),-1)))

print(*sorted(ans))