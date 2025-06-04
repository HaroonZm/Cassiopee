while True:
    N = int(input())
    if N == 0:
        break
    crops = []
    for _ in range(N):
        data = input().split()
        L = data[0]
        P, A, B, C, D, E, F, S, M = map(int, data[1:])
        total_time = A + B + C + D + E * M
        income = F * S * M - P
        efficiency = income / total_time
        crops.append(( -efficiency, L))
    crops.sort(key=lambda x: (x[0], x[1]))
    for _, name in crops:
        print(name)
    print("#")