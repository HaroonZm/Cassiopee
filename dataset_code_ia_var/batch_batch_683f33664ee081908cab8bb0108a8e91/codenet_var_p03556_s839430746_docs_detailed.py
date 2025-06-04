def plus_grand_carre_inferieur(n):
    """
    Calcule le plus grand carré parfait inférieur ou égal à n.

    Paramètres:
        n (int): La borne supérieure (doit être un entier positif).

    Retourne:
        int: Le plus grand carré parfait inférieur ou égal à n.
    """
    ans = 0  # Variable pour stocker le plus grand carré parfait trouvé
    i = 1    # Compteur qui servira à générer les carrés parfaits (i^2)

    # Boucle tant que le carré d'i est inférieur ou égal à n
    while (i * i) <= n:
        ans = i * i      # Met à jour 'ans' avec le carré actuel
        i += 1           # Passe à l'entier suivant

    return ans

if __name__ == "__main__":
    # Demande à l'utilisateur d'entrer un entier
    n = int(input("Entrez un entier positif: "))

    # Calcule et affiche le plus grand carré parfait inférieur ou égal à n
    resultat = plus_grand_carre_inferieur(n)
    print(resultat)