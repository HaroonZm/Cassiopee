while True:
    t = int(input())
    if t == 0:
        break
    n = int(input())
    total = 0
    for _ in range(n):
        s, f = map(int, input().split())
        total += f - s
    print("OK" if total >= t else t - total)