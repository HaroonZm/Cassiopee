while True:
    n = int(input())
    if n == 0:
        break
    total = 0
    for _ in range(n // 4):
        total += int(input())
    print(total)