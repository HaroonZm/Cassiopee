N,X = map(int,input().split())
target = []
ans = 0
for i in range(N):
    target.append(int(input()))
X -= sum(target)
ans = len(target)
ans += X // min(target)
print(ans)