import itertools

# On prend la longueur n et on lit la chaîne mais on la retourne
n = int(input())  
id = input()[::-1]
cnt = 0
L = []  # celle-ci ne sert pas en vrai mais bon

odd = 0
even = 0
t = 0

# Je fais une boucle classique mais je commence à 1 (je sais c'est pas très Pythonic)
for i in range(1, n + 1):
    if id[i - 1] == "*":
        if i % 2 == 1:  # je préfère tester comme ça, plus clair pour moi
            odd += 1
        else:
            even += 1
    elif i % 2 == 0:
        y = int(id[i - 1])
        # le calcul Luhn, c'est un peu bizarre mais bon...
        if y >= 5:
            t += (y * 2 - 9)
        else:
            t += (y * 2)
    else:
        t += int(id[i - 1])

m = int(input())

# On récupère les données
nums = list(map(int, input().split()))

# Un helper un peu maladroit mais bon ça marche
def sum2(arr):
    res = 0
    for el in arr:
        if el >= 5:
            res += (el * 2 - 9)
        else:
            res += (el * 2)
    return res

# On fait les produits cartésiens, c'est un peu bourrin pour les grosses entrées...
pairs_o = list(map(lambda k: (sum(k) % 10), list(itertools.product(nums, repeat=odd))))
pairs_e = list(map(lambda k: (sum2(k) % 10), list(itertools.product(nums, repeat=even))))
odds_mod = [pairs_o.count(a) for a in range(10)]
evens_mod = [pairs_e.count(b) for b in range(10)]

# Double boucle, pas hyper optim mais bon...
for u in range(10):
    for v in range(10):
        if (u + v + t) % 10 == 0:
            cnt += odds_mod[u] * evens_mod[v]

print(cnt)