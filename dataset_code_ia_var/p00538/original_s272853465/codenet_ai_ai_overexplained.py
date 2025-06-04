# Demander à l'utilisateur de saisir un nombre entier et stocker cette valeur dans la variable n
# Cela détermine la taille de la liste à traiter ci-dessous
n = int(input())

# Créer une liste 'a' de taille n, où chaque élément est obtenu en demandant à l'utilisateur de saisir un entier
# On utilise une compréhension de liste pour répéter l'opération n fois
a = [int(input()) for _ in range(n)]

# Initialiser une liste 'dp' de taille n contenant uniquement des zéros
# Cette liste pourra servir de stockage pour des valeurs intermédiaires dans les calculs dynamiques
dp = [0 for _ in range(n)]

# Démarrer une boucle for avec la variable de boucle i qui va de 0 à n-1 (inclus)
for i in range(n):
    # Vérifier si le reste de la division de i par 2 est égal au reste de la division de n par 2
    # (en d'autres termes, si i et n sont tous deux pairs ou impairs)
    if i % 2 == n % 2:
        # Si cette condition est vraie,
        # On reconstruit la liste 'dp' en utilisant une compréhension de liste
        # On parcourt chaque indice l de 0 à n-1
        dp = [ 
            # Si l'élément d'indice l dans a est strictement supérieur à l'élément d'indice (l + i) modulo n
            # Remarquez l'utilisation du modulo pour faire un "tour" circulaire dans la liste
            dp[(l + 1) % n] if a[l] > a[(l + i) % n]
            # Alors, on prend la valeur suivante dans la liste dp (avec un décalage circulaire)
            # Sinon, on garde la valeur actuelle à cette position l dans dp
            else dp[l] 
            for l in range(n)
        ]
    else:
        # Si la condition précédente est fausse, on entre dans la branche else
        # On met à jour la liste 'dp' selon une logique différente (encore via une compréhension de liste)
        dp = [
            # Pour chaque indice l de 0 à n-1
            # On calcule la somme de l'élément a[l] et dp[(l + 1) % n]
            # On calcule aussi la somme de l'élément a[(l + i) % n] et dp[l]
            # On prend le maximum de ces deux quantités et on l'affecte à dp[l]
            max(a[l] + dp[(l + 1) % n], a[(l + i) % n] + dp[l])
            for l in range(n)
        ]

# Une fois que la boucle est terminée, la liste dp contient les résultats calculés
# On affiche le plus grand élément contenu dans la liste dp à l'aide de max(dp)
print(max(dp))