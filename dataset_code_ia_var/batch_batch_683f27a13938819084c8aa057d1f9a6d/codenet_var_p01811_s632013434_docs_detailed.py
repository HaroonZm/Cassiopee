def transform_sequence():
    """
    Lit une chaîne depuis l'entrée utilisateur.
    Tente de transformer cette chaîne en "ABC" en remplaçant chaque sous-chaîne "ABC" par une lettre manquante.
    À chaque étape, si la transformation est impossible, affiche "No" et arrête la boucle.
    Si la chaîne devient exactement "ABC", affiche "Yes".
    """
    # Lire la chaîne d'entrée fournie par l'utilisateur
    s = input()
    # La chaîne cible à atteindre
    end = "ABC"

    # Boucle principale de transformation
    while True:
        # Si la chaîne actuelle correspond à la chaîne cible, afficher "Yes" et arrêter la boucle
        if s == end:
            print("Yes")
            break

        # Remplacer toutes les occurrences de "ABC" par "X"
        s = s.replace("ABC", "X")

        # Vérification des conditions d'arrêt :
        # 1. Si "X" n'est plus présent dans la chaîne
        # 2. Si le nombre total de lettres parmi 'A', 'B' et 'C' dans la chaîne n'est pas égal à 2
        # (C'est-à-dire que la chaîne ne contient pas exactement deux de ces lettres)
        if ("X" not in s) or (("A" in s) + ("B" in s) + ("C" in s) != 2):
            print("No")
            break

        # Recherche de la lettre manquante parmi 'A', 'B', 'C'
        for c in "ABC":
            if c not in s:
                # Remplacer tous les "X" par la lettre manquante
                s = s.replace("X", c)
                break

# Appel de la fonction principale pour exécution
transform_sequence()