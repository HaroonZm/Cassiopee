def calculate_min_partition(s):
    """
    Calcule la plus petite taille maximale d'une sous-chaîne résultante
    lorsqu'on coupe la chaîne à chaque occurrence de chaque lettre minuscule alphabétique.
    Pour chaque lettre présente, on considère la distance maximale entre deux occurrences consécutives
    et on conserve la plus petite de ces valeurs pour toutes les lettres.

    Args:
        s (str): La chaîne d'entrée à analyser.

    Returns:
        int: La plus petite taille maximale d'une sous-chaîne résultante possible.
    """
    ans = int(len(s) / 2)  # Initialisation avec une valeur maximale plausible (moitié de la longueur)
    
    # Parcours de chaque lettre minuscule de l'alphabet
    for i in range(97, 97 + 26):
        current_char = chr(i)
        if current_char in s:
            ct = s.count(current_char)  # Nombre de fois que la lettre apparaît dans la chaîne
            
            # Liste pour stocker les positions (indices + 1) de chaque occurrence de la lettre
            place = [0] * ct  
            
            # Recherche des positions de chaque occurrence
            for j in range(ct - 1):
                if j == 0:
                    # La première occurrence : position +1 car on commence de 1 (pas 0)
                    place[0] = s.find(current_char) + 1
                # Recherche relative à la chaîne tronquée à partir du dernier trouvé
                place[j + 1] = s[place[j]:].find(current_char) + place[j] + 1
            
            # Calcul du plus grand écart entre les occurrences,
            # y compris le début et la fin de la chaîne
            haba = max(len(s) - place[ct - 1], place[0] - 1)
            for j in range(ct - 1):
                haba = max(haba, place[j + 1] - place[j] - 1)
            
            ans = min(ans, haba)  # Mise à jour de notre résultat minimal
    
    return ans

if __name__ == "__main__":
    # Lecture de la chaîne en entrée depuis l'utilisateur
    s = str(input())
    
    # Calcul et affichage du résultat
    print(calculate_min_partition(s))