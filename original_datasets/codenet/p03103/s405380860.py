from operator import itemgetter
N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort(key = itemgetter(0))
#print(AB)
ans = 0
for i in range(N):
  if AB[i][1] >= M:
    ans += AB[i][0] * M
    print(ans)
    exit()
  else:
    M -= AB[i][1]
    ans += AB[i][0] * AB[i][1]