n,m = map(int,input().split())
sp = list(map(int,input().split()))
cl = list(map(int,input().split()))
sum = 0
ans = 0
for a in sp:
    sum += a
for a in cl:
    ans += sum * a
print(ans)