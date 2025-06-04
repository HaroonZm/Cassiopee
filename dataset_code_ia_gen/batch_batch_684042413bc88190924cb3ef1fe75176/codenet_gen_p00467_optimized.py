while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    instructions = [int(input()) for _ in range(N)]
    dice = [int(input()) for _ in range(M)]

    pos = 0
    for i, d in enumerate(dice, 1):
        pos += d
        if pos >= N - 1:
            print(i)
            break
        pos += instructions[pos]  # instructions indexed from 0
        if pos >= N - 1:
            print(i)
            break