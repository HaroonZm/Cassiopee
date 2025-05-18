N, M = map(int, input().split())
list = [list(map(int, input().split())) for x in range(N)]
list.sort(key=lambda x: x[0])
remain = M
cost = 0
for i in range(N):
    store = list[i][1]
    if remain>=store:
        remain -= store
        cost += list[i][0]*store
    elif remain<store:
        cost += list[i][0]*(remain)
        remain = 0
    if remain==0: break
print(cost)