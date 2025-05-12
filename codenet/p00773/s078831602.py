while True:
    x,y,s = map(int,input().split())
    if x == 0:
        break
    ans = 0
    for i in range(1,s+1):
        for j in range(i,s+1):
            komi_mae = i * (100 + x) // 100 + j * (100 + x) // 100
            if komi_mae == s:
                komi_now = i * (100 + y) // 100 + j * (100 + y) // 100
                ans = max(ans,komi_now)
    print(ans)