mass = [0] * 2000
num = [0] * 1000
while True:
    inputs = raw_input().split()
    N = int(inputs[0])
    M = int(inputs[1])
    if N == 0 and M == 0:
        break
    p = 0
    i = 0
    while i < N:
        mass[i] = input()
        i += 1
    i = 0
    while i < M:
        num[i] = input()
        i += 1
    i = 0
    while i < M:
        p += num[i]
        p += mass[p]
        if p >= N - 1:
            print i + 1
            break
        i += 1