def main():
    """
    Fonction principale qui lit un nombre m, puis lit m paires d'entiers (x, w),
    calcule la somme pondérée x * w pour chaque paire, et affiche :
      - '1\nsig abs(s)' où sig vaut 1 si la somme est négative ou zéro, -1 si positive,
         et abs(s) est la valeur absolue de la somme calculée, si s ≠ 0
      - 0 si la somme est nulle
    """
    input()  # Lecture de l'entrée non utilisée, généralement pour synchroniser l'entrée avec l'énoncé
    
    m = int(input())  # Nombre de paires à traiter
    
    # Calcul de la somme pondérée pour les m paires
    s = 0
    for _ in range(m):
        x, w = map(int, input().split())
        s += x * w  # Ajout de la pondération courante à la somme totale
    
    # Affichage du résultat selon la valeur de s
    if s == 0:
        print(0)
    else:
        # Détermine le signe affiché : 1 si s négatif ou nul, -1 si positif
        sign = 1 if s <= 0 else -1
        print('1\n{} {}'.format(sign, abs(s)))

if __name__ == "__main__":
    main()