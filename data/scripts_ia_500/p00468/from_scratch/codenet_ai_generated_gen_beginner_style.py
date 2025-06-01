while True:
    n = int(input())
    m = int(input())
    if n == 0 and m == 0:
        break
    friends = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    invited = set()
    for f in friends[1]:
        invited.add(f)
        for ff in friends[f]:
            if ff != 1:
                invited.add(ff)
    print(len(invited))