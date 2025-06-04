while True:
    line = input()
    if line == '0 0':
        break
    M, W = map(int, line.split())
    bm = list(map(int, input().split()))
    bw = list(map(int, input().split()))

    max_energy = 0
    for i in range(M):
        for j in range(W):
            diff = abs(bm[i] - bw[j])
            energy = diff * (diff - 30) * (diff - 30)
            if energy > max_energy:
                max_energy = energy
    print(max_energy)