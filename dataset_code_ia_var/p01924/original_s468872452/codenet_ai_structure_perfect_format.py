while True:
    T, D, L = map(int, input().split())
    if T == 0 and D == 0 and L == 0:
        break
    rem = 0
    ans = 0
    for _ in range(T):
        x = int(input())
        if x >= L:
            rem = D
        if rem > 0:
            ans += 1
            rem -= 1
    if ans > 0:
        ans -= 1
    print(ans)