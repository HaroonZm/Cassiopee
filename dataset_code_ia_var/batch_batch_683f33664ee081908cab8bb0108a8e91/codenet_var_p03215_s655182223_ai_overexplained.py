# On commence par lire deux entiers depuis l'entrée standard, séparés par un espace
N, K = map(int, input().split(" "))  # N : longueur de la séquence, K : nombre de sous-séquences à prendre en compte

# On lit une ligne d'entiers séparés par des espaces qu'on convertit en une liste d'entiers. Ceci représente la séquence a.
a = list(map(int, input().split(" ")))  # Liste contenant N entiers

# On crée une somme partielle de la liste 'a'
# Cela remplace chaque élément a[i+1] par la somme de a[i+1] et a[i]
# Range(N-1) produit les indices de 0 à N-2, c'est-à-dire qu'on s'arrête avant N-1 car on accède à a[i+1]
for i in range(N - 1):  # Itération de 0 à N-2 pour visiter chaque paire d'éléments consécutifs
    a[i + 1] += a[i]   # On ajoute la valeur précédente à la suivante pour réaliser le cumul

# On initialise une liste vide qui va contenir les sommes de toutes les sous-séquences possibles
seq = []

# On parcourt tous les indices i de 0 à N-1, où i désigne la fin (à rebours) de la sous-séquence
for i in range(N):
    # sl est l'indice de début de la sous-séquence
    for sl in range(i + 1):  # de 0 à i inclus
        # Si sl == 0, la somme de la sous-séquence [0, N-1-i+sl] est a[N-1-i+sl], car il n'y a rien à soustraire
        if sl == 0:
            seq.append(a[N - 1 - i + sl])  # Ajoute la somme directement
        else:
            # La somme de la sous-séquence [sl, N-1-i+sl] s'obtient en soustrayant la somme cumulative jusqu'à sl-1
            # Cela revient à a[N-1-i+sl] - a[sl-1]
            seq.append(a[N - 1 - i + sl] - a[sl - 1])  # Ajoute la somme appropriée

# Maintenant, on va essayer de construire le plus grand entier possible (ans)
# Il doit être tel qu'il existe au moins K sous-séquences dont la somme a au moins tous les bits de ans à 1

ans = 0  # Résultat final, initialisé à zéro

l = len(seq)  # Le nombre total de sous-séquences considérées

# On inspecte tous les bits depuis 50 (le bit le plus élevé possible ici) jusqu'à 0 (bit le moins significatif)
for i in range(50, -1, -1):  # i descend de 50 à 0, inclusivement
    cnt = 0  # Nombre de sous-séquences candidates avec le bit courant à 1
    s = set()  # Ensemble d'indices des sous-séquences qui satisfont la condition courante

    # On parcourt toutes les sommes de sous-séquences présentes dans seq
    for j in range(l):  # Pour chaque sous-séquence potentielle

        # On vérifie si la somme n'est pas négative
        # et si le i-ème bit de la somme est à 1
        if seq[j] >= 0 and (seq[j] & (1 << i)) != 0:
            cnt += 1           # On incrémente le compteur
            s.add(j)           # On mémorise l'indice de la sous-séquence

    # Si au moins K sous-séquences ont le i-ème bit à 1, on peut le prendre pour la réponse
    if cnt >= K:
        ans += (1 << i)  # On met à jour ans pour inclure le bit courant

        # On retranche ce bit de toutes les sous-séquences qui l'ont, pour ne pas le compter deux fois ou plus loin
        for j in range(l):
            if j in s:
                seq[j] = seq[j] - (1 << i)  # On enlève la valeur du bit i dans cada sous-séquence sélectionnée
            else:
                seq[j] = -1  # On marque les autres comme invalides (négatives) pour qu'elles ne soient plus prises

# À la fin, on affiche le résultat
print(ans)  # Imprime la plus grande somme dont au moins K sous-séquences ont tous les bits à 1 en commun