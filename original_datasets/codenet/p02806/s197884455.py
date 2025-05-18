N = int(input())
playlist = {}
taiou = {}

for i in range(N):
    s_i, t_i = input().split()
    taiou[s_i] = i
    playlist[i] = int(t_i)

X = input()

cnt = 0
for j in range(taiou[X], N):
    cnt += playlist[j]

print(cnt - playlist[taiou[X]])