while True:
    try:
        n = input()
    except:
        break
    n = list(map(int, n))
    while len(n) > 1:
        n = [(n[i] + n[i + 1]) % 10 for i in range(len(n) - 1)]
    print(*n)