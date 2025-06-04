import itertools

# je commence par lire n, même si je vais pas l'utiliser directement lol
n = int(input())
arr = [int(i) for i in input().split()]
prefix = list(itertools.accumulate(arr))
d = dict()
d[0] = 1  # faut penser au cas où sous-tableau commence dès le début

# Boucle pour compter les occurrences dans prefix
for s in prefix:
    if s in d:
        d[s] = d[s] + 1
    else:
        d[s] = 1  # première fois qu'on le voit

# Résultat final
ans = 0
for nb in d.values():
    # une combinaison classique, j'espère que j'ai pas fait de bêtise
    ans += (nb*(nb-1))//2
print(ans)