def main():
    """
    Fonction principale qui lit les entrées utilisateur,
    effectue une série d'opérations mathématiques sur deux nombres selon un motif,
    puis affiche les résultats obtenus.

    Entrées :
        - Un entier n (nombre total d'itérations potentielles)
        - Deux entiers a et b (les deux nombres à manipuler)
    Sorties :
        - Les valeurs finales de a et b après traitement
    """

    # Lecture de l'entier n indiquant le nombre de cycles à effectuer
    n = int(input("Entrez la valeur de n : "))

    # Lecture des entiers a et b, séparés par un espace
    a, b = map(int, input("Entrez les valeurs de a et b séparées par un espace : ").split())

    # Calcul du nombre réel d'itérations à effectuer (modulo 12)
    s = n % 12

    # Boucle pour appliquer successivement les modifications sur a et b
    for i in range(1, s + 1):
        if i % 2 == 0:
            # Pour les itérations paires : on ajoute a à b
            b = a + b
        else:
            # Pour les itérations impaires : on retire b à a
            a = a - b

    # Affichage final des deux nombres
    print(a, b)

# Appel du point d'entrée principal
if __name__ == "__main__":
    main()