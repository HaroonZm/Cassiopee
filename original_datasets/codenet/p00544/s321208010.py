inf = 10**20
n,m = map(int, input().split())
flist = []
wbrnum = {}
for i in range(n):
    a = list(str(input()))
    flist.append(a)
    b = []
    b.append(a.count('W'))
    b.append(a.count('B'))
    b.append(a.count('R'))
    wbrnum[i] = b
cnt = inf
for i in range(n-2):
    cnti = 0
    for l in range(i+1):
        cnti += (wbrnum[l][1]+wbrnum[l][2])
    for j in range(i+1,n-1):
        cntj = 0
        cnto = 0
        for o in range(i+1,j+1):
            cntj += (wbrnum[o][0]+wbrnum[o][2])
        for o in range(j+1,n):
            cnto += (wbrnum[o][0]+wbrnum[o][1])
        cnt = min(cnt,(cnti+cntj+cnto))
        #print(i,j,cnti,cntj,cnto,cnt)
print(cnt)