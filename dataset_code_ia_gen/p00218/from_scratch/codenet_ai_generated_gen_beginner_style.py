while True:
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        pm, pe, pj = map(int, input().split())
        if pm == 100 or pe == 100 or pj == 100:
            print("A")
            continue
        avg_me = (pm + pe) / 2
        avg_all = (pm + pe + pj) / 3
        if avg_me >= 90:
            print("A")
        elif avg_all >= 80:
            print("A")
        elif avg_all >= 70:
            print("B")
        elif avg_all >= 50 and (pm >= 80 or pe >= 80):
            print("B")
        else:
            print("C")