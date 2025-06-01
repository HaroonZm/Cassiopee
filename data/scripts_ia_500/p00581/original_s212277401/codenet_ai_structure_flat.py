h, w = [int(i) for i in input().split()]
squares = [list(input()) for _ in range(h)]
ans = 0
h_cnts = [0] * w
i = h - 1
while i >= 0:
    o_cnt = 0
    j = w - 1
    while j >= 0:
        if squares[i][j] == 'I':
            h_cnts[j] += 1
        elif squares[i][j] == 'O':
            o_cnt += 1
        else:
            ans += h_cnts[j] * o_cnt
        j -= 1
    i -= 1
print(ans)