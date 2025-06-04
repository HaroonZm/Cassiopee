from itertools import product  # Importe la fonction product du module itertools, qui permet de calculer le produit cartésien d'itérables.

# Lit trois entiers à partir de l'entrée standard (entrée utilisateur), les découpe avec split, puis les convertit en entiers avec map.
n, m, l = map(int, input().split())  # n: nombre maximal de périodes/jours; m: nombre d'entrées matière; l: nombre maximal de plages horaires

# Crée une liste contenant 5 sous-listes vides. 
# Cela représente un conteneur pour stocker, pour chaque jour de la semaine (numéroté 0 à 4), une liste de matières/cours.
subjects = [[] for _ in range(5)]

# Boucle m fois, c'est-à-dire pour chaque info de matière/cours donnée par l'utilisateur.
for _ in range(m):
    # Lit quatre entiers sur une ligne, les assigne aux variables d (jour), a (début), k (durée), t (valeur/bonheur).
    d, a, k, t = map(int, input().split())
    # Sur le jour d, ajoute à la sous-liste correspondante un tuple ayant :
    # a: position de départ, a + k - 1: position de fin, t: score/valeur.
    subjects[d].append((a, a + k - 1, t))

# Pour chaque jour (il y a 5 jours, 0 à 4):
for i in range(5):
    # Trie la liste des matières du jour i selon la position de fin, pour organiser les cours par leur fin croissante.
    # La fonction lambda x:x[1] récupère simplement le deuxième élément (position de fin) du tuple (a, a + k - 1, t).
    subjects[i].sort(key=lambda x:x[1])
 
# Définition d'une fonction calcDp qui calcule, pour un jour donné, le score maximal atteignable pour un nombre donné de matières.
def calcDp(i):
    # Création d'une matrice dp (programmation dynamique), initialisée à zéro.
    # dp[y][x] représentera le score maximal possible en choisissant y matières totalisant x plages horaires (créneaux) pour le jour i.
    # La taille de la matrice est (n+1) x (n+1) car l'index 0 est aussi inclus (pour 0 à n matières, 0 à n créneaux).
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # Prend la liste des matières pour le jour i.
    sub = subjects[i]
    # Pour chaque matière dans la liste du jour courant :
    for init, end, value in sub:
        # Parcours en y le nombre de matières déjà choisies (de 0 à n-1).
        for y in range(n):
            # Calcule le score si on ajoute cette matière à une configuration optimale précédente:
            # dp[y][init - 1] est le score maximal pour y matières jusqu'à juste avant "init".
            new_score = dp[y][init - 1] + value
            # Parcours en x toutes les cases de fin potentielle, de "end" (fin de cette matière) jusqu'à n (maximum possible).
            for x in range(end, n + 1):
                # Met à jour dp[y + 1][x] si le nouveau score est supérieur. 
                # Cela représente avoir ajouté une matière de plus qui finit à l'heure x.
                dp[y + 1][x] = max(dp[y + 1][x], new_score)
    # Une fois tous les ajouts possibles considérés, on détermine, pour chaque nombre d'items (de 0 à n matières), le score maximal obtenu.
    ret = []
    for i in range(n + 1):
        # Cherche la plus grande valeur sur toutes les plages horaires possibles pour i matières.
        ret.append(max(dp[i]))
    # Retourne une liste des meilleurs scores pour chaque nombre de matières (de 0 à n) pour le jour courant.
    return ret

# Applique la fonction calcDp à chaque jour (0 à 4), ce qui donne une liste de 5 listes, chaque sous-liste donnant les scores max par matière pour ce jour.
lst = [calcDp(i) for i in range(5)]

# Initialise la réponse finale à zéro, c'est-à-dire le meilleur score trouvé.
ans = 0
# Parcourt toutes les combinaisons possibles du nombre de matières choisies par jour,
# product(range(n + 1), repeat=5) génère toutes les 5-uples possibles, chaque valeur entre 0 et n.
for t in product(range(n + 1), repeat=5):
    # Si la somme totale des créneaux (tous jours confondus) dépasse l limite (l), on saute cette combinaison.
    if sum(t) > l:
        continue  # Passe à la combinaison suivante.
    # Initialise la variable score pour calculer le bonheur/score de la sélection courante.
    score = 0
    # Pour chaque jour (i) et le nombre de matières choisi ce jour-là (v):
    for i, v in enumerate(t):
        # On ajoute le score maximal possible pour v matières ce jour (pré-calculé dans lst[i]).
        score += lst[i][v]
    # Met à jour la meilleure réponse si la combinaison actuelle dépasse la précédente.
    ans = max(score, ans)
# Affiche le score maximum trouvé parmi toutes les combinaisons respectant la contrainte sur l.
print(ans)  # Affiche la solution finale.