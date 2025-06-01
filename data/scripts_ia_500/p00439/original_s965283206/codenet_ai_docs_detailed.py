def fun(n, k):
    """
    Calcule la somme maximale d'une sous-séquence de longueur k dans une liste d'entiers.

    Cette fonction lit n entiers depuis l'entrée standard, puis trouve la 
    somme maximale possible d'une sous-séquence contiguë de longueur k parmi ces entiers.
    Elle imprime ensuite cette valeur maximale.

    Args:
        n (int): Le nombre d'entiers à lire.
        k (int): La taille de la sous-séquence dont on cherche la somme maximale.

    Procedure:
        - Lit n entiers et les stocke dans la liste A.
        - Calcule la somme des k premiers éléments (fenêtre initiale).
        - Parcourt la liste en faisant glisser une fenêtre de taille k:
            * À chaque étape, retire l'élément sortant de la fenêtre et ajoute le nouvel élément entrant.
            * Mets à jour la somme maximale rencontrée.
        - Affiche la somme maximale trouvée.
    """
    # Lecture de la liste d'entiers
    A = [int(input()) for _ in range(n)]
    
    # Initialisation de la somme courante pour la fenêtre de taille k
    k_sum = 0
    # Initialisation du maximum rencontré
    maximam = 0
    
    # Parcours des éléments avec leur indice
    for num, a in enumerate(A):
        # Tant qu'on remplit la première fenêtre de taille k
        if 0 <= num <= k-1:
            # Ajout de l'élément courant à la somme de la fenêtre initiale
            k_sum += a
        else:
            # Pour les fenêtres suivantes, on fait glisser la fenêtre:
            # on ajoute l'élément entrant, on retire l'élément sortant
            k_sum = k_sum + a - A[num-k]
            # Mise à jour de la somme maximale si besoin
            maximam = max(maximam, k_sum)

    # Affichage de la somme maximale de sous-séquence de taille k
    print(maximam)


# Boucle principale pour traiter plusieurs cas
for _ in range(5):
    # Lecture des paramètres n et k
    n, k = map(int, input().split())
    # Condition d'arrêt: si n et k sont à zéro, on termine la boucle
    if n == 0 and k == 0:
        break
    else:
        # Appel de la fonction pour traiter le cas
        fun(n, k)