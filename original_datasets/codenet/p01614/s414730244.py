N = int(input())

ph = {}
for i in range(N):
    s,l,p = map(int,input().split())
    for j in range(s,l+1):
        if j not in ph:
            ph[j] = p
        else:
            ph[j] = max(p, ph[j])

M = int(input())
melody = []
for i in range(M):
    melody.append(int(input()))

#print(ph)
phrase = [0 for i in range(393+1)]
for k,p in ph.items():
    for j in range(k,393+1):
        if phrase[j] < phrase[j-k] + p:
            phrase[j] = phrase[j-k] + p

ans = [phrase[i] for i in melody if phrase[i]]
if len(ans) == M:
    [print(i) for i in ans]
else:
    print(-1)