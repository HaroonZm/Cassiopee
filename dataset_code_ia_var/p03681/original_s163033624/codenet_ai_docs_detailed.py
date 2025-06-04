import math

def compute_special_factorial(n, m):
    """
    Calcule une valeur spéciale basée sur les entrées n et m, selon les règles suivantes :
    - Si la différence absolue entre n et m est supérieure à 1, retourne 0.
    - Si n et m sont égaux, retourne (n! * m! * 2) modulo 1000000007.
    - Sinon, retourne (n! * m!) modulo 1000000007.
    
    Paramètres:
        n (int): premier entier positif.
        m (int): second entier positif.
        
    Retourne:
        int: le résultat calculé selon les règles ci-dessus.
    """
    MOD = 1000000007  # Modulo à appliquer sur les résultats pour éviter les grands nombres entiers

    # Calcul si la différence est autorisée
    if abs(n - m) <= 1:
        # Cas où les deux valeurs sont identiques
        if n == m:
            result = (math.factorial(n) ** 2) * 2 % MOD
            return result
        else:
            # Cas où la différence est de 1
            result = math.factorial(n) * math.factorial(m) % MOD
            return result
    else:
        # Cas où la différence est supérieure à 1, résultat nul
        return 0

def main():
    """
    Fonction principale qui lit l'entrée utilisateur, appelle compute_special_factorial et affiche le résultat.
    """
    # Lecture de l'entrée utilisateur, attend deux entiers séparés par un espace
    n, m = map(int, input().split())
    
    # Calcul du résultat selon les règles spécifiées
    result = compute_special_factorial(n, m)
    
    # Affichage du résultat final
    print(result)

# Point d'entrée du script
if __name__ == "__main__":
    main()