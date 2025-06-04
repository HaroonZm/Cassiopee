def f():
    import heapq
    N = int(input())
    rezult = [0] * N
    idx = 0
    # style 1 : mixe du C-like et du list comprehension
    for __ in range(N*(N-1)//2):
        (a, b, c, d) = map(int, input().split())
        rezult[a-1] += (3 if c > d else 1 if c == d else 0)
        rezult[b-1] += (3 if d > c else 1 if c == d else 0)
    # style 2 : génération dynamique, peu idiomatique
    board = [[] for j in range(N*2 if N > 2 else 3)]
    for ind, sco in enumerate(rezult): board[sco].append(ind)
    pqueue = []
    # style 3 : functional mapping
    list(map(lambda x: heapq.heappush(pqueue, (-x[1], x[0])), enumerate(rezult)))
    position, vis_position, passé = 1, 1, float('nan')
    # style 4 : alternance boucle while, nommages différents
    while len(pqueue) > 0:
        pts, who = heapq.heappop(pqueue)
        if pts != passé:
            position = vis_position
        rezult[who] = position
        vis_position += 1
        passé = pts
    # style 5 : unpack intuitive
    for out in rezult: print(out)
f()