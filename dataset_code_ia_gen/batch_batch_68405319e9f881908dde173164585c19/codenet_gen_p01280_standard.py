while True:
    N = int(input())
    if N == 0:
        break
    max_volume = 0
    for _ in range(N):
        data = list(map(int, input().split()))
        d, t = data[0], data[1]
        volumes = data[2:]
        for v in volumes:
            if v > max_volume:
                max_volume = v
    print(max_volume)