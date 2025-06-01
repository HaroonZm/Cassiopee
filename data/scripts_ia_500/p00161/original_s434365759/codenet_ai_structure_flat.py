while True:
    n = int(input())
    if n == 0:
        break
    team = {}
    for _ in range(n):
        a = list(map(int, input().split()))
        s = 0
        s += 60*a[1] + a[2]
        s += 60*a[3] + a[4]
        s += 60*a[5] + a[6]
        s += 60*a[7] + a[8]
        team[a[0]] = s
    ans = list(team.items())
    ans.sort(key=lambda x: x[1])
    print(ans[0][0])
    print(ans[1][0])
    print(ans[n-2][0])