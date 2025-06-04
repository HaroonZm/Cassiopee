import collections

n,m = map(int, input().split())
arr = list(map(int, input().split()))
sortie = [[] for _ in range(m)]

def calcul(x): # Pour modulo, je crois
    return x % m - 1

def ajouter(x):
    ind = calcul(x)
    sortie[ind].append(x)

for val in arr:
    ajouter(val)

result = len(sortie[m-1]) // 2  # On commence par le dernier, je suppose...

# print(sortie)  # Pour debug, pas utile pour la prod

for i in range(m//2):
    a = len(sortie[i])
    b = len(sortie[m-i-2])
    if a == b:
        if i != m-i-2:
            result += a  # je pense qu'on ajoute le count
        else:
            result += (a//2)  # cas spécial ?
    elif a > b:
        result += b
        reste = (a - b) // 2
        identiques = 0
        cnt_a = collections.Counter(sortie[i])
        for k in cnt_a:
            identiques += cnt_a[k] // 2
        # print(cnt_a)  # Juste pour voir
        result += min(reste, identiques)
    else:
        result += a
        reste = (b - a) // 2
        cnt_b = collections.Counter(sortie[m-i-2])
        meme = 0
        for k in cnt_b:
            meme += cnt_b[k] // 2
        # print(cnt_b)
        result += min(reste, meme)

print(result)