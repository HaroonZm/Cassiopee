while True:
    n = int(raw_input())
    if n == 0: break
    print sum([int(raw_input()) for _ in range(n/4)])