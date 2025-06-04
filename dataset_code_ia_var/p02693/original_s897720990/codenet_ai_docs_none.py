k = int(input())
a, b = map(int, input().split())
ans = 'NG'
if a <= (b // k) * k:
    ans = 'OK'
print(ans)