while True:
    n = int(input())
    if n == 0:
        break
    ls = []
    for i in range(n):
        game = list(map(int, input().split()))
        score = 0
        thrw = 1
        for frame in range(10):
            if game[thrw] == 10:
                score += sum(game[thrw:thrw+3])
                thrw += 1
            elif game[thrw] + game[thrw+1] == 10:
                score += 10 + game[thrw+2]
                thrw += 2
            else:
                score += game[thrw] + game[thrw+1]
                thrw += 2
        ls.append([game[0], score])
    ls.sort(key=lambda x: (x[1], x[0]), reverse=True)
    for k, s in ls:
        print(k, s)