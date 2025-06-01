while 1:
    n = int(input())
    if n == 0:
        break
    score = []
    for _ in range(n):
        datas = list(map(int, input().split()))
        num = datas[0]
        time = 0
        time += datas[1] * 60 + datas[2]
        time += datas[3] * 60 + datas[4]
        time += datas[5] * 60 + datas[6]
        time += datas[7] * 60 + datas[8]
        score.append([num, time])
    score = sorted(score, key=lambda x: x[1])
    print(score[0][0])
    print(score[1][0])
    print(score[-2][0])