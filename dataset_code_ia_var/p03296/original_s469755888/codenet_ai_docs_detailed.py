def count_pairs_in_sequence():
    """
    Lit une séquence d'entiers depuis l'entrée standard, compte pour chaque sous-séquence de nombres identiques
    combien de paires (paquets de deux éléments ayant la même valeur consécutivement) peuvent être formées,
    puis affiche le nombre total de paires trouvées.
    
    Entrée:
        - Un entier N suivi de N entiers séparés par des espaces.
    
    Sortie:
        - Un entier : le total de paires pouvant être formées dans la liste fournie.
    """
    # Lire le nombre d'éléments de la liste
    N = int(input())
    
    # Initialiser la liste qui contiendra les longueurs des sous-séquences consécutives
    dif = []
    
    # Lire la séquence de N entiers
    a = list(map(int, input().split()))
    
    # Initialiser la valeur précédente et le compteur de la séquence courante
    bef = a[0]
    count = 0
    
    # Parcourir la séquence pour détecter les blocs consécutifs de la même valeur
    for i, j in enumerate(a):
        if i == 0:
            # Premier élément : initialiser 'bef' et le compteur de la séquence
            bef = j
            count = 1
        elif j == bef:
            # Même valeur que la précédente : continuer la séquence
            count += 1
        else:
            # Valeur différente : sauvegarder la taille de la séquence précédente,
            # réinitialiser le compteur et mettre à jour 'bef'
            dif.append(count)
            count = 1
            bef = j
    # Ajouter la dernière séquence (en dehors de la boucle)
    dif.append(count)
    
    # Calculer le nombre total de paires (chaque paire = deux éléments identiques consécutifs)
    res = 0
    for seq_len in dif:
        res += seq_len // 2  # Division entière : nombre de paires dans chaque bloc
    
    # Afficher le résultat final
    print(res)

# Appeler la fonction principale
count_pairs_in_sequence()