def main():
    """
    Programme principal.
    Lit la longueur maximale L et le nombre d'éléments N.
    Ensuite pour chaque élément, lit deux entiers (x, w), calcule la somme pondérée.
    Selon la valeur de la somme obtenue s :
        - affiche 0 si s == 0
        - affiche 1 puis 1 et -s si s < 0
        - affiche 1 puis -1 et s si s > 0
    """
    # Lire la longueur maximale (n'est pas utilisée dans ce code, mais potentiellement utile selon le contexte)
    L = int(input())
    # Lire le nombre de paires à traiter
    N = int(input())
    # Initialiser la somme pondérée
    s = 0
    # Boucle sur chaque paire d'entrée (x, w)
    for i in range(N):
        x, w = map(int, input().split())  # Lire et convertir les deux entiers
        s += x * w                        # Ajouter le produit à la somme
    # Traitement du résultat selon la valeur de la somme s
    if s == 0:
        # Quand la somme totale est nulle, afficher simplement 0
        print(0)
    elif s < 0:
        # Quand la somme totale est négative
        print(1)
        print(1, -s)  # Afficher le couple (1, -s)
    else:
        # Quand la somme totale est positive
        print(1)
        print(-1, s)  # Afficher le couple (-1, s)

# Appeler la fonction principale
if __name__ == "__main__":
    main()