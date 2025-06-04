while True:
    N, A, B, C, X = map(int, input().split())
    if N == 0 and A == 0 and B == 0 and C == 0 and X == 0:
        break
    Y = list(map(int, input().split()))
    
    current = X
    stopped = 0
    frame = 0
    max_frame = 10000
    while frame <= max_frame and stopped < N:
        # next random number
        current = (A * current + B) % C
        frame += 1
        if current == Y[stopped]:
            stopped += 1
    if stopped == N:
        print(frame)
    else:
        print(-1)