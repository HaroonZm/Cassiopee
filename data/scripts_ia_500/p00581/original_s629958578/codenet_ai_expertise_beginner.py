h, w = map(int, input().split())
mp = []
for _ in range(h):
    mp.append(input())

i_cnt = []
o_cnt = []
for _ in range(h):
    i_cnt.append([0] * w)
    o_cnt.append([0] * w)

for x in range(w):
    if mp[h-1][x] == "I":
        i_cnt[h-1][x] = 1

for y in range(h):
    if mp[y][w-1] == "O":
        o_cnt[y][w-1] = 1

ans = 0
for y in range(h-2, -1, -1):
    for x in range(w-2, -1, -1):
        if mp[y][x] == "I":
            i_cnt[y][x] = i_cnt[y+1][x] + 1
            o_cnt[y][x] = o_cnt[y][x+1]
        elif mp[y][x] == "O":
            i_cnt[y][x] = i_cnt[y+1][x]
            o_cnt[y][x] = o_cnt[y][x+1] + 1
        else:
            i_cnt[y][x] = i_cnt[y+1][x]
            o_cnt[y][x] = o_cnt[y][x+1]
            ans += i_cnt[y][x] * o_cnt[y][x]

print(ans)