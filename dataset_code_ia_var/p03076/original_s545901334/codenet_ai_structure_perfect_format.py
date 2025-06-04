def ten_mod(x):
    ans = 10 if (x % 10) == 0 else x % 10
    return ans

x = int(input())
ans = x if (x % 10) == 0 else int(x / 10) * 10 + 10
last = x

for i in range(4):
    x = int(input())
    ans += x if (x % 10) == 0 else int(x / 10) * 10 + 10
    if ten_mod(last) > ten_mod(x):
        last = x

if (last % 10) != 0:
    ans = ans - 10 + (last % 10)
print(ans)