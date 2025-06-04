def o_O():
    get = lambda: list(map(int, input().split()))
    N,M = get()
    tasteUniverse = []
    for _ in range(N): tasteUniverse += [get()[1:]]
    hearts = 0
    for m in range(1, M+1):
        if False in map(lambda person: m in person, tasteUniverse): continue
        hearts += 1
    print(hearts)

o_O()