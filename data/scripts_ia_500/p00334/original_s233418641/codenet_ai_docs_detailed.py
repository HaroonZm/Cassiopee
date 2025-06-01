def main():
    """
    Lit N listes d'entiers depuis l'entrée standard, trie chaque liste, 
    et calcule combien de listes sont des doublons (après tri).
    Affiche le nombre de doublons détectés.

    Étapes détaillées :
    1. Lire un entier N indiquant le nombre de listes à lire.
    2. Pour chaque liste lue :
       - Convertir les chaînes de caractères en entiers.
       - Trier la liste pour pouvoir comparer indépendamment de l'ordre.
       - Vérifier si cette liste triée est déjà présente dans la collection A.
         Si elle ne l'est pas, l'ajouter.
    3. Calculer la différence entre N et la taille de A pour obtenir le nombre de doublons.
    4. Afficher ce nombre.
    """
    # Lire le nombre total de listes à traiter
    N = int(input())
    A = []  # Liste pour stocker les listes triées uniques

    for _ in range(N):
        # Lire une ligne, la convertir en liste d'entiers
        a = list(map(int, input().split()))
        # Trier la liste pour une comparaison cohérente
        a.sort()
        # Ajouter à A seulement si cette liste triée n'est pas déjà présente
        if A.count(a) == 0:
            A.append(a)

    # Afficher le nombre de listes dupliquées (les repeats après tri)
    print(N - len(A))


if __name__ == "__main__":
    main()