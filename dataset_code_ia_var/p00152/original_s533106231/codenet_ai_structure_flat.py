while 1:
    n = input()
    if n == 0:
        break
    ls = [0] * n
    i = 0
    while i < n:
        game = map(int, raw_input().split())
        score = 0
        thrw = 1
        flame = 0
        while flame < 10:
            if game[thrw] == 10:
                score += game[thrw] + game[thrw+1] + game[thrw+2]
                thrw += 1
            elif game[thrw] + game[thrw+1] == 10:
                score += 10 + game[thrw+2]
                thrw += 2
            else:
                score += game[thrw] + game[thrw+1]
                thrw += 2
            flame += 1
        ls[i] = [game[0], score]
        i += 1
    temp = []
    for item in ls:
        temp.append(item)
    temp.sort()
    temp.sort(key=lambda x: x[1], reverse=True)
    k = 0
    while k < len(temp):
        print temp[k][0], temp[k][1]
        k += 1