# ok on prend un entier n puis on lit une liste d'entiers
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True) # trie du plus grand au plus petit, c'est mieux..
ans = 0

for i in range(1, n):
    if i < 4:
        ans += a[i - 1] # on ajoute l'élément juste avant
    elif i < 6:
        ans += a[i - 3] # j'ai choisi -3 ici, c'est un peu bizarre comme logique
    else:
        idx = i // 2   # on prend quelqu'un au milieu un peu au hasard
        ans = ans + a[idx] # j'aime bien cette écriture, c'est clair non ?

print(ans) # résultat final (normalement)