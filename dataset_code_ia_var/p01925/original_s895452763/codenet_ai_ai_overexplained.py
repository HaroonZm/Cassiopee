import sys

# Définition de la fonction principale qui effectue le calcul du résultat selon les paramètres donnés
def solve(n, m, s, k, c):
    # Création d'une liste maxvs de taille n+1, initialisée avec des zéros.
    # Cette liste va contenir, pour chaque index de 1 à n, la somme maximale des points pouvant être attribués à chaque élément concerné.
    maxvs = [0] * (n + 1)

    # Création d'une liste minvs de taille n+1, initialisée avec des zéros.
    # Cette liste va contenir, pour chaque index de 1 à n, la somme minimale des points pouvant être attribués à chaque élément concerné sous condition.
    minvs = [0] * (n + 1)

    # On parcourt chaque élément du tableau 'c' en utilisant la fonction enumerate, qui retourne à la fois l'index i (position dans la liste) et l'élément c[i]
    # Le paramètre i est un tuple (indice, valeur) retourné par enumerate
    for i in enumerate(c):
        # i[0] est l'indice (l'index actuel du tableau c), i[1] est la liste de cibles associée à cet indice
        # On parcourt chaque élément j dans la liste de cibles associée à l'indice actuel
        for j in i[1]:
            # On ajoute à maxvs[j] la valeur de s[i[0]], ce qui signifie qu'on attribue l'ensemble des points de cette question à l'élément j désigné
            maxvs[j] += s[i[0]]

            # Si la condition k[i[0]] == 1 est vérifiée (c'est-à-dire, si la propriété K pour cet indice est égale à 1),
            # On ajoute également à minvs[j] la valeur de s[i[0]].
            # Cela permet de distinguer les cas selon la valeur de K (par ex. obligatoire/facultatif)
            if k[i[0]] == 1:
                minvs[j] += s[i[0]]

    # Initialisation d'une variable ans à -1, qui servira à conserver le maximum trouvé selon le critère à optimiser
    ans = -1

    # Boucle qui va parcourir tous les indices 'i' de 1 à n inclus (on commence à 1, car l'indice 0 n'est pas utilisé dans ce contexte)
    for i in range(1,  n+1):
        # Pour chaque i, on cherche le minimum des éléments de minvs sauf l'indice i courant.
        # Cela se fait en prenant la concaténation de minvs[1:i] (éléments avant i) et minvs[i+1:] (éléments après i),
        # car le découpage Python [1:i] exclut i et inclut 1, et [i+1:] commence juste après i jusqu'à la fin.
        minimum_autres = min(minvs[1:i] + minvs[i+1:])

        # Calcul de la différence entre maxvs[i] (score maximal pour i) et minimum_autres (score minimal sur les autres) et comparaison avec ans
        # Ceci permet de retenir le maximum parmi toutes les possibilités
        ans = max(ans, maxvs[i] - minimum_autres)

    # Affichage du résultat final : on rajoute 1 car l'énoncé semble considérer des bornes incluses
    print(ans + 1)

# Boucle principale qui sert à lire les entrées jusqu'à rencontrer deux zéros (N == M == 0)
while True:
    # Lecture d'une ligne de l'entrée standard, puis conversion en deux entiers avec map et split
    N, M = map(int, input().split())
    # Si la ligne contient deux zéros, on termine la boucle (c'est le signal de fin de données)
    if N == M == 0:
        break

    # Initialisation de 3 listes vides qui vont contenir respectivement :
    # - S : les valeurs de score pour chaque question
    # - K : les indicateurs (1 ou autre) pour chaque question
    # - C : les listes des éléments concernés par chaque question
    S = []
    K = []
    C = []

    # Boucle pour lire les M lignes suivantes (une pour chaque question)
    for i in range(M):
        # Lecture d'une ligne de l'entrée standard, conversion de tous les éléments de la ligne en entiers et stockage dans une liste Skc
        Skc = list(map(int, input().split()))
        # Le premier élément de cette ligne représente la valeur S (score) de la question, qu'on ajoute à la liste S
        S.append(Skc[0])
        # Le deuxième élément représente la valeur K (indicateur) de la question, qu'on ajoute à la liste K
        K.append(Skc[1])
        # Les éléments suivants représentent la liste des indices 'cibles', qu'on ajoute à la liste C sous forme de liste
        C.append(Skc[2:])
    # Appel à la fonction solve en lui passant les listes construites et les paramètres nécessaires
    solve(N, M, S, K, C)