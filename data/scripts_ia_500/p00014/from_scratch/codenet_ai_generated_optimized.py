while True:
    try:
        d = int(input())
        n = 600 // d
        s = d**3 * n * (n + 1) * (2*n + 1) // 6
        print(s)
    except EOFError:
        break