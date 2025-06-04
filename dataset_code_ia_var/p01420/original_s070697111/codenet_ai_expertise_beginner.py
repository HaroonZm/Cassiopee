def nCr(n, r):
    if r > n - r:
        r = n - r
    result_top = 1
    for i in range(n, n - r, -1):
        result_top = result_top * i
    result_bottom = 1
    for i in range(r, 1, -1):
        result_bottom = result_bottom * i
    return result_top // result_bottom

n, m, l = map(int, input().split())
data = []
for i in range(n):
    row = []
    p, t, v = map(int, input().split())
    for j in range(m + 1):
        if v != 0:
            time = t * j + l / v
        else:
            time = 9999999999999999
        prob = (p / 100.0) ** j * nCr(m, j) * (1 - p / 100.0) ** (m - j)
        row.append( (time, prob) )
    data.append(row)

ans = []
for i in range(n):
    total_win = 0.0
    for j in range(m + 1):
        win_prob = data[i][j][1]
        for x in range(n):
            if x == i:
                continue
            prob_other = 0.0
            for a, b in data[x]:
                if a > data[i][j][0]:
                    prob_other += b
            win_prob = win_prob * prob_other
        total_win += win_prob
    ans.append(total_win)

for value in ans:
    print('%.8f' % value)