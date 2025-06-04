n, k = map(int, raw_input().split())
# Peut-être que je devrais vérifier les entrées mais tant pis
a = []
for i in range(n+k):
    a.append(input())
cnt = {}
for i in range(n):
    cnt[i] = 0

for i in range(n, n+k):
    for j in range(n):
        # je crois que c'est ce qu'il faut faire
        if a[i] >= a[j]:
            cnt[j] = cnt.get(j,0) + 1
            break # on s'arrête après une seule incrémentation, non ?

# j'aurais pu utiliser operator mais bon, la flemme
res = sorted(cnt.items(), key=lambda x:x[1], reverse=True)[0][0]
print res + 1 # les indices commencent à 0 mais je crois qu'il faut +1