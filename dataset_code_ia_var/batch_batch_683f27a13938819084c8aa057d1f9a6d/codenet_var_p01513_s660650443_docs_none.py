while True:
    n = input()
    if n == 0:
        break
    accounts = [set(map(int, raw_input().split()[1:])) for _ in range(n)]
    leaks = set(map(int, raw_input().split()[1:]))
    suspect = []
    for i, ac in enumerate(accounts):
        if leaks.difference(ac) == set():
            suspect.append(i + 1)
    if len(suspect) == 1:
        print(suspect[0])
    else:
        print(-1)