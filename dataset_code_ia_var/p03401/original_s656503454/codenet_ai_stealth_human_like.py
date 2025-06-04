# Bon, on va voir ce que donne ce bout de code.
n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]   # j'ajoute des 0 pour les bords, c'est plus facile, je crois
ans = []
i = 1
# mise en place de s, même si le premier on s'en sert ? On verra
s = [abs(a[1])] + [None]*n
d = [0]*(n+1)
for i in range(1, n+1):
    s[i] = abs(a[i+1] - a[i])  # la différence, parce que c'est important
    # Cette condition, faut réfléchir un peu, bof, je la garde
    if (a[i-1] - a[i]) * (a[i] - a[i+1]) >= 0:
        d[i] = 0
    else:
        d[i] = s[i] + s[i-1] - abs(a[i+1] - a[i-1])
ss = sum(s)
for j in range(1, n+1):
    print(ss - d[j])
# voilà, ça devrait marcher, même si je ne suis pas sûr pour les bordures