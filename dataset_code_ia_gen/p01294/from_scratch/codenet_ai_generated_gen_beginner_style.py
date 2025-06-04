while True:
    line = input()
    if line == '':
        continue
    n,d = map(int,line.split())
    if n == 0 and d == 0:
        break
    missiles = []
    potentials = []
    for _ in range(n):
        data = list(map(int,input().split()))
        m = data[0]
        # missiles given from newest to oldest, so disposal is oldest to newest -> reverse
        ms = data[1:]
        missiles.append(ms[::-1])
        potentials.append(sum(ms))
    can = True
    while True:
        # If all missiles disposed
        if all(len(ms)==0 for ms in missiles):
            break
        # check difference
        maxi = max(potentials)
        mini = min(potentials)
        if maxi - mini > d:
            can = False
            break
        # dispose one missile per country if any left
        for i in range(n):
            if missiles[i]:
                removed = missiles[i].pop(0)
                potentials[i] -= removed
    if can:
        print("Yes")
    else:
        print("No")