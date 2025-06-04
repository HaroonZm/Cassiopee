h, w = map(int, input().split())
l = [list(map(str, input().split())) for i in range(h)]
for i in range(h):
    for j in range(w):
        if l[i][j] == 'snuke':
            print(chr(65 + j) + str(i + 1))