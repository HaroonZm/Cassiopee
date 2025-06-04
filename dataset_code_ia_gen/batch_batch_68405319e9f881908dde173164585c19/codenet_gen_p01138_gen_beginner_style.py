while True:
    n = int(input())
    if n == 0:
        break
    trains = []
    for _ in range(n):
        start, end = input().split()
        sh, sm, ss = map(int, start.split(':'))
        eh, em, es = map(int, end.split(':'))
        start_sec = sh*3600 + sm*60 + ss
        end_sec = eh*3600 + em*60 + es
        trains.append((start_sec, end_sec))
    trains.sort(key=lambda x: x[0])
    used = []
    for s,e in trains:
        placed = False
        for i in range(len(used)):
            if used[i] <= s:
                used[i] = e
                placed = True
                break
        if not placed:
            used.append(e)
    print(len(used))