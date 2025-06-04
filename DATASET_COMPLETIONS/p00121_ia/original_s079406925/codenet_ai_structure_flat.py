from heapq import heappush, heappop
MOVE = [[1,4],[0,2,5],[1,3,6],[2,7],[0,5],[1,4,6],[2,5,7],[3,6]]
ans = {"01234567":0}
q = [[0,"01234567"]]
while q:
    g, field = q.pop(0)
    a = field.find("0")
    for b in MOVE[a]:
        tmp = list(field)
        tmp[a], tmp[b] = tmp[b], tmp[a]
        tmp = "".join(tmp)
        if tmp not in ans:
            ans[tmp] = g + 1
            q.append([g+1, tmp])
while True:
    try:
        s = raw_input().replace(" ","")
        print ans[s]
    except:
        break