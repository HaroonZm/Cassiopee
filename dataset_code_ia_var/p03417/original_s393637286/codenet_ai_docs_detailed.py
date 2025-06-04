def compute_result(A, B):
    """
    Calcule le résultat selon les contraintes suivantes :
    - Si A et B sont tous deux égaux à 1, retourne 1.
    - Si A est égal à 1, retourne B - 2.
    - Si B est égal à 1, retourne A - 2.
    - Sinon, retourne (A - 2) * (B - 2).
    
    Paramètres :
        A (int): Premier entier, représentant généralement le nombre de lignes.
        B (int): Deuxième entier, représentant généralement le nombre de colonnes.
    Retour :
        int: Le résultat calculé selon les règles ci-dessus.
    """
    # Vérifie si A et B sont tous les deux égaux à 1
    if A == 1 and B == 1:
        return 1
    # Vérifie si seulement A est égal à 1
    elif A == 1:
        return B - 2
    # Vérifie si seulement B est égal à 1
    elif B == 1:
        return A - 2
    # Cas général pour A >= 2 et B >= 2
    else:
        return (A - 2) * (B - 2)

def main():
    """
    Fonction principale qui lit l'entrée utilisateur, interprète les valeurs, 
    appelle la fonction de calcul et affiche le résultat.
    """
    # Lecture de l'entrée utilisateur, découpe en deux entiers
    A, B = map(int, input().split())
    
    # Calcul du résultat avec la fonction 'compute_result'
    result = compute_result(A, B)
    
    # Affiche le résultat à l'utilisateur
    print(result)

# Appel de la fonction principale si ce fichier est exécuté comme script
if __name__ == "__main__":
    main()