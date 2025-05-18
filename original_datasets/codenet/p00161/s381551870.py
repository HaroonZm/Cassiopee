while 1:
    n = int(input())
    if n == 0:
        break

    score = []
    for _ in range(n):
        datas = list(map(int, input().split()))
        num = datas.pop(0)

        time = 0
        for _ in range(4):
            time += datas.pop(0) * 60 + datas.pop(0)

        score.append([num, time])

    score = sorted(score, key=lambda x: x[1])
    print(score[0][0])
    print(score[1][0])
    print(score[-2][0])