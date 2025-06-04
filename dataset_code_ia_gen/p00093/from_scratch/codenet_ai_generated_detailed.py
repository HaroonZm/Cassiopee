def is_leap_year(year):
    """
    Détermine si une année donnée est une année bissextile selon les règles spécifiées.
    Une année est bissextile si :
    - elle est divisible par 4,
    - sauf si elle est divisible par 100, alors ce n'est pas une année bissextile,
    - sauf si elle est divisible par 400, alors c'est quand même une année bissextile.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    """
    Programme principal pour lire plusieurs ensembles de données.
    Chaque ensemble est constitué de deux entiers a et b (0 < a <= b < 3000).
    On doit afficher toutes les années bissextiles entre a et b inclus.
    Si aucune année bissextile n'existe dans cet intervalle, on affiche 'NA'.
    L'entrée se termine quand a et b valent tous les deux 0.
    Une ligne vide est imprimée entre chaque ensemble de résultats (sauf avant le premier).
    """
    first_output = True  # Pour gérer l'affichage des lignes vides entre groupes

    while True:
        # On lit une ligne d'entrée
        line = input().strip()
        if not line:
            # Si la ligne est vide, on la saute
            continue
        a_str, b_str = line.split()
        a, b = int(a_str), int(b_str)

        # Condition de terminaison
        if a == 0 and b == 0:
            break

        # Collecte des années bissextiles dans l'intervalle
        leap_years = []
        for year in range(a, b + 1):
            if is_leap_year(year):
                leap_years.append(year)

        # Affichage
        if not first_output:
            # Ligne vide entre les blocs de sortie
            print()
        else:
            first_output = False

        if leap_years:
            for ly in leap_years:
                print(ly)
        else:
            print("NA")

if __name__ == "__main__":
    main()