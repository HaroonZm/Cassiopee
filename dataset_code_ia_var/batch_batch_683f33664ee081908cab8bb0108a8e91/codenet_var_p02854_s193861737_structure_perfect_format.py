n = int(input())
a = list(map(int, input().split()))
x = sum(a)
i = ans1 = 0
while True:
    if ans1 < x / 2 and i < n:
        ans1 += a[i]
        i += 1
    else:
        break
i -= 1
ans2 = x - ans1
ans1 -= a[i]
print(a[i] - abs(ans1 - ans2))