while True:
    line = input().strip()
    if not line:
        continue
    N, K = map(int, line.split())
    if N == 0 and K == 0:
        break
    fridge = list(map(int, input().split()))
    vampires = [list(map(int, input().split())) for _ in range(N)]

    total_need = [0]*K
    for v in vampires:
        for i in range(K):
            total_need[i] += v[i]

    can_prepare = all(total_need[i] <= fridge[i] for i in range(K))
    print("Yes" if can_prepare else "No")