ans = 0
def count(use, total, n, target):
    global ans
    if total > target or n < 0:
        return
    if n == 0 and total == target:
        ans += 1
    else:
        for i in range(use + 1, 10):
            count(i, total + i, n - 1, target)

while True:
    try:
        n = list(map(int, input().split()))
    except Exception:
        break
    ans = 0
    if n[0] == 0 and n[1] == 0:
        break
    count(-1, 0, n[0], n[1])
    print(ans)