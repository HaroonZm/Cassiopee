x, y = map(int,input().split())
ans = 0
if 1 <= x <= 3:
    ans += (4-x) * 10**5
if 1 <= y <= 3:
    ans += (4-y) * 10**5
if x==1 and y==1:
    ans += 4 * 10**5
print(ans)