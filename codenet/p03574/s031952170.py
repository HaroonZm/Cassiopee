high,width = map(int, input().split())
s_list = [list(input()) for _ in range(high)]
tmp_list = [[0 for _ in range(width)] for _ in range(high)]
dir = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
for h in range(high):
    for w in range(width):
        if s_list[h][w] == '#':
            tmp_list[h][w] = '#'
            for x,y in dir:
                tate = h+x
                yoko = w+y
                if tate >= 0 and yoko >= 0 and tate < high and yoko < width:
                    if s_list[tate][yoko]=='.':
                        tmp_list[tate][yoko] += 1

for tmp in tmp_list:
    t = map(str, tmp)
    print(''.join(t))