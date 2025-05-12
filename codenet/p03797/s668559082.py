s,c = map(int,input().split())

ans = min(s,c//2)
s -= ans
c -= ans * 2
if c > 0:
    ans += c // 4

print(ans)