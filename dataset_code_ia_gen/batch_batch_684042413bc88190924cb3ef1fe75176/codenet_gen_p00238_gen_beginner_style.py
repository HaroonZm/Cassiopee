while True:
    t = input()
    if t == '0':
        break
    t = int(t)
    n = int(input())
    total = 0
    for _ in range(n):
        s, f = map(int, input().split())
        total += (f - s)
    if total >= t:
        print("OK")
    else:
        print(t - total)