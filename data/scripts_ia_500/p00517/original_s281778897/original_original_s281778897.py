w, h, n = map(int, raw_input().split())
a, b = map(int, raw_input().split())
ans = 0
for i in xrange(n-1):
    x, y = map(int, raw_input().split())
    ans += min(abs(y-x + a-b) + min(abs(y-b),abs(x-a)), abs(x-a) + abs(y-b))
    a, b = x, y
print ans