# B - Common Raccoon vs Monster
H,N = map(int,input().split())
A = list(map(int,input().split()))
ans = 'Yes' if H<=sum(A) else 'No'
print(ans)