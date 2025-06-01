while True:
    t = int(input())
    if t == 0:
        break
    n = int(input())
    total = 0
    for i in range(n):
        s, f = map(int, input().split())
        total += f - s
    if total >= t:
        print("OK")
    else:
        print(t - total)