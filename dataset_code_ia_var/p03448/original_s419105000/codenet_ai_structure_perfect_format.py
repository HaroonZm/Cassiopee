a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0

for i in range(a + 1):
    for j in range(b + 1):
        res = x - (500 * i + 100 * j)
        if res >= 0 and res % 50 == 0 and res // 50 <= c:
            ans += 1

print(ans)