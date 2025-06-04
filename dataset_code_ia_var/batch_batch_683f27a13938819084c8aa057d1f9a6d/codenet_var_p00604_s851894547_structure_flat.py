while True:
    try:
        n = input()
    except EOFError:
        break
    L = sorted(map(int, raw_input().split()))
    i = 1
    while i < int(n):
        L[i] += L[i-1]
        i += 1
    print sum(L)