def roman_to_integer(roman):
    """
    Convertit une chaîne de caractères représentant un nombre romain en entier décimal.
    
    Args:
        roman (str): La chaîne de caractères avec les chiffres romains ('IVXLCDM').
        
    Returns:
        int: La valeur décimale correspondante.
    """
    # Dictionnaire de correspondance des symboles romains à leur valeur décimale
    Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    phase = 1000  # Valeur maximale de base pour démarrer la conversion (M)
    ret = 0       # Résultat en décimal à retourner
    cnt = 0       # Compteur du nombre de chiffres consécutifs de la même 'phase'
    
    # Parcours caractère par caractère de l'entrée romaine
    for x in roman:
        cur = Roman[x]  # Valeur décimale du chiffre romain actuel
        
        if cur < phase:
            # Si la valeur baisse, on additionne la série précédente et change de 'phase'
            ret += phase * cnt
            phase = cur
            cnt = 1
        elif cur == phase:
            # Si la valeur reste identique, on continue la série en l'incrémentant
            cnt += 1
        elif cur > phase:
            # Si la valeur monte, on applique la règle de soustraction romaine
            ret += cur - cnt * phase
            phase = cur
            cnt = 0
    else:
        # Ajout du reste éventuel non traité à la fin de la boucle
        ret += phase * cnt
        
    return ret

def main():
    """
    Boucle principale qui lit les lignes de l'entrée standard contenant des nombres romains
    et affiche leur valeur décimale correspondante.
    """
    while True:
        try:
            # Lecture de l'entrée (remplacer raw_input par input selon la version de Python)
            roman = raw_input()
        except EOFError:
            # Fin de l'entrée atteinte, on sort de la boucle
            break
        
        # Conversion et affichage du résultat
        result = roman_to_integer(roman)
        print result

# Lancement du programme principal
if __name__ == "__main__":
    main()