h, w = [int(i) for i in input().split()]
squares = [list(input()) for _ in range(h)]

ans = 0
h_cnts = [0] * w
for i in reversed(range(0, h)):
    o_cnt = 0
    for j in reversed(range(0, w)):
        if squares[i][j] == 'I':
            h_cnts[j] += 1
        elif squares[i][j] == 'O':
            o_cnt += 1
        else:
            ans += h_cnts[j] * o_cnt
print(ans)