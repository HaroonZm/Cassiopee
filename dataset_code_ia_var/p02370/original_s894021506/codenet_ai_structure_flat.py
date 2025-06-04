V,E = list(map(int,input().split()))
visit = []
no_visit = []
for i in range(V):
    no_visit.append(i)
enter = []
for i in range(V):
    enter.append(0)
ad_list = []
for i in range(V):
    ad_list.append([])
for _ in range(E):
    s_e = input().split()
    start = int(s_e[0])
    end = int(s_e[1])
    ad_list[start].append(end)
    enter[end] = enter[end] + 1
while True:
    if len(visit) == V:
        break
    found = False
    for idx in range(len(no_visit)):
        n_v = no_visit[idx]
        if enter[n_v] == 0:
            v = no_visit.pop(idx)
            visit.append(v)
            for j in range(len(ad_list[n_v])):
                a = ad_list[n_v][j]
                enter[a] = enter[a] - 1
            found = True
            break
    if not found:
        break
for i in range(len(visit)):
    print(visit[i])