def is_leap_year(year):
    """
    Détermine si une année donnée est une année bissextile selon les règles:
    - Divisible par 4
    - Mais pas divisible par 100 sauf si divisible par 400
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    import sys
    
    first_dataset = True
    for line in sys.stdin:
        # Lecture de la ligne et extraction des années a et b
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        # Condition d'arrêt : si a et b sont tous les deux 0
        if a == 0 and b == 0:
            break
        
        # Affichage d'une ligne vide entre deux jeux de données (sauf avant le premier)
        if not first_dataset:
            print()
        else:
            first_dataset = False
        
        leap_years = []
        for year in range(a, b + 1):
            if is_leap_year(year):
                leap_years.append(str(year))
        
        if leap_years:
            # Affichage des années bissextiles trouvées
            print("\n".join(leap_years))
        else:
            # Aucun année bissextile dans l'intervalle
            print("NA")

if __name__ == "__main__":
    main()