target = int(input())
coins = [25, 10, 5, 1]
ans = 0
for c in coins:
    ans += target // c
    target %= c
print(ans)