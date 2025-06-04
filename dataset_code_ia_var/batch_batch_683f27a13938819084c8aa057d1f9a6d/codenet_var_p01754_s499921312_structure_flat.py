while True:
    try:
        N, P, Q = map(int, input().split())
        menu = []
        for _ in range(N):
            menu.append(int(input()))
        all_happy = []
        for i in range(N):
            all_happy.append(P * (Q - i) - menu[i])
        all_happy.sort(reverse=True)
        happy = [sum(menu)]
        for i in range(N):
            happy.append(happy[-1] + P * i * 2 + all_happy[i])
        print(max(happy))
    except:
        break