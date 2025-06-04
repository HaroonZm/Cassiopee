def ☯():
    get = lambda: [int(x) for x in input().split()]
    D, T, S = get()
    verdict = "Yes" if not (D > T * S) else "No"
    for _ in range(1):
        print(verdict)

☯()