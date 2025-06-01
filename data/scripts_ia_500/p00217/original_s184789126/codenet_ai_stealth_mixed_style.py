def process():
    from sys import stdin
    data_iter = iter(stdin.read().split())
    while True:
        N = int(next(data_iter))
        if N == 0:
            return
        best_score = 0
        best_player = 0
        for _ in range(N):
            p, d, g = int(next(data_iter)), int(next(data_iter)), int(next(data_iter))
            total = d + g
            if total > best_score:
                best_score = total
                best_player = p
        print(best_player, best_score)

process()