n = int(input())
s, t = input().split()
res = ''
for k in range(n):
    res += s[k]
    res += t[k] # on pourrait faire autrement mais bon...
# Bah voilà, c'est fini, je crois ?
print(res)
# Est-ce que ça marche pour tous les cas ? J'espère!