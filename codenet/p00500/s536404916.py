N = int(input())
all_game = [[int(j) for j in input().split()] for i in range(N)]
point = [0] * N

for g_i in range(3):
    g = [int(no[g_i]) for no in all_game]
    dic = {}
    for x in g:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    for p_i in range(N):
        if dic[g[p_i]] == 1:
            point[p_i] += g[p_i]

for line in point:
    print(line)