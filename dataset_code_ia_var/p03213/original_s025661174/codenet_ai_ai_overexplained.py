# Définition de la fonction prime_factorization qui prend en paramètre un entier n.
# Cette fonction va calculer les facteurs premiers de chaque entier entre 2 et n inclus,
# et enregistrer le nombre d'occurrences de chaque facteur premier dans le dictionnaire rec.
def prime_factorization(n):
    # On boucle sur tous les entiers i entre 2 et n inclus (donc i = 2, 3, ..., n)
    for i in range(2, n + 1):
        # On calcule la racine carrée de i, puis on la convertit en entier afin de limiter les recherches de diviseur.
        # Cela vise à optimiser l'identification des facteurs premiers.
        num = int(i ** 0.5)
        # Pour chaque entier prime potentiel (candidat à être un facteur premier),
        # on part du plus petit nombre premier, soit 2, jusqu'à num + 1 inclusivement
        for prime in range(2, num + 2):
            # On vérifie si prime divise i sans reste, c'est-à-dire si i est divisible par prime.
            if i % prime == 0:
                # On initialise un compteur cnt à 0, pour compter combien de fois prime divise i.
                cnt = 0
                # On utilise une boucle while pour continuer à diviser i par prime tant que c'est possible.
                while True:
                    # Si i n'est plus divisible par prime, on sort de la boucle.
                    if i % prime != 0: break
                    # Sinon, cela signifie que prime divise encore i, donc on incrémente le compteur cnt.
                    cnt += 1
                    # On met à jour i en le divisant par prime, éliminant ainsi une occurrence de prime dans i.
                    i = i // prime
                # À ce stade, on a compté combien de fois prime divise le nombre d'origine.
                # On met à jour le dictionnaire rec pour ce facteur premier.
                # Si prime existe déjà comme clé dans rec, on ajoute cnt à la valeur existante.
                if rec.get(prime):
                    rec[prime] += cnt
                # Sinon, on crée la clé prime dans rec et on lui assigne comme valeur cnt.
                else:
                    rec[prime] = cnt

        # À la sortie de la boucle for sur prime, il est possible qu'il reste un facteur premier plus grand
        # que la racine carrée initiale de i (c'est-à-dire que le résidu de i après factorisation est supérieur à 1).
        # Si c'est le cas, on enregistre ce résidu comme facteur premier aussi.
        if i != 1:
            # Si rec contient déjà le facteur premier i, on incrémente sa valeur de 1.
            if rec.get(i):
                rec[i] += 1
            # Sinon, on crée une nouvelle clé dans rec pour ce facteur premier avec la valeur 1.
            else:
                rec[i] = 1

# Lecture d'un nombre entier depuis l'entrée standard de l'utilisateur.
n = int(input())
# Création d'un dictionnaire rec, qui va servir à stocker la décomposition en facteurs premiers.
# Les clés sont les nombres premiers, et les valeurs sont les sommes de leurs puissances dans les factorisations de 2 à n.
rec = dict()
# Appel de la fonction prime_factorization avec le paramètre n, pour remplir le dictionnaire rec.
prime_factorization(n)
# Initialisation d'un autre dictionnaire dic,
# où chaque clé correspond à un seuil spécifique de puissance de facteurs premiers,
# et la valeur initiale de chaque clé est 0.
# Les seuils sont 2, 4, 14, 24, et 74.
dic = {2:0, 4:0, 14:0, 24:0, 74:0}
# Initialisation d'un compteur cnt à 0 qui servira à stocker le résultat final.
cnt = 0
# On parcourt tous les couples (clé, valeur) du dictionnaire rec.
# Ici, clé représente le nombre premier et valeur le nombre total de fois qu'il apparaît parmi les factorisations
# de 2 jusqu'à n (en tenant compte des puissances).
for key, val in rec.items():
    # Si la puissance de ce facteur premier est au moins 2, on augmente le compteur de facteurs >=2.
    if val >= 2:dic[2] += 1
    # Même logique pour les puissances supérieures ou égales à 4, 14, 24 et 74 respectivement.
    if val >= 4:dic[4] += 1
    if val >= 14:dic[14] += 1
    if val >= 24:dic[24] += 1
    if val >= 74:dic[74] += 1

# On va calculer le résultat final cnt, en combinant différentes configurations des puissances de facteurs premiers.
# Pour chaque seuil dans la liste [74, 24, 14, 4], on applique un calcul différent.
for i in [74, 24, 14, 4]:
    # On récupère le nombre de facteurs premiers dans rec dont la puissance dépasse i-1, grâce à dic[i].
    temp = dic.get(i)
    # Si le seuil est 74, chaque facteur unique avec une puissance >=74 compte pour 1 solution (choix possible),
    # donc on ajoute temp à cnt.
    if i == 74:cnt += temp
    # Si le seuil est 24, on sélectionne une combinaison d'un facteur de puissance >=24 et un autre différent
    # qui a au moins puissance >=2, donc on multiplie le nombre de facteurs >=24 par le nombre de facteurs >=2,
    # sans inclure le facteur déjà pris, donc -1.
    elif i == 24:cnt += temp * (dic[2] - 1)
    # Même logique avec le seuil 14 : un facteur >=14 et un facteur différent >=4.
    elif i == 14:cnt += temp * (dic[4] - 1)
    # Enfin, pour i=4, on veut former une combinaison de trois facteurs différents :
    # deux facteurs (a, b) avec puissance >=4 et un facteur c (différent des deux premiers) avec puissance >=2,
    # le tout en prenant les combinaisons uniques sans permutations inutiles, d'où la division entière par 2.
    else:cnt += (dic[2] - 2) * (temp - 1) * temp // 2
# On affiche le résultat final, le nombre de façons calculées selon la logique du problème.
print(cnt)