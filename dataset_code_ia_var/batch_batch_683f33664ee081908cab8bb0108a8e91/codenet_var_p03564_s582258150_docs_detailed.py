def compute_ans(n, k):
    """
    Calcule la valeur finale en appliquant une séquence d'opérations sur une variable 'ans' initialisée à 1.
    Pour chaque itération (jusqu'à 'n'):
      - Si 'ans' est strictement inférieur à 'k', on double sa valeur.
      - Sinon, on ajoute 'k' à 'ans'.
    Args:
        n (int): Le nombre d'itérations à effectuer.
        k (int): La valeur de seuil et l'incrémentation à utiliser dans les opérations.
    Returns:
        int: La valeur finale de 'ans' après 'n' itérations.
    """
    ans = 1  # Initialisation de la variable résultat à 1
    count = 0  # Initialisation du compteur d'itérations
    # Boucle principale exécutée 'n' fois
    while count < n:
        if ans < k:
            # Si 'ans' est inférieur à 'k', multiplier 'ans' par 2
            ans *= 2
        else:
            # Sinon, ajouter 'k' à 'ans'
            ans += k
        count += 1  # Incrémenter le compteur d'itérations
    return ans

def main():
    """
    Fonction principale qui lit les entrées de l'utilisateur, appelle la fonction de calcul,
    et affiche le résultat.
    """
    n = int(input("Entrer le nombre d'itérations (n) : "))  # Lecture du nombre d'itérations
    k = int(input("Entrer la valeur du seuil/incrément (k) : "))  # Lecture de la valeur de seuil/incrément
    result = compute_ans(n, k)  # Calcul de la valeur finale avec 'n' et 'k'
    print(result)  # Affichage du résultat final

if __name__ == "__main__":
    main()