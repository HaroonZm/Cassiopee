def compute_result():
    """
    Lit les entrées utilisateur, effectue un calcul mathématique à partir des entrées
    puis affiche le résultat selon la formule spécifiée :
    résultat = 1 + int((c - 1) / (n + 1))
    où :
        - n : entier entré par l'utilisateur (par ex. nombre de joueurs)
        - p : entier non utilisé ici mais nécessaire pour la cohérence des entrées
        - c : somme d'une liste d'entiers (par ex. scores ou éléments)
    """
    # Demander à l'utilisateur de saisir deux entiers séparés par un espace.
    n, p = map(int, input().split())

    # Demander à l'utilisateur de saisir p entiers séparés par des espaces.
    # Ces valeurs sont converties puis leur somme est calculée et stockée dans 'c'.
    c = sum(map(int, input().split()))

    # Calculer le résultat selon la formule requise.
    # (c-1) // (n+1) calcule combien de fois (n+1) "tient" dans (c-1), arrondi par défaut.
    # On ajoute 1 selon la spécification du problème.
    result = 1 + int((c - 1) / (n + 1))

    # Afficher le résultat.
    print(result)

# Lancer la fonction principale si ce fichier est exécuté.
if __name__ == "__main__":
    compute_result()