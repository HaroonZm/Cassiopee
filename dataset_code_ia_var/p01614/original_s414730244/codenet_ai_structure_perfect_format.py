N = int(input())

ph = {}
for i in range(N):
    s, l, p = map(int, input().split())
    for j in range(s, l + 1):
        if j not in ph:
            ph[j] = p
        else:
            ph[j] = max(p, ph[j])

M = int(input())
melody = []
for i in range(M):
    melody.append(int(input()))

phrase = [0 for _ in range(394)]
for k, p in ph.items():
    for j in range(k, 394):
        if phrase[j] < phrase[j - k] + p:
            phrase[j] = phrase[j - k] + p

ans = [phrase[i] for i in melody if phrase[i]]
if len(ans) == M:
    for val in ans:
        print(val)
else:
    print(-1)