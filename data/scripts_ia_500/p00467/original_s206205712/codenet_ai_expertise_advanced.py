from sys import stdin

mass = [0] * 2000
num = [0] * 1000
input_lines = iter(stdin.read().splitlines())

for line in input_lines:
    N, M = map(int, line.split())
    if N == 0 and M == 0:
        break
    mass[:N] = map(int, (next(input_lines) for _ in range(N)))
    num[:M] = map(int, (next(input_lines) for _ in range(M)))

    p = 0
    for i, val in enumerate(num[:M]):
        p += val + mass[p]
        if p >= N - 1:
            print(i + 1)
            break