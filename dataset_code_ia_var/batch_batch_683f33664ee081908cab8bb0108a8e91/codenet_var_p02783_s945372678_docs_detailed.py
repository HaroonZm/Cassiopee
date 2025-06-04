def turns_to_defeat_monster(H, A):
    """
    Calcule le nombre de tours nécessaires pour vaincre un monstre.
    
    Args:
        H (int): Points de vie initiaux du monstre.
        A (int): Nombre de points de dégâts infligés au monstre par tour.
        
    Returns:
        int: Nombre minimal de tours pour ramener les points de vie du monstre à zéro ou moins.
    """
    # Initialisation des points de vie courants du monstre
    HP = H
    # Initialisation du compteur de tours
    count = 0
    # Répéter tant que le monstre a des points de vie positifs
    while HP > 0:
        # Incrémentation du nombre de tours
        count += 1
        # Soustraction des dégâts à la vie courante du monstre
        HP -= A
    # Retourne le nombre de tours nécessaires
    return count

def main():
    """
    Fonction principale pour lire les entrées de l'utilisateur,
    appeler la fonction de calcul, et afficher le résultat.
    """
    # Lecture des deux entiers en entrée : H (points de vie), A (dégâts)
    H, A = map(int, input().split())
    # Appel de la fonction calculant le nombre de tours
    result = turns_to_defeat_monster(H, A)
    # Affiche le résultat
    print(result)

# Appel de la fonction principale si ce fichier est exécuté directement
if __name__ == "__main__":
    main()