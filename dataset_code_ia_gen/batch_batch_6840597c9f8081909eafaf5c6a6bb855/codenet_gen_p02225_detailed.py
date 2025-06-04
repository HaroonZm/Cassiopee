# Comme l'énoncé précis du problème n'a pas été fourni,
# je vais illustrer une solution complète Python avec une approche générique.
# Pour un problème typique, par exemple "Trouver la somme des deux nombres les plus grands dans une liste".

def somme_deux_maximums(liste):
    """
    Cette fonction retourne la somme des deux plus grands éléments dans la liste donnée.

    Approche :
    1. On vérifie que la liste contient au moins deux éléments.
    2. On initialise deux variables max1 et max2 pour suivre les deux plus grandes valeurs.
    3. On parcours la liste une seule fois pour déterminer ces deux valeurs.
    4. On retourne la somme des deux plus grands nombres.

    Complexité :
    - Temps : O(n), n étant la longueur de la liste.
    - Espace : O(1).
    """

    if len(liste) < 2:
        raise ValueError("La liste doit contenir au moins deux éléments")

    # Initialisation des deux maximums avec des valeurs très petites
    max1 = float('-inf')  # le plus grand
    max2 = float('-inf')  # le deuxième plus grand

    for num in liste:
        # Si on trouve un nombre plus grand que max1
        if num > max1:
            max2 = max1  # le max précédent devient le second max
            max1 = num   # max1 est mis à jour avec le nouveau max
        # Sinon, si num est entre max1 et max2
        elif num > max2:
            max2 = num

    return max1 + max2

# Exemple d'utilisation
if __name__ == "__main__":
    tableau = [12, 34, 10, 6, 40]
    resultat = somme_deux_maximums(tableau)
    print(f"La somme des deux plus grands nombres est : {resultat}")