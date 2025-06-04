X, Y = map(int, input().split())
ans = 0
while X <= Y:
    X <<= 1
    ans += 1
print(ans)